# Rotom Repository Tooling Overview

This directory contains the guarded repository helper, compatibility entry points, and offline validation scripts. These are tooling and tests, not Rotom Support members or Available Sources.

## Commands and checks

- [`rs`](rs) implements the supported repository workflow, including path resolution, status, lint, synchronization checks, diffs, history, commits, and pushes.
- [`rr`](rr) is the compatibility wrapper for `rs`.
- [`test-rs-cli`](test-rs-cli) exercises the helper in an isolated fixture; [`test-rr-cli`](test-rr-cli) delegates to it for compatibility coverage.
- [`test-rr-runbooks`](test-rr-runbooks) validates the permanent structure, links, safety markers, and membership assumptions of the numbered runbooks.
- [`test-guides`](test-guides) validates supplementary material under [`guide/`](../../guide/README.md) without expanding RS membership.

Use `rs` for routine Git operations and do not bypass a safety failure. Tooling changes must follow the root [`AGENTS.md`](../../AGENTS.md), remain compatible with the [canonical maintenance contract](../../runbook/00-Rotom-Change-Log.md#current-documentation-maintenance-rules), and be covered by the relevant CLI or content validation. Installed copies are live-state changes and require separate authorization from repository edits.
