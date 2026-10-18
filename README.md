# Rotom Support Overview

This repository is the Git working copy for **Rotom Support** (**RS**). RS is all intentionally tracked repository content; local untracked files, ignored files, temporary artifacts, generated output, and Git's internal metadata are not RS merely because they exist inside the checkout.

The RS describes supported state. It distinguishes **Current**, **Historical**, **Retired**, **Proposed**, and **Needs Verification** information so that plans and old evidence are not mistaken for live configuration.

## Start here

Begin with [01 - Rotom Server Inventory](runbook/01-Rotom-Server-Inventory.md), the architecture and navigation index. For how the documentation is maintained and for the historical record, see [00 - Rotom Change Log](runbook/00-Rotom-Change-Log.md).

Use this reading order for administration or recovery:

1. Start with document 01 and choose the task or symptom.
2. Follow its link to the canonical procedure in documents 02–07, or to the path reference in 08.
3. Read the procedure's current-state inputs, preflight, and stop conditions before taking action.
4. Treat reconstruction, retired, and historical sections as evidence, not current instructions.

## Documentation map

The primary operational authority within RS is the Core Numbered Reference Set in `runbook/`:

| Document | Purpose |
| --- | --- |
| [00 - Rotom Change Log](runbook/00-Rotom-Change-Log.md) | Canonical maintenance contract and material change history |
| [01 - Rotom Server Inventory](runbook/01-Rotom-Server-Inventory.md) | Task router, symptom index, architecture overview, and source map |
| [02 - Docker Services](runbook/02-Docker-Services.md) | Container and application operations, recovery, and reference |
| [03 - Network and Domains](runbook/03-Network-and-Domains.md) | Listener, routing, DNS, proxy, TLS, and access operations |
| [04 - NAS and Storage](runbook/04-NAS-and-Storage.md) | NAS/NFS diagnosis, mount recovery, and storage reference |
| [05 - Backup and Restore](runbook/05-Backup-and-Restore.md) | Backup execution, assurance levels, repositories, and restore operations |
| [06 - Maintenance and Automation](runbook/06-Maintenance-and-Automation.md) | Timers, automation, updates, and routine administration |
| [07 - Users and Permissions](runbook/07-Users-and-Permissions.md) | Identity, ownership, permission, privilege, and access operations |
| [08 - Rotom Directory Tree](runbook/08-Rotom-Directory-Tree.txt) | Current filesystem reference with historical paths clearly separated |

The runbook is RS's primary authority for Rotom's documented current state, operation, troubleshooting, configuration, maintenance, migration, recovery, Docker, networking, storage, backups, permissions, and services. The current repository-area model and source map live in [01 - Rotom Server Inventory](runbook/01-Rotom-Server-Inventory.md).

## Repository map

- [`runbook/`](runbook/README.md) contains the authoritative Core Numbered Reference Set and primary operational documentation.
- [`architecture/`](architecture/README.md) contains explanatory system architecture and orientation.
- [`guide/`](guide/README.md) contains supplementary task and recovery guides that do not replace runbook authority.
- [`internals/`](internals/README.md) contains agent support, repository tooling, validation, and publication implementation.
- Root-level tracked files provide repository governance, navigation, and Git configuration or metadata according to each file's purpose.

All intentionally tracked files in these areas are RS components. Membership does not give supplementary, internal, or navigational material authority over the applicable current runbook.

## Supplementary guides

Every tracked file under `guide/` is an RS component but remains outside the Core Numbered Reference Set and is validated separately. Use [PVE and Rotom Total-Loss Recovery](guide/PVE-and-Rotom-Total-Loss-Recovery.md) for blank-hardware disaster-recovery orchestration and acceptance. The repository mirror publishes the guide without making it a canonical operational fact owner.

The [Rotom Architecture System](architecture/Rotom-Architecture-System.md) is an explanatory RS component. It helps readers understand the system but does not override current runbook facts or procedures.

Available Sources is a separate, manually maintained publication or reference destination. It is not the RS membership boundary or a complete copy of the repository; Jared manually replaces its contents.

## Using this repository

- Treat dated evidence and explicit state labels as more authoritative than unstated assumptions.
- Use the current runbook documents for operational reference; do not use older change-log entries as instructions to recreate prior state.
- Read the canonical maintenance contract in [00 - Rotom Change Log](runbook/00-Rotom-Change-Log.md) before preparing an RS change.
- Use the guarded `rs` helper for normal repository operations. `rs path` resolves the active checkout.
- Run the repository's offline `internals/tooling/rs lint` validation before synchronization checks. After the matching helper version is installed, `rs lint` is equivalent.
- From any directory, run `bash "$(rs path)/internals/tooling/test-rr-runbooks"` to validate the numbered runbook's permanent structure, authority model, and nine-file Core Numbered Reference Set.
- Run `bash "$(rs path)/internals/tooling/test-guides"` separately to validate the guide area under its narrower role.

## Safety

Never commit passwords, tokens, private keys, VPN credentials, cookies, Home Assistant secrets, Restic passwords, or other authentication material. Do not publish or share repository contents without reviewing them for sensitive operational, personal, or infrastructure information.

## Keeping the RS current

The canonical RS maintenance contract is [00 - Rotom Change Log](runbook/00-Rotom-Change-Log.md). It defines the required evidence standard, consistency review, state labels, dated change-history entries, and the supported publication workflow. This README is repository navigation and does not replace that contract.
