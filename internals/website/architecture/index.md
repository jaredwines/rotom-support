# Rotom Architecture

This page is for readers who need a quick map of Rotom before choosing an operational document. It summarizes the verified infrastructure, application, access, storage, recovery, and ownership boundaries; the numbered [Runbook](../runbook/index.md) remains authoritative for current facts and procedures.

## Start here

- For a detailed newcomer-oriented map, read the [Rotom Architecture System: services, routes, storage, and protection](rotom-architecture-system.md).
- For an active task or fault, use the [Server Inventory task and symptom router](../runbook/01-Rotom-Server-Inventory.md#start-by-task-or-symptom).
- For total loss of PVE and Rotom, follow the [Total-Loss Recovery emergency path](../guides/pve-and-rotom-total-loss-recovery.md#emergency-recovery-path).

## System at a glance

### Physical infrastructure and virtualization

Rotom is a Debian virtual machine (VMID 100) on the `pve` Proxmox VE host. The VM uses reserved LAN address `192.168.1.69`; PVE uses `192.168.1.68`; and the UniFi NAS uses `192.168.1.70`. The [Server Inventory current Rotom summary](../runbook/01-Rotom-Server-Inventory.md#2-current-rotom-summary) is the authoritative high-level system map.

### Application platform

Compose-managed workloads are grouped under five local domains: Platform, Libraries, Hosted Websites, Game Servers, and Smart Home. [Docker Services: current runtime and service contracts](../runbook/02-Docker-Services.md#1-current-docker-runtime-and-deployment-state) owns their stack definitions, local application state, identities, and recovery boundaries. Persistent state stays on the VM unless the Runbook explicitly assigns it to NAS-backed storage.

`mkdocs-rr` is the read-only documentation service. Its guarded publisher uses a root-owned deployment clone, a fixed source allowlist, a clean-tree and fast-forward check, an isolated build, and an atomic generated-site swap. The service remains loopback-only; it is not a source of authority or a writable documentation checkout.

### Network, DNS, and private access

Nginx Proxy Manager is host-networked and terminates TLS for Rotom application routes. Cloudflare DDNS maintains the Rotom hostname, while wildcard DNS and the certificate cover supported subdomains. The Support portal is proxied to Rotom's loopback-only MkDocs endpoint and retains the trusted-LAN access policy. [Network and Domains: current access paths](../runbook/03-Network-and-Domains.md#2-current-access-paths) owns the exact routes, listeners, certificate, and access-list facts.

### Storage, backup, and recovery

Five NFSv3 systemd automount contracts provide scoped NAS dependencies. Recovery uses complementary Rotom Restic, PVE Restic, VM-backup, and NAS-snapshot layers; they are not interchangeable. Confirm the exact contract in [NAS and Storage: current storage and recovery policy](../runbook/04-NAS-and-Storage.md#1-current-storage-and-recovery-policy) and [Backup and Restore: current recovery architecture](../runbook/05-Backup-and-Restore.md#1-current-recovery-architecture) before relying on a recovery path.

### Security and ownership boundaries

Human administration and locked service identities are intentionally separate. Docker, NPM, generated documentation, and backup credentials have distinct ownership and access constraints. [Users and Permissions: current identity and access model](../runbook/07-Users-and-Permissions.md#1-current-identity-and-access-model) is authoritative for those contracts.

## How to use this overview

Use this page to understand relationships and select the right owner, not as a procedure. If it conflicts with the numbered Runbook, preserve the discrepancy, verify the evidence, and reconcile the supplementary page through the Runbook maintenance process.
