# Disclosed reconstructed history for canonical-json-digest

This reference implementation and all of the following milestone commits were prepared on **24 October 2026** with AI coding assistance.

**Every recorded author and committer date in this timeline is synthetic. These dates are not evidence that the code was written, tested, deployed, or used professionally in the past.**

This snapshot is milestone 11 of 19. It is an incomplete tutorial stage; source, fixtures, tests, the CLI, and automation are introduced progressively.

The progression decomposes already-completed October 2026 code into meaningful additions. It is not recovered original development history. Publication time is separate from the synthetic Git timestamps.

## Reconstructed milestone plan

| Stage | Synthetic date | Change |
| --- | --- | --- |
| 1 | 2023-05-10T16:23:55+05:30 | add repository metadata and Python ignore rules (present) |
| 2 | 2023-06-20T17:28:35+05:30 | add module imports, constants, and scope documentation (present) |
| 3 | 2023-07-16T09:26:29+05:30 | reject duplicate JSON keys and non-finite parser constants (present) |
| 4 | 2023-10-18T11:02:17+05:30 | validate JSON values and produce deterministic UTF-8 bytes (present) |
| 5 | 2023-11-29T15:13:24+05:30 | derive SHA-256 content digests from canonical bytes (present) |
| 6 | 2024-06-17T10:00:13+05:30 | add the deterministic demonstration and command-line entry point (present) |
| 7 | 2024-08-09T14:49:28+05:30 | test object order and whitespace do not change digest (present) |
| 8 | 2024-10-02T12:09:35+05:30 | test array order matters (present) |
| 9 | 2024-10-05T18:29:52+05:30 | test duplicate keys rejected at any depth (present) |
| 10 | 2024-10-26T19:44:36+05:30 | test nonfinite numbers rejected (present) |
| 11 | 2024-11-21T14:20:51+05:30 | test non json values and keys rejected (present) |
| 12 | 2024-12-11T10:00:57+05:30 | test utf8 and digest known bytes (later stage) |
| 13 | 2025-02-24T12:28:12+05:30 | test cycles rejected but reused children allowed (later stage) |
| 14 | 2025-04-07T14:04:55+05:30 | test lone surrogates rejected (later stage) |
| 15 | 2025-05-16T09:06:27+05:30 | test float and integer remain distinct (later stage) |
| 16 | 2025-07-16T09:54:57+05:30 | add isolated tests, demo, and help verification (later stage) |
| 17 | 2025-09-05T09:02:32+05:30 | add the hosted Python verification workflow (later stage) |
| 18 | 2026-01-04T19:59:50+05:30 | record the completed local verification and its limits (later stage) |
| 19 | 2026-08-15T09:21:08+05:30 | Document usage, limitations and the disclosed reconstructed timeline (later stage) |
