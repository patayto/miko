---
title: "API Design Fundamentals"
type: concept
tags: [REST, HTTP, API-design, systems-design]
created: 2026-04-09
updated: 2026-04-09
---

REST (Representational State Transfer) is the default architectural style for modern APIs, emphasizing stateless interactions and resource-oriented design. HTTP methods form the foundation of REST operations: GET for retrieval, POST for creation, PUT for full replacement, and DELETE for removal. Status codes communicate operation results: 2xx for success, 3xx for redirection, 4xx for client errors, and 5xx for server errors.

Request structure distinguishes between path parameters (identifying a specific resource) and query parameters (for filtering, sorting, and pagination). A resource like `/users/123?sort=name&limit=10` uses the path parameter `123` to identify a specific user and query parameters for request options. Pagination strategies typically use limit/offset or cursor-based approaches to handle large datasets efficiently.

Core REST principles include idempotency (repeated identical requests produce the same result), statelessness (no session state on the server), and cacheability (responses can be cached where appropriate). Request/response formats typically use JSON for serialization, with clear schemas defining expected structures. Authentication can be implemented through basic auth, tokens (Bearer tokens, API keys), or OAuth flows depending on security requirements.

API versioning strategies address backward compatibility when APIs evolve. Common approaches include URL versioning (`/v1/users`), header versioning, and query parameter versioning. Proper error handling includes meaningful error messages, specific status codes, and response bodies that help clients understand what went wrong and how to fix it.

---
*No notes yet.*
