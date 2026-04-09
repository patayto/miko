---
title: "Testing Fundamentals"
type: concept
tags: [testing, QA, software-engineering, test-pyramid]
created: 2026-04-09
updated: 2026-04-09
---

The test pyramid provides a framework for balanced test coverage across different levels of granularity. The base consists of unit tests, which test individual functions and components in isolation—these should form the majority of tests due to their speed and precision. The middle layer comprises integration tests, which verify that different components work together correctly. The smallest top layer contains end-to-end (E2E) tests, which validate entire user workflows—expensive and slow but critical for confidence.

Testing encompasses both functional and non-functional dimensions. Functional testing verifies that the system produces correct outputs for given inputs. Non-functional testing covers performance, reliability, security, and scalability. Different test types serve different purposes: unit tests catch logic bugs early, integration tests reveal interaction failures, API tests specifically validate endpoint contracts and data formats, and E2E tests ensure user workflows complete successfully.

Contract testing validates that APIs and services interact correctly according to agreed interfaces. This approach is useful for testing integrations where services may be developed independently—a consumer defines expected request/response patterns, and a provider verifies it fulfills those contracts.

The AAA (Arrange-Act-Assert) pattern structures individual tests clearly. Arrange sets up the preconditions and fixtures, Act performs the specific action being tested, and Assert verifies the result matches expectations. This structure makes tests readable and intent clear.

Test coverage metrics measure the percentage of code exercised by tests, but coverage alone doesn't guarantee quality. Well-designed tests focus on critical paths, edge cases, and error conditions rather than achieving maximum line coverage.

---
*No notes yet.*
