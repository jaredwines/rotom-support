# 05 - Backup and Restore

**Documentation set:** Rotom Support
**Document role:** Canonical source for Restic backup architecture, scope, retention, verification, restore evidence, and recovery boundaries
**Recovery scope:** pre-migration Rotom plus current Proxmox/VM foundation  
**Baseline verified:** Mixed evidence dates; see section-level evidence notes  
**Documentation updated:** 2026-10-17 — Add AI-assisted total-loss recovery routing
**Related canonical sources:** `01-Rotom-Server-Inventory.md`, `04-NAS-and-Storage.md`, `06-Maintenance-and-Automation.md`, `07-Users-and-Permissions.md`
**Index:** [01-Rotom-Server-Inventory.md](01-Rotom-Server-Inventory.md)  
**Change history and update rules:** [00-Rotom-Change-Log.md](00-Rotom-Change-Log.md)

Record substantive changes to this document in the change log as part of the same task, following its maintenance guide.

## Navigation and Authority

- Start with **1. Current Recovery Architecture**, **2. Rotom Restic Backup**, and **3. PVE Restic Backup**.
- Use **7. Restore Procedure** for recovery planning, while verifying the selected recovery point and current target paths before action.
- Treat **6. Recovery-Critical Historical Evidence** as evidence; it does not prove that a snapshot, local artifact, mount, or credential path still exists.
- Review **8. Recovery Limitations and Outstanding Work** before relying on a protection domain.
- For complete loss of the PVE computer, use the supplementary RS [PVE and Rotom Total-Loss Recovery guide](../guide/PVE-and-Rotom-Total-Loss-Recovery.md#emergency-recovery-path). When AI assistance is available, its [AI-Assisted Recovery Bootstrap](../guide/PVE-and-Rotom-Total-Loss-Recovery.md#ai-assisted-recovery-bootstrap) provides a copy-ready coordination prompt with the same authority and stop boundaries. The guide orchestrates recovery but is not a canonical operational fact owner; this document retains ownership of backup architecture and ordinary restores.
- This file owns backup and restore claims; storage locations, automation schedules, and privilege boundaries remain canonical in documents 04, 06, and 07.

## Start by Task or Symptom

| Task | Procedure |
|---|---|
| Run or verify Rotom Restic Backup | [Run and Verify Rotom Restic Backup](#run-and-verify-rotom-restic-backup) |
| Prove a complete Rotom Restic snapshot can be restored and its databases opened | [Rehearse a Complete Rotom Restic Restore in Isolation](#rehearse-a-complete-rotom-restic-restore-in-isolation) |
| Investigate a failed scheduled backup | Perform the runbook preflight, then inspect the owning timer/service in [document 06](06-Maintenance-and-Automation.md#investigate-a-failed-timer-or-automation) |
| Verify repository structure or full pack readability | Use the assurance-level guidance in this document; do not confuse snapshot creation with `restic check` or `restic check --read-data` |
| Restore data | Select a known recovery point and restore to an isolated restricted staging location before planning live replacement |
| PVE Restic or Rotom VM VZDump work | Use the PVE sections in this document; all PVE actions are **PVE — Jared executes** |
| Rebuild from blank replacement hardware | Use the supplementary [PVE and Rotom Total-Loss Recovery guide](../guide/PVE-and-Rotom-Total-Loss-Recovery.md#emergency-recovery-path) |
| Coordinate blank-hardware recovery with AI | Use the guide's optional [AI-Assisted Recovery Bootstrap](../guide/PVE-and-Rotom-Total-Loss-Recovery.md#ai-assisted-recovery-bootstrap); AI does not replace RS, credentials, human approval, or the manual fallback |

## Run and Verify Rotom Restic Backup

### 1. Outcome

Create one Rotom Restic host-data snapshot through the installed worker, apply its established `7 daily / 4 weekly / 12 monthly` automatic-snapshot retention and prune policy, and verify that the run completed successfully and produced a current snapshot. Source data and repository internals must not be manually edited.

### 2. Use this runbook when

- an authorized manual Rotom host backup is needed;
- the scheduled Rotom Restic Backup must be verified;
- the backup timer or service reports failure;
- a backup must be checked before maintenance.

Do **not** use this runbook for:

- PVE Restic Backup;
- Rotom VM VZDump backup;
- NAS-side snapshots;
- restoring over live application data;
- changing include/exclude files, credentials, retention, or repository location;
- deleting, moving, or reorganizing Restic repository internals.

### 3. Impact and authorization

The backup reads configured Rotom paths, refreshes restricted system-information files under `/var/backups/system-info`, creates transactionally consistent copies of the NPM and Home Assistant SQLite databases, writes a tagged Restic snapshot, then runs `forget --prune` under the installed retention policy. It can use significant disk, CPU, NAS I/O, and time.

The repository password file is `/etc/restic/restic-repository-password`. Never print, copy, paste, hash, or record its contents. Backups may contain credentials, certificates, application data, and personal information; do not expose snapshot contents in routine evidence.

### 4. Canonical current-state inputs

| Item | Current contract |
|---|---|
| Manual launcher | `/usr/local/bin/backup-restic-to-nas` |
| systemd service | `rotom-restic-backup.service` |
| timer | `rotom-restic-backup.timer`, daily around `03:00` with up to 10 minutes randomized delay |
| worker | `/usr/local/sbin/rotom-restic-backup` |
| mount | `/mnt/nas-rotom-restic-backup` |
| repository | `/mnt/nas-rotom-restic-backup/rotom-restic-backup` |
| retention | automatic snapshots: 7 daily, 4 weekly, 12 monthly, followed by prune |

Rotom Restic Backup protects configured VM-local host/application state. `/mnt` is excluded; NAS-resident Libraries/Paperless media and the repository itself are separate protection domains.

### 5. Read-only preflight

**Read-only**

```bash
systemctl is-enabled rotom-restic-backup.timer
systemctl is-active rotom-restic-backup.timer \
  rotom-restic-backup.service
systemctl list-timers rotom-restic-backup.timer --all --no-pager
systemctl status rotom-restic-backup.service --no-pager
sudo journalctl -u rotom-restic-backup.service -n 120 --no-pager
findmnt -M /mnt/nas-rotom-restic-backup -t nfs,nfs4 \
  -o TARGET,SOURCE,FSTYPE,OPTIONS
df -h / /var /mnt/nas-rotom-restic-backup
pgrep -af '(^|/)(restic|rotom-restic-backup)( |$)' || true
sudo stat -c '%U:%G %a %n' \
  /usr/local/bin/backup-restic-to-nas \
  /usr/local/sbin/rotom-restic-backup \
  /etc/restic/include.txt \
  /etc/restic/exclude.txt \
  /etc/restic/restic-repository-password
```

List snapshot metadata without printing secret contents:

**Read-only**

**Credential-sensitive**

```bash
sudo env \
  RESTIC_REPOSITORY=/mnt/nas-rotom-restic-backup/rotom-restic-backup \
  RESTIC_PASSWORD_FILE=/etc/restic/restic-repository-password \
  restic snapshots --host rotom --tag automatic --latest 3
```

Expected result is an enabled/active timer, inactive oneshot service between runs, exact active NFS mount, no concurrent Restic process, protected control files, and readable snapshot metadata.

### 6. Stop conditions

Stop before starting a backup if:

- another Restic process or `rotom-restic-backup.service` is active;
- the mount is absent, read-only, or from an unexpected source;
- the repository path or credential-file path differs from the current contract;
- `/`, `/var`, the NAS, or repository lacks safe working capacity;
- required SQLite source databases are missing or report integrity problems;
- include/exclude configuration or worker content differs unexpectedly;
- the repository reports corruption, an unexplained lock, missing packs, or another writer;
- the requested task is actually PVE, VZDump, NAS snapshot, or restore work.

Do not use `restic unlock`, `repair`, `forget`, `prune`, or repository-file deletion as an automatic preflight fix.

### 7. Procedure

The canonical interactive launcher executes the protected worker through `sudo`.

**Changes Rotom and protected storage/repository state**

```bash
/usr/local/bin/backup-restic-to-nas
```

Keep the session attached until the command exits. A successful run must complete both snapshot creation and the installed retention/prune phase with exit status zero.

For a disconnect-safe manually initiated run, use the existing systemd service instead of wrapping the worker in an ad hoc background process:

**Changes Rotom and protected storage/repository state**

```bash
sudo systemctl start rotom-restic-backup.service
```

Use only one launch method for a run. Never start the service while the launcher or another Restic process is active.

### 8. Verification

**Read-only**

```bash
systemctl status rotom-restic-backup.service --no-pager
sudo journalctl -u rotom-restic-backup.service -n 160 --no-pager
findmnt -M /mnt/nas-rotom-restic-backup -t nfs,nfs4 \
  -o TARGET,SOURCE,FSTYPE,OPTIONS
sudo env \
  RESTIC_REPOSITORY=/mnt/nas-rotom-restic-backup/rotom-restic-backup \
  RESTIC_PASSWORD_FILE=/etc/restic/restic-repository-password \
  restic snapshots --host rotom --tag automatic --latest 3
systemctl --failed --no-pager
```

Success requires:

- the command or service exited successfully;
- the backup output contains a completed snapshot rather than only a scan;
- the retention/prune phase completed without error;
- the newest automatic snapshot timestamp corresponds to the run;
- the repository remains reachable through the exact NFS mount;
- no new failed systemd unit or application failure appears.

Snapshot existence proves that Restic committed a snapshot; it does not by itself prove full-pack readability or end-to-end restoration. Use the separately scoped repository-check and isolated-restore procedures in document 05 for those assurance levels.

### 9. Rollback or recovery

A completed backup is not rolled back. Restic retention governs automatic snapshot cleanup. Do not delete a new snapshot merely because the run was manually initiated.

If a run fails before committing a snapshot, source data should remain unchanged. Preserve the error and inspect the repository using supported Restic commands. Do not manually delete files from `data`, `index`, `keys`, `snapshots`, `locks`, or `config`.

If Restic reports a stale lock, first prove that no Restic process and no backup service is active. `restic unlock` changes repository metadata and requires a separately reviewed, explicitly authorized recovery step. Never remove a lock file manually.

### 10. Troubleshooting branches

- **Backup mount absent:** follow the NAS mount runbook for `/mnt/nas-rotom-restic-backup`; do not run the Libraries container helper.
- **Service already active:** monitor it; do not start a second run.
- **Required SQLite database missing or invalid:** stop and repair the application/state discrepancy before backup.
- **Repository locked:** identify the holder. If none exists, prepare a reviewed supported unlock; do not delete lock files.
- **Snapshot succeeds but prune fails:** treat the run as incomplete, preserve logs, and inspect repository health/capacity before any retry.
- **No new snapshot:** confirm the exact exit status and full error. Do not infer success from an inactive oneshot service.
- **Repository check requested:** use document 05; `restic check --read-data` is a long, NAS-intensive operation and is not routine post-run verification.
- **Restore requested:** select and inspect a recovery point, restore into an isolated restricted staging location, verify it, and only then plan any live replacement.

### 11. Evidence to retain

Record the run time in `America/Los_Angeles`, launch method, mount source, service/command result, newest snapshot short ID and timestamp, retention/prune result, and outstanding errors. Do not record passwords, environment values containing secrets, private application data, or restored file contents.

### 12. Related documentation

- [05-Backup and Restore](05-Backup-and-Restore.md)
- [04-NAS and Storage](04-NAS-and-Storage.md)
- [06-Maintenance and Automation](06-Maintenance-and-Automation.md)
- [NAS mount recovery](04-NAS-and-Storage.md#diagnose-and-recover-a-configured-nas-mount)

### 13. Maintenance notes

Revalidate this runbook whenever the service/timer, launcher, worker, repository, mount, password-file path, include/exclude policy, SQLite staging set, retention, or backup scope changes.


## Rehearse a Complete Rotom Restic Restore in Isolation

### 1. Outcome and scope

Restore one exact Rotom snapshot into a new root-only staging tree, make Restic verify every restored file, run offline SQLite checks, and prove that restored Paperless PostgreSQL and RomM MariaDB state can recover, pass native checks, and produce logical dumps without exposing a network or touching production data.

Use this after important persistence, database-image, backup-scope, or Restic changes and whenever current end-to-end Rotom Restic evidence is required. It does not promote data, test NAS-resident `/mnt` payload, change repository policy, repair a repository, or replace VZDump, PVE, NAS snapshot, credential-retrieval, or authenticated application testing.

### 2. Impact and current inputs

The rehearsal reads the complete selected snapshot and creates a large temporary tree under `/var/backups`. It can consume substantial root-disk space, NAS I/O, CPU, and time. Database containers start only against the restored copy with `--network none`, no published ports, and restart disabled. Database crash recovery and integrity tooling may modify only that disposable copy.

The restored tree contains credentials, keys, personal data, databases, and application state. Keep it owned by root with mode `0700`, never copy contents into evidence, and remove it promptly after validation.

Current database inputs are:

- PostgreSQL data at `/srv/rotom/appdata/libraries/paperless/database`, image from `paperless-db`, and the non-secret `POSTGRES_USER` locator in restored `postgres.env`;
- MariaDB data at `/srv/rotom/appdata/libraries/romm/database`, image from `romm-db`, and restored `mariadb.env`, whose values must never be printed;
- transactionally consistent SQLite copies under restored `/var/backups/system-info/sqlite`.

### 3. Read-only preflight and stop conditions

**Read-only**

```bash
systemctl is-active rotom-restic-backup.service
systemctl list-timers rotom-restic-backup.timer --all --no-pager
pgrep -a -x restic || true
findmnt -M /mnt/nas-rotom-restic-backup -t nfs,nfs4 \
  -o TARGET,SOURCE,FSTYPE,OPTIONS
df -h / /var/backups
sudo docker ps -a --format '{{.Names}}' | \
  rg '^recovery-(paperless|romm)-restore$' || true
sudo env \
  RESTIC_REPOSITORY=/mnt/nas-rotom-restic-backup/rotom-restic-backup \
  RESTIC_PASSWORD_FILE=/etc/restic/restic-repository-password \
  restic snapshots --host rotom --tag automatic --latest 3
```

Proceed only when the backup service is inactive, no Restic process exists, the exact repository export is mounted, the next timer run leaves a safe window, the selected snapshot is unambiguous, and free root space exceeds its logical size with safe operating margin. Both current database images must already exist locally.

Stop on an unexpected mount or repository, active writer/lock, insufficient capacity, existing recovery-container name, missing restored secret locator, unavailable current image, or target that is not a new exact child of `/var/backups`.

### 4. Restore and verify every file

Choose and record an exact new staging path. The example prefix is a safety contract; replace its date and snapshot suffix deliberately.

**Changes Rotom**

**Credential-sensitive**

```bash
read -r -p 'Exact selected snapshot ID: ' ROTOM_SNAPSHOT
read -r -p 'Exact new /var/backups/rotom-restic-rehearsal-* path: ' ROTOM_STAGE
case "$ROTOM_STAGE" in
  /var/backups/rotom-restic-rehearsal-*) ;;
  *) echo 'Unsafe staging path' >&2; exit 1 ;;
esac
sudo test ! -e "$ROTOM_STAGE"
sudo install -d -o root -g root -m 0700 "$ROTOM_STAGE"
sudo env \
  RESTIC_REPOSITORY=/mnt/nas-rotom-restic-backup/rotom-restic-backup \
  RESTIC_PASSWORD_FILE=/etc/restic/restic-repository-password \
  restic restore "$ROTOM_SNAPSHOT" \
  --target "$ROTOM_STAGE" \
  --verify
sudo stat -c '%u:%g %a %n' "$ROTOM_STAGE"
sudo du -sh "$ROTOM_STAGE"
```

Success requires restore exit zero and completed `--verify`. Record the snapshot ID/time/size, restored object count, verified file count, durations, target metadata, and remaining space without listing restored contents.

### 5. Check restored SQLite databases

Run full integrity checks against the consistent backup copies and every restored application SQLite file. Output only status and relative path.

**Read-only**

```bash
sudo bash -c 'rehearsal_root=$1
while IFS= read -r -d "" db_path; do
  db_result=$(sqlite3 -readonly "$db_path" "PRAGMA integrity_check;" 2>&1)
  db_status=$?
  db_relative=${db_path#"$rehearsal_root"}
  if [ "$db_status" -eq 0 ] && [ "$db_result" = ok ]; then
    printf "PASS\t%s\n" "$db_relative"
  else
    printf "FAIL(%s)\t%s\t%s\n" \
      "$db_status" "$db_relative" "$db_result"
  fi
done < <(find \
  "$rehearsal_root/var/backups/system-info/sqlite" \
  "$rehearsal_root/srv/rotom/appdata" \
  -type f \( -iname "*.db" -o -iname "*.sqlite" \) \
  -print0 | sort -z)' _ "$ROTOM_STAGE"
```

Every selected database must report `PASS`. Treat a failed live-copy database separately from a failed transactionally consistent copy; never promote a failed database.

### 6. Validate restored Paperless PostgreSQL

These commands use the existing local image, restored data, and only the non-secret restored role name. They do not publish a port or join a Docker network.

**Changes Rotom**

**Credential-sensitive**

```bash
PAPERLESS_IMAGE="$(sudo docker inspect paperless-db \
  --format '{{.Config.Image}}')"
PAPERLESS_DB_USER="$(sudo awk -F= \
  '$1 == "POSTGRES_USER" {print $2}' \
  "$ROTOM_STAGE/srv/rotom/secrets/libraries/paperless/postgres.env")"
test -n "$PAPERLESS_DB_USER"
sudo docker image inspect "$PAPERLESS_IMAGE" >/dev/null
sudo docker run -d \
  --name recovery-paperless-restore \
  --network none \
  --restart no \
  --mount \
  type=bind,src="$ROTOM_STAGE/srv/rotom/appdata/libraries/paperless/database",dst=/var/lib/postgresql \
  "$PAPERLESS_IMAGE"
for readiness_try in $(seq 1 60); do
  if sudo docker exec -u postgres recovery-paperless-restore \
    pg_isready -q -U "$PAPERLESS_DB_USER"; then
    break
  fi
  sudo docker inspect -f '{{.State.Running}}' \
    recovery-paperless-restore | rg -qx true || exit 1
  sleep 1
done
sudo docker exec -u postgres recovery-paperless-restore \
  pg_isready -q -U "$PAPERLESS_DB_USER"
sudo docker exec -e PGUSER="$PAPERLESS_DB_USER" -u postgres \
  recovery-paperless-restore sh -c '
set -e
set -o pipefail
for restored_db in paperless postgres; do
  pg_dump --format=custom "$restored_db" | sha256sum >/dev/null
  printf "PG_DUMP_PASS %s\n" "$restored_db"
done
pg_amcheck --all --install-missing --on-error-stop
printf "PG_AMCHECK_PASS all\n"'
sudo docker inspect recovery-paperless-restore \
  --format 'STATUS={{.State.Status}} NETWORK={{.HostConfig.NetworkMode}} RESTART={{.HostConfig.RestartPolicy.Name}} PORTS={{json .NetworkSettings.Ports}}'
```

If readiness is not immediate, wait only while the container remains running and inspect sanitized logs. Success requires expected crash recovery if the backup captured a running database, logical dump passes for `paperless` and `postgres`, `pg_amcheck` success, `NETWORK=none`, `RESTART=no`, and no published ports.

### 7. Validate restored RomM MariaDB

The restored environment file is passed directly to the disposable container and must never be printed or included in evidence.

**Changes Rotom**

**Credential-sensitive**

```bash
ROMM_DB_IMAGE="$(sudo docker inspect romm-db \
  --format '{{.Config.Image}}')"
sudo docker image inspect "$ROMM_DB_IMAGE" >/dev/null
sudo docker run -d \
  --name recovery-romm-restore \
  --network none \
  --restart no \
  --env-file \
  "$ROTOM_STAGE/srv/rotom/secrets/libraries/romm/mariadb.env" \
  --mount \
  type=bind,src="$ROTOM_STAGE/srv/rotom/appdata/libraries/romm/database",dst=/var/lib/mysql \
  "$ROMM_DB_IMAGE"
for readiness_try in $(seq 1 60); do
  if sudo docker exec recovery-romm-restore \
    healthcheck.sh --connect --innodb_initialized >/dev/null 2>&1; then
    break
  fi
  sudo docker inspect -f '{{.State.Running}}' \
    recovery-romm-restore | rg -qx true || exit 1
  sleep 1
done
sudo docker exec recovery-romm-restore \
  healthcheck.sh --connect --innodb_initialized
sudo docker exec recovery-romm-restore bash -c '
set -euo pipefail
if ! MYSQL_PWD="$MARIADB_ROOT_PASSWORD" \
  mariadb-check --all-databases --check --extended --user=root \
  >/tmp/recovery-mariadb-check.log 2>&1; then
  tail -200 /tmp/recovery-mariadb-check.log
  exit 1
fi
printf "MARIADB_CHECK_PASS all\n"
MYSQL_PWD="$MARIADB_ROOT_PASSWORD" \
  mariadb-dump --all-databases --single-transaction \
  --routines --events --triggers \
  --user=root |
  sha256sum >/dev/null
printf "MARIADB_DUMP_PASS all\n"'
sudo docker inspect recovery-romm-restore \
  --format 'STATUS={{.State.Status}} NETWORK={{.HostConfig.NetworkMode}} RESTART={{.HostConfig.RestartPolicy.Name}} PORTS={{json .NetworkSettings.Ports}}'
```

Success requires expected crash recovery, native readiness, extended table checks, a complete streamed logical dump, `NETWORK=none`, `RESTART=no`, and no published ports.

### 8. Safe stop, cleanup, and evidence

On failure, preserve sanitized logs and keep production untouched. Stop and remove only the exact disposable container names after retaining evidence.

**Changes Rotom**

```bash
for recovery_container in \
  recovery-paperless-restore recovery-romm-restore
do
  if sudo docker inspect "$recovery_container" >/dev/null 2>&1; then
    sudo docker stop -t 30 "$recovery_container"
    sudo docker rm "$recovery_container"
  fi
done
```

Review the exact staging path, confirm it is the disposable root-only tree created by this rehearsal, and obtain explicit approval before removing it. Type the complete literal path; do not use a variable, glob, shell substitution, or broad parent directory.

**Destructive — explicit approval required**

```bash
sudo rm -rf -- /var/backups/rotom-restic-rehearsal-EXACT-DATE-AND-SNAPSHOT
```

Confirm the exact tree and containers are absent, root capacity returned, the backup timer remains active, the repository mount remains exact, and no unit failed.

Retain snapshot ID/time/size, repository identity, restore and verify counts/durations, target metadata, SQLite relative-path results, database image IDs/versions, PostgreSQL and MariaDB recovery/readiness/check/dump results, isolation proof, cleanup result, and outstanding application/NAS gaps. Never retain restored contents, environment values, passwords, private keys, cookies, or protected application data.

Rehearse again after Restic, PostgreSQL, MariaDB, Paperless, RomM, persistence paths, roles, images, backup scope, or repository behavior changes. A database-layer pass does not close NAS-media consistency, authenticated application, PVE, VZDump, credential-retrieval, off-site, or blank-hardware gates.


## 1. Current Recovery Architecture

Rotom recovery is layered. No single layer replaces another:

1. Rotom Restic Backup protects selected guest-local configuration and application state.
2. PVE Restic Backup protects PVE host configuration and recovery material.
3. Rotom VM Backup creates whole-VM Proxmox VZDump archives.
4. NAS snapshot/restore protects authoritative NAS payload excluded from guest Restic.
5. Historical application-aware artifacts and the pre-virtualization raw image provide additional dated recovery evidence.

Select and verify an incident-appropriate recovery point before use. A successful scheduled job, repository check, archive decompression, or file listing is not by itself a complete restore rehearsal.

## 2. Rotom Restic Backup

| Control | Current value |
|---|---|
| Repository | `/mnt/nas-rotom-restic-backup/rotom-restic-backup` |
| NAS export | `Rotom_Restic_Backup/.data` |
| Manual launcher | `/usr/local/bin/backup-restic-to-nas` |
| Worker | `/usr/local/sbin/rotom-restic-backup` |
| Service / timer | `rotom-restic-backup.service` / `rotom-restic-backup.timer` |
| Schedule | Around `03:00`, persistent, randomized delay up to ten minutes |
| Retention | 7 daily / 4 weekly / 12 monthly |
| Credential path | `/etc/restic/restic-repository-password`; contents never document |

The current source scope includes `/etc`, `/home`, `/root`, `/opt`, `/srv`, `/usr/local`, `/var/lib/docker/volumes`, and `/var/backups/system-info`, subject to the installed include/exclude files. `/mnt` remains excluded.

The latest documented automatic observation is snapshot `aad4a52e` from 2026-10-17 at 03:05 PDT, approximately 18.600 GiB. The service exited successfully after retention and prune. A same-day read-only preflight found the timer enabled and active, the exact NAS export mounted read/write, no concurrent Restic process, protected control-file permissions, readable snapshot metadata, and no failed systemd units. A standard `restic check` completed across all 22 snapshots with no errors. A separate `restic check --read-data` then read all 1,077 packs in 4 minutes 15 seconds and found no errors.

A complete isolated restore of `aad4a52e` recovered 39,398 files/directories totaling 18.600 GiB in two minutes, and Restic `--verify` then verified all 27,581 restored files without error. Full SQLite integrity checks passed all 17 discovered restored databases, including the transactionally consistent NPM, Home Assistant, and Zigbee copies. The restored Paperless PostgreSQL 18 cluster completed crash recovery with no network or published ports; logical dumps of `paperless` and `postgres` succeeded, and `pg_amcheck` passed all relations and indexes. The restored RomM MariaDB 11.8.9 cluster completed InnoDB crash recovery with no network or published ports; extended native checks and a complete logical dump succeeded. Both disposable containers and the root-only 19 GiB rehearsal tree were removed after evidence retention.

Manual post-credential-path snapshot `333c87b3` also completed successfully. The current database-layer rehearsal does not prove NAS-resident media consistency or authenticated application behavior; those remain separate acceptance gates.

The VM-local `/srv/rotom/backup-staging` path is absent. Historical references to local fast-rollback archives below that root do not establish current availability.

## 3. PVE Restic Backup

| Control | Current value |
|---|---|
| Repository | `/mnt/nas-pve-restic-backup/pve-restic-backup` |
| NAS export | `PVE_Restic_Backup/.data` |
| Worker | `/usr/local/sbin/pve-restic-backup` |
| Service / timer | `pve-restic-backup.service` / `pve-restic-backup.timer` |
| Schedule | Daily `04:00` |
| Staging | `/var/backups/pve-restic-recovery` |
| Credential path | `/etc/restic/restic-repository-password` on PVE |

On 2026-10-17 the timer was enabled and active, the exact repository mount was read/write, and no failed systemd units were present. Snapshot `19ed0226` from 04:00:21 PDT was selected from ten retained snapshots. A full-data-read check read both repository packs without error. A root-only `0700` staging restore recovered 307 files/directories totaling 231.557 KiB, and Restic `--verify` verified all 116 restored files. The reviewed inventory contained the expected boot, network, package, public PVE configuration, VM configuration, service, worker, and reconstruction evidence; its private-material path scan was empty. Public `/root/.ssh/authorized_keys` data is reconstruction evidence, not a private key. Exact-target cleanup removed the 920 KiB staging tree; PVE root retained 56 GiB free, the timer remained enabled and active, the service was correctly inactive between runs, and zero failed units were present.

PVE work remains Jared-executed where the RS labels it **PVE — Jared executes**.

## 4. Rotom VM Backup

Proxmox job `rotom-vm-daily` protects VMID `100` on storage `nas-rotom-vm-backup`:

- Daily at `05:00`.
- Snapshot mode with zstd compression.
- `repeat-missed=0`.
- Retention: 7 daily / 4 weekly / 6 monthly.

Manual execution uses `/usr/local/bin/backup-rotom-vm-to-nas`, `rotom-vm-vzdump-manual.service`, worker `/usr/local/sbin/rotom-vm-vzdump-manual`, and lock `/run/lock/rotom-vm-vzdump-manual.lock`. Systemd owns the long-running job so it survives SSH disconnect.

On 2026-10-17 eight retained VMID 100 archives were present. The newest archive, `vzdump-qemu-100-2026_10_17-05_00_07.vma.zst` (40,777,108,083 bytes), passed a complete zstd stream test producing 75,669,850,112 decompressed bytes. Full streamed VMA verification reached 100 percent with pipeline status zero, found the expected VM configuration, 540,672-byte EFI disk, and 107,374,182,400-byte `scsi0`, and reported 107,374,772,224 total bytes with 29.5 percent sparse data.

The same archive then completed a current disposable restore into VMID `101` on temporary directory storage backed by the exact VM-backup NFS export, avoiding local thin-pool overcommit. Before boot, the test VM was set to `onboot=0`, reduced to 1 GiB and two cores, and stripped of its NIC, iGPU, ConBee, and Bluetooth attachments. It booted without network or host-device access; the guest agent responded on the fifth three-second poll and reported hostname `rotom`, Debian 13, and kernel `6.12.107+deb13-amd64`. PVE remained healthy with zero failed units and at least 1.6 GiB memory available during the test. Graceful shutdown timed out, so the disposable guest was stopped; this does not prove graceful application shutdown. Exact-target cleanup removed VMID `101`, its two NFS-backed disks, the temporary storage definition, and the test path. Production VMID `100` remained running and guest-agent responsive, the archive remained present, the PVE Restic timer remained enabled/active, and NFS available-space accounting returned to the pre-test `3,794,723,328 KiB`. This proves current archive restoration and isolated OS boot, not authenticated application behavior or a full production-size boot under replacement-hardware conditions. Archive availability changes under normal retention.

An earlier 2026-09-29 disposable restore remains useful historical portability evidence; the current 2026-10-17 exercise supersedes it for archive-specific restore and isolated-boot readiness.

## 5. NAS-Resident Application Data

Rotom Restic excludes `/mnt`. Authoritative Libraries data, including Paperless media, therefore depends on NAS-side protection.

Paperless VM-local database, broker, configuration, search data, consume/export paths, and protected inputs are under `/srv/rotom/{appdata,secrets}/libraries/paperless`. Authoritative media is `/mnt/nas-libraries/paperless`. The restored five-file media set matched its retained manifest. Jared confirmed Libraries snapshot retention and an isolated restore outcome; exact policy values and the selected recovery point were not supplied.

On 2026-10-17 Jared declined a repeat NAS snapshot rehearsal because the existing workflow is accepted as working. Treat this as an owner acceptance decision, not as a new retained snapshot identifier, isolated-restore transcript, or application/NAS consistency proof.

Game Servers, Smart Home, and Hosted Websites NAS shares are empty service boundaries. Their application state remains VM-local and depends on Rotom Restic and, at a broader layer, whole-VM backup.

## 6. Recovery-Critical Historical Evidence

### Final pre-virtualization Restic baseline

Snapshot `fbe1838e` at 2026-09-25 18:14:22 PDT is the final documented pre-virtualization guest recovery point. Standard `restic check` and full `restic check --read-data` passed, reading all 971 packs without error. A representative isolated restore recovered both Palworld saves, the preserved audit artifacts, and staged Home Assistant, Zigbee, and NPM databases; restored SQLite quick checks passed.

Related audit paths are:

- `/home/jared/audits/jar-22-2026-09-22`
- `/home/jared/audits/jar-23-2026-09-23`
- `/home/jared/audits/jar-24-2026-09-25`

Verify that the selected snapshot still exists before relying on these paths.

### Raw NVMe rollback image

The historical raw image is:

`/mnt/nas-shared-drive/rotom-bare-metal/jar-25-2026-09-25/rotom-nvme-live-pre-proxmox-2026-09-25.img`

Recorded logical size: `250059350016` bytes. Recorded SHA-256:

`b62b2c8210bb2a6446abc29c5767c7d8531f547dfd2ec3f0259dbee8d74c5e90`

The acquisition-stream and complete stored-image reread hashes matched, and partition inspection found EFI and Linux filesystem partitions. The image is **best-effort live / crash-consistent** because the source root filesystem remained mounted. An actual bare-metal restore has not been rehearsed.

The guest Shared Drive mount is retired. Accessing, retaining, or restoring this NAS-resident image requires a separately authorized NAS path and exact target verification. The image and Restic repository are on different shares of the same physical UNAS appliance and therefore share that failure domain.

## 7. Restore Procedure

1. Identify the failure domain and the authoritative source before changing anything.
2. Stop writers only when the selected application or restore method requires it.
3. Verify the selected Restic snapshot, VZDump archive, NAS snapshot, or raw image exists and matches the intended system and date.
4. Restore into an isolated target whenever practical. Never overwrite current production data merely to test recoverability.
5. Preserve numeric ownership, modes, ACLs, service identity, Compose paths, and non-creating NAS-bind protections.
6. Validate files and databases before promotion. Use application-native integrity checks where available.
7. Promote only the reviewed target, then verify the application, storage, network, proxy, and backup state.
8. Retain the command results, selected recovery identifier, checksums, and validation evidence.

Stop if the repository is locked by active work, credentials are unavailable, the target contains current data, the expected source is not the documented filesystem, or the requested action would change retention, prune data, delete a recovery point, or overwrite protected state without explicit authorization.

## 8. Recovery Limitations and Outstanding Work

- No off-site layer is documented; Rotom Restic, PVE Restic, VM Backup, and NAS snapshots share the local site and substantial hardware failure domains.
- The raw NVMe image has not been restored to bare metal.
- Current detailed transcripts for the owner-confirmed Restic, VMA/disposable-restore, and Libraries NAS restore exercises were not supplied.
- NAS snapshot schedules and exact retention must be revalidated before incident reliance.
- Root-only historical rollback artifacts require exact-path inspection before any retention decision.
- Credentials, repository internals, NAS snapshot policy, and retention/prune behavior require separate authorization to change.

## 9. Related Documentation

- [02 — Docker Services](02-Docker-Services.md)
- [04 — NAS and Storage](04-NAS-and-Storage.md)
- [06 — Maintenance and Automation](06-Maintenance-and-Automation.md)
- [07 — Users and Permissions](07-Users-and-Permissions.md)

## Maintenance and Revalidation Triggers

Follow the canonical [Runbook-First Maintenance Standard](00-Rotom-Change-Log.md#runbook-first-maintenance-standard). Revalidate this document after a source path, exclusion, repository, credential path, timer, schedule, retention rule, archive destination, NAS snapshot policy, restore result, application persistence path, or recovery procedure changes. Revalidate the supplementary total-loss guide when one of its RS-owned dependencies changes.
