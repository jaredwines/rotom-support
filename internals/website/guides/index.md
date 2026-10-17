# Rotom Guides

This page is for Rotom administrators and recovery operators who know what they need to do but are not sure which document owns the work. Use it to choose an entry point; follow the linked Runbook procedure for current facts, safeguards, and commands.

## Start here

- For routine administration or an active fault, start with the [Server Inventory task and symptom router](../runbook/01-Rotom-Server-Inventory.md#start-by-task-or-symptom).
- For replacement-hardware recovery after losing both PVE and Rotom, use the [PVE and Rotom Total-Loss Recovery guide](pve-and-rotom-total-loss-recovery.md).
- If you already know the affected area, choose the matching task below.

These guides and indexes are explanatory entry points. The numbered Runbook remains the operational authority.

## Applications and access

### Deploy or recover a Docker application

Use [Docker Services: container and website diagnosis](../runbook/02-Docker-Services.md#diagnose-and-recover-a-container-or-docker-backed-website) for Compose contracts, persistent-data boundaries, read-only preflight, stop conditions, verification, and recovery. Inspect the existing `compose.yaml` before changing it, and do not recreate unrelated containers.

### Trace a domain, proxy, TLS, or listener problem

Use [Network and Domains: access-path diagnosis](../runbook/03-Network-and-Domains.md#diagnose-a-proxy-listener-dns-tls-routing-or-external-access-failure) to check client resolution, TLS, the Nginx Proxy Manager route and access list, the listener, and the application upstream. A working backend alone does not prove the complete access path is correct or safely exposed.

## Storage, backup, and recovery

### Diagnose NAS-backed storage

Use [NAS and Storage: configured-mount diagnosis and recovery](../runbook/04-NAS-and-Storage.md#diagnose-and-recover-a-configured-nas-mount) to identify the exact automount contract, dependent services, ownership model, and safe recovery sequence. A retired guest path does not prove that NAS data was deleted. Do not create an outage merely to test recovery.

### Back up or restore Rotom

Use [Backup and Restore: task and symptom router](../runbook/05-Backup-and-Restore.md#start-by-task-or-symptom) to choose among Rotom Restic Backup, PVE Restic Backup, Rotom VM Backup, and NAS snapshots. The document explains their different scopes, assurance levels, verification requirements, and restore limits. Credential handling and protected repository changes remain separately controlled.

### Recover the complete platform after total loss

Use [PVE and Rotom Total-Loss Recovery: emergency recovery path](pve-and-rotom-total-loss-recovery.md#emergency-recovery-path) only for blank-hardware reconstruction. It coordinates recovery order, evidence gates, safe stops, and final acceptance across the numbered Runbook sources; those sources still own the current operational facts and procedures.

## Maintenance and administration

### Investigate timers, updates, or scheduled work

Use [Maintenance and Automation: task and symptom router](../runbook/06-Maintenance-and-Automation.md#start-by-task-or-symptom) for timers, routine maintenance, monitoring, and the guarded Rotom Support workflow. Begin with read-only evidence and preserve the existing safeguards around backups and publication.

### Resolve an identity, ownership, or access problem

Use [Users and Permissions: identity and access task router](../runbook/07-Users-and-Permissions.md#start-by-task-or-symptom) for account state, UID/GID contracts, filesystem ownership, ACLs, sudo, Docker access, and authentication boundaries.

### Find an important path

Use the [Rotom Directory Tree current-topology reference](../runbook/08-Rotom-Directory-Tree.txt) to locate service roots, persistent data, mountpoints, backup paths, and retained recovery artifacts. Treat its historical and retired paths as evidence, not instructions to recreate them.

## Using Codex with Rotom

Resolve the checkout with `rs path`, read the repository instructions and the relevant numbered source, inspect live state, and compare it with the documented state. Make the smallest authorized change, verify the result, and update the Runbook from the final supported state. Codex does not replace approval boundaries for protected data, credentials, destructive actions, or PVE work.
