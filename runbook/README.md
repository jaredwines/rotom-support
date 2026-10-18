# Rotom Runbook Overview

The numbered `00`–`08` files in this directory are the nine-file **Core Numbered Reference Set** within Rotom Support. Start with [01 — Rotom Server Inventory](01-Rotom-Server-Inventory.md) to choose the correct subject owner; use [00 — Rotom Change Log](00-Rotom-Change-Log.md) for the canonical maintenance contract and protected history.

## Numbered sources

- [`00`](00-Rotom-Change-Log.md): maintenance contract and change history
- [`01`](01-Rotom-Server-Inventory.md): task router, high-level inventory, and source map
- [`02`](02-Docker-Services.md): Docker applications and service recovery
- [`03`](03-Network-and-Domains.md): networking, DNS, proxying, TLS, and access
- [`04`](04-NAS-and-Storage.md): NAS, NFS, storage, and mount recovery
- [`05`](05-Backup-and-Restore.md): backup and restore
- [`06`](06-Maintenance-and-Automation.md): maintenance, timers, automation, and RS tooling
- [`07`](07-Users-and-Permissions.md): identities, ownership, privileges, and access
- [`08`](08-Rotom-Directory-Tree.txt): current and historical filesystem topology

Maintain these sources under the [Runbook-First Maintenance Standard](00-Rotom-Change-Log.md#runbook-first-maintenance-standard) and validate them with [`internals/tooling/test-rr-runbooks`](../internals/tooling/README.md) plus `rs lint`. Detailed procedures and configuration facts belong in their numbered owners, not in this index.

This tracked README is an RS navigation file. It is **not** a numbered runbook, part of the Core Numbered Reference Set, or a canonical operational fact owner. Available Sources is a separate manually maintained destination and does not define this file's RS membership.
