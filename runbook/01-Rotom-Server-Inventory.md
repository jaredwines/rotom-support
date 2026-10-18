# 01 - Rotom Server Inventory

**Documentation set:** Rotom Support
**Document role:** Task-first starting page, symptom router, architecture overview, and source map
**Hosts:** PVE hypervisor `pve` and portable Debian VM `rotom`  
**Baseline verified:** Mixed evidence dates; see section-level evidence notes  
**Documentation updated:** 2026-10-17 — Define RS repository membership and authority
**Related canonical sources:** `02-Docker-Services.md`, `03-Network-and-Domains.md`, `04-NAS-and-Storage.md`, `05-Backup-and-Restore.md`, `06-Maintenance-and-Automation.md`, `07-Users-and-Permissions.md`, `08-Rotom-Directory-Tree.txt`
**Change history and update rules:** [00-Rotom-Change-Log.md](00-Rotom-Change-Log.md)

## 1. Purpose and Scope

This is the starting page for anyone administering, troubleshooting, maintaining, or recovering Rotom. Use it to choose the canonical procedure, understand the current system at a glance, and identify recorded uncertainty before acting.

This inventory routes work and summarizes cross-system state. The detailed account, container, network, mount, backup, automation, and filesystem registers remain in their numbered subject owners.

**RS state labels:** **Current** means the latest supported recorded state; **Historical** preserves dated evidence that may no longer apply; **Retired** means intentionally no longer active; **Proposed** is not implemented; **Needs Verification** means the RS lacks enough current evidence and should not be treated as settled.

## Start by Task or Symptom

Choose the row that best matches the work. In the destination, read the current-state inputs, read-only preflight, and stop conditions before using a procedure.

| Task or symptom | Canonical destination |
|---|---|
| Website, container, or application unavailable | [02 — container and Docker-backed website diagnosis and recovery](02-Docker-Services.md#diagnose-and-recover-a-container-or-docker-backed-website) |
| Proxy, listener, DNS, TLS, domain, routing, or external-access problem | [03 — end-to-end access-path diagnosis](03-Network-and-Domains.md#diagnose-a-proxy-listener-dns-tls-routing-or-external-access-failure) |
| NAS path, NFS mount, or storage dependency unavailable | [04 — configured NAS-mount diagnosis and recovery](04-NAS-and-Storage.md#diagnose-and-recover-a-configured-nas-mount) |
| Backup execution, failure, repository verification, or restore | [05 — backup and restore task router](05-Backup-and-Restore.md#start-by-task-or-symptom) |
| Timer, scheduled automation, update, or maintenance problem | [06 — automation and maintenance task router](06-Maintenance-and-Automation.md#start-by-task-or-symptom) |
| Permission, ownership, user, group, identity, or access problem | [07 — identity and access task router](07-Users-and-Permissions.md#start-by-task-or-symptom) |
| Filesystem-path lookup | [08 — current and historical filesystem topology](08-Rotom-Directory-Tree.txt) |
| Website repository synchronization or publication | [06 — documentation and synchronization workflow](06-Maintenance-and-Automation.md#6-documentation-and-synchronization-workflow) |
| RS maintenance or publication | [00 — documentation maintenance rules and change history](00-Rotom-Change-Log.md#current-documentation-maintenance-rules) |

Procedures answer **what to do**; current-state sections answer **what exists**. Reconstruction material supports disaster recovery. Historical and retired sections are evidence, not current instructions. Document `00` is the sole RS maintenance authority.

### Maintaining the Runbook-First Model

Follow the canonical [Runbook-First Maintenance Standard](00-Rotom-Change-Log.md#runbook-first-maintenance-standard). Supported tasks must remain reachable from this router within one or two links. Update this table whenever a procedure, heading, filename, destination, or canonical owner changes. This document routes tasks; it does not duplicate complete procedures.

### Recommended reading path

1. Read **Current Rotom Summary** for a system-wide orientation.
2. Use the task router above or **Choose by Subject** below to select the canonical document.
3. In that document, read its navigation/authority block and current-state sections before any procedure.
4. Review **Outstanding and Needs Verification** for uncertainty that must not be guessed through.
5. Consult preserved history only for provenance, rollback context, or reconstruction, and reconcile it with current sections plus read-only live evidence first.

The inventory summarizes cross-system facts but does not replace the detailed subject owners listed below. When a summary and a detailed owner appear inconsistent, preserve both, investigate the evidence dates, and record the discrepancy rather than silently choosing one.

### Jared-confirmed recovery follow-up closure — 2026-10-14

Jared confirmed completion and verification of the current Rotom Restic full-data-read plus restore rehearsal, current Rotom VM Backup VMA verification or disposable restore, Libraries/Paperless NAS snapshot retention plus isolated restore, NAS metadata persistence after a NAS/UniFi Drive event, controlled live Libraries-NFS-loss behavior, end-to-end Wake-on-LAN, VPN credential rotation, UniFi/router-policy review, full isolated Palworld disaster-recovery rehearsal, authenticated Paperless acceptance, Fran PVE browser login, legacy NPM-record review, certificate renewal, and dormant Docker-artifact review. Detailed transcripts, identifiers, and retain/remove decisions were not supplied in this chat; retain historical test evidence below as history, but do not present these items as current gaps.

### Choose by subject

Start here, then follow the canonical subject document instead of relying on duplicated detail:

| Need | Canonical source |
|---|---|
| Documentation governance and dated history | [00 — maintenance contract and protected change history](00-Rotom-Change-Log.md) |
| Containers, Compose, images, and runtime deployment | [02 — Docker service operations and current contracts](02-Docker-Services.md) |
| Addresses, DNS, ports, proxying, TLS, and exposure | [03 — network, domain, and access-path operations](03-Network-and-Domains.md) |
| NAS exports, NFS mounts, storage ownership, and automounts | [04 — NAS storage contracts and mount recovery](04-NAS-and-Storage.md) |
| Backup scope, repositories, verification, and restore | [05 — backup architecture, assurance, and restore procedures](05-Backup-and-Restore.md) |
| Timers, maintenance, monitoring, and administration workflow | [06 — maintenance, automation, and RS tooling](06-Maintenance-and-Automation.md) |
| Accounts, UID/GID contracts, ACLs, sudo, and access policy | [07 — identities, permissions, and administrative access](07-Users-and-Permissions.md) |
| Filesystem topology and important paths | [08 — current topology and retained historical paths](08-Rotom-Directory-Tree.txt) |

Within each subject document, use the current-state sections first. Use historical or pre-migration evidence only for provenance, reconstruction, or recovery; do not replay it as current instruction without reconciling it against live read-only state.

## 2. Current Rotom Summary

**Evidence date:** 2026-10-17 unless a row states otherwise.

Rotom is Debian 13 VMID 100 on Proxmox VE host `pve`. The guest uses reserved address `192.168.1.69`; PVE uses `192.168.1.68`; the UniFi NAS uses `192.168.1.70`.

The verified application topology is **23 running Compose-managed containers, 19 Docker networks, two named volumes, and 18 active Compose definitions**. The nineteenth network is the unattached `rotom-docs_default` network retained with the inactive rollback stack; its existence is not cleanup authorization. The active definitions are grouped under five local domains:

| Domain | Identity | Active roots | Current services |
|---|---:|---|---|
| Platform | `997:5002` | `/srv/rotom/{stacks,appdata,secrets}/platform` | Nginx Proxy Manager, Homepage with Glances, Arcane, Cloudflare DDNS, Rotom Support |
| Libraries | `127:5000` | `/srv/rotom/{stacks,appdata,secrets}/libraries` | Jellyfin, Radarr, Sonarr, Prowlarr, qBittorrentVPN, RomM, Paperless |
| Hosted Websites | `902:5004` | `/srv/rotom/{stacks,appdata}/hosted-websites` | Aloha Millworks, Jared Wines |
| Game Servers | `995:5001` | `/srv/rotom/{stacks,appdata,secrets}/game-servers` | Palworld Jared, Palworld Fran |
| Smart Home | `126:5003` | `/srv/rotom/{stacks,appdata}/smart-home` | Home Assistant, Homebridge |

The five service accounts are locked. Their NSS home fields still name absent `/home/<service>` paths; those paths are not deployment or recovery roots. Human administrators are Jared and Fran. Fran is a full administrator and the sole human member of Docker group GID `989`; Docker membership is root-equivalent.

Homepage and Glances share `/srv/rotom/stacks/platform/homepage/compose.yaml` and the private `homepage_default` network. Glances has no host listener. `jaredwines.com` is intentionally active and publishes only `127.0.0.1:7777:80` for NPM proxy host `8`. Aloha publishes `7778:80`.

Cloudflare DDNS uses explicit container DNS `192.168.1.1`; the container was recreated after the setting was added and then confirmed the current Cloudflare A record was already up to date. Arcane's accepted automation baseline is daily automatic update at midnight with no excluded containers, automatic healing every five minutes with no excluded containers, at most five restarts within a 30-minute window, scheduled pruning disabled, and project-symlink following enabled. Both Palworld servers are intended to remain running under `restart: unless-stopped`.

Remote Desktop Commander runs from `/opt/desktop-commander` as locked identity `desktopcmd` (`1001:1001`). Its former home is absent.

## 3. Current Storage Summary

Rotom has five current guest NFSv3 systemd-automount contracts:

| NAS export | Guest path | Purpose |
|---|---|---|
| `Game_Servers/.data` | `/mnt/nas-game-servers` | Empty Game Servers service boundary; Palworld state remains VM-local |
| `Smart_Home/.data` | `/mnt/nas-smart-home` | Empty Smart Home service boundary; application state remains VM-local |
| `Libraries/.data` | `/mnt/nas-libraries` | Authoritative Libraries payload, including Paperless media |
| `Hosted_Websites/.data` | `/mnt/nas-hosted-websites` | Empty Hosted Websites service boundary; website content remains VM-local |
| `Rotom_Restic_Backup/.data` | `/mnt/nas-rotom-restic-backup` | Rotom Restic repository |

All five were observed mounted read/write on 2026-10-15. The Libraries recovery helper validates the exact source, re-arms the generated automount after boot-time start-limit failure, and conditionally recovers only eligible NAS-dependent containers.

Historical guest paths such as `/mnt/nas-media`, `/mnt/nas-library`, `/mnt/nas-downloaders`, `/mnt/nas-documents`, `/mnt/nas-filesync`, `/mnt/nas-web`, `/mnt/nas-gameserver`, `/mnt/nas-smarthome`, `/mnt/nas-customapps`, `/mnt/nas-apps`, `/mnt/nas-auth`, and `/mnt/nas-shared-drive` are retired locally. Their absence does not establish deletion of NAS-side exports or data. Do not recreate them from historical records.

## 4. Current Backup and Recovery Summary

- **Rotom Restic Backup:** repository `/mnt/nas-rotom-restic-backup/rotom-restic-backup`; worker `/usr/local/sbin/rotom-restic-backup`; timer around `03:00`; retention `7 daily / 4 weekly / 12 monthly`; protected local credential path `/etc/restic/restic-repository-password`.
- **PVE Restic Backup:** repository `/mnt/nas-pve-restic-backup/pve-restic-backup`; daily `04:00`; current credential path `/etc/restic/restic-repository-password` on PVE.
- **Rotom VM Backup:** Proxmox job `rotom-vm-daily`; VMID `100`; daily `05:00`; snapshot mode with zstd; retention `7 daily / 4 weekly / 6 monthly`.
- **NAS-resident application data:** outside Rotom Restic because `/mnt` is excluded. Confirm the applicable NAS snapshot and isolated-restore path before relying on it.

Current recovery procedures and limitations are owned by [05 — Backup and Restore](05-Backup-and-Restore.md). Backup layers are complementary and must not be treated as interchangeable.

On 2026-10-17 Jared confirmed that the router/WAN, PVE, NAS control plane, and NAS snapshot protection are working and asked that further authenticated inspection be waived. This resolves them as active audit gaps; exact control-plane exports were not captured and must still be rechecked during a relevant incident or configuration change.

## 5. Retired Infrastructure Warnings

Uptime Kuma and its Rotom/PVE alert-delivery layer, Syncthing, Gamarr, JDownloader, the ROM importer, Igir automation, and the browser-upload bridge are retired. Their former service ports `3002`, `8384`, `6767`, and `8090` had no listeners during the 2026-10-15 audit.

The former external Docker bridges `rotom-proxy`, `rotom-arr`, and `rotom-monitoring` are absent from active Compose definitions. Actual residual Docker objects were not independently enumerated during the documentation cleanup; do not infer authorization to delete any object.

The alerting worker, units, timers, scripts, Homepage integration, and delivery configuration are absent. An empty root-only `/var/lib/rotom-alerting` directory remains; its existence is not evidence that alerting is active.

## 6. Outstanding and Needs Verification

- Root-only rollback archives for the retired shared Docker bridges and the pre-change NAS-recovery helper were not readable during this audit. Retain or remove them only after a separately authorized exact-path inspection.
- Arcane's two named volumes, stale project rows, and any unreferenced images require exact-object review before cleanup; the accepted automation policy is not cleanup authorization.
- Continue normal monitoring of the historical PVE NIC/reset and non-fatal iGPU option-ROM warning. Do not infer a single cause without new evidence.
- Select and verify an incident-appropriate recovery point at recovery time; retention changes available snapshot and archive sets.

## 7. Rotom Support Model

Rotom Support is all intentionally tracked content in the Rotom-Support repository. Local untracked files, ignored files, temporary artifacts, generated output, and Git's internal metadata are not part of RS merely because they exist inside the checkout. The numbered files `00`–`08` in `runbook/` are the current nine-file Core Numbered Reference Set, and the runbook is RS's primary authority for Rotom's documented current state, operation, troubleshooting, configuration, maintenance, migration, recovery, Docker, networking, storage, backups, permissions, and services.

Other tracked areas are RS components with narrower purposes: `architecture/` explains system relationships and orientation; `guide/` supplies supplementary task and recovery guidance; `internals/` supports agents, tooling, validation, and publication; and root-level files govern or navigate the repository and provide Git configuration or metadata according to their individual purpose. RS membership does not make these areas canonical operational procedure or allow them to override the runbook.

The RS checkout is `/home/jared/rotom-support` on Rotom and `/Users/jared/Documents/ChatGPT/rotom-support` on the Mac. On Rotom, `rs path` resolves the checkout using the existing `~/.config/rr/repository` compatibility fallback; append `runbook/` to locate the numbered files. The Mac resolver configuration points to its checkout; `/usr/local/bin/rs` was independently installed and verified there. Its `/usr/local/bin/rr` is a verified compatibility wrapper for `rs`.

Available Sources is a separate, manually maintained publication or reference destination. It does not define RS membership and must not be treated as the complete repository; replacement remains manual by Jared.

The private **Rotom Support** portal mirrors every tracked file on GitHub `main`, including repository internals and supplementary guides, with the repository README as its home page. Original bytes are available under `/raw/`; publication does not alter repository membership, the distinct purpose and authority of each area, or the contents of Available Sources. The publisher checks for changes every five minutes and retains a previous site before each replacement. See [06 — Documentation and Synchronization Workflow](06-Maintenance-and-Automation.md#6-documentation-and-synchronization-workflow).

## 8. Current Source Map

| Repository area | Role and authority |
|---|---|
| `runbook/` | Primary operational documentation and documented-current-state authority; numbered fact and procedure ownership is listed below |
| `architecture/` | Explanatory architecture and orientation; must defer to applicable current runbook facts and procedures |
| `guide/` | Supplementary task and recovery orchestration; separately validated and not a canonical operational fact owner |
| `internals/` | Agent support, guarded tooling, tests, and publication implementation; not an operational runbook collection |
| Root-level tracked files | Repository governance, navigation, and Git configuration or metadata according to each file's purpose |

If another RS component conflicts with the applicable current runbook about Rotom's operation or documented current state, preserve and report the discrepancy, investigate the evidence, and resolve current guidance in favor of the runbook authority rather than silently rewriting either source.

### Core Numbered Reference Set

| File | Canonical subject |
|---|---|
| `00-Rotom-Change-Log.md` | Maintenance contract and protected history |
| `01-Rotom-Server-Inventory.md` | Task router and current high-level inventory |
| `02-Docker-Services.md` | Applications, containers, Compose, and service recovery |
| `03-Network-and-Domains.md` | Addressing, listeners, DNS, TLS, proxying, and access |
| `04-NAS-and-Storage.md` | NAS exports, mounts, storage identity, and mount recovery |
| `05-Backup-and-Restore.md` | Backup systems, recovery evidence, and restore procedures |
| `06-Maintenance-and-Automation.md` | Timers, maintenance, monitoring, and RS tooling |
| `07-Users-and-Permissions.md` | Accounts, ownership, privilege, ACLs, and access |
| `08-Rotom-Directory-Tree.txt` | Concise current topology and recovery-critical paths |

## 9. Canonical Fact Ownership

Document 01 routes tasks and summarizes current state; it does not replace the detailed owning documents. Application facts belong to document 02, transport to 03, storage and NAS contracts to 04, backup/recovery facts and ordinary restores to 05, automation to 06, identities to 07, topology to 08, and governance/history to 00. The repository's supplementary total-loss guide orchestrates these subjects without becoming an RS fact owner.

When a current fact changes, update its owner, affected runbook procedure, task-router destination if needed, revalidation triggers, structural tests, and the protected change log in the same authorized task.
