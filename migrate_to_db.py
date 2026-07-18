#!/usr/bin/env python3
"""
One-time migration: parse log.md and index.md into miko.db (SQLite).
Run from the miko/ directory or with DB_PATH set.
"""

import sqlite3
import re
import json
import os

BASE = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE, "miko.db")

# ---------------------------------------------------------------------------
# Schema
# ---------------------------------------------------------------------------

SCHEMA = """
CREATE TABLE IF NOT EXISTS index_pages (
    title           TEXT PRIMARY KEY,
    type            TEXT NOT NULL,          -- concept | entity | source | query
    summary         TEXT,
    updated         TEXT,                   -- YYYY-MM-DD
    ignored         INTEGER NOT NULL DEFAULT 0,
    ignored_reason  TEXT,
    ignored_scanned TEXT                    -- YYYY-MM-DD
);

CREATE TABLE IF NOT EXISTS log (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp   TEXT NOT NULL,              -- YYYY-MM-DD HH:MM
    operation   TEXT NOT NULL,              -- ingest | consolidate | lint | query | update | create | ops
    subject     TEXT,
    status      TEXT NOT NULL,             -- complete | failed | partial
    summary     TEXT,
    details     TEXT                        -- JSON array of bullet strings
);

CREATE INDEX IF NOT EXISTS idx_log_timestamp  ON log (timestamp);
CREATE INDEX IF NOT EXISTS idx_log_operation  ON log (operation);
CREATE INDEX IF NOT EXISTS idx_pages_type     ON index_pages (type);
CREATE INDEX IF NOT EXISTS idx_pages_updated  ON index_pages (updated);
"""

# ---------------------------------------------------------------------------
# Parse index.md
# ---------------------------------------------------------------------------

def parse_index(path: str) -> list[dict]:
    with open(path, encoding="utf-8") as f:
        content = f.read()

    SECTION_MAP = {
        "Concepts": "concept",
        "Entities": "entity",
        "Sources": "source",
        "Queries": "query",
    }

    rows = []
    current_section = None

    for line in content.splitlines():
        stripped = line.strip()

        # Detect section
        if stripped.startswith("## "):
            heading = stripped[3:].strip()
            current_section = SECTION_MAP.get(heading, "ignored" if heading == "Ignored Sources" else None)
            continue

        if not current_section or not stripped.startswith("|"):
            continue

        parts = [p.strip() for p in stripped.split("|")[1:-1]]
        if len(parts) < 3:
            continue

        # Skip header / separator rows
        if parts[0] in ("Page", "File") or set(parts[0].replace(" ", "")) <= {"-"}:
            continue

        if current_section != "ignored":
            m = re.match(r"\[\[(.+?)\]\]", parts[0])
            if not m:
                continue
            rows.append({
                "title": m.group(1),
                "type": current_section,
                "summary": parts[1],
                "updated": parts[2],
                "ignored": 0,
                "ignored_reason": None,
                "ignored_scanned": None,
            })
        else:
            # Ignored source: `filename` (location) | Reason | YYYY-MM-DD
            m = re.match(r"`(.+?)`", parts[0])
            if not m:
                continue
            rows.append({
                "title": m.group(1),
                "type": "source",
                "summary": None,
                "updated": None,
                "ignored": 1,
                "ignored_reason": parts[1],
                "ignored_scanned": parts[2],
            })

    return rows

# ---------------------------------------------------------------------------
# Parse log.md
# ---------------------------------------------------------------------------

def parse_log(path: str) -> list[dict]:
    with open(path, encoding="utf-8") as f:
        content = f.read()

    entries = []
    # Split on entry boundaries; keep delimiter
    raw_entries = re.split(r"(?=## \[\d{4}-\d{2}-\d{2})", content)

    for block in raw_entries:
        block = block.strip()
        if not block.startswith("## ["):
            continue

        lines = block.splitlines()
        # Header: ## [YYYY-MM-DD HH:MM] operation | subject
        header_m = re.match(
            r"## \[(\d{4}-\d{2}-\d{2} \d{2}:\d{2})\]\s+(\S+)\s*(?:\|\s*(.+))?",
            lines[0],
        )
        if not header_m:
            continue

        timestamp = header_m.group(1)
        operation = header_m.group(2).lower().rstrip("|").strip()
        subject = (header_m.group(3) or "").strip()

        status = ""
        summary = ""
        details = []
        in_details = False

        for line in lines[1:]:
            if line.startswith("Status:"):
                status = line[7:].strip()
            elif line.startswith("Summary:"):
                summary = line[8:].strip()
            elif line.startswith("Details:"):
                in_details = True
            elif in_details and line.startswith("-"):
                details.append(line[1:].strip())

        if status:
            entries.append(
                {
                    "timestamp": timestamp,
                    "operation": operation,
                    "subject": subject,
                    "status": status,
                    "summary": summary,
                    "details": json.dumps(details),
                }
            )

    # Return in chronological order (log.md is newest-first)
    return list(reversed(entries))

# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    conn = sqlite3.connect(DB_PATH)
    conn.executescript(SCHEMA)
    conn.commit()

    # --- Index ---
    index_rows = parse_index(os.path.join(BASE, "index.md"))
    conn.executemany(
        """INSERT OR REPLACE INTO index_pages
           (title, type, summary, updated, ignored, ignored_reason, ignored_scanned)
           VALUES (:title, :type, :summary, :updated, :ignored, :ignored_reason, :ignored_scanned)""",
        index_rows,
    )
    print(f"Index: inserted {len(index_rows)} rows")

    # --- Log ---
    log_entries = parse_log(os.path.join(BASE, "log.md"))
    conn.executemany(
        """INSERT INTO log (timestamp, operation, subject, status, summary, details)
           VALUES (:timestamp, :operation, :subject, :status, :summary, :details)""",
        log_entries,
    )
    print(f"Log:   inserted {len(log_entries)} entries")

    conn.commit()
    conn.close()
    print(f"Done → {DB_PATH}")


if __name__ == "__main__":
    main()
