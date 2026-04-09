---
title: "Matrix Protocol"
type: concept
tags: [messaging, self-hosted, federation, open-source, communication]
created: 2026-04-09
updated: 2026-04-09
---

# Matrix Protocol

Matrix is an open, decentralised communication protocol designed for real-time messaging, VoIP, and collaboration. It uses a federated architecture where anyone can run their own homeserver, and servers communicate with each other so users on different servers can still message each other — similar in spirit to email federation.

The reference homeserver implementation is Synapse (Python), with a lighter alternative called Dendrite (Go). The primary client is Element (formerly Riot), available on web, desktop, and mobile. Bridges allow Matrix to connect to other platforms — Slack, Discord, WhatsApp, Telegram — making it viable as a unified messaging hub.

Key properties:
- **Decentralised**: no single point of control; users own their data
- **Federated**: homeservers communicate across the network
- **End-to-end encryption**: supported via the Olm/Megolm cryptographic ratchet
- **Bridging**: first-class support for connecting to proprietary chat networks
- **Open standard**: protocol is public; multiple client and server implementations exist

Running a personal Matrix homeserver is a common choice for individuals wanting to consolidate messaging, reduce reliance on proprietary platforms, and maintain data ownership — themes consistent with [[Account Consolidation]] and [[Subscription Management]].

See also: bridges (not yet written), Synapse homeserver (not yet written), Element client (not yet written)

---
*My notes - do not edit below this line*
