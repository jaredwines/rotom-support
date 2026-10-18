# Rotom Guide Overview

**Artifact class:** Supplementary RS guide; outside the Core Numbered Reference Set

This directory is an RS component containing supplementary guides. The guides remain outside the Core Numbered Reference Set, use guide-specific validation, and may explain or orchestrate material owned by the numbered runbooks, but they do not become authoritative operational fact owners.

## Contents

- [Editing Docker Compose on Rotom](Editing-Docker-Compose.md) maps Compose paths, workloads, and website addresses and provides an editing walkthrough linked to the authoritative runbooks.
- [PVE and Rotom Total-Loss Recovery](PVE-and-Rotom-Total-Loss-Recovery.md) coordinates blank-hardware disaster recovery across the authoritative subject runbooks and includes an optional copy-ready AI-assisted recovery bootstrap with human approval gates and a manual fallback. It is also published in the private repository mirror.

Maintain guide-specific structure and links with [`internals/tooling/test-guides`](../internals/tooling/README.md). RS membership and portal publication do not give a guide runbook authority or make it part of numbered-runbook validation. If a guide change also changes a runbook-owned fact or procedure, update its canonical numbered owner under the [RS maintenance contract](../runbook/00-Rotom-Change-Log.md#current-documentation-maintenance-rules) and validate the two scopes separately. This tracked README is RS navigation, not a numbered runbook or canonical operational source. Available Sources is a separate manually maintained destination.
