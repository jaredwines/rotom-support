# 06 - Maintenance and Automation

**Documentation set:** Rotom Support
**Document role:** Canonical source for scheduled/routine maintenance, automation, monitoring behavior, and operational administration workflow
**Hosts:** PVE hypervisor `pve` and Debian VM `rotom`  
**Baseline verified:** Current state reconciled through 2026-10-17; see outstanding items for remaining verification
**Documentation updated:** 2026-10-20 — Resolve the Arcane Analytics Heartbeat observation
**Related canonical sources:** `01-Rotom-Server-Inventory.md`, `02-Docker-Services.md`, `04-NAS-and-Storage.md`, `05-Backup-and-Restore.md`, `07-Users-and-Permissions.md`
**Index:** [01-Rotom-Server-Inventory.md](01-Rotom-Server-Inventory.md)  
**Change history and update rules:** [00-Rotom-Change-Log.md](00-Rotom-Change-Log.md)

Record substantive changes to this document in the change log as part of the same task, following its maintenance guide.

## Start by Task or Symptom

- Failed timer, missed run, failed oneshot service, or automation drift: use [Investigate a Failed Timer or Automation](#investigate-a-failed-timer-or-automation).
- Rotom Restic execution or repository behavior: use [document 05](05-Backup-and-Restore.md#start-by-task-or-symptom).
- NAS recovery-helper behavior: establish storage state in [document 04](04-NAS-and-Storage.md#diagnose-and-recover-a-configured-nas-mount), then use this document for service/timer scheduling.
- Container lifecycle or health: use [document 02](02-Docker-Services.md#start-by-task-or-symptom).

## Investigate a Failed Timer or Automation

### Outcome, entry conditions, exclusions

Identify whether a supported timer/worker failed because of schedule, dependency, storage, application, or policy state, and retry only the existing owning service when its desired action and safety conditions are established. Exclude new automation, schedule changes, package-policy changes, retention/prune, destructive cleanup, and PVE action not executed by Jared.

### Risk, preflight, and Stop conditions

Inspection is read-only. Starting a service may change Rotom and, for backup workers, protected repository state. Before a retry, identify the exact timer/service pair, last/next trigger, current process state, dependencies, and documented owner. Stop if another run is active, the unit invokes an unreviewed script, required storage or credentials are unavailable, the desired outcome is unclear, or logs show protected-data/repository damage.

**Read-only**

```bash
systemctl list-timers --all --no-pager
systemctl --failed --no-pager
systemctl status UNIT.timer UNIT.service --no-pager
sudo journalctl -u UNIT.timer -u UNIT.service -n 160 --no-pager
systemctl cat UNIT.timer UNIT.service
```

Replace `UNIT` only with the exact documented unit name.

### Smallest targeted action and immediate result

Correct the owning dependency first: document 04 for NFS, document 05 for Restic/repository issues, document 02 for application state, or document 07 for identity/permission state. When current policy clearly supports a retry and no concurrent work exists:

**Changes Rotom**

```bash
sudo systemctl start UNIT.service
```

For `rotom-restic-backup.service`, this label is instead **Changes Rotom and protected storage/repository state** and the complete document 05 procedure is mandatory. For any PVE unit, the action is **PVE — Jared executes**.

### Verification, safe stop, branches, and evidence

Verify the exact service result, journal, dependency state, downstream application outcome, next timer trigger, and `systemctl --failed`. Do not repeatedly retry a deterministic failure. A failed oneshot normally needs no rollback; preserve logs, leave the timer policy unchanged, and stop safely. If a partial action changed state, use the owning document's rollback guidance.

Retain the unit name, trigger time, exit result, sanitized journal error, dependency finding, retry authorization, downstream check, and next trigger. Revalidate after any service, timer, schedule, worker, dependency, update process, monitoring behavior, or automation-policy change.

## Navigation and Authority

- Start with **1. Current Maintenance and Automation** for active timers, helpers, and routine operating behavior.
- Use **5. Command-Line Safety and Administration**, **6. Documentation and Synchronization Workflow**, and **7. RS Validation** for administration and RS workflow.
- Treat retired automation and preserved historical evidence as context, not as active scheduling or execution instructions.
- Review **Outstanding / Needs Verification** before depending on an automation, notification, certificate, or recovery behavior.
- This file owns operational workflow and automation; backup semantics, service deployment, and privileges remain canonical in documents 05, 02, and 07.

## 1. Current Maintenance and Automation

### Rotom guest

| Function | Current implementation |
|---|---|
| NAS-backed Docker recovery | `rotom-nas-docker-recovery.service`; validates and recovers only eligible Libraries consumers |
| Rotom Restic Backup | `rotom-restic-backup.timer`; around `03:00`, persistent, randomized delay up to ten minutes |
| qBittorrent mount guard | `rotom-qbittorrent-media-guard.timer`; validates Libraries NFS/sentinel and stops qBittorrentVPN if unsafe |
| Weekly maintenance | `rotom-weekly-maintenance.timer`; Sunday `01:15`; ordinary package upgrades without automatic reboot |
| Backup status | `rotom-restic-backup-status-api.service`; read-only port `8787` |

The older reboot-capable `weekly-linux-update` script exists, but its cron schedule is intentionally absent. Do not reinstall that schedule merely because the script remains.

### PVE host

| Function | Current implementation |
|---|---|
| PVE Restic Backup | Daily `04:00` service/timer |
| Rotom VM Backup | Native Proxmox job `rotom-vm-daily` at `05:00` |
| Weekly maintenance | `pve-weekly-maintenance.timer`; Sunday `00:30` |
| CPU-temperature status | Read-only API at `192.168.1.68:8788` |
| Backup status | Read-only API at `192.168.1.68:8789` |
| NIC stability / Wake-on-LAN | Interface hooks retain WOL and the documented TSO/GSO workaround |

PVE actions remain Jared-executed where labelled.

### Bluetooth adapter

PVE VM 100 passes the Intel Bluetooth adapter (`8087:0aaa`) to Rotom as `usb1`; the existing ConBee II uses `usb0`. Rotom has the Debian `bluez` and `firmware-iwlwifi` packages, and `bluetooth.service` is enabled. After Jared rebooted PVE on 2026-10-16, Rotom detected the adapter, the service was active, and the powered controller was discovering nearby devices. The current boot's kernel firmware log was not accessible during that check; pairing and data exchange with a specific device remain unverified. PVE passthrough is host-specific and must be revalidated when the host or adapter changes.

## 2. Libraries Recovery Automation

The NAS recovery helper handles the boot-time race in which Docker requests Libraries before the NAS is reachable. It resets failed generated units, arms `mnt-nas\x2dlibraries.automount`, starts or triggers the exact mount, verifies the documented NFS source plus `games/`, `movies/`, `shows/`, `torrents/`, `documents/paperless/`, and the readiness sentinel, and fails closed if the automount does not remain active.

The helper can recover only supported containers with an eligible restart policy and a recorded NAS/mount startup-failure signature. It leaves running and intentionally stopped containers untouched. Its earlier verified reboot path required the configured retry about thirty seconds after the first pre-NAS attempt. The 2026-10-20 Libraries-layout reboot verified the new directory contract: the exact export returned read/write, both generated unit layers were active, and the helper completed successfully with exit zero.

## 3. Arcane Automation

On 2026-10-17 Jared accepted the following Arcane settings as the intended baseline: automatic update enabled daily at midnight (`0 0 0 * * *`) with an empty container-exclusion list; automatic healing enabled every five minutes (`0 */5 * * * *`) with an empty exclusion list; no more than five healing restarts in a 30-minute window; scheduled pruning disabled; and project-symlink following enabled. Arcane project polling remains enabled hourly.

The final Docker reset intentionally removed Arcane's stored database and settings. Afterward, Jared restored the account credentials independently and confirmed the UI controls with Auto Update, Image Update Watcher, and Auto Heal enabled; Scheduled Prune, Image Auto Patch, and Vulnerability Scan disabled. No credential value is recorded. This confirms the saved control posture, not the exact schedules, restart threshold, symlink setting, or polling cadence; reread those values before relying on them operationally. The same UI screenshot showed the most recent Analytics Heartbeat run failed, while Image Update Watcher, Docker Client Refresh, and Environment Health showed successful runs. Sanitized logs attributed the heartbeat failure to a `429 Too Many Requests` response from Arcane's analytics endpoint; Arcane scheduled an automatic retry after one hour, and no configuration change or repeated manual run is needed.

Arcane now uses `https://arcane.rotom.casa` and deliberately has zero registered Projects. Its Compose definition has neither `PROJECTS_DIRECTORY` nor a host Compose-directory bind, so the Projects UI cannot directly edit the host Compose trees. Arcane retains writable appdata and Docker socket access plus read-only Platform secrets. Docker-socket access remains root-equivalent and is not a security boundary.

Arcane automatic activity has recreated or updated containers in the past. Empty exclusion lists mean every otherwise eligible container is in scope for those functions; they do not authorize image, named-volume, stale-project-row, or intentionally stopped-service cleanup.

Cloudflare DDNS checks the external address every minute. Its Compose definition explicitly uses router DNS `192.168.1.1`; this was added on 2026-10-17 after the container's embedded resolver repeatedly failed to reach Cloudflare. The recreated container resolved successfully and reported the existing A record already current.

## 4. Monitoring and Retired Alerting

Homepage, Glances, the Rotom/PVE backup-status APIs, and the PVE CPU-temperature API are current read-only monitoring surfaces. Homepage’s **NAS Storage** card uses Glances filesystem capacity for `/mnt/host-root/mnt/nas-libraries`; the NFS mounts report capacity for the shared underlying NAS volume, not the Libraries folder alone. Homepage no longer has a separate UNAS Reachability ping card.

Uptime Kuma and the Rotom/PVE alert-delivery layer are retired. No worker, service, timer, script, Homepage mapping, or delivery input remains. An empty root-only `/var/lib/rotom-alerting` directory persists; it is not active state and is not authorized for deletion by documentation cleanup.

NPM certificate renewal remains active. Diagnose renewal by inspecting the currently served certificate, NPM state, and logs without exposing protected inputs.

## 5. Command-Line Safety and Administration

- Use small, reviewable command blocks.
- Read before writing.
- Do not expose secrets, protected environment files, repository passwords, private keys, cookies, or tokens.
- Do not use `chmod 777`.
- Keep PVE commands separate and clearly labelled for Jared when required.
- Stop if a command would delete, recursively rewrite, remount, prune, overwrite protected state, or affect more than the approved target.

## 6. Documentation and Synchronization Workflow

Resolve the active checkout with `rs path`. On Rotom, `/usr/local/bin/rs` is the canonical implementation; `/usr/local/bin/rr` delegates to it for compatibility while Mac and other dependencies remain unverified. The prior installed helper is retained as a recovery copy. Repository `AGENTS.md` and document 00 govern RS changes.

Supported helper commands are `path`, `status`, `check`, `lint`, `pull`, `diff`, `log`, `commit`, `push`, and `help`. Do not bypass a helper safety failure with reset, clean, merge, rebase, force-push, or ad-hoc publication.

The Rotom RS checkout is `/home/jared/rotom-support`; `/home/jared/.config/rr/repository` points to it, and its origin is `git@github.com:jaredwines/rotom-support.git`. The Mac checkout has the verified `rs` helper and an `rr` compatibility wrapper; the earlier Mac checks and helper installation are recorded in document 00. All intentionally tracked content in the repository is RS; untracked, ignored, temporary, generated, and Git-internal checkout content is not included merely by location. The private site publishes from the separate root-owned deployment clone `/srv/rotom/appdata/platform/mkdocs-rr/repository` using `https://github.com/jaredwines/rotom-support.git`, branch `main`. `/usr/local/sbin/rotom-support-sync` verifies a clean deployment checkout and fast-forward-only upstream, builds with the pinned MkDocs image in isolated staging directories, excludes paths with any component beginning with `.git`, source-code and systemd unit extensions, files whose Git index mode is executable, and files with a script shebang from navigation and raw downloads, validates every remaining tracked file against its raw copy and navigation entry, and replaces the site only after validation. Using the Git-tracked executable mode prevents POSIX ACL masks on the deployment clone from reclassifying ordinary documents. Markdown and Mermaid diagrams are rendered, with an expand control for each diagram; other text is displayed as source; published original bytes are available under `/raw/`. The repository README supplies the home page. Markdown navigation labels use each file's level-one title, falling back to its filename if no title is present; repository filenames and raw copies remain unchanged. Tabs organize files into Runbook, Architecture, Guides, Internals, and Repository. Nested folder labels capitalize their first letter without changing paths, and the contents panel follows document headings. Publication preserves each area's defined role: the runbook remains the primary operational authority, while architecture, guides, internals, and root files retain their narrower purposes. Symlinks and unsupported filenames stop publication rather than being followed. The previous site is retained as `site.before-mirror.*`; the previous publisher is retained as `publish-source.before-repository-mirror-20261017`. The installed builder and timer definitions are recorded under `internals/publisher/`.

The `rotom-support-sync.timer` starts the updater at boot and checks again five minutes after each run. An unchanged revision does not rebuild or restart the site. Failed fetch, validation, or build leaves the published site intact; failed container recreation attempts to restore the previous site. The existing `scripts/publish-source` entry point delegates to this updater; `MKDOCS_RR_VALIDATE_ONLY=1` performs a non-publishing build.

### Verify or recover repository publication

**Outcome and entry conditions:** Use this procedure when the site is stale or a scheduled synchronization fails. Preserve the site, deployment clone, and recovery copies. Do not reset, clean, or force a divergent clone.

**Read-only**

Check `systemctl status rotom-support-sync.timer rotom-support-sync.service`, the service journal, the deployed commit in `/srv/rotom/appdata/platform/mkdocs-rr/site/.repository-commit`, and the root-owned deployment clone's branch, status, and upstream. Compare with GitHub `main` and check loopback HTTP on `127.0.0.1:8082`. Do not display credentials.

**Stop conditions:** Stop and investigate a dirty or divergent clone, an unexpected remote, unavailable GitHub, failed validation, an unexpected site path, or a failed container. Preserve the current site and backup directories; do not delete or replace data to make a check pass.

**Changes Rotom**

After resolving the cause and confirming the expected remote and clean clone, run `sudo /usr/local/sbin/rotom-support-sync --validate-only`; if it passes, run `sudo /usr/local/sbin/rotom-support-sync`. The latter publishes the validated GitHub revision and recreates only `mkdocs-rr`. Confirm the deployed commit matches GitHub, representative pages and raw files return successfully, the timer is active, and the service log reports success. Record the revision and validation outcome.

If publication or recreation fails, the updater retains or attempts to restore the previous site. Inspect its log and the exact `site.before-mirror.*` candidates before any manual recovery; do not overwrite a candidate or perform cleanup without verifying the target and impact. Revalidate this workflow when the publisher, repository structure, timer, access boundary, build image, or deployment paths change.

Available Sources is a separate, manually maintained publication or reference destination, not the RS membership boundary or a complete repository copy. Replacement remains manual by Jared.

## 7. RS Validation

The tracked `internals/tooling/rs` owns offline lint. The legacy test filename `test-rr-runbooks` remains in use; `test-rr-cli` delegates to `test-rs-cli`. Before publication, the maintenance contract requires:

- `internals/tooling/test-rr-runbooks`
- `internals/tooling/test-rs-cli`
- `internals/tooling/rs lint`
- `git diff --check`
- semantic ownership/duplication review
- `rs check` at a clean checkpoint

`rs check` performs a network comparison and requires explicit authorization when the task withholds it.

## 8. Outstanding / Needs Verification

- Root-only rollback archive retention.
- PVE iGPU option-ROM warning and historical reset/NIC stability only if symptoms recur.
- Incident-specific recovery-point selection.
- Fran's deferred SSH-key setup.
- Bluetooth pairing and data exchange with a specific device; post-reboot kernel firmware log verification.

## 9. Related Documentation

- [02 — Docker Services](02-Docker-Services.md)
- [04 — NAS and Storage](04-NAS-and-Storage.md)
- [05 — Backup and Restore](05-Backup-and-Restore.md)
- [07 — Users and Permissions](07-Users-and-Permissions.md)

## Maintenance and Revalidation Triggers

Follow the canonical [Runbook-First Maintenance Standard](00-Rotom-Change-Log.md#runbook-first-maintenance-standard). Revalidate after a service, timer, schedule, worker, update policy, monitoring endpoint, maintenance procedure, RS tool, checkout path, RS membership/publisher source selection, automation dependency, Bluetooth adapter, firmware, or PVE passthrough changes. Revalidate the supplementary total-loss guide when a recovery dependency changes.
