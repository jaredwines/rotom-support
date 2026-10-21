# 00 - Rotom Change Log

**Documentation set:** Rotom Support
**Document role:** Canonical history of documentation/server changes, adopted decisions, corrections, status, outstanding checks, and the sole RS maintenance contract
**Scope:** Rotom system history across bare metal, Proxmox host, and portable VM  
**Baseline verified:** Historical record; evidence dates are entry-specific  
**Documentation updated:** 2026-10-20 — Remove retired ticket history
**Related canonical sources:** `01-Rotom-Server-Inventory.md` through `08-Rotom-Directory-Tree.txt`


**Index:** [01-Rotom-Server-Inventory.md](01-Rotom-Server-Inventory.md)

This file records meaningful changes to Rotom Support and the server changes or decisions those updates describe. The numbered files `01`–`08` remain the detailed state/reference sources for the latest recorded configuration and clearly labeled plans, while other tracked repository areas retain their narrower defined roles. Older entries here describe history, not instructions to restore an old configuration.

**Terminology:** **Rotom Support** is the proper name for **all intentionally tracked content in the Rotom-Support repository**. Local untracked files, ignored files, temporary artifacts, generated output, and Git's internal metadata are not RS merely because they exist inside the checkout. The numbered files **00–08** are the **Core Numbered Reference Set** within RS, and `runbook/` is the primary authority for Rotom's documented current state and operations. Other tracked areas retain their narrower defined roles. Within the Rotom project, **RS** is the accepted acronym for **Rotom Support**. **RC** means **Rotom Compose**: the reviewed non-secret deployment configuration in `/srv/rotom/stacks` and its Git history. “Update RC” invokes the canonical **Update Rotom Compose Configuration** procedure in document 02; it does not independently authorize a container lifecycle change or an RS update. “Project docs,” “rotom project docs,” “project documentation,” “project documents,” and “project reference files” are informal aliases only when context does not imply a narrower scope. Available Sources is a separate, manually maintained publication or reference destination; it neither defines RS membership nor represents the complete repository. The definition and current source map are maintained in [01-Rotom-Server-Inventory.md](01-Rotom-Server-Inventory.md).

### How to use this file safely

- Use **Current Documentation Maintenance Rules** for the active RS maintenance contract.
- Use the newest entry under **Change History** to understand the latest recorded change, then follow its named canonical subject document for supported state and procedures.
- Treat older entries as dated evidence. They may contain retired paths, names, commands, or architecture and must not be replayed as current instructions without reconciliation.
- Use [01-Rotom-Server-Inventory.md](01-Rotom-Server-Inventory.md) when the correct subject document is unknown.

## Current Documentation Maintenance Rules

This section is the **sole canonical maintenance contract** for Rotom Support. `01-Rotom-Server-Inventory.md` defines RS membership and the source map; other RS files may point here, but they should not duplicate this procedure.

### Runbook-First Maintenance Standard

Every RS change must identify the canonical document owner for each changed fact or procedure and assess whether the change affects how Rotom is operated, diagnosed, maintained, recovered, or verified. When it does, review and update the affected operational procedure and current-state reference together. Keep operational procedures before detailed reference and historical evidence.

Each supported state-changing procedure must preserve an observable outcome, precise entry conditions, explicit exclusions, authorization and impact, canonical current-state inputs, read-only preflight, stop conditions, the smallest targeted action, expected immediate result, observable verification, rollback or safe-stop recovery, troubleshooting branches, evidence to retain, and revalidation triggers. Command blocks must use the applicable approved label: **Read-only**, **Read-only; may activate an existing automount**, **Changes Rotom**, **Changes Rotom and protected storage/repository state**, **Credential-sensitive**, **PVE — Jared executes**, or **Destructive — explicit approval required**.

Document `01` must be updated whenever a supported task, destination, filename, heading, or canonical owner changes, so a person or Codex can reach the canonical procedure within one or two links. It routes tasks and must not duplicate complete procedures. Do not maintain competing canonical procedures in multiple documents; supporting facts and cross-domain branches must link to the owning document.

Review the affected document's **Maintenance and Revalidation Triggers** whenever current state changes. Update automated tests whenever a supported task, procedure, ownership boundary, or required structure changes. Before publication, run `internals/tooling/test-rr-runbooks`, `internals/tooling/rs lint`, `git diff --check`, the required semantic ownership/duplication review, and `rs check` at clean Git checkpoints.

> An RS update is incomplete if it changes how Rotom is operated, diagnosed, maintained, or recovered without also reviewing and updating the affected runbook procedure, task-router entry, revalidation triggers, and automated tests.

Not every factual change requires a new procedure. Create or update a procedure when the change affects how a person or Codex safely operates, diagnoses, maintains, verifies, or recovers Rotom.

Update this log as part of the same task whenever a substantive change is made to any Rotom Support file. This includes documented configuration changes, corrected findings, new verification results, adopted decisions, proposed architecture, methodology changes, and plans that are completed or withdrawn. A documentation-only update still belongs here; it does not mean the server was changed.

Do not add an entry for an unchanged re-upload, download, repackaging, or a formatting-only edit. Record typo corrections only when they change the meaning of a command, path, ID, or other operational detail. Discussion alone does not require an entry until a decision or finding is incorporated into the documentation.

The sole canonical documentation-update command is **`Update the RS`**. It means apply this maintenance procedure to **the final supported state established in the current chat**. It authorizes documentation preparation and packaging only; it does **not** authorize changes to Rotom, Proxmox, Docker, NAS, networking, applications, external services, or other live state unless those changes are separately authorized.

For each `Update the RS` task:

1. Review the current chat and the complete intentionally tracked repository content relevant to the task. Git tracking defines RS membership; do not treat untracked, ignored, temporary, generated, or Git-internal checkout content as RS.
2. Establish the **final supported state** from the chat. Include verified changes, explicit decisions, meaningful corrections, clearly labeled proposals, and unresolved findings worth preserving. Do not promote superseded ideas, abandoned approaches, failed experiments, suggested-but-unrun commands, or temporary troubleshooting states unless they have lasting historical, recovery, or diagnostic value.
3. Update every materially affected RS file while preserving still-valid information, evidence provenance, and the distinctions between **Current**, **Historical**, **Retired**, **Proposed**, and **Needs Verification**. Leave unaffected files unchanged.
4. Cross-check the complete current RS for contradictions introduced or exposed by the update. Reconcile contradictions where the available evidence supports a resolution; otherwise preserve the uncertainty explicitly rather than guessing.
5. Add one dated entry at the top of **Change History**, below this maintenance guide, for the documentation task. Use `YYYY-MM-DD` in Rotom's project timezone, `America/Los_Angeles`. State the actual change or evidence date separately if it differs from the documentation date. Combine related work from the same task into one entry.
6. In that entry, list the changed filenames and briefly explain what changed and why. Label relevant items **Implemented**, **Documentation only**, **Proposed**, or **Verified**. Use **Verified** only for results supported by supplied output or an actual check, identify the evidence, and record unresolved checks or limitations. Keep passwords, tokens, keys, and other secrets out of the log.
7. Preserve earlier dated entries as historical evidence. Do not silently rewrite history to match current terminology or policy unless Jared explicitly authorizes an archival terminology rewrite. If an older entry is wrong, add a dated correction identifying what it supersedes. Historical command names are never current instructions.
8. Complete RS delivery according to the execution environment:
   - **ChatGPT on Mac (non-Codex):** deliver replacement copies of the **materially changed RS files individually** and package the **complete current tracked RS set**, including unchanged tracked members but excluding Git metadata and untracked or generated artifacts, into one ZIP named **`Rotom-Support-YYYY-MM-DD.zip`** using the documentation-update date in `America/Los_Angeles`. Tell Jared to run `rs path` on the Mac to resolve the active local checkout, copy the materially changed files into that checkout, manually replace the corresponding Available Sources copies as applicable, then run `rs commit "<relevant concise commit message>"`, `rs check`, and `rs push` on the Mac and verify success. ChatGPT prepares the files and instructions only; it does not execute the RS Git commit or push itself.
   - **Codex on Mac:** resolve the active local RS checkout with `rs path` and work directly in that checkout. After the final RS files are complete, run `rs commit "<relevant concise commit message>"`, then `rs check`, then `rs push`, and verify the commit and push succeeded. A separate replacement-file/ZIP package is not required unless Jared explicitly requests one.
   - **Codex on Rotom:** resolve the active local RS checkout with `rs path` and work directly in that checkout. When the active sandbox restricts the checkout's `.git` directory or GitHub network access, request the necessary execution access before running `rs check` or other affected `rs` Git operations; retain all helper safety checks. After the final RS files are complete, run `rs commit "<relevant concise commit message>"`, then `rs check`, then `rs push`, and verify the commit and push succeeded. A separate replacement-file/ZIP package is not required unless Jared explicitly requests one.
   - **All environments:** Available Sources is a separate destination and replacement remains manual by Jared. Do not treat it as a complete repository or membership inventory, open or control a browser for synchronization, claim a manual destination is updated before Jared confirms it, commit unrelated changes or temporary files, or commit secrets. If an `rs` check, commit, or push fails, stop and report the problem rather than bypassing the guardrails. Preserve existing RS filenames whenever possible and do not add checksum manifests, packaging metadata, generated README files, or other untracked extras unless explicitly requested. Generated packages and separate artifacts belong under `Downloads/`; the local `sources/` mirror remains read-only.
9. For Rotom work tied to an active Linear ticket, keep that ticket current as meaningful work is verified: record material design or scope decisions, verified implementation milestones, blockers, rollbacks, and intentional deferrals as they occur. Do not use Linear as a raw command transcript or duplicate routine diagnostic output. When ChatGPT is actively assisting with the ticket and Linear access is available, these meaningful updates should be made during the work without requiring Jared to separately request each one. The current runbook remains the canonical verified as-built source of truth within RS; update it from the final verified state at ticket closeout.


Keep future entries brief: the change log should point to the detailed documents rather than duplicate them. Updating the log for a task does not require a second entry merely to record that log update.

### Entry template

```markdown
## YYYY-MM-DD — Short description

- **Files changed:** filename.md, other-file.txt
- **Status:** Documentation only / Implemented / Proposed / Verified (choose applicable labels)
- **Changes:** What changed and why; distinguish different statuses if needed.
- **Evidence:** Command results, dated audit, or recorded user decision; say when not verified.
- **Outstanding:** Remaining checks, or "None" if none remain.
```

## Change History

## 2026-10-20 — Remove retired ticket history

- **Files changed:** `00-Rotom-Change-Log.md`.
- **Status:** **Documentation only.**
- **Changes:** Removed retired ticket-associated historical entries, ticket-derived artifact/path references, and the obsolete active-ticket command at Jared's direction.
- **Evidence:** Jared's 2026-10-20 decision to delete the tickets; repository search confirms no remaining ticket-identifier or ticket-history placeholder in this file.
- **Outstanding:** None. Available Sources replacement remains manual by Jared.

## 2026-10-20 — Record verified post-reset recovery points

- **Files changed:** `00-Rotom-Change-Log.md`, `01-Rotom-Server-Inventory.md`, `05-Backup-and-Restore.md`, and `08-Rotom-Directory-Tree.txt`.
- **Status:** **Implemented / Verified.**
- **Changes:** Recorded the verified recovery coverage rebuilt after the intentional reset: two Rotom Restic snapshots, two PVE Restic snapshots, and one Rotom VMID 100 VMA archive. The existing repositories, workers, timers, and native Proxmox job remained enabled throughout; historical recovery-test evidence remains historical.
- **Evidence:** Jared supplied final Restic listings showing Rotom snapshots `7998f4f6` and `f6cae3c8`, PVE snapshots `75c4b19a` and `00600860`, and the sole PVE VMA listing `vzdump-qemu-100-2026_10_20-19_01_20.vma.zst` at 34,853,099,624 bytes. The manual VZDump job logged successful completion at 19:09:16 PDT after streaming 100 GiB.
- **Outstanding:** These new recovery points have not yet completed a fresh full-data Restic check, isolated restore, or VMA verification; retain the earlier exercises only as historical evidence. NAS snapshots and the historical raw NVMe image remain outside this reset. Available Sources replacement remains manual by Jared.

## 2026-10-20 — Record intentional backup reset and console banners

- **Files changed:** `00-Rotom-Change-Log.md`, `01-Rotom-Server-Inventory.md`, `05-Backup-and-Restore.md`, `06-Maintenance-and-Automation.md`, and `08-Rotom-Directory-Tree.txt`.
- **Status:** **Implemented / Verified.**
- **Changes:** Recorded Jared's intentional reset of retained Rotom Restic, PVE Restic, and Rotom VM VMA backup data while preserving the existing repository configuration, workers, timers, and `rotom-vm-daily` job. Recorded the retained PVE local recovery-staging tree, removal of the obsolete VMID 100 pre-disk-shrink configuration copy and Rotom Support prior-site rollback directory, and visual-only Rotom/PVE MOTD headers.
- **Evidence:** Jared's supplied command output showed all 22 Rotom Restic snapshots pruned (16.462 GiB), all 11 PVE Restic snapshots pruned (572.228 KiB), and empty final `restic snapshots` checks for both repositories. PVE's final VMID 100 backup-storage listing was empty after removal of its three VMA archives. Read-only inspection found `/var/backups/pve-restic-recovery` populated by the 04:00 worker run and confirmed the exact removed rollback-copy paths. Jared supplied successful banner displays for both hosts.
- **Outstanding:** No currently usable Rotom Restic, PVE Restic, or VMID 100 VMA recovery point remained at verification; wait for and verify newly scheduled backups before depending on these layers. NAS snapshots and the historical raw NVMe image were outside this reset. Available Sources replacement remains manual by Jared.

## 2026-10-20 — Resolve the Arcane Analytics Heartbeat observation

- **Files changed:** `00-Rotom-Change-Log.md`, `01-Rotom-Server-Inventory.md`, `02-Docker-Services.md`, and `06-Maintenance-and-Automation.md`.
- **Status:** **Documentation updated / Verified.**
- **Changes:** Resolved the post-reset Arcane Analytics Heartbeat observation. The failed run was not a Docker or application-health failure and requires no configuration change or repeated manual run.
- **Evidence:** Sanitized Arcane logs recorded HTTP `429 Too Many Requests` from its analytics heartbeat endpoint, then scheduled a one-hour automatic retry. The Arcane container remained running and healthy. Image Update Watcher completed with zero failed images or containers; Docker Client Refresh and Environment Health also succeeded.
- **Outstanding:** Exact Arcane schedules, thresholds, and project-polling settings remain unrecorded. Available Sources replacement remains manual by Jared.

## 2026-10-20 — Record verified post-reset Docker runtime and Arcane controls

- **Files changed:** `00-Rotom-Change-Log.md`, `01-Rotom-Server-Inventory.md`, `02-Docker-Services.md`, `03-Network-and-Domains.md`, `04-NAS-and-Storage.md`, `06-Maintenance-and-Automation.md`, `07-Users-and-Permissions.md`, `08-Rotom-Directory-Tree.txt`, and `internals/tooling/test-rr-runbooks`.
- **Status:** **Documentation updated / Verified.**
- **Changes:** Reconciled the current runtime after Jared's authorized global Docker and Arcane reset. All 18 validated Compose definitions were started; the final inventory is 23 running containers, 18 networks including Docker defaults, zero named volumes, and 21 images. The current Arcane Compose definition persists its state through `/srv/rotom/appdata/platform/arcane` rather than named Docker volumes. Jared restored Arcane credentials independently and confirmed the intended UI controls without recording any credential value.
- **Evidence:** Before removal, the readable automatic Rotom Restic snapshot dated 2026-10-20 and the two active NFS mounts were verified; both mounts were read/write. The reset removed the inventoried 23 containers, 15 Compose-created networks, two named Arcane volumes, 25 images, and Arcane appdata, then recreated all 18 Compose projects. Post-rebuild inspection found all 23 containers running with no exited or unhealthy container, successful local checks for Arcane, Homepage, Aloha Millworks, Jared Wines, and Rotom Support, and successful local-SNI HTTPS checks for Arcane and Rotom Support. The Arcane UI screenshot confirmed Auto Update, Image Update Watcher, and Auto Heal enabled; Scheduled Prune, Image Auto Patch, and Vulnerability Scan disabled.
- **Outstanding:** The screenshot's most recent Analytics Heartbeat run showed failed; its impact has not been investigated. Exact Arcane schedules, thresholds, and project-polling settings remain unrecorded. Available Sources replacement remains manual by Jared.

## 2026-10-20 — Define the RC shorthand for Rotom Compose

- **Files changed:** `AGENTS.md`, `00-Rotom-Change-Log.md`, `01-Rotom-Server-Inventory.md`, and `02-Docker-Services.md`.
- **Status:** **Documentation only.**
- **Changes:** Defined **RC** as **Rotom Compose** in the agent instructions and current runbook. “Update RC” now unambiguously routes to the existing Update Rotom Compose procedure: review the exact non-secret tracked configuration change, validate it, inspect and commit/push it, then apply only the separately intended service action. It does not by itself authorize a container lifecycle change or an RS update.
- **Evidence:** Jared explicitly adopted the shorthand on 2026-10-20. No live Rotom, PVE, NAS, Docker, GitHub, or Compose change occurred.
- **Outstanding:** None.

## 2026-10-20 — Version-control current Rotom Compose configuration

- **Files changed:** `00-Rotom-Change-Log.md`, `01-Rotom-Server-Inventory.md`, `02-Docker-Services.md`, `05-Backup-and-Restore.md`, and `08-Rotom-Directory-Tree.txt`.
- **Status:** **Implemented / Verified.**
- **Changes:** Created the nested Git working tree at `/srv/rotom/stacks` and published the reviewed current deployment configuration to `https://github.com/jaredwines/rotom-compose`. Jared explicitly approved the remote being public after the original private-remote requirement could not be met. The repository tracks the 18 current Compose definitions, `mkdocs-rr`'s non-secret support files, and its own README/ignore rules. It excludes secrets, `.env` files, appdata, Docker state, NAS data, generated output, and historical copies. Added the supported **Update Rotom Compose** workflow; it is a configuration-history/off-site-copy layer and does not replace Restic, PVE VZDump, NAS protection, or RS.
- **Evidence:** All 18 definitions passed `docker compose config -q` before and after setup. The guest Restic repository was mounted read/write; the 2026-10-20 automatic snapshot was readable, and its backup completed retention/prune successfully. The public remote's reviewed tree contained only the 22 intended files. Ownership and ACL contracts remained intact; no Git operation restarted or recreated a container, and no failed guest systemd unit appeared. Jared's 2026-10-20 PVE check confirmed the enabled `rotom-vm-daily` VMID 100 job, its expected snapshot/zstd/retention policy, three retained October 18–20 archives, and zero failed PVE units. The separately verified 2026-10-17 VZDump archive/restoration evidence remains current in document 05.
- **Outstanding:** The public remote is intentionally an additional configuration-history copy, not a secret store or recovery substitute. Select and verify an incident-appropriate Restic, VZDump, NAS, or other recovery point when it is needed.

## 2026-10-20 — Restrict Arcane project-file access

- **Files changed:** `00-Rotom-Change-Log.md`, `01-Rotom-Server-Inventory.md`, `02-Docker-Services.md`, `03-Network-and-Domains.md`, `06-Maintenance-and-Automation.md`, `08-Rotom-Directory-Tree.txt`, `architecture/Rotom-Architecture-System.md`, and `internals/tooling/test-rr-runbooks`.
- **Status:** **Implemented / Verified.**
- **Changes:** Changed Arcane's canonical application URL to `https://arcane.rotom.casa`. Removed `PROJECTS_DIRECTORY` and the writable `/srv/rotom/stacks/platform` bind from Arcane's Compose definition, so Arcane no longer discovers host Compose definitions or presents their files through its Projects UI. Removed the five stale project records from the fresh Arcane database while Arcane was stopped. Jared restored the Arcane account credentials independently and saved the accepted UI automation controls; no credential values are recorded.
- **Evidence:** Docker inspection after recreation showed only Arcane appdata writable, the Docker socket writable, and Platform secrets read-only; no host Compose-directory mount remained. The Arcane project database contained zero rows, Arcane was healthy, and local-SNI HTTPS for `arcane.rotom.casa` returned `200`. The prior `arcane.smart-hub.xyz` application URL no longer served Arcane.
- **Outstanding:** The Docker socket is root-equivalent control of the host Docker daemon. Removing the project-directory bind prevents direct host Compose-file editing through Arcane Projects, but it is not a complete privilege boundary. Exact post-reset automation schedules and thresholds have not been reread from Arcane after Jared saved the UI controls. The Libraries and Rotom Restic NFS read-only discrepancy remains separate.

## 2026-10-20 — Reset Docker runtime and Arcane project state

- **Files changed:** `00-Rotom-Change-Log.md`, `01-Rotom-Server-Inventory.md`, `02-Docker-Services.md`, `03-Network-and-Domains.md`, `04-NAS-and-Storage.md`, `05-Backup-and-Restore.md`, `06-Maintenance-and-Automation.md`, `07-Users-and-Permissions.md`, `08-Rotom-Directory-Tree.txt`, and `internals/tooling/test-rr-runbooks`.
- **Status:** **Implemented / Verified.**
- **Changes:** At Jared's explicit direction, removed the entire Docker runtime inventory: 22 containers, 15 Compose-created networks, two Arcane internal volumes, 25 images, and Arcane's persistent application-data directory. Recreated all 18 validated Compose definitions. A fresh Arcane database discovered the five Platform projects only; its former project rows, settings, backup history, and duplicate records were intentionally discarded. Jared then intentionally stopped both Palworld containers and `jaredwines.com`.
- **Evidence:** Before removal, all 18 Compose files passed `docker compose config -q`. Post-rebuild, 23 containers were running and healthy, with 18 networks and two fresh Arcane internal volumes. After Jared's stop request, the two Palworld containers exited with status 143 and `jaredwines.com` exited with status 0; the remaining 20 containers continued running. Arcane logs recorded a fresh database migration and discovery of exactly the five Platform Compose roots.
- **Outstanding:** Superseded for Arcane project scope and core UI controls by the later 2026-10-20 Arcane access-restriction entry above. The Libraries and Rotom Restic NFS mounts were observed read-only during the reset; Jared explicitly authorized proceeding without repairing that discrepancy or taking a fresh Restic snapshot.

## 2026-10-20 — Retire three removed NAS mount contracts

- **Files changed:** 00-Rotom-Change-Log.md, 01-Rotom-Server-Inventory.md, 03-Network-and-Domains.md, 04-NAS-and-Storage.md, 05-Backup-and-Restore.md, 08-Rotom-Directory-Tree.txt, architecture/Rotom-Architecture-System.md, and guide/PVE-and-Rotom-Total-Loss-Recovery.md.
- **Status:** **Implemented / Verified.**
- **Changes:** At Jared's direction after he deleted the corresponding NAS drives, removed the Game_Servers/.data, Smart_Home/.data, and Hosted_Websites/.data guest NFS automount entries; stopped and cleared their generated units; and removed the verified-empty local /mnt/nas-game-servers, /mnt/nas-smart-home, and /mnt/nas-hosted-websites directories. Palworld, Smart Home, and hosted-site state remains VM-local. Libraries and the Rotom Restic repository remain the only current guest NFS contracts.
- **Evidence:** Pre-removal inspection found no running container bind for any retired path. Game Servers had a stale NFS handle and the other two retired mounts had failed after their NAS sources were deleted. After removal, findmnt --fstab listed only Libraries and Rotom Restic; both mounts and automounts were active; no failed units remained; and all three exact local paths were absent.
- **Outstanding:** The NAS-side drive deletion is Jared-reported; no authenticated NAS control-plane inspection was performed. Available Sources replacement remains manual by Jared.

## 2026-10-20 — Repair Libraries resolver, download-client, and stale-root failures

- **Files changed:** `00-Rotom-Change-Log.md`, `01-Rotom-Server-Inventory.md`, `02-Docker-Services.md`, and `03-Network-and-Domains.md`.
- **Status:** **Implemented / Verified.** Prowlarr, Sonarr, Radarr, and qBittorrentVPN were repaired without changing NAS data, download queues, or application configuration outside the named collection root.
- **Changes:** Added explicit router DNS `192.168.1.1` to Prowlarr after Docker restored it before DHCP had supplied an external resolver. Retained qBittorrent's loopback listener for NPM and added its trusted-LAN `192.168.1.69:8080` listener so the existing Sonarr/Radarr download-client targets work. Changed the unmonitored Avatar Aang collection's obsolete `/media/library/movies` root to `/media/movies`. At Jared's request, cleared historical Sonarr/Radarr application and Docker logs before restarting those two containers; only fresh post-restart logs remain.
- **Evidence:** Prowlarr resolved external indexer hosts and its health response was empty after its built-in indexer test. qBittorrentVPN recreated from the existing local image with WireGuard `wg0` at `10.2.0.2/32`; loopback and LAN HTTP probes both returned `200`, and both Sonarr and Radarr reached its LAN listener. The built-in download-client and indexer tests returned `200` for each application, followed by empty health responses. The Radarr collection record now names `/media/movies`.
- **Outstanding:** The additional qBittorrent listener is intentionally limited to the trusted LAN. Available Sources replacement remains manual by Jared.

## 2026-10-20 — Enable narrow RomM browser-upload access and metadata providers

- **Files changed:** `00-Rotom-Change-Log.md`, `01-Rotom-Server-Inventory.md`, `02-Docker-Services.md`, `04-NAS-and-Storage.md`, `07-Users-and-Permissions.md`, `08-Rotom-Directory-Tree.txt`, `architecture/Rotom-Architecture-System.md`, and `internals/tooling/test-rr-runbooks`.
- **Status:** **Implemented / Verified.**
- **Changes:** Kept RomM's `/mnt/nas-libraries/games -> /romm/library` bind read-only and added only the nested `/mnt/nas-libraries/games/roms -> /romm/library/roms` writable bind, both non-creating. Browser uploads now land beneath the authoritative NAS `games/roms/<platform>/` tree without granting writes to the rest of `games/`. RomM's protected environment now supplies its IGDB client variables; their values remain outside RS. The existing LaunchBox provider completed its initial local metadata-store update.
- **Evidence:** The edited Compose file validated before applying; only `romm` was recreated. Runtime inspection confirmed the parent mount `RW=false` and ROM subdirectory `RW=true`; a browser upload succeeded; RomM returned local HTTP `200` with zero restarts; IGDB authentication and LaunchBox provider health each returned `true`. The three current NAS ROM files and the three RomM database records matched after Jared confirmed that library state is intentional. The manually run cleanup task removed 2,423 stale database records only; it did not delete ROM files.
- **Outstanding:** Browser-uploaded files were observed as `root:5000` mode `0644`; preserve that observed contract unless a separately authorized ownership change is designed and verified. Available Sources replacement remains manual by Jared.

## 2026-10-20 — Record Jared's verified Rotom-side SSH client configuration

- **Files changed:** `00-Rotom-Change-Log.md`, `01-Rotom-Server-Inventory.md`, `07-Users-and-Permissions.md`, and `internals/tooling/test-rr-runbooks`.
- **Status:** **Verified / Documentation only.** Recorded the current Rotom-side aliases for GitHub, the UniFi gateway, NAS, and PVE, including their targets, accounts, authentication methods, and client-file modes; routed SSH access lookup to the identity/access owner. No live SSH configuration, key, authorization, server policy, or appliance state was changed.
- **Changes:** Recorded the preserved GitHub key pair under its corrected `id_ed25519_github` basename, the explicit GitHub identity constraint, password-authenticated infrastructure aliases, and the unchanged separate `id_ed25519_codex_rotom` pair. Preserved the local-execution, appliance-console, PVE-execution, and service-account credential boundaries.
- **Evidence:** Jared supplied the final SSH client configuration and successful 2026-10-20 manual tests for all four aliases, including GitHub authentication as `jaredwines`. Read-only inspection in this task matched the supplied file exactly and confirmed `0600` for the client file and GitHub private key plus `0644` for its public key. The Codex sandbox could not independently run `ssh -G` because it rejected the presented ownership of `/etc/ssh/ssh_config.d/20-systemd-ssh-proxy.conf`; this known sandbox limitation did not affect the supplied connection evidence.
- **Outstanding:** None for the documented Rotom-side configuration. Available Sources replacement remains manual by Jared.

## 2026-10-19 — Clarify local Rotom execution and Mac SSH alias scope

- **Files changed:** `internals/agents/rotom-global-AGENTS.md`, `runbook/00-Rotom-Change-Log.md`. The active `~/.codex/AGENTS.md` is synchronized outside RS.
- **Status:** **Documentation only.**
- **Changes:** Replaced the ambiguous SSH-first instruction with the local-execution policy for Codex on Rotom. Recorded that `rotom` and `rotom.casa` resolve locally on Rotom, while `ssh rotom` is a Mac-only alias for Jared's configured connection to `rotom.casa`.
- **Evidence:** On 2026-10-19, `hostname` configuration named the current VM `rotom`, `/etc/hosts` mapped `127.0.1.1` to `rotom.casa rotom`, and Jared confirmed the Mac-only alias behavior. No Rotom service, DNS, SSH, or access configuration was changed.
- **Outstanding:** Available Sources replacement remains manual by Jared.

## 2026-10-18 — Prefer Jared SSH for Rotom Agent access

- **Files changed:** `internals/agents/rotom-global-AGENTS.md`, `runbook/00-Rotom-Change-Log.md`. The active `~/.codex/AGENTS.md` was synchronized outside RS.
- **Status:** **Documentation only.**
- **Changes:** Made SSH as `jared` the primary Rotom connection, required investigation of SSH failures, and limited Desktop Commander to a last resort without changing its security restrictions. Preserved existing administration, safety, and RS maintenance rules.
- **Evidence:** Jared requested the connection policy; the active instructions and tracked backup matched before editing. No Rotom service or access configuration was changed.
- **Outstanding:** This Codex session could not complete SSH as `jared`: restricted execution rejected the SSH config drop-in ownership presented by its sandbox, while a direct retry reached host-key verification with no trusted `rotom` entry in Jared's `known_hosts`. SSH configuration and trust were left unchanged. Available Sources replacement remains manual by Jared.

## 2026-10-18 — Record Blastiorse SSH access

- **Files changed:** `07-Users-and-Permissions.md`, `00-Rotom-Change-Log.md`.
- **Status:** **Verified / Documentation update.**
- **Changes:** Recorded Windows workstation Blastiorse SSH aliases, their target accounts, and the unresolved PVE root authorization. Appliance console access remains for targeted troubleshooting.
- **Evidence:** Jared tested all four aliases with batch-mode SSH: Rotom and PVE returned `jared`; NAS and gateway returned `root`. An attempted removal of the mistakenly added PVE root key produced no confirmation.
- **Outstanding:** Verify and, if still present, remove only the Blastiorse PVE root authorization; verify gateway and NAS key persistence after appliance updates or reboots. Available Sources replacement remains manual by Jared.

## 2026-10-18 — Remove retired Rotom Docs rollback stack

- **Files changed:** `00-Rotom-Change-Log.md`, `01-Rotom-Server-Inventory.md`, `02-Docker-Services.md`, `08-Rotom-Directory-Tree.txt`, `architecture/Rotom-Architecture-System.md`, `guide/Editing-Docker-Compose.md`, `guide/PVE-and-Rotom-Total-Loss-Recovery.md`, `internals/tooling/test-rr-runbooks`.
- **Status:** **Implemented / Verified.**
- **Changes:** At Jared's request, removed the stopped `rotom-docs` container, its unattached `rotom-docs_default` network, and its dedicated stack and appdata directories. Updated current topology and validation references; historical entries remain evidence of the prior state.
- **Evidence:** Preflight confirmed the stopped container's read-only old-site bind and an unattached network. After removal, all 23 active containers remained running, the named directories and network were absent, 18 Docker networks remained, and the active `mkdocs-rr` listener and local HTTPS support route both returned HTTP 200.
- **Outstanding:** Available Sources replacement remains manual by Jared.

## 2026-10-17 — Repair ACL-safe Rotom Support publication

- **Files changed:** `00-Rotom-Change-Log.md`, `06-Maintenance-and-Automation.md`, `internals/publisher/README.md`, `internals/publisher/build-input.py`, `internals/publisher/sync`, `internals/publisher/test-publisher.py`.
- **Status:** **Implemented / Verified.** The current GitHub `main` revision is published by the private Rotom Support site.
- **Changes:** Changed executable-file classification from the deployment filesystem's ACL-influenced mode bits to the executable mode recorded in Git's index, while retaining exclusions for source extensions and shebang files. This preserves the `/srv/rotom` human-read ACL policy without misclassifying ordinary RS documents. Reconciled the installed agent-navigation title and link mappings back into the tracked builder and added an ACL-mode regression test.
- **Evidence:** The failure was reproduced as a manifest mismatch after named ACL masks made ordinary deployment-clone documents appear group-executable. Publisher tests, RS tests and lint, a non-publishing full build, live publication, representative rendered and raw-file requests, deployed-revision comparison, timer state, container health, and failed-unit checks passed after the repair.
- **Outstanding:** Available Sources replacement remains manual by Jared.

## 2026-10-17 — Add AI-assisted total-loss recovery bootstrap

- **Files changed:** `05-Backup-and-Restore.md`, `guide/PVE-and-Rotom-Total-Loss-Recovery.md`, `guide/README.md`, `internals/tooling/test-guides`, `00-Rotom-Change-Log.md`.
- **Status:** **Implemented / Documentation only.** No PVE, Rotom, NAS, backup, network, credential, or external-service state was changed.
- **Changes:** Added a copy-ready, provider-neutral AI recovery-coordinator prompt, required-input packet, structured phase/evidence protocol, explicit human approval boundaries, prompt-injection and secret-handling rules, completion definition, resumable handoff, and manual fallback. Added canonical backup-runbook routing and structural validation for the new section.
- **Evidence:** The prompt follows the existing RS phase gates and current authority model, including **PVE — Jared executes**, restricted staging, exact-source verification, isolated VM boot, human approval for destructive or production-identity actions, and Phases 0–20 acceptance. Guide and RS validation passed before publication.
- **Outstanding:** AI remains optional and cannot supply missing credentials, surviving backups, hardware facts, external access, or human authorization. Available Sources replacement remains manual by Jared.

## 2026-10-17 — Record /srv/rotom human access ACLs

- **Files changed:** `07-Users-and-Permissions.md`, `00-Rotom-Change-Log.md`.
- **Status:** **Implemented / Verified / Documentation only.**
- **Changes:** Recorded Jared and Fran named access and default ACLs under `/srv/rotom`, including secrets, the limits of inheritance, and the potential effect of recalculated ACL masks. The temporary broader `/home` change was restored from the pre-change snapshot for recorded entries; post-snapshot items were not included.
- **Evidence:** Recursive ACL commands completed successfully; 5,934 current directories had default entries for each account. Root and secrets ACLs and selected access tests passed. Home root ACLs and SSH private-key modes were spot checked after restore. No failed systemd units were reported. Not every file or application was individually tested.
- **Outstanding:** Future restrictive creation modes can mask named access; no automatic repair was installed. Audit post-snapshot `/home` items and application-specific effects if needed. Available Sources replacement remains manual by Jared.

## 2026-10-17 — Update Homepage NAS monitoring

- **Files changed:** `06-Maintenance-and-Automation.md`, `00-Rotom-Change-Log.md`.
- **Status:** **Implemented / Verified.**
- **Changes:** Renamed the Library NAS Storage card to NAS Storage and its description to Shared NAS volume capacity; retained its Libraries mount filesystem metric. Removed the separate UNAS Reachability ping card. The earlier entry describing that card remains historical.
- **Evidence:** Homepage's service API reported the renamed card with the existing Glances metric and no UNAS Reachability card. The five live NFS mounts reported the same capacity and usage for the shared NAS volume.
- **Outstanding:** Available Sources replacement remains manual by Jared.

## 2026-10-17 — Refresh total-loss recovery readiness evidence

- **Files changed:** `05-Backup-and-Restore.md`, `guide/PVE-and-Rotom-Total-Loss-Recovery.md`, `internals/tooling/test-rr-runbooks`, `00-Rotom-Change-Log.md`.
- **Status:** **Verified / Implemented / Documentation only.** Temporary root-only Rotom and PVE staging plus two network-isolated database containers were created for the rehearsals and removed afterward. Production data, running application containers, backup policy, retention, repository contents, PVE configuration, NAS configuration, and external services were not changed.
- **Changes:** Recorded the current Rotom Restic preflight, standard and full-data-read checks, complete verified restore, and native database recovery results. Added a tested canonical full-restore rehearsal procedure and an objective maximum-readiness gate so plan completeness cannot be mistaken for demonstrated recoverability. Added the current PVE Restic full-data-read, verified staging-restore, scope-review, exact VZDump compression/VMA verification, NFS-backed disposable restore, isolated boot, and exact cleanup evidence.
- **Evidence:** On 2026-10-17 Rotom snapshot `aad4a52e` completed at 03:05 PDT with service exit zero after retention/prune; standard `restic check` found no errors across 22 snapshots; full-data-read verification read all 1,077 packs without error; the complete 18.600 GiB snapshot restored 39,398 files/directories and verified all 27,581 files; all 17 discovered SQLite databases passed integrity checks; isolated restored Paperless PostgreSQL 18 and RomM MariaDB 11.8.9 copies completed crash recovery, native checks, and complete logical dumps with no network or published ports; and both containers plus the 19 GiB staging tree were removed. Final Rotom verification found 23 production containers running, no rehearsal containers or staging tree, the backup timer enabled/active, the service inactive between runs, the exact repository mount active, no failed units, and root capacity returned. PVE snapshot `19ed0226` then passed a full-data-read check of both packs and a verified root-only restore of 307 files/directories totaling 231.557 KiB, including verification of all 116 files; scope review found expected reconstruction inputs and no private-material paths. Current archive `vzdump-qemu-100-2026_10_17-05_00_07.vma.zst` (40,777,108,083 bytes) passed a complete zstd test and streamed VMA verification to 100 percent with pipeline status zero. It then restored completely as NFS-backed disposable VMID `101`; after removal of its NIC and all host-device attachments, the 1 GiB/two-core test boot reached guest-agent readiness and reported the expected `rotom` identity, Debian 13, and kernel. Graceful shutdown timed out and the disposable guest was stopped. Exact-target cleanup removed VMID `101`, both test disks, the temporary storage definition and path, and the earlier root-owned PVE Restic staging tree. Production VMID `100` remained running and agent-responsive, all normal storage stayed active, the PVE Restic timer remained enabled/active, no failed units were present, and delayed NAS accounting returned to its exact pre-test available-space value.
- **Outstanding:** A retained blank-hardware Phases 0–20 rehearsal, current NAS snapshot transcript, authenticated application/NAS consistency acceptance, independently tested recovery access and media, and a verified off-site layer remain necessary for maximum demonstrated readiness. On 2026-10-17 Jared accepted the existing NAS snapshot workflow as working and declined a repeat test; this is an owner decision, not new transcript evidence, so the objective maximum-readiness gate remains open. Available Sources replacement remains manual by Jared.

## 2026-10-17 — Expand the Docker Compose editing guide

- **Files changed:** `guide/Editing-Docker-Compose.md`, `guide/README.md`, `00-Rotom-Change-Log.md`.
- **Status:** **Documentation only**.
- **Changes:** Added a scoped editing walkthrough, validation example, recovery and verification guidance, and updated guide navigation. The numbered runbooks remain authoritative.
- **Evidence:** Existing Docker and backup runbooks; no live service was changed or newly audited.
- **Outstanding:** Available Sources replacement remains manual by Jared.

## 2026-10-17 — Improve the architecture system overview

- **Files changed:** `architecture/Rotom-Architecture-System.md`, `00-Rotom-Change-Log.md`.
- **Status:** **Documentation only**.
- **Changes:** Added a concise orientation and a link to the compact diagram; corrected DNS versus request paths and simplified the storage and protection diagram while retaining dated inspection evidence.
- **Evidence:** Current inventory and the existing architecture, network, storage, and backup documentation; no new live audit.
- **Outstanding:** Available Sources replacement remains manual by Jared.

## 2026-10-17 — Clarify the Rotom architecture diagrams

- **Files changed:** `architecture/Rotom-Architecture-Diagram.md`, `00-Rotom-Change-Log.md`.
- **Status:** **Documentation only**.
- **Changes:** Reorganized the architecture into separate system, access, and protection diagrams; distinguished DNS lookups from request traffic and the three backup paths.
- **Evidence:** Current inventory, network, storage, backup, and architecture documents; no new live audit.
- **Outstanding:** Available Sources replacement remains manual by Jared.

## 2026-10-17 — Fix diagram expand controls after rendering

- **Files changed:** `internals/publisher/diagram-expand.js`, `internals/publisher/diagram-expand.css.js`, `00-Rotom-Change-Log.md`.
- **Status:** **Implemented**.
- **Changes:** Attach expand controls to rendered Mermaid diagrams and move the original diagram into the expanded view, preserving the theme's closed shadow DOM.
- **Evidence:** The site theme replaces the original Mermaid code element with a rendered element containing a closed shadow root; the original control targeted the replaced element.
- **Outstanding:** Available Sources replacement remains manual by Jared.

## 2026-10-17 — Add diagram expand controls

- **Files changed:** `internals/publisher/build-input.py`, `internals/publisher/diagram-expand.js`, `internals/publisher/diagram-expand.css.js`, `internals/publisher/test-publisher.py`, `internals/publisher/README.md`, `06-Maintenance-and-Automation.md`, `00-Rotom-Change-Log.md`.
- **Status:** **Implemented**.
- **Changes:** Added an expandable view for each Mermaid diagram in the support site and included its site-only assets in the publisher.
- **Evidence:** Publisher configuration and validation for the updated site.
- **Outstanding:** Available Sources replacement remains manual by Jared.

## 2026-10-17 — Enable Mermaid diagrams on the support site

- **Files changed:** `internals/publisher/build-input.py`, `internals/publisher/test-publisher.py`, `internals/publisher/README.md`, `06-Maintenance-and-Automation.md`, `00-Rotom-Change-Log.md`.
- **Status:** **Implemented**.
- **Changes:** Configured the repository mirror to render Mermaid fenced diagrams and added a publisher configuration check.
- **Evidence:** The published architecture page displayed Mermaid source as a code block; the site builder did not enable Mermaid fences.
- **Outstanding:** Available Sources replacement remains manual by Jared.

## 2026-10-17 — Add the Rotom architecture diagram

- **Files changed:** `architecture/Rotom-Architecture-Diagram.md`, `architecture/README.md`, `00-Rotom-Change-Log.md`.
- **Status:** **Documentation only**.
- **Changes:** Added a Mermaid overview of system, service, storage, and backup relationships and linked it from architecture navigation.
- **Evidence:** Current server inventory and existing architecture overview; no new live audit.
- **Outstanding:** Available Sources replacement remains manual by Jared.

## 2026-10-17 — Simplify the Docker Compose guide

- **Files changed:** `guide/Editing-Docker-Compose.md`, `guide/README.md`, `00-Rotom-Change-Log.md`.
- **Status:** **Documentation only**.
- **Changes:** Replaced the long beginner guide with a compact map of Compose, appdata, and secrets paths, workload domains and services, and key website addresses; retained links to the authoritative runbooks.
- **Evidence:** Current Docker and network runbooks and a read-only listing of Compose paths; container runtime was not independently verified.
- **Outstanding:** Available Sources replacement remains manual by Jared.

## 2026-10-17 — Hide systemd unit files from the site

- **Files changed:** `internals/publisher/build-input.py`, `internals/publisher/sync`, `internals/publisher/test-publisher.py`, `internals/publisher/README.md`, `01-Rotom-Server-Inventory.md`, `06-Maintenance-and-Automation.md`, `00-Rotom-Change-Log.md`.
- **Status:** **Implemented / Verified** for the installed publisher and non-publishing build; publication remains to be verified.
- **Changes:** Exclude systemd unit files from site navigation and raw downloads without changing repository files.
- **Evidence:** Jared requested hiding files such as `rotom-support-sync.service`; publisher tests and a non-publishing build passed after installation.
- **Outstanding:** Validate and publish the revised site; Available Sources replacement remains manual by Jared.

## 2026-10-17 — Hide source code and scripts from the site

- **Files changed:** `internals/publisher/build-input.py`, `internals/publisher/sync`, `internals/publisher/test-publisher.py`, `internals/publisher/README.md`, `01-Rotom-Server-Inventory.md`, `06-Maintenance-and-Automation.md`, `00-Rotom-Change-Log.md`.
- **Status:** **Implemented / Verified** for the installed publisher and non-publishing build; publication remains to be verified.
- **Changes:** Exclude source files and scripts from site navigation and raw downloads; retain the repository files and render links to excluded files as text.
- **Evidence:** Jared requested hiding source code and scripts, including extensionless scripts; publisher tests and a non-publishing build passed after installation.
- **Outstanding:** Validate and publish the revised site; Available Sources replacement remains manual by Jared.

## 2026-10-17 — Capitalize site folder labels

- **Files changed:** `internals/publisher/build-input.py`, `internals/publisher/test-publisher.py`, `06-Maintenance-and-Automation.md`, `00-Rotom-Change-Log.md`.
- **Status:** **Implemented / Verified** for the installed builder and non-publishing build; publication remains to be verified.
- **Changes:** Capitalize the first letter of nested folder labels in site navigation without changing repository paths.
- **Evidence:** Jared's request; publisher fixture tests and a non-publishing build passed after installation.
- **Outstanding:** Verify installation and site labels; Available Sources replacement remains manual by Jared.

## 2026-10-17 — Use Markdown titles in site navigation

- **Files changed:** `internals/publisher/build-input.py`, `internals/publisher/test-publisher.py`, `06-Maintenance-and-Automation.md`, `00-Rotom-Change-Log.md`.
- **Status:** **Implemented / Verified** for the installed builder and non-publishing build; publication remains to be verified.
- **Changes:** Extend title-based navigation from README files to all Markdown files, with a filename fallback when a title is absent. Repository filenames and raw content remain unchanged.
- **Evidence:** Jared's request; publisher fixture tests and a non-publishing build passed after installation.
- **Outstanding:** Verify installation and published labels; Available Sources replacement remains manual by Jared.

## 2026-10-17 — Organize agent instructions

- **Files changed:** `internals/codex/` moved to `internals/agents/`; `internals/README.md`, `internals/tooling/test-rr-runbooks`, `00-Rotom-Change-Log.md`.
- **Status:** **Documentation only.**
- **Changes:** Grouped the global instruction backup under agents and linked to the authoritative root `AGENTS.md` instead of duplicating it. Updated validation paths.
- **Evidence:** Jared approved the organization in chat.
- **Outstanding:** Available Sources replacement remains manual by Jared.

## 2026-10-17 — Exclude Git-related paths from the site

- **Files changed:** `internals/publisher/build-input.py`, `internals/publisher/sync`, `internals/publisher/test-publisher.py`, `internals/publisher/README.md`, `01-Rotom-Server-Inventory.md`, `06-Maintenance-and-Automation.md`, `00-Rotom-Change-Log.md`.
- **Status:** **Implemented / Verified** for the installed publisher and non-publishing build; publication remains to be verified.
- **Changes:** Exclude paths containing a component beginning with `.git` from site navigation and raw downloads, without changing repository files or membership.
- **Evidence:** Jared's request; publisher fixture tests and a non-publishing build passed after installation. The previous publisher exposed tracked Git-related files in navigation and raw copies.
- **Outstanding:** Validate and publish the revised site; Available Sources replacement remains manual by Jared.

## 2026-10-17 — Name README pages in site navigation

- **Files changed:** `internals/publisher/build-input.py`, `internals/publisher/test-publisher.py`, `06-Maintenance-and-Automation.md`, `00-Rotom-Change-Log.md`.
- **Status:** **Implemented / Verified** for the installed builder and non-publishing build; published labels remain to be verified.
- **Changes:** Use each README's level-one title as its site navigation label while retaining its filename and raw content.
- **Evidence:** Publisher source-selection test and non-publishing build passed. The installed builder retains legacy website link mappings absent from the tracked builder; those mappings were preserved and require separate investigation.
- **Outstanding:** Verify publication and displayed labels; Available Sources replacement remains manual by Jared.

## 2026-10-17 — Add publisher overview

- **Files changed:** `internals/publisher/README.md`, `internals/README.md`, `00-Rotom-Change-Log.md`.
- **Status:** **Documentation only.**
- **Changes:** Added an overview of publisher files and a link from the internals index, with the runbook retaining ownership of publication operations.
- **Evidence:** Reviewed the publisher implementation and the current maintenance runbook.
- **Outstanding:** Available Sources replacement remains manual by Jared; verify the repository mirror after the pushed revision is published.

## 2026-10-17 — Define Rotom Support by tracked repository content

- **Files changed:** `AGENTS.md`, `README.md`; current navigation and classification files under `architecture/`, `guide/`, `internals/`, and `runbook/`; `internals/tooling/rs`, `internals/tooling/test-rr-runbooks`, and `internals/tooling/test-guides`.
- **Status:** **Documentation only / Verified.** No Rotom live configuration or publication destination was changed.
- **Changes:** Adopted intentionally tracked repository content as the RS membership boundary, with untracked, ignored, temporary, generated, and Git-internal content excluded. Established `runbook/` as RS's primary operational and documented-current-state authority; retained architecture, guide, internals, and root-level files as RS components with narrower roles. Available Sources is now explicitly a separate manually maintained destination rather than the RS boundary. This current policy supersedes the active Available-Sources membership definition adopted on 2026-09-19 and its later current restatements; those dated entries remain unchanged as historical evidence.
- **Evidence:** Jared's 2026-10-17 policy decision; complete tracked-file inventory and active-definition review; repository validation and delivery checks recorded at completion.
- **Outstanding:** Available Sources replacement remains manual by Jared. Verify the repository mirror after the pushed revision is published.

## 2026-10-17 — Remove retired website inputs

- **Files changed:** `00-Rotom-Change-Log.md`, `01-Rotom-Server-Inventory.md`; repository navigation, publisher, and test files; removed `internals/website/`.
- **Status:** **Documentation only.**
- **Changes:** Removed the former website landing-page inputs and their obsolete repository references; the private site continues to mirror tracked repository files.
- **Evidence:** The retained inputs identified themselves as former landing pages; runbook and publisher source-selection tests passed after removal. No live publication was performed.
- **Outstanding:** Available Sources replacement remains manual by Jared; verify repository publication after the push.

## 2026-10-17 — Organize repository site navigation

- **Files changed:** `00-Rotom-Change-Log.md`, `06-Maintenance-and-Automation.md`, and `internals/publisher/` builder, publisher, and test.
- **Status:** **Implemented / Verified.** The site groups tracked repository files under Home, Runbook, Architecture, Guides, Internals, and Repository tabs and provides a contents panel for document headings. Source membership and raw file preservation are unchanged.
- **Evidence:** The isolated build contained all 40 tracked file pages and rendered the tabs and document contents. The first publication rolled back after an immediate startup health check raced the container; adding a bounded retry allowed the validated build to publish. The preceding site and publisher files were retained.
- **Outstanding:** Available Sources replacement remains manual by Jared; verify the final GitHub revision after this change is pushed.

## 2026-10-17 — Mirror the complete repository on the private site

- **Files changed:** `00-Rotom-Change-Log.md`, `01-Rotom-Server-Inventory.md`, `06-Maintenance-and-Automation.md`, repository navigation and publisher files.
- **Status:** **Implemented / Verified.** The private site now displays every tracked GitHub `main` file, serves exact original copies under `/raw/`, and checks for updates every five minutes. RS membership and Available Sources are unchanged.
- **Evidence:** A clean checkout passed `rs check`; an isolated build verified all 34 then-tracked files and raw copies. The published site served all 34 originals byte-for-byte over loopback HTTP; the updater timer was active, its first check succeeded, and `mkdocs-rr` was running with a read-only root filesystem. The prior publisher and site were retained for recovery.
- **Outstanding:** Available Sources replacement remains manual by Jared. Recheck the final GitHub revision after this documentation update is pushed.

## 2026-10-17 — Correct Mac checkout path

- **Files changed:** `00-Rotom-Change-Log.md`, `01-Rotom-Server-Inventory.md`.
- **Status:** **Documentation only / Verified.**
- **Changes:** Updated the current Mac checkout path and resolver fact; prior path records remain historical.
- **Evidence:** Jared supplied terminal output showing `rs path` resolves `/Users/jared/Documents/ChatGPT/rotom-support` and `rs status` reports the expected SSH origin, clean `main`, and zero cached commits ahead or behind at `09233c1`. The resolver configuration was updated on the Mac.
- **Outstanding:** A fresh GitHub check was not shown; Available Sources replacement remains manual by Jared.

## 2026-10-17 — Align published page titles

- **Files changed:** `00-Rotom-Change-Log.md`, `01-Rotom-Server-Inventory.md`, `06-Maintenance-and-Automation.md`; installed `mkdocs-rr` publisher and `mkdocs.yml`.
- **Status:** **Implemented / Verified.** The Runbook landing heading is now Rotom Runbook; navigation labels and browser titles match their page headings. The overall site remains Rotom Support.
- **Evidence:** The guarded publisher's validation build and publication succeeded; all 15 generated pages had matching browser titles and headings, and the live Runbook page returned the new title and heading. Pre-change publisher and configuration recovery copies remain beside the installed files.
- **Outstanding:** Available Sources replacement remains manual by Jared.

## 2026-10-17 — Rewrite published overview and landing pages

- **Files changed:** `00-Rotom-Change-Log.md`, `01-Rotom-Server-Inventory.md`, `06-Maintenance-and-Automation.md`, supplementary architecture document `architecture/Rotom-Architecture-System.md`, and website inputs `internals/website/README.md`, `internals/website/home.md`, `internals/website/architecture/index.md`, and `internals/website/guides/index.md`.
- **Status:** **Documentation only / Verified / Published.** Generated-site output and the `mkdocs-rr` container changed; no Rotom application, storage, network, identity, backup, or publisher configuration changed.
- **Changes:** Reworked the editable published overview and landing sources around explicit audiences, practical starting points, descriptive destinations, logical task groups, and preserved authority boundaries and cautions. Reconciled current RS publisher facts after read-only inspection confirmed that the installed publisher now reads `architecture/Rotom-Architecture-System.md` and publishes `/architecture/rotom-architecture-system/`; this supersedes the unresolved current-state statements in the two preceding architecture-rename entries without rewriting their historical evidence. Published the revised sources through the existing guarded workflow.
- **Evidence:** Repository publication-source and navigation audit; numbered-RS and guide validation, RS lint, Git whitespace validation, and an isolated non-publishing MkDocs build passed. The guarded publisher fast-forwarded its clean deployment checkout to `e4d1a80`, completed the pinned isolated build, and recreated only `mkdocs-rr`. Home, Runbook, Server Inventory, Architecture, Architecture System, Guides, and Total-Loss Recovery routes returned HTTPS `200`; the new overview text rendered; the container remained running with zero restarts and a read-only site mount; and generated copies matched the selected landing and numbered sources. The current architecture route returned `200`, while the prior route returned `404` before publication.
- **Outstanding:** The short `/runbook/` overview is generated by the installed live publisher rather than an editable repository input. Rewriting it requires a separate publisher-source change, so it remains unchanged. Available Sources replacement remains manual by Jared.

## 2026-10-17 — Rename supplementary architecture title

- **Files changed:** `00-Rotom-Change-Log.md`, repository navigation files `README.md` and `architecture/README.md`, supplementary website input `internals/website/architecture/index.md`, and `architecture/Rotom-Architecture-System.md`.
- **Status:** **Documentation only / Verified.** No Rotom application, generated-site, or live publisher state changed.
- **Changes:** Changed the supplementary document title and matching repository navigation labels from **Rotom Architecture Overview** to **Rotom Architecture System**.
- **Evidence:** User-requested title change, repository-wide title audit, numbered-RS and guide validation, RS lint, and Git whitespace validation.
- **Outstanding:** The installed guarded publisher still requires the separately authorized filename update recorded below before this title can be published. Available Sources replacement remains manual by Jared.

## 2026-10-17 — Rename supplementary architecture source

- **Files changed:** `00-Rotom-Change-Log.md`, `01-Rotom-Server-Inventory.md`, `06-Maintenance-and-Automation.md`, repository navigation files `README.md` and `architecture/README.md`, supplementary website inputs `internals/website/README.md` and `internals/website/architecture/index.md`; moved `architecture/Rotom-Architecture-Overview.md` to `architecture/Rotom-Architecture-System.md`.
- **Status:** **Documentation only / Verified.** No Rotom application, storage, network, identity, credential, backup, recovery, generated-site, or live publisher state changed.
- **Changes:** Renamed the canonical supplementary architecture source and updated repository navigation and future-build links. Preserved the current published `/architecture/rotom-architecture-overview/` route and recorded that the installed guarded publisher still expects the prior source filename pending separate live-change authorization.
- **Evidence:** User-requested filename change, repository-wide reference audit, numbered-RS and guide validation, RS lint, and Git whitespace validation.
- **Outstanding:** Update and verify the installed guarded publisher before the next publication, then publish the renamed page and reconcile the canonical portal route. Available Sources replacement remains manual by Jared.

## 2026-10-17 — Rename repository internals directory

- **Files changed:** Moved repository directory `support/` to `internals/`; updated current paths in `AGENTS.md`, `README.md`, `architecture/README.md`, `guide/README.md`, `runbook/README.md`, `01-Rotom-Server-Inventory.md`, `06-Maintenance-and-Automation.md`, repository tooling and navigation files, and the live guarded publisher.
- **Status:** **Implemented / Documentation only / Verified / Published.** No Rotom application, storage, network, identity, credential, backup, or recovery state changed.
- **Changes:** Renamed the repository-only umbrella directory to distinguish internal agent material, tooling, and website inputs from the Rotom Support repository name. Updated current references, structural tests, secret-scan scope, and the publisher's explicit supplementary-source allowlist while preserving historical `support/` paths as dated evidence.
- **Evidence:** Began from clean `main` matching cached `origin/main`. Repository structure, CLI, guide, lint, shell-syntax, link, secret-pattern, and whitespace checks passed. The guarded publisher validated the renamed explicit source selection in an isolated build, publication completed, and the existing private portal routes remained available over loopback and HTTPS.
- **Outstanding:** Available Sources replacement remains manual by Jared.

## 2026-10-17 — Publish supplementary architecture and recovery documents

- **Files changed:** `00-Rotom-Change-Log.md`, `01-Rotom-Server-Inventory.md`, `06-Maintenance-and-Automation.md`, repository navigation files `README.md`, `architecture/README.md`, and `guide/README.md`, supplementary website inputs `support/website/README.md`, `support/website/architecture/index.md`, and `support/website/guides/index.md`, plus the live guarded publisher and MkDocs navigation configuration.
- **Status:** **Implemented / Documentation only / Verified / Published.**
- **Changes:** Added the canonical supplementary `architecture/Rotom-Architecture-Overview.md` and `guide/PVE-and-Rotom-Total-Loss-Recovery.md` files to the private portal's explicit allowlist and organized navigation without changing their source content, RS membership, Available Sources status, or canonical ownership boundaries. Repository navigation, the publisher description, and section landing pages now expose those relationships clearly. Internal control files, repository-navigation-only READMEs, and tooling/development artifacts remain excluded.
- **Evidence:** Repository and live-site audit found a clean checkout, no untracked files, the expected trusted-LAN-only portal, a clean guarded deployment clone five commits behind GitHub, and no credential values, private keys, tokens, cookies, or personal contact data in either selected document. Numbered-RS, guide, CLI, lint, link, secret-pattern, shell, and whitespace validation passed. The guarded deployment clone fast-forwarded cleanly to source checkpoint `6e64a4f`, and a second isolated MkDocs build completed without warnings after the publisher normalized only generated-site links whose GitHub and MkDocs heading anchors differ. Atomic publication recreated only `mkdocs-rr`. All 15 tested Home, Runbook, Architecture, Guides, and document routes returned HTTP `200`; both new pages returned `200` through `support.rotom.casa`, their landing links and representative recovery phase anchors rendered correctly, and the container was running with zero restarts, its loopback-only listener, and read-only site mount. A disposable untrusted Docker-bridge client received HTTP `403`, and no systemd units were failed.
- **Outstanding:** None for this publication. Available Sources replacement remains manual by Jared.

## 2026-10-17 — Move repository architecture overview

- **Files changed:** `00-Rotom-Change-Log.md`, `01-Rotom-Server-Inventory.md`, `08-Rotom-Directory-Tree.txt`, repository navigation files `README.md`, `guide/README.md`, and `architecture/README.md`; moved `guide/Rotom-Architecture-Overview.md` to `architecture/Rotom-Architecture-Overview.md`.
- **Status:** **Documentation only / Verified.**
- **Changes:** Moved the supplementary Rotom architecture overview into the repository's architecture directory and updated navigation, source-map, publication-boundary, and directory-reference text. The overview remains outside Rotom Support and Available Sources.
- **Evidence:** Requested repository organization change, local checkout inspection, guide and numbered-RS structural tests, RS lint, and Git whitespace validation.
- **Outstanding:** Available Sources replacement remains manual by Jared.

## 2026-10-17 — Resolve architecture audit findings

- **Files changed:** `00-Rotom-Change-Log.md`, `01-Rotom-Server-Inventory.md`, `02-Docker-Services.md`, `03-Network-and-Domains.md`, `04-NAS-and-Storage.md`, `06-Maintenance-and-Automation.md`, `08-Rotom-Directory-Tree.txt`, and repository guide `guide/Rotom-Architecture-Overview.md`.
- **Status:** **Implemented / Verified / Documentation only.** Added explicit DNS `192.168.1.1` to the Cloudflare DDNS Compose service and recreated only that container. Corrected the recorded Aloha NPM upstream to live `127.0.0.1:7778`. Recorded Jared's acceptance of the observed Arcane update/heal policy and of both healthy Palworld servers remaining running under `restart: unless-stopped`.
- **Evidence:** Before the DDNS correction, its generated resolver reported no external nameservers and logs repeatedly showed resolution failure. After recreation it named `192.168.1.1`, retained restart count zero, and reported the Cloudflare A record already current; the other 23 running containers remained running. Live NPM data plus local and external probes verified Aloha HTTP `200`. Cloudflare API/public DNS checks verified the unproxied apex A record and wildcard CNAME. Arcane settings were read from its live database; Palworld health, restart policies, and scheduled update/backup settings were inspected live. PVE read-only status APIs reported successful current VM and PVE Restic backups. Jared confirmed the router/WAN, PVE, NAS control plane, and NAS snapshot protection work and waived further authenticated inspection.
- **Outstanding:** Arcane stale project rows, two named volumes, and any unreferenced images remain a separate exact-object cleanup review. Exact router, PVE, and NAS control-plane exports were intentionally not captured; this is an evidence-provenance limit, not an active discrepancy. Available Sources replacement remains manual by Jared.

## 2026-10-17 — Rename repository architecture directory

- **Files changed:** `architecture/.gitkeep`, `00-Rotom-Change-Log.md`, `01-Rotom-Server-Inventory.md`, `08-Rotom-Directory-Tree.txt`.
- **Status:** **Implemented / Documentation only.**
- **Changes:** Renamed the repository's empty `Architecture/` directory to `architecture/` and updated its current source map and directory reference. The separate website architecture input remains unchanged.
- **Evidence:** Local checkout inspection and the requested rename.
- **Outstanding:** Available Sources replacement remains manual by Jared.

## 2026-10-16 — Verify Mac compatibility cutover

- **Files changed:** `00-Rotom-Change-Log.md`, `01-Rotom-Server-Inventory.md`, `06-Maintenance-and-Automation.md`; Mac `/usr/local/bin/rr` and its recovery copy.
- **Status:** **Implemented / Verified.**
- **Changes:** Jared replaced the Mac's independent `rr` with the minimal `rs` compatibility wrapper after `rs` passed its checks. The wrapper remains for unverified legacy consumers; the existing Mac checkout path and resolver remain unchanged. Apple's unrelated `/usr/bin/rs` remains available at its absolute path; the login PATH selects `/usr/local/bin/rs` first.
- **Evidence:** Jared's Terminal output showed `rs check` and the installed `rr check` passing against GitHub. Independent Mac inspection confirmed root:wheel mode `0755` and wrapper SHA-256 `dde6073b21a08f928b8cd17c0c1e1458171e3a00a3bbcd110da51a2c0f8af73e`, matching the tracked wrapper. The prior implementation is retained at `/usr/local/bin/rr.pre-rs-20261016`, root:wheel mode `0700`; restore that file to `/usr/local/bin/rr` if rollback is required.
- **Outstanding:** Jared manually replaces Available Sources. Audit additional environments independently if they become accessible; do not infer coverage beyond Rotom and this Mac. The legacy `docs.rotom.casa` route continues to redirect to the existing private portal.

## 2026-10-16 — Verify the Mac RS installation

- **Files changed:** `00-Rotom-Change-Log.md`, `01-Rotom-Server-Inventory.md`, `06-Maintenance-and-Automation.md`; Mac `/usr/local/bin/rs`.
- **Status:** **Implemented / Verified**, with compatibility cutover outstanding.
- **Evidence:** Jared installed `/usr/local/bin/rs` as `root:wheel` mode `0755`. Its SHA-256 `f263f681b55ce8f2dab3f7be7cf46e1d30ae3b8407a5d41e92501a39f427037c` matches the tracked implementation; `rs check` passed against clean GitHub `main`. Mac CLI, structural, and guide tests passed after the portability fixes. The existing Apple `/usr/bin/rs` was preserved; the login PATH resolves `/usr/local/bin/rs` first.
- **Recovery / outstanding:** The old Mac `/usr/local/bin/rr` remains an independent implementation pending a root-owned backup and replacement with the tested compatibility wrapper. Desktop Commander blocks privileged commands, so Jared must perform that installation. Available Sources replacement remains manual. Existing Mac checkout and publisher paths are intentionally retained.

## 2026-10-16 — Correct validation portability on the Mac

- **Files changed:** `00-Rotom-Change-Log.md` and repository support files `support/tooling/test-rr-runbooks` and `support/tooling/test-guides`.
- **Status:** **Implemented / Verified** on Rotom and Mac.
- **Changes:** Replaced the GNU-only `find -printf` use in the website input allowlist check with portable `find` and `sed`, preserving the same exact membership comparison. Replaced guide enumeration requiring Bash 4 and GNU sort with portable NUL-delimited enumeration.
- **Evidence:** The Mac checkout fast-forwarded cleanly to `6aa7cbe` using `rr pull`; its isolated RS CLI tests passed. The structural test then stopped because macOS `find` does not support `-printf`. The corrected structural test passed on both Rotom and the Mac; guide validation then exposed Bash 3 incompatibility. The corrected guide validation passed on the Mac, as did the tracked `rs check` against GitHub; isolated RS CLI tests also passed.
- **Outstanding:** Install and verify the Mac RS helper; Desktop Commander blocks privileged commands. The Mac already has an unrelated `/usr/bin/rs`, which remains unchanged and can be invoked by its absolute path; `/usr/local/bin` precedes `/usr/bin` in the observed login PATH. Available Sources replacement remains manual.

## 2026-10-16 — Verify RS repository and publication checkpoints

- **Files changed:** `00-Rotom-Change-Log.md`.
- **Status:** **Documentation only / Verified**, with Mac and Available Sources work outstanding.
- **Evidence:** GitHub reports repository ID `1390601496`, owner `jaredwines`, default branch `main`, public visibility, and administrator access for Jared. The public branch API reports `main` unprotected with no active branch rules, matching the earlier recorded baseline. At revision `2c5435d6462d3df163ba46455eb377b3e84a4ded`, the clean Rotom checkout passed `rs check` and the clean publisher checkout matched it. The final RS publication served the expected title and denied an untrusted bridge client with HTTP 403; the prior entry records the recovery copies.
- **Outstanding:** Only Rotom is connected to Desktop Commander; the Mac is not mounted and has no configured SSH host. Its `rs` installation, dependencies, and independent checks remain unverified. Jared must manually replace Available Sources. Repository permissions beyond the observed administrator access and the full settings inventory were not independently compared.

## 2026-10-16 — Migrate documentation identity to Rotom Support

- **Files changed:** Numbered documents `00`–`08`, `AGENTS.md`, `README.md`, the separate total-loss guide, website guide input, and documentation tooling. Rotom's installed helper and Codex entry point are also updated.
- **Status:** **Implemented / Verified**, with outstanding environment and publishing checks below.
- **Changes:** Adopted Rotom Support (RS), `rs`, and `Update the RS`, retaining the established maintenance and ticket authorization contracts and Available Sources boundary. The existing GitHub repository was renamed earlier in place to `jaredwines/rotom-support`; its recorded pre-rename checkpoint is `4746e81`. The Rotom checkout remains `/home/jared/rotom-support`. The installed `rr` is a compatibility wrapper for `rs`, and the old resolver path remains a fallback; legacy publisher paths and test filenames remain intentional. Historical records are preserved.
- **Evidence:** The clean pre-change Rotom checkout at `c5d3187348fbf1fd67cf8973a334088874bd4a55` passed `rr check`; isolated RS CLI, numbered-structure, and guide tests passed. The installed `rs` passed `rs check` and the `rr` wrapper resolved the same checkout. Revision `926eb979dc2c22e52ca8b57d4062672a6e5e510a` was pushed, accepted by the guarded publisher, built and published. Local HTTPS served the Rotom Support overview; `docs.rotom.casa` redirected to `support.rotom.casa`. The effective proxy configuration allows loopback and the trusted LAN and denies others; an isolated Docker-bridge client received HTTP 403. Routing and access policy were not changed.
- **Recovery:** The previous Rotom helper is retained as `/usr/local/bin/rr.pre-rs-20261016` (SHA-256 `a56c440ea87fe6b0a3558aa28736ed4308402cbf2b9c2400c01b5cc66b73746d`); reinstall it at `/usr/local/bin/rr` if the new helper must be rolled back. The pre-publication deployment clone was clean at `4a3c8f4272418ec6aae4fbc68f7aba8006f3dad2`; the immediate pre-migration publisher script and current and previous site/source copies are retained with the `.pre-rs-20261016` suffix. The previous Codex entry point is retained at `/home/jared/.codex/AGENTS.md.pre-rs-20261016`.
- **Outstanding:** Independently install and verify `rs` on the Mac and audit its dependencies; manually replace Available Sources. Verify the final Git and publisher revision after this evidence update and inspect any unavailable environments; the legacy hostname remains a redirect rather than the portal's canonical host.

## 2026-10-16 — Move the Rotom checkout to rotom-support

- **Files changed:** `00-Rotom-Change-Log.md`, `01-Rotom-Server-Inventory.md`, `06-Maintenance-and-Automation.md`, `08-Rotom-Directory-Tree.txt`; Rotom checkout location and private `rr` resolver configuration.
- **Status:** **Implemented / Verified.**
- **Changes:** Moved Jared's Rotom checkout from `/home/jared/documentation/rotom-runbook` to `/home/jared/rotom-support` and updated its private resolver. The GitHub origin, Mac checkout, and separate Support publisher checkout were not moved. Earlier path records remain historical evidence.
- **Evidence:** Before the move, `rr check` passed on a clean checkout matching GitHub, the destination was absent, and both paths were on the same filesystem. After the move, `rr path` and `rr check` confirmed the new checkout and GitHub synchronization.
- **Outstanding:** Available Sources replacement remains manual by Jared; the Mac checkout needs a routine pull for these documentation changes.

## 2026-10-16 — Verify the Mac after the repository rename

- **Files changed:** `00-Rotom-Change-Log.md`, `06-Maintenance-and-Automation.md`.
- **Status:** **Documentation only / Verified.**
- **Changes:** Recorded the Mac checkout and helper cutover to `jaredwines/rotom-support`. This supersedes the outstanding Mac synchronization and verification items in the preceding repository-rename, Architecture-directory, publisher-repair, and runbook-directory entries; their dated evidence remains historical.
- **Evidence:** Jared supplied Mac terminal output showing the checkout fast-forwarded to `0b63c03`, the helper and origin were updated, and `rr check` passed with a clean `main`, the new SSH origin, all nine numbered files, successful lint, and a GitHub match. Jared also confirmed replacement of the prior Available Sources copies.
- **Outstanding:** Jared must manually replace these newly updated Available Sources files; the Mac checkout will need a routine pull for this documentation update.

## 2026-10-16 — Rename the GitHub repository to Rotom Support

- **Files changed:** `00-Rotom-Change-Log.md`, `06-Maintenance-and-Automation.md`, `support/tooling/rr`, `support/tooling/test-rr-cli`; installed Rotom helper, checkout origin, publisher script, and deployment-clone origin.
- **Status:** **Implemented / Verified.**
- **Changes:** Jared renamed the existing GitHub repository to `jaredwines/rotom-support`. Updated the helper and its CLI test to expect the new SSH origin, and updated the publisher and its deployment clone to the new HTTPS origin. The Rotom checkout path and the Rotom Runbook documentation name remain unchanged.
- **Evidence:** Before the rename, `rr check` passed on clean `main`; preparation commit `4746e81` passed the isolated helper and numbered-runbook tests and was pushed. After the rename, the new SSH and HTTPS origins returned that same `main` revision, the installed Rotom helper passed `rr check`, and the publisher fast-forwarded its clean clone and completed a validation-only MkDocs build.
- **Outstanding:** The Mac checkout and installed helper require independent synchronization and verification. Available Sources replacement remains manual by Jared.

## 2026-10-16 — Record repository Architecture directory

- **Files changed:** `00-Rotom-Change-Log.md`, `01-Rotom-Server-Inventory.md`, `08-Rotom-Directory-Tree.txt`.
- **Status:** **Documentation only / Verified.**
- **Changes:** Recorded the new `Architecture/` directory in the repository source map and directory reference. It currently contains only a Git placeholder and no RR source; the existing supplementary website architecture input remains separate. This does not decide the membership or publication status of future files.
- **Evidence:** Local repository inspection and commit `481fa37`; the existing numbered RR set remains `00`–`08` in `runbook/`.
- **Outstanding:** Available Sources replacement remains manual by Jared; the Mac checkout and helper synchronization remain unverified.

## 2026-10-16 — Repair Rotom Support publisher synchronization

- **Files changed:** `00-Rotom-Change-Log.md`, `06-Maintenance-and-Automation.md`, `08-Rotom-Directory-Tree.txt`; live Rotom Support publisher script and deployment checkout.
- **Status:** **Implemented / Verified.**
- **Changes:** With Jared's approval, preserved the clean divergent deployment checkout and replaced it with a fresh clone of the verified GitHub `main`. Updated the guarded publisher to read the numbered sources from `runbook/` while retaining its origin, branch, clean-tree, fast-forward, allowlist, staged-build, and rollback safeguards. In the generated site only, the two references to the separate recovery guide are rendered as plain text because the guide is outside the publication allowlist.
- **Evidence:** The old checkout at `e87d6f3` and rewritten GitHub history had no common ancestor; corresponding historical commits had matching subjects and timestamps but different tree contents. SSH and HTTPS both identified the same GitHub branch. A separate checkout and the installed publisher each passed isolated MkDocs validation without warnings. The guarded publisher built and published successfully; local Home, Runbook, inventory, backup, architecture, and guides routes returned HTTP 200, the guide references appeared as text, and the documentation container was running.
- **Recovery:** Retained the previous checkout at `/srv/rotom/appdata/platform/mkdocs-rr/repository.pre-runbook-directory-20261016` and publisher script at `/srv/rotom/stacks/platform/mkdocs-rr/scripts/publish-source.pre-runbook-directory-20261016`. Preserved the earlier `site.previous` and `source.previous` copies with the `.pre-runbook-directory-20261016` suffix and the immediate pre-cutover site and source with the `.pre-runbook-publication-20261016` suffix.
- **Outstanding:** Mac helper and checkout synchronization and manual Available Sources replacement remain Jared's tasks.

## 2026-10-16 — Place the numbered RR in `runbook/`

- **Files changed:** All nine numbered RR documents were moved into `runbook/`; repository instructions, README, guide links, and RR tooling were updated for the new paths.
- **Status:** **Implemented / Verified**, with publisher synchronization blocked.
- **Changes:** The checkout root still identifies the repository via `rr path`; append `runbook/` for the numbered documents. The separate `guide/` boundary and the existing filenames remain unchanged.
- **Evidence:** Repository path, link, structural, and isolated helper tests pass against the new layout. Rotom's global Codex instructions identify the new directory. The installed `/usr/local/bin/rr` matches the tracked helper and `rr check` passed; its previous version is retained at `/usr/local/bin/rr.pre-runbook-directory-20261016`.
- **Outstanding:** An isolated publisher validation stopped at the deployment checkout's guard: its `main` at `e87d6f3` is ahead by 177 commits and behind by 187 commits relative to fetched `origin/main` at `70903e2`, and the histories have no common ancestor. No reset, merge, replacement, build, or publication was attempted. Investigate that discrepancy before updating the publisher's source paths or publishing. The existing site continues serving its previously generated content. The Mac helper and checkout still require synchronization. Available Sources replacement remains manual by Jared.

## 2026-10-16 — Establish `guide/` as a hard boundary outside RR

- **Files changed:** `00-Rotom-Change-Log.md`, `01-Rotom-Server-Inventory.md`; repository instruction/support files `AGENTS.md`, `README.md`, `support/tooling/rr`, `support/tooling/test-rr-cli`, `support/tooling/test-rr-runbooks`, and new `support/tooling/test-guides`.
- **Status:** **Documentation only / Implemented / Verified.** No PVE, Rotom, VM, NAS, repository data, snapshot, archive, network, credential, DNS, external service, or live publisher state changed.
- **Changes:** Established the directory-wide rule that every file under `guide/` is separate from RR, the Core Numbered Reference Set, Available Sources, RR-only validation, and RR publication. Removed the guide dependency from `rr lint`, its CLI fixture, and the RR structural suite; created an independent guide validator that retains link, fence, label, secret-pattern, phase, and diagram checks without changing RR membership.
- **Evidence:** RR and guide validation suites, isolated RR CLI tests, shell syntax, whitespace, local link/fragment checks, secret-pattern checks, and four-diagram Mermaid grammar validation passed independently.
- **Outstanding:** Available Sources remains the numbered `00`–`08` RR set. Files under `guide/` require separate distribution or publication decisions if desired.

## 2026-10-16 — Separate the total-loss guide from Rotom Runbook

- **Files changed:** `00-Rotom-Change-Log.md`, `01-Rotom-Server-Inventory.md`, `02-Docker-Services.md`, `05-Backup-and-Restore.md`, `06-Maintenance-and-Automation.md`, `08-Rotom-Directory-Tree.txt`; repository guide `guide/PVE-and-Rotom-Total-Loss-Recovery.md`; repository support files `README.md`, `support/tooling/rr`, `support/tooling/test-rr-cli`, `support/tooling/test-rr-runbooks`, and `support/website/guides/index.md`.
- **Status:** **Documentation only / Implemented / Verified.** No PVE, Rotom, VM, NAS, repository data, snapshot, archive, network, credential, DNS, external service, or live publisher state changed.
- **Changes:** Jared clarified that the total-loss document is a guide, not a Rotom Runbook member. Moved it from root numbered document `09` to `guide/PVE-and-Rotom-Total-Loss-Recovery.md`, removed the numeric prefix and RR-member metadata, restored the Core Numbered Reference Set to `00`–`08`, and separated guide validation from RR membership validation. This entry supersedes only the membership, source-map, and publication classifications in the two immediately following total-loss entries; their guide content, evidence, and validation history remain valid.
- **Evidence:** Repository-wide reference audit, source-map reconciliation, local link/fragment checks, guide structure checks, four-diagram Mermaid grammar validation, RR tooling tests, shell syntax, whitespace, and secret-pattern checks.
- **Outstanding:** Available Sources must remain `00`–`08`; if document `09` was manually added, Jared must remove it. The guide is not admitted to the live Rotom Support publisher. The installed `/usr/local/bin/rr` still requires separate synchronization with the corrected tracked helper.

## 2026-10-16 — Harden total-loss recovery for emergency execution

- **Files changed:** `00-Rotom-Change-Log.md`, `09-PVE-and-Rotom-Total-Loss-Recovery.md`; repository support file `support/tooling/test-rr-runbooks`.
- **Status:** **Documentation only / Verified.** No PVE, Rotom, VM, NAS, repository, snapshot, archive, network, credential, DNS, external service, or live publisher state changed.
- **Changes:** Added a fast-navigation map, explicit recovery-state model, printable control sheet, command/version provenance, evidence fields in phase and acceptance gates, and an actionable gap-closure register. Replaced the VM-only flow diagram with the required full end-to-end verification/safe-stop flow, added a second archive-path guard before `qmrestore`, and removed TLS verification bypass from the local-SNI acceptance probe. Structural tests now preserve the new emergency-control sections.
- **Evidence:** Complete semantic/tabletop review against the recovery requirements and current RR; local link, fence, label, secret-pattern, shell, whitespace, Mermaid grammar, and RR validation repeated after the changes.
- **Outstanding:** Operational readiness still requires Jared to close the explicitly blocked external-credential, installer, NAS-snapshot, application-database, off-site-protection, Available Sources, live publisher, and installed-helper deployment gaps. The guide now provides a proof requirement and blocking effect for each recovery-critical gap.

## 2026-10-16 — Add PVE and Rotom total-loss recovery orchestration

- **Files changed:** `00-Rotom-Change-Log.md`, `01-Rotom-Server-Inventory.md`, `02-Docker-Services.md`, `05-Backup-and-Restore.md`, `06-Maintenance-and-Automation.md`, `08-Rotom-Directory-Tree.txt`, `09-PVE-and-Rotom-Total-Loss-Recovery.md`; repository support files `README.md`, `support/tooling/rr`, `support/tooling/test-rr-cli`, `support/tooling/test-rr-runbooks`, and `support/website/guides/index.md`.
- **Status:** **Documentation only / Verified / Needs Verification.** No PVE, Rotom, VM, NAS, repository, snapshot, archive, network, credential, DNS, external service, or live publisher state changed.
- **Changes:** Added document `09` as the canonical blank-hardware total-loss recovery orchestrator and expanded the Core Numbered Reference Set to `00`–`09`. Added the emergency path, source hierarchy, offline kit, recovery-point consistency rules, 21 gated phases, four Mermaid diagrams, fallback and safe-stop matrices, evidence record, and final checklist. Routed total loss from document 01 while preserving document 05 as the owner of routine backup architecture and ordinary restores. Updated RR structural tooling for ten-file membership and document 09's required structure. Corrected the current Docker-network count from 18 to 19 after identifying the unattached `rotom-docs_default` network retained with the inactive rollback stack; this is not cleanup authorization.
- **Evidence:** Read-only Rotom inspection on 2026-10-16 confirmed Debian 13, VM address/MAC, five NFS contracts, 23 running containers, 19 networks, two volumes, 18 active Compose definitions, current identities, backup timers, Restic scope, and ConBee/Bluetooth/iGPU visibility. Jared's read-only PVE output confirmed PVE `9.2.0`, manager `9.2.21`, VMID `100` configuration, exact NFS storage, eight retained VZDump archives, the native `05:00` job, PVE Restic snapshot/staging evidence, IOMMU groups, and current restore/VMA command help. Procedure syntax was cross-checked against official Proxmox, Debian, and Restic documentation.
- **Outstanding:** Jared must manually add/replace document `09` and the other changed RR sources in Available Sources. The live Rotom Support publisher still permits only `00`–`08`; admitting and publishing `09` requires separate live-change authorization. External credential locations, exact NAS snapshot settings/procedure, and upgrade-sensitive application-native database recovery commands remain explicitly marked pre-disaster gaps.

## 2026-10-16 — Record Bluetooth setup and reinforce RR access preflight

- **Files changed:** `00-Rotom-Change-Log.md`, `06-Maintenance-and-Automation.md`; repository support file `AGENTS.md`.
- **Status:** **Implemented / Verified / Documentation only.**
- **Changes:** Recorded PVE USB passthrough and Rotom Bluetooth packages, service, and reboot evidence. Added a prominent reminder to the repository instructions to obtain the execution access required for RR Git operations before running them in a restricted sandbox.
- **Evidence:** Jared supplied the PVE configuration and applied `usb1` passthrough for Intel `8087:0aaa`. Rotom detected the adapter, loaded Intel firmware before reboot, and after the PVE reboot showed an active enabled service, powered controller, and device discovery. A sandboxed `rr check` failed to write Git metadata; the check subsequently passed with the required execution access.
- **Outstanding:** Specific-device pairing and data exchange and the post-reboot firmware log were not verified. Available Sources replacement remains manual by Jared.

## 2026-10-16 — Clarify sandbox access for RR Git checks

- **Files changed:** `00-Rotom-Change-Log.md`.
- **Status:** **Documentation only / Verified.**
- **Changes:** Clarified that Codex on Rotom should request the execution access needed for RR Git operations before running them when the sandbox restricts Git metadata or GitHub. Existing helper guardrails and stop-on-failure rules remain in force.
- **Evidence:** A sandboxed `rr check` could not write `.git/FETCH_HEAD`; the same check passed with the necessary execution access, and the preceding RR update was committed and pushed through `rr`.
- **Outstanding:** Available Sources replacement remains manual by Jared.

## 2026-10-16 — Restore Smart Home DNS and ConBee passthrough

- **Files changed:** `00-Rotom-Change-Log.md`, `02-Docker-Services.md`, `03-Network-and-Domains.md`.
- **Status:** **Implemented / Verified.**
- **Changes:** Configured Home Assistant and Homebridge Compose DNS to use `192.168.1.1` after their container resolver files lacked a nameserver. Jared reconnected the ConBee II and configured PVE VM 100 USB passthrough for `1cf1:0030`; Home Assistant's existing ZHA configuration uses `/dev/ttyACM0`. This supersedes the earlier historical disconnected-state evidence, not its unresolved stability investigation.
- **Evidence:** Following Jared's PVE reboot, Rotom detected the ConBee II and Home Assistant's container saw `/dev/ttyACM0`; both Smart Home services were running, retained the configured DNS, and returned HTTP `200`. Home Assistant resolved the Sensibo hostname; no matching recent ZHA or Sensibo setup errors were observed.
- **Outstanding:** Individual Zigbee device response and complete Sensibo integration operation were not independently verified. Monitor PVE stability with the adapter reconnected. Available Sources replacement remains manual by Jared.

## 2026-10-16 — Simplify Rotom Support Homepage status

- **Files changed:** `00-Rotom-Change-Log.md`.
- **Status:** **Implemented / Verified.**
- **Changes:** Removed the Rotom Support card's `siteMonitor` configuration from Homepage, retaining its `my-docker` / `mkdocs-rr` Docker-status binding as the sole indicator. This corrects the 2026-10-15 migration entry's historical statement that the card also had a site monitor.
- **Evidence:** Homepage's service API now reports the Rotom Support card without `siteMonitor`; its Docker-status API reports `mkdocs-rr` as `running`. The removed URL-monitor request had reported `500` after approximately five seconds even though the Support proxy and loopback upstream each returned `200`.
- **Outstanding:** None.

## 2026-10-16 — Retire legacy documentation identity remnants

- **Files changed:** `00-Rotom-Change-Log.md`, `01-Rotom-Server-Inventory.md`, `06-Maintenance-and-Automation.md`, `08-Rotom-Directory-Tree.txt`, and `support/tooling/test-rr-runbooks`.
- **Status:** **Implemented / Verified.**
- **Changes:** Moved Rotom's independently managed RR checkout to `/home/jared/documentation/rotom-runbook`, updated its private `rr` discovery path, and removed the retired helper and publisher rollback artifacts that retained the former documentation identity. At Jared's explicit direction, replaced the former identity throughout current and historical RR records.
- **Evidence:** `rr status` was clean before the move; afterward `rr path` resolves the new checkout and reports the expected `origin/main`. Jared removed the three exact root-owned artifacts on Rotom; follow-up checks found no active service, timer, cron, or configuration dependency on the former identity.
- **Outstanding:** Git object history and local interactive transcripts are archival records outside the tracked RR and active Rotom configuration; they were not rewritten or erased.

## 2026-10-15 — Migrate private documentation portal to Rotom Support

- **Files changed:** `00-Rotom-Change-Log.md`, `01-Rotom-Server-Inventory.md`, `02-Docker-Services.md`, `03-Network-and-Domains.md`, `06-Maintenance-and-Automation.md`, `08-Rotom-Directory-Tree.txt`, `support/tooling/test-rr-runbooks`, and the explicit supplementary inputs under `support/website/`.
- **Status:** **Implemented / Verified / Published.**
- **Changes:** Created the private **Rotom Support** MkDocs Material portal with primary Home, Runbook, Architecture, and Guides sections. The Runbook remains the controlled rendering of the authoritative numbered `00`–`08` set at `/runbook/`; Architecture and Guides are explicitly selected supplementary inputs and do not change Available Sources. Prepared `/srv/rotom/{stacks,appdata}/platform/mkdocs-rr`, preserved the existing `rotom-docs` stack and data as inactive rollback material, then moved the loopback `127.0.0.1:8082` listener to the read-only `mkdocs-rr` container. The guarded publisher retains origin/branch/clean-tree/fast-forward validation, fixed source selection, isolated build, atomic output swap, and one previous generated source/site revision. NPM host `27` routes `support.rotom.casa` to the loopback endpoint with existing certificate `24` and trusted-LAN access list `1`; legacy host `22` now permanently redirects historical paths and query strings to `/runbook/` under the same access list. The Platform Homepage card is now Rotom Support with the requested description, URL, compatible icon, Docker status binding, and site monitor.
- **Evidence:** The replacement Compose configuration and publisher shell syntax passed; an inactive publisher validation completed an isolated MkDocs build with the explicit source allowlist and no link warnings. The preloaded target output contained Home, `/runbook/`, `/architecture/`, and `/guides/` before the controlled listener handoff. After a transient first-start connection reset, the guarded rollback restored `rotom-docs`; a retried handoff passed all four local routes and left `mkdocs-rr` running read-only on `127.0.0.1:8082`. HTTPS checks returned `200` for every new section through `support.rotom.casa`; the existing wildcard certificate covered the hostname. A representative historical deep link with a query string returned `301` to the matching `/runbook/` page. An ephemeral Docker-bridge request received `403`, while authorized local and LAN-path checks succeeded. Homepage reported healthy and its API returned the updated card. No system units failed and no unrelated container was recreated.
- **Recovery:** The previous `rotom-docs` stack, application data, stopped container, and generated `site.previous` content remain. A consistent pre-change NPM database backup and previous host-22 configuration are retained beside NPM state. Available Sources replacement remains manual by Jared.
- **Outstanding:** URL fragments are client-side and cannot be observed by the redirecting host; the equivalent anchors remain published in the routed Runbook pages. Retention or removal of inactive `rotom-docs` rollback material requires a future explicit decision.

## 2026-10-15 — Rename the Mac RR checkout directory

- **Files changed:** `00-Rotom-Change-Log.md` and `01-Rotom-Server-Inventory.md`.
- **Status:** **Implemented / Verified.** The Mac checkout path and its private RR discovery configuration were changed; repository contents, Git history, the GitHub remote, installed tooling, Available Sources, and Rotom live state were not changed by the directory move.
- **Changes:** Renamed the clean Mac checkout to `/Users/jared/Documents/ChatGPT/rotom-runbook` and updated `~/.config/rr/repository` to the canonical path. This supersedes the migration entry below only for the current Mac checkout-path fact; its dated cutover evidence remains historical.
- **Evidence:** A pre-move `rr check` passed with clean `main` matching `origin/main`. The destination was required to be absent before the move. From the new path, `rr path` returned `/Users/jared/Documents/ChatGPT/rotom-runbook`; `rr check` passed again with a clean tree, `main`, `origin/main`, and `git@github.com:jaredwines/rotom-runbook.git` for fetch and push.
- **Outstanding:** Available Sources replacement remains manual by Jared.

## 2026-10-15 — Complete the Rotom Runbook identity migration

- **Files changed:** `00-Rotom-Change-Log.md`, `01-Rotom-Server-Inventory.md`, `02-Docker-Services.md`, `03-Network-and-Domains.md`, `04-NAS-and-Storage.md`, `05-Backup-and-Restore.md`, `06-Maintenance-and-Automation.md`, `07-Users-and-Permissions.md`, `08-Rotom-Directory-Tree.txt`, `AGENTS.md`, `README.md`, `support/tooling/rr`, `support/tooling/test-rr-runbooks`, and `support/tooling/test-rr-cli`; removed `support/tooling/test-retired-helper-runbooks` in favor of its RR replacement and removed the transitional `support/tooling/retired-helper` wrapper after final environment verification.
- **Status:** **Implemented / Verified / Published.** Documentation, GitHub identity, Rotom CLI integration, local origin, publisher configuration, website identity, and access controls were migrated and verified.
- **Changes:** Established **Rotom Runbook**, **RR**, `rr`, and `rotom-runbook` as the canonical current identity while preserving protected change-log history. GitHub renamed the existing repository in place to `jaredwines/rotom-runbook`. The tracked and installed `rr` helper is the single canonical implementation. A minimal `retired-helper` wrapper preserved compatibility only during the phased cutover; it was removed from both installations and the repository after independent verification and dependency audits. The structural test was renamed, made portable across GNU/Linux and macOS, and paired with isolated CLI safeguard tests. The working Rotom and Mac checkouts intentionally retain their legacy directory names, with `~/.config/rr/repository` pointing to each verified path. The root-owned publisher now expects the renamed GitHub origin and generates the Rotom Runbook title.
- **Evidence:** Discovery began from clean `main` at `d385fe747ff53943bedb87d2f32d5031c08d06a2`; preparation checkpoint `d23ee5b23f637d73f1a1109bd9dd054beef384be` was pushed before the rename. GitHub reported the same repository ID `1390601496`, owner, visibility, administrator permission, default branch, revision, unprotected-branch state, empty rulesets, and empty issue/pull-request sets before and after the in-place rename. Installed `/usr/local/bin/rr` on Rotom and the Mac is byte-identical to the tracked implementation, and each environment passed `rr check` against `git@github.com:jaredwines/rotom-runbook.git`. On both GNU/Linux and macOS, the isolated RR suite passed path/status/check/lint/pull/commit/push behavior plus dirty-tree, wrong-origin, wrong-branch, behind-remote, and unknown-command cases; the numbered-runbook suite, shell syntax checks, offline lint, Compose validation, and Git whitespace checks passed. Mac ownership and modes were verified as `root:wheel` `0755` for `rr` and `root:wheel` `0700` for its recovery copy. Targeted shell, Git, cron, launchd, systemd, and stack audits found no active former-interface dependency; the only privileged Rotom match was the intentionally retained pre-migration publisher recovery script. Both live `retired-helper` wrappers were then removed, and `rr check` passed afterward in each environment. The established publisher fast-forwarded its clean deployment clone to `90d3272983b73b6c97dffb2b8345470132e20ea3`, built successfully, reproduced all nine numbered sources byte-for-byte, and recreated only `rotom-docs`; all other container IDs remained unchanged. Direct loopback and authorized HTTPS returned `200` with the **Rotom Runbook** title. A disposable Docker-bridge client outside the allowed loopback and LAN ranges reached the correct TLS virtual host and received `403 Forbidden`. The effective NPM host remains restricted to `127.0.0.1` and `192.168.1.0/24`, and `site.previous` retains the former published title for rollback.
- **Recovery checkpoints:** The repository baseline is `d385fe747ff53943bedb87d2f32d5031c08d06a2`, and `d23ee5b23f637d73f1a1109bd9dd054beef384be` is the verified pre-rename checkpoint. The prior helper is retained root-only on both Rotom and the Mac at `/usr/local/bin/retired-helper.pre-rr-20261015` with SHA-256 `bd20aaefc733ef25d8f4ba62b33940b7552a2da5d966eaef872a5768ea561fc7`. The publisher's pre-migration script and MkDocs configuration are retained beside their live files as `publish-source.pre-rr-20261015` and `mkdocs.yml.pre-rr-20261015`. The clean deployment clone baseline is `576a03650c66841ddd1d0177db8ef6220fad6bcd`; both direct loopback and authorized HTTPS returned `200` with the former title before cutover. The publisher's atomic `site.previous` and `source.previous` rollback model remains unchanged.
- **Outstanding:** Available Sources replacement remains manual by Jared.

## 2026-10-15 — Remove obsolete ticket labels and consolidate operational references

- **Files changed:** `00-Rotom-Change-Log.md`, `01-Rotom-Server-Inventory.md`, `02-Docker-Services.md`, `03-Network-and-Domains.md`, `04-NAS-and-Storage.md`, `05-Backup-and-Restore.md`, `06-Maintenance-and-Automation.md`, `07-Users-and-Permissions.md`, `08-Rotom-Directory-Tree.txt`, and `support/tooling/test-retired-helper-runbooks`.
- **Status:** **Documentation only / Implemented / Verified.** No service, container, image, network, mount, timer, account, permission, backup, repository, NAS data, certificate, credential, or other live configuration was changed.
- **Changes:** Removed obsolete ticket-label narrative from the operational reference documents while preserving the protected history in this file and literal recovery artifact paths. Consolidated superseded same-day and pre-migration layers into concise current-state, retirement, recovery, ownership, and Needs Verification sections. Preserved the six runbooks, task router, maintenance triggers, current service/storage/backup contracts, recovery evidence, and security boundaries. Corrected the documented alerting-state and retired rollback-path discrepancies found during read-only inspection, and added regression coverage for the concise topology and ticket-label boundary.
- **Evidence:** Began from clean `main` at `576a03650c66841ddd1d0177db8ef6220fad6bcd`. Read-only inspection confirmed the current five stack domains, eighteen Compose definitions, five read/write NFSv3 mounts, the current service identities, absence of retired stack/path definitions and retired ports, and the empty root-only `/var/lib/rotom-alerting` directory. The tracked repository-wide case-insensitive scan fell from 1,273 matches to protected change-log history plus nine literal audit/image paths outside this file. Structural runbook tests, offline lint, link/fragment checks, secret-pattern checks, and `git diff --check` passed in the prepared tree.
- **Outstanding:** Privileged Docker object/image/network enumeration and unreadable root-only rollback artifacts were not verified. Arcane exclusions, exact current NAS snapshot settings, and incident-specific recovery-point selection remain **Needs Verification**. `retired-helper check` was not authorized and remains pending; Available Sources replacement remains manual by Jared.

## 2026-10-15 — Retire unused repository contribution guide

- **Files changed:** `00-Rotom-Change-Log.md`, `01-Rotom-Server-Inventory.md`, `06-Maintenance-and-Automation.md`, `08-Rotom-Directory-Tree.txt`, `README.md`, `support/tooling/retired-helper`, and `support/tooling/test-retired-helper-runbooks`; removed `support/CONTRIBUTING.md`.
- **Status:** **Documentation only / Implemented / Verified.** The only live change was replacing Rotom's installed `retired-helper` helper with the reviewed tracked helper; no service, container, mount, backup, network, account, or application configuration changed.
- **Changes:** Removed the unused repository-facing contribution guide at Jared's direction. Current repository navigation, source-map, lint, and structural-test references now point directly to document 00 as the sole legacy documentation maintenance authority. Synchronized Rotom's `/usr/local/bin/retired-helper` with the changed tracked helper so its lint no longer requires the removed guide. The numbered legacy documentation membership and maintained runbook-structure test remain unchanged.
- **Evidence:** Jared confirmed the guide will not be used. Rotom's installed helper is `root:root` mode `0755`, passed syntax validation, and is byte-identical to `support/tooling/retired-helper` at SHA-256 `bd20aaefc733ef25d8f4ba62b33940b7552a2da5d966eaef872a5768ea561fc7`; repository-reference scan and validation passed before publication.
- **Outstanding:** The Mac installed helper remains at the earlier version until separately synchronized; do not treat it as equivalent to this repository revision.

## 2026-10-15 — Convert the legacy documentation to a runbook-first reference

- **Files changed:** `00-Rotom-Change-Log.md`, `01-Rotom-Server-Inventory.md`, `02-Docker-Services.md`, `03-Network-and-Domains.md`, `04-NAS-and-Storage.md`, `05-Backup-and-Restore.md`, `06-Maintenance-and-Automation.md`, `07-Users-and-Permissions.md`, `08-Rotom-Directory-Tree.txt`, `README.md`, `support/CONTRIBUTING.md`, and `support/tooling/test-retired-helper-runbooks`; removed `support/tooling/test-runbooks` and all five files under `runbooks/`.
- **Status:** **Documentation only / Verified / Published.** Rotom live configuration was not changed. The first post-push Rotom Docs publication was verified.
- **Changes:** Converted the complete nine-file legacy documentation to a task-oriented runbook-first reference while retaining `00`–`08` as the complete Available Sources and publication set. Installed the permanent Runbook-First Maintenance Standard; established canonical ownership boundaries (`02` applications, `03` transport, `04` storage, `05` backup, `06` automation, `07` identities, `01` routing, `00` governance/history, and `08` topology); integrated the Docker website, NAS recovery, and Rotom Restic pilots into their owners; added document-specific revalidation triggers; retired the parallel pilot layer; preserved its authoring rules in `support/CONTRIBUTING.md`; and replaced its test with numbered-legacy documentation structural validation.
- **Evidence:** Every original major section was inventoried in a temporary preservation matrix and reconciled in place; automated structure/link/fence/secret-pattern checks, legacy documentation lint, shell syntax checks, diff checks, complete semantic ownership review, and safe read-only live checks were performed. Current and historical material remain in the numbered set; historical extraction is intentionally deferred. Available Sources remains exactly `00`–`08`.
- **Publication evidence:** At `2026-10-15 16:22:00 PDT`, the established publisher fast-forwarded its clean deployment clone to conversion revision `ce5aa4b231a980518002fd0c75f1eac80aae8803`, completed the MkDocs build successfully, recreated and started only `rotom-docs`, and returned HTTP `200` from both `http://127.0.0.1:8082/` and `https://docs.rotom.casa/`. Container-ID comparison confirmed no unrelated container was recreated. The derived source contains only the nine numbered sources, plus the publisher-generated landing page and Markdown rendering of document `08`.
- **Outstanding:** None for the first publication. The required second refresh must publish the verification commit containing this evidence; its delivery result is reported in the task handoff rather than a third documentation commit.

## 2026-10-15 — Restore Jared Wines and privatize Homepage monitoring

- **Files changed:** `00-Rotom-Change-Log.md`, `01-Rotom-Server-Inventory.md`, `02-Docker-Services.md`, `03-Network-and-Domains.md`, `08-Rotom-Directory-Tree.txt`.
- **Status:** **Implemented / Verified.** Jared Wines was restored through its retained NPM host, and Glances was moved into Homepage's private Compose project. No NAS data, Docker volume, certificate, secret, or unrelated workload was changed.
- **Changes:** `jaredwines.com` now publishes only `127.0.0.1:7777:80`; NPM proxy host `8` forwards to `127.0.0.1:7777` with forced TLS. Its stale generated NPM configuration was regenerated from that verified database record. Homepage resolves `jaredwines.com` internally to Rotom's LAN address so its HTTPS site monitor reaches NPM without changing public DNS. Glances is now the `glances` service in `/srv/rotom/stacks/platform/homepage/compose.yaml`, on the existing private `homepage_default` bridge with no published host port. Homepage's eight Glances widgets use `http://glances:61208`; Glances configuration moved to `/srv/rotom/appdata/platform/homepage/glances/glances.conf`. The obsolete standalone Glances stack and appdata directories were removed after verification.
- **Evidence:** `jaredwines.com` listened only on `127.0.0.1:7777`; its direct loopback, local-SNI TLS, and public HTTPS probes returned `200` and the expected Jared Wines portfolio title. NPM's regenerated host-8 configuration named `127.0.0.1:7777`. Homepage was healthy; its own Jared Wines monitor returned `200` (about 16 ms). Homepage and Glances shared `homepage_default`; Glances had no host TCP `61208` listener, and Homepage successfully reached Glances `status`, `cpu`, `mem`, `containers`, `diskio`, `fs`, `network`, and `sensors` API endpoints. Docker reported 23 running containers and 18 networks.
- **Outstanding:** Available Sources replacement remains manual by Jared.

## 2026-10-15 — Verify Libraries automount recovery through a full reboot

- **Files changed:** `00-Rotom-Change-Log.md`, `04-NAS-and-Storage.md`, `06-Maintenance-and-Automation.md`, `runbooks/NAS-Mount-Recovery.md`.
- **Status:** **Verified.** Documentation records the final reboot acceptance of the previously implemented Libraries automount recovery; no further live configuration changed during this verification.
- **Changes:** Replaced the provisional reboot-validation requirement with the observed boot behavior. At boot, Docker initially triggered the Libraries mount before the NAS was reachable, producing brief `Network is unreachable` failures and `mount-start-limit-hit`. The enabled recovery service made its configured retry about 30 seconds later, reset and armed the generated automount, mounted the documented Libraries export, and recovered the covered services.
- **Evidence:** The VM booted at `2026-10-15 11:39:51 PDT`. `mnt-nas\\x2dlibraries.automount` became active at `11:40:00`; after the retry, `mnt-nas\\x2dlibraries.mount` became active at `11:40:33`; and `rotom-nas-docker-recovery.service` completed successfully at `11:40:48`. Final checks confirmed the exact read/write Libraries NFSv3 source, all 23 containers running, healthy Paperless/RomM/Arcane/Homepage/Palworld checks where defined, qBittorrentVPN `wg0` at `10.2.0.2/32`, expected service HTTP responses, zero covered-container restarts, and zero failed systemd units.
- **Outstanding:** The root-only pre-change helper remains an available rollback artifact at `/root/rotom-nas-docker-recovery.pre-automount-20261015-113500`; retain or remove it only under a separately authorized rollback-retention decision. Available Sources replacement remains manual by Jared.

## 2026-10-15 — Restore Libraries automount and harden NAS recovery

- **Files changed:** `00-Rotom-Change-Log.md`, `04-NAS-and-Storage.md`, `06-Maintenance-and-Automation.md`, `runbooks/NAS-Mount-Recovery.md`.
- **Status:** **Implemented / Verified.** The repair changed only the Libraries NFS mount lifecycle, its seven dependent container runtime states, and the root-owned recovery helper. No Compose definition, NAS export, NAS ownership/ACL, application data, backup, repository, network, or credential was changed.
- **Changes:** During a short controlled maintenance window, stopped only `qbittorrentvpn`, `radarr`, `sonarr`, `jellyfin`, `romm`, `paperless`, and `nginx-proxy-manager`; cleanly stopped the active direct Libraries NFS mount; reset the generated mount/automount failure state; re-armed `mnt-nas\\x2dlibraries.automount`; triggered the configured mount through the required `library/` and `paperless/` paths; and restarted the seven containers. Hardened `/usr/local/sbin/rotom-nas-docker-recovery` so, when its target NFS mount is inactive, it resets both generated units, arms the automount before starting the mount, verifies the exact NFS filesystem, and fails closed if the automount is not active. The helper's existing eligible-container-only recovery behavior is unchanged. A root-only mode-`0750` pre-change helper is retained at `/root/rotom-nas-docker-recovery.pre-automount-20261015-113500` for rollback.
- **Evidence:** Before repair, the Libraries mount was active from the documented `Libraries/.data` NFSv3 export while its automount was inactive with historical `mount-start-limit-hit`; journal evidence showed repeated Docker-triggered boot attempts before NAS reachability. The seven listed containers were the exact current consumers of Libraries binds and stopped cleanly with exit `0`. The re-armed mount and automount both reported `active`; `findmnt` confirmed the exact documented source read/write; the helper syntax check and installed-versus-reviewed comparison passed; a live helper restart completed successfully and left every covered container running. Final verification found qBittorrentVPN `wg0` at `10.2.0.2/32`, expected local responses from qBittorrent, Radarr, Sonarr, Jellyfin, RomM, Paperless, and NPM/Aloha, Paperless health `healthy`, zero container restarts, and zero failed systemd units.
- **Outstanding:** Superseded by the successful same-day full-reboot verification recorded above. Retain the root-only rollback copy until an explicit retention decision. Available Sources replacement remains manual by Jared.

## 2026-10-15 — Prepare the runbook template and three operational pilots

- **Files changed:** `00-Rotom-Change-Log.md`, `01-Rotom-Server-Inventory.md`, `04-NAS-and-Storage.md`, `README.md`, `support/CONTRIBUTING.md`, `runbooks/README.md`, `runbooks/RUNBOOK-TEMPLATE.md`, `runbooks/Docker-Website-Recovery.md`, `runbooks/NAS-Mount-Recovery.md`, `runbooks/Rotom-Restic-Backup.md`.
- **Status:** **Documentation only / Verified / Needs Verification.** No Docker object, Compose definition, service, timer, mount, backup, Restic repository, NAS data, proxy route, network, account, permission, application data, or other live configuration was changed. The runbook files are prepared repository sources and do not become current legacy documentation members until Jared manually adds them to Available Sources.
- **Changes:** Established the final task-oriented runbook template, safety labels, stop-condition model, evidence standard, and task index. Added three pilot runbooks for Docker-backed website diagnosis/recovery, current Rotom NAS-mount recovery, and Rotom Restic Backup execution/verification. Preserved documents `00`–`08` as the canonical current-state reference set and linked each pilot to its fact owners. Added explicit guards for Jared Wines' unresolved deployment intent, shared NPM blast radius, exact-source NFS recovery, eligible-container-only NAS recovery, concurrent Restic work, protected credentials, repository locks, retention/prune behavior, and the distinction between snapshot creation and restore assurance.
- **Evidence:** Began from a clean `main` checkout matching the cached upstream. Read-only live inspection confirmed 23 running containers and 19 Compose projects; Aloha's `7778:80` listener, read-only content bind, and direct/local-SNI/public `200` responses; Jared Wines running without a published port; host-networked NPM; the five current NFS automount contracts and exact sources; active NFSv3 Libraries and Rotom Restic Backup mounts; the enabled/active `rotom-nas-docker-recovery.service` and its exact Libraries directory/container gates; and the enabled/active `rotom-restic-backup.timer`, successful latest service result, current launcher/worker, repository mount, schedule, installed retention/prune commands, and latest three `rotom` automatic snapshots. Command validation corrected the generated systemd unit spelling to `mnt-nas\x2dlibraries.*`. It also found that the Libraries NFS filesystem is active and all consumers are running, but its automount unit remains inactive with historical boot result `mount-start-limit-hit`; the other four automounts are active. The recovery-changing branches were reviewed against live definitions but were not deliberately exercised by causing an outage, resetting that unit, or starting an extra backup.
- **Outstanding:** Jared must manually add the five `runbooks/` files to Available Sources before they become current legacy documentation. Rotom Docs still builds the controlled nine-file source and requires a separately authorized publisher/allowlist update before it can publish the new layer. After membership and publishing are coordinated, update document 01's current source map and replace the staged-runbook labels. The active-but-degraded Libraries automount posture needs a separately authorized targeted reset/start and verification; do not unmount the working NFS filesystem merely to clear it. A future controlled exercise should validate the state-changing recovery branches without manufacturing risk to production data.

## 2026-10-15 — Synchronize the installed legacy documentation validation helpers

- **Files changed:** `00-Rotom-Change-Log.md`, `01-Rotom-Server-Inventory.md`, `06-Maintenance-and-Automation.md`, `08-Rotom-Directory-Tree.txt`.
- **Status:** **Implemented / Verified.** Only the Rotom and Mac `/usr/local/bin/retired-helper` helpers and their documentation were changed; no service, container, mount, backup, NAS, network, permission, storage, or application data was changed.
- **Changes:** Installed the tracked `support/tooling/retired-helper` over the older Rotom and Mac `/usr/local/bin/retired-helper` copies with their established root ownership and executable mode. Both installed commands now support offline `retired-helper lint`, and `retired-helper check` runs that lint before its GitHub comparison. No persistent rollback copy was added; the prior helper remains recoverable from repository history.
- **Evidence:** Rotom preflight syntax validation passed and showed that the installed-versus-versioned diff contained only the reviewed lint implementation, `check` integration, and matching help/dispatch updates. After installation, the Rotom copies were 20,999 bytes with SHA-256 `7d987132d76c6fdac970122bd61407fd72185c081b2ba46ca31c6f92c56262dc`; `cmp` returned identical, the installed script passed `bash -n`, `retired-helper lint` passed, and the full `retired-helper check` passed with a clean checkout matching `origin/main`. Jared then fast-forwarded the Mac checkout to `d51aa0e`, installed the tracked helper as `root:wheel` mode `0755`, observed no `cmp` difference, and returned passing `retired-helper lint` plus a full clean-checkout `retired-helper check` matching `origin/main`.
- **Outstanding:** Available Sources replacement remains manual by Jared.

## 2026-10-15 — Record post-cleanup Docker and Arcane automation audit

- **Files changed:** `00-Rotom-Change-Log.md`, `01-Rotom-Server-Inventory.md`, `02-Docker-Services.md`, `03-Network-and-Domains.md`, `06-Maintenance-and-Automation.md`.
- **Status:** **Documentation only / Verified / Needs Verification.** The audit and this legacy documentation update made no Docker, Compose, service, image, volume, network, NAS, mount, application-data, or live configuration change.
- **Changes:** Recorded the complete read-only Docker audit after container cleanup/recreation. Corrected the current runtime to 23 running containers, 19 networks, two unattached named volumes, 23 images, and containerd `2.4.1`. Documented that the intended 22-workload set is healthy and matches all current Compose hashes, but `jaredwines.com` was also running despite its documented undeployed intent. Corrected Arcane's live automatic-update and auto-heal settings to enabled, scheduled pruning to disabled, and `followProjectSymlinks` to enabled. Recorded Arcane's non-dry-run 10:40 PDT update of Jared Wines, the resulting unreferenced prior Nginx image, the absent retired Syncthing image, and uncertain Arcane Rustic/backup-helper resources. Superseded current-facing statements that Paperless still joins retired `rotom-proxy`; older dated network records remain historical.
- **Evidence:** Docker Engine/client `29.9.0`, Compose `v5.6.0`, and containerd `2.4.1` were active. All 19 Compose definitions rendered; all 23 objects were running with `unless-stopped`, zero restarts, expected Compose labels/paths/hashes, and healthy configured healthchecks. Documented direct and local-SNI probes returned their expected `200`/`302` responses, while Jared Wines remained `502` because its Compose definition publishes no host port. Docker events and Arcane activity records align on a successful non-dry-run automatic update at 10:40 PDT that replaced `nginx:alpine` and recreated Jared Wines. Arcane's classified boolean settings showed auto-update and auto-heal enabled; its system/volume backup policy and run tables were empty. No secret or complete configuration value was read or recorded.
- **Outstanding:** Jared Wines' desired deployment state and its original inclusion in the recreation remain **Needs Verification**. Do not remove its container/network, the prior unreferenced Nginx image, `ghcr.io/rustic-rs/rustic:v0.11.2`, `arcane-rustic-cache`, or `arcane-backups` without the additional read-only ownership/dependency checks recorded in documents 02 and 06 and separate cleanup authorization. Three documented NAS automounts were armed but idle and were not activated by this audit. Available Sources replacement remains manual by Jared.

## 2026-10-15 — Retire Rotom shared Docker networks

- **Files changed:** `00-Rotom-Change-Log.md`, `01-Rotom-Server-Inventory.md`, `02-Docker-Services.md`, `03-Network-and-Domains.md`, `06-Maintenance-and-Automation.md`, `08-Rotom-Directory-Tree.txt`.
- **Status:** **Implemented / Verified.**
- **Changes:** At Jared's direction, removed the active Compose references to the external `rotom-proxy`, `rotom-arr`, and `rotom-monitoring` bridges, recreated the affected workloads, and removed each now-unused Docker network. NPM remains host-networked and continues to use documented host/loopback upstreams. Prowlarr, Radarr, Sonarr, and qBittorrentVPN retain their existing `192.168.1.69` control targets. Glances now publishes only `127.0.0.1:61208`; Homepage reaches it through its existing `host.docker.internal` gateway mapping. Root-only pre-change Compose/configuration archives were retained at `/root/rotom-{proxy,arr,monitoring}-*-20261015-*.tar.gz` for rollback.
- **Evidence:** All 19 active Compose definitions rendered successfully. Docker reported all 22 expected container objects running; Homepage, Arcane, Paperless, RomM database, and both Palworld containers were healthy. Local checks returned the expected responses for Aloha, qBittorrent, Radarr, Sonarr, Prowlarr, RomM, Rotom Docs, Jellyfin, Paperless, Homepage, and Glances. qBittorrentVPN retained `wg0`. Homepage successfully fetched Glances through `http://host.docker.internal:61208/api/4/status`; no active Compose definition or running network referenced the three retired names.
- **Outstanding:** `/srv/rotom/stacks/RUNTIME-POLICY.md`, referenced by older documentation, was absent during this work; no replacement was created. Retention of the three root-only rollback archives requires a separate decision. Available Sources replacement remains manual by Jared.

## 2026-10-15 — Improve legacy documentation navigation and maintenance guidance

- **Files changed:** `00-Rotom-Change-Log.md`, `01-Rotom-Server-Inventory.md`, `02-Docker-Services.md`, `03-Network-and-Domains.md`, `04-NAS-and-Storage.md`, `05-Backup-and-Restore.md`, `06-Maintenance-and-Automation.md`, `07-Users-and-Permissions.md`, `08-Rotom-Directory-Tree.txt`, `README.md`, `support/CONTRIBUTING.md`, `support/tooling/retired-helper`.
- **Status:** **Documentation only / Verified.** No live Rotom, PVE, Docker, NAS, network, account, permission, backup, service, storage, or data state was changed.
- **Changes:** Added concise safe-use and navigation guidance to every core legacy documentation member, made the current-versus-historical reading path explicit, clarified mixed current/history Docker sections, stale automation chronology, and current Libraries diagnostic context, normalized out-of-order subsection suffixes, documented the gated procedure for a later history split, and added an offline `retired-helper lint` command for whitespace, document-title/fence, local-link, core-filename-reference, and private-key-marker checks across the full numbered set. Preserved all filenames, historical evidence, recovery material, and Available Sources membership; technical corrections are limited to explicitly superseding stale current-state wording with already documented newer evidence.
- **Evidence:** Complete repository inventory and diff review; clean initial `retired-helper status`; passing `bash -n support/tooling/retired-helper` and versioned `support/tooling/retired-helper lint`; internal-link, Markdown-fence, changed-line sensitive-value, critical-topic, and changed-file-scope checks. The final versioned `support/tooling/retired-helper check` passed repository identity, core-file, lint, GitHub fetch, and upstream-equality checks and reported only the expected uncommitted documentation changes. Read-only live follow-up found both Palworld containers healthy with `unless-stopped`, started at 2026-10-14 12:24 PDT while Docker remained continuously active since 2026-10-13; the journal records their starts thirty seconds after an operator-run Docker system prune but no explicit start command, so causation and intent remain unverified. Both documented rollback files remain present and differ from their active counterparts.
- **Outstanding:** Historical extraction is gated on Jared's manual addition of all destination files to Available Sources in one coordinated release; no split was performed. Palworld start cause/desired persistence and rollback-file retention remain Needs Verification. The enhanced versioned helper differs from `/usr/local/bin/retired-helper`; installation on Rotom and Mac requires a separately authorized live/tooling synchronization. Available Sources replacement remains manual by Jared.

## 2026-10-15 — Reconcile legacy documentation consistency audit findings

- **Files changed:** `00-Rotom-Change-Log.md`, `01-Rotom-Server-Inventory.md`, `02-Docker-Services.md`, `04-NAS-and-Storage.md`, `05-Backup-and-Restore.md`, `06-Maintenance-and-Automation.md`, `07-Users-and-Permissions.md`, `08-Rotom-Directory-Tree.txt`.
- **Status:** **Documentation only / Verified / Needs Verification.** No live service, container, mount, timer, backup, NAS, network, account, permission, or configuration state was changed.
- **Changes:** Reconciled the 2026-10-15 read-only legacy documentation audit with current guest evidence. Corrected unsafe reconstruction pointers for storage and Docker-group privileges; current Docker, Compose, Arcane, Restic, legacy documentation-checkout, service-home, Remote Desktop Commander, and filesystem-tree statements; and malformed historical tree text. Documented two otherwise unrecorded local rollback artifacts without changing them. Preserved superseded facts as dated history rather than rewriting historical entries.
- **Evidence:** `retired-helper path` resolved Jared's checkout. Read-only guest checks found five current NFSv3 automount contracts; 22 running Docker containers including both healthy Palworld servers; one Docker named volume and seventeen networks; nineteen Compose files split 2 Game Servers / 2 Hosted Websites / 7 Libraries / 6 Platform / 2 Smart Home; Docker Engine `29.9.0` and Compose `v5.6.0`; Arcane auto-update, auto-heal, and scheduled pruning disabled; latest guest automatic Restic snapshot `553e7a39` from 2026-10-14 20:30 PDT; the five service-home directories and `/home/desktopcmd` absent; and Docker GID `989` with Fran as its sole listed member.
- **Outstanding:** The reason and intended persistence of the now-running Palworld containers were not established; document their observed running state without inferring deployment intent. PVE, UNAS, UniFi, Mac, public-DNS/TLS, authenticated application, and full restore state were outside this guest-level audit. The two documented rollback artifacts require a separate retention decision. Available Sources synchronization remains manual by Jared.

## 2026-10-14 — Retire unused service-home trees and `/opt/containerd`

- **Files changed:** `00-Rotom-Change-Log.md`, `01-Rotom-Server-Inventory.md`, `07-Users-and-Permissions.md`, `08-Rotom-Directory-Tree.txt`.
- **Status:** **Implemented / Verified.**
- **Changes:** At Jared's explicit authorization, removed the verified-unused `/home/game-servers`, `/home/hosted-websites`, `/home/libraries`, `/home/platform`, and `/home/smart-home` trees. The five locked service accounts and their configured NSS home fields remain; active service Compose, state, and protected-input roots remain under `/srv/rotom`. Also removed the unused 12 KiB `/opt/containerd` directory; the active runtime continues to use `/usr/bin/containerd`, `/run/containerd/containerd.sock`, and `/var/lib/docker`.
- **Evidence:** Immediately before deletion, all five paths were directories on the root ext4 filesystem and checks found no nested mounts, open users, or Docker bind mounts. Afterward, every listed path was absent and the accounts remained present. The system reported `running`; listed containers remained up; `desktop-commander.service` remained active; `containerd.service` remained active; and Docker reported `DockerRootDir=/var/lib/docker`.
- **Outstanding:** The NSS home fields intentionally still name the removed paths; no account-home migration was performed. Available Sources synchronization remains manual by Jared.

## 2026-10-14 — Rename current Restic credential files

- **Files changed:** `00-Rotom-Change-Log.md`, `01-Rotom-Server-Inventory.md`, `05-Backup-and-Restore.md`, `07-Users-and-Permissions.md`, `08-Rotom-Directory-Tree.txt`.
- **Status:** **Implemented / Verified.**
- **Changes:** Renamed the root-only current Restic credential file on both hosts to `/etc/restic/restic-repository-password` and updated the Rotom and PVE root backup workers to use it. The repositories, schedules, retention, mounts, backup scope, and credential contents were unchanged.
- **Evidence:** Jared supplied both host-side preflights showing idle services and root-only `0600` source files; each worker path change passed shell syntax validation. A manual Rotom backup created snapshot `333c87b3` at 20:25 PDT, and a manual PVE backup created snapshot `b5af666b` at 20:27 PDT. Both services returned `Result=success` / `ExecMainStatus=0`, and both timers were re-enabled and active. The PVE repository password rotation was separately verified earlier in this chat; no password content was recorded.
- **Outstanding:** Historical references retain their original paths as evidence. Available Sources synchronization remains manual by Jared.

## 2026-10-14 — Retire Remote Desktop Commander old-home rollback contents

- **Files changed:** `00-Rotom-Change-Log.md`, `01-Rotom-Server-Inventory.md`, `05-Backup-and-Restore.md`, `06-Maintenance-and-Automation.md`, `07-Users-and-Permissions.md`, `08-Rotom-Directory-Tree.txt`.
- **Status:** **Implemented / Verified.**
- **Changes:** At Jared's explicit authorization after successful migration verification, removed the 35,248-entry / 1.6 GiB rollback contents from `/home/desktopcmd`. The empty legacy directory remains `desktopcmd:desktopcmd` mode `0750` under the inherited named Jared read/traverse ACL; it is not the account home or an active service dependency. The separate root-owned pre-migration service-unit copy remains configuration history only and is not a complete rollback path without the removed application tree.
- **Evidence:** Before deletion, `desktopcmd` was already configured for `/opt/desktop-commander`, the active service executed and worked there, no old-home handles were open, and the active unit contained no old path. Final checks found the old home empty, `desktop-commander.service` enabled and active, and zero failed units.
- **Outstanding:** Restoring the former `/home/desktopcmd` application state now requires a suitable Rotom Restic Backup recovery point; no local fast rollback copy remains. Available Sources synchronization remains manual by Jared.

## 2026-10-14 — Migrate Remote Desktop Commander to `/opt`

- **Files changed:** `00-Rotom-Change-Log.md`, `01-Rotom-Server-Inventory.md`, `05-Backup-and-Restore.md`, `06-Maintenance-and-Automation.md`, `07-Users-and-Permissions.md`, `08-Rotom-Directory-Tree.txt`.
- **Status:** **Implemented / Verified.**
- **Changes:** Migrated the existing native Remote Desktop Commander installation and `desktopcmd` configured home from `/home/desktopcmd` to `/opt/desktop-commander`, retaining UID:GID `1001:1001`, the locked account, Zsh/Oh My Zsh, the installed agent version `0.2.52`, workspace, device-registration state, privacy ACLs, and all service hardening. The original `/home/desktopcmd` tree and a root-owned pre-migration unit copy remain as rollback material; neither was deleted.
- **Evidence:** A live initial plus stopped-service final `rsync -aHAX --numeric-ids` converged with no differences before cutover. `desktop-commander.service` is enabled and active from the new location with `UMask=0077`, `NoNewPrivileges=true`, and `PrivateTmp=true`; it reconnected using the existing registration. A harmless command through that connection ran as `desktopcmd` and created then removed a workspace test file. The account remains password-locked with no supplementary groups or authorized SSH keys; the listener set and failed-unit list are unchanged. The enabled Rotom Restic Backup configuration includes both `/home` and `/opt`; its scheduled run preceding the migration succeeded, but no additional backup run was triggered.
- **Outstanding:** Retain `/home/desktopcmd` and the unit rollback copy until Jared explicitly authorizes their retirement. Available Sources synchronization remains manual by Jared.

## 2026-10-14 — Reconcile current-state audit findings

- **Files changed:** `00-Rotom-Change-Log.md`, `01-Rotom-Server-Inventory.md`, `02-Docker-Services.md`, `04-NAS-and-Storage.md`, `05-Backup-and-Restore.md`, `06-Maintenance-and-Automation.md`, `08-Rotom-Directory-Tree.txt`.
- **Status:** **Documentation only.** No Rotom, PVE, Docker, NAS, router, backup, account, or credential state was changed.
- **Changes:** Reconciled stale current-looking recovery, NFS-loss, Fran-login, alerting, Palworld-rehearsal, Arcane-automation, NAS-path, and recovery-point wording with the newest 2026-10-14 supported evidence. Preserved historical evidence and explicit limitations: exact Libraries snapshot-policy values, selected restore/archive identifiers, router-policy detail, off-site recovery coverage, PVE reset attribution, and PVE mail-delivery intent remain documented as unresolved rather than inferred.
- **Evidence:** Complete read-only cross-document audit of the nine-file Available Sources set, using existing 2026-10-14 evidence and Jared-confirmed outcomes already recorded in this log.
- **Outstanding:** Record exact recovery-test identifiers and NAS snapshot-policy values when supplied; establish and document any off-site recovery layer, PVE mail-delivery disposition, router-policy summary, and post-reset evidence as separately authorized work. Available Sources synchronization remains manual by Jared.

## 2026-10-14 — Clarify active weekly update scheduling

- **Documentation only / Verified:** `01-Rotom-Server-Inventory.md` and `06-Maintenance-and-Automation.md` now distinguish the enabled `rotom-weekly-maintenance.timer` from the retired historical reboot-capable cron schedule. Live systemd evidence showed the Rotom timer enabled and active for Sundays at `01:15`, with persistent missed-run behavior; it performs the supported ordinary package-upgrade workflow without automatic reboot. The absent `/etc/cron.d/weekly-linux-update` schedule is intentional and is not required for weekly update coverage.

## 2026-10-14 — Accept current trusted-LAN exposure policy

- **Files changed:** `00-Rotom-Change-Log.md`, `01-Rotom-Server-Inventory.md`, `03-Network-and-Domains.md`.
- **Status:** **Documentation only / Owner decision.** No firewall, listener, proxy, router, VLAN, or port-forwarding configuration was changed.
- **Changes:** Jared accepted the current trusted-LAN design: PVE's firewall remains disabled, and the documented direct Rotom LAN listeners remain intentional. No hardening or firewall-project work is planned from this decision; preserve the current operating model unless Jared separately requests a change.
- **Evidence:** Jared's explicit owner decision in this chat.
- **Outstanding:** None for the exposure-policy decision. Available Sources synchronization remains manual by Jared.

## 2026-10-14 — Record PVE stability-monitoring interval

- **Files changed:** `00-Rotom-Change-Log.md`, `01-Rotom-Server-Inventory.md`, `06-Maintenance-and-Automation.md`.
- **Status:** **Documentation only / Verified.** No PVE configuration change was made.
- **Changes:** Recorded a Jared-executed filtered review of the preceding PVE boot. It found no recurrent `e1000e` hardware-unit hang, `NETDEV WATCHDOG`, panic, MCE, OOM, or i915 failure across the October 1–8 interval. The recurring iGPU passthrough invalid option-ROM warning remains non-fatal. The historical NIC hang still explains the prior network/NFS outage, but evidence still does not prove it caused the whole-host reset.
- **Evidence:** Jared-supplied `journalctl -b -1` output. NIC link-up was normal; the iGPU VFIO resets completed; PVE Restic Backup completed daily during the observed interval.
- **Outstanding:** Continue normal monitoring after reboots and investigate only if the hang or reset recurs. The direct-LAN/PVE-firewall policy decision remains open. Available Sources synchronization remains manual by Jared.

## 2026-10-14 — Capture current PVE VM-backup storage configuration

- **Files changed:** `00-Rotom-Change-Log.md`, `04-NAS-and-Storage.md`.
- **Status:** **Documentation only / Verified.** No PVE configuration change was made.
- **Changes:** Closed the exact PVE storage-stanza gap for Rotom VM Backup. The active `nas-rotom-vm-backup` storage is an NFS definition for `192.168.1.70:/volume/4d6b927b-3d90-4af3-9bd7-be668266998a/.srv/.unifi-drive/Rotom_VM_Backup/.data`, mounted at `/mnt/pve/nas-rotom-vm-backup`, with `content backup` only.
- **Evidence:** Jared-executed read-only `/etc/pve/storage.cfg` output supplied in this chat.
- **Outstanding:** The PVE boot excerpt shows normal NIC link-up and recurring iGPU passthrough option-ROM warnings, but does not establish a cause for the historical whole-host reset. The direct-LAN/PVE-firewall policy decision remains open. Available Sources synchronization remains manual by Jared.

## 2026-10-14 — Verify Rotom account locks and active Library routes

- **Files changed:** `00-Rotom-Change-Log.md`, `03-Network-and-Domains.md`, `07-Users-and-Permissions.md`.
- **Status:** **Documentation only / Verified.** No live configuration, privilege, proxy, or application change was made.
- **Changes:** Closed the remaining Rotom-side service-account lock-state and post-Libraries route-detail gaps.
- **Evidence:** Privileged read-only `passwd -S` showed `L` (locked) for `platform`, `libraries`, `hosted-websites`, `game-servers`, `smart-home`, and `desktopcmd`. Local NPM/SNI probes returned `200` for qBittorrent and RomM and expected login `302` responses for Paperless and Prowlarr. Docker confirmed loopback-only publishing for qBittorrent, RomM, and Paperless; Prowlarr remains LAN-published on `9696` and its NPM route returned the expected redirect.
- **Outstanding:** PVE-only storage/stability checks and the owner decision on the direct-LAN/PVE-firewall exposure policy remain. Available Sources synchronization remains manual by Jared.

## 2026-10-14 — Record additional Jared-confirmed operational verification

- **Files changed:** `00-Rotom-Change-Log.md`, `01-Rotom-Server-Inventory.md`, `02-Docker-Services.md`, `03-Network-and-Domains.md`, `05-Backup-and-Restore.md`, `06-Maintenance-and-Automation.md`, `07-Users-and-Permissions.md`.
- **Status:** **Documentation only / Verified by Jared confirmation.** No new live test, cleanup, or configuration change was performed in this chat.
- **Changes:** Jared confirmed completion of the UniFi/router-policy review, full isolated Palworld disaster-recovery rehearsal, authenticated Paperless acceptance, Fran PVE browser login, legacy NPM-record review, certificate-renewal observation, and dormant Docker-artifact review. These are no longer current operational gaps. The results of the legacy-NPM and artifact-retention decisions were not supplied, so this update does not infer record or artifact deletion.
- **Evidence:** Jared's explicit confirmation in this chat; detailed command output, browser evidence, test artifacts, and decisions were not supplied.
- **Outstanding:** Direct-LAN/PVE-firewall policy confirmation, exact PVE storage stanza capture, service-account lock-state inspection, and PVE stability/hardware follow-up remain documented separately. Available Sources synchronization remains manual by Jared.

## 2026-10-14 — Record Jared-confirmed recovery verification

- **Files changed:** `00-Rotom-Change-Log.md`, `01-Rotom-Server-Inventory.md`, `03-Network-and-Domains.md`, `04-NAS-and-Storage.md`, `05-Backup-and-Restore.md`, `06-Maintenance-and-Automation.md`, `07-Users-and-Permissions.md`, `08-Rotom-Directory-Tree.txt`.
- **Status:** **Documentation only / Verified by Jared confirmation.** No new live test or configuration change was performed in this chat.
- **Changes:** Jared confirmed that the current Rotom Restic full-data-read and restore rehearsal, current Rotom VM Backup VMA verification or disposable restore, Libraries/Paperless NAS snapshot retention and isolated restore, post-NAS-restart metadata observation, planned live Libraries-NFS-loss test, end-to-end Wake-on-LAN test, and VPN credential rotation were all completed and verified. The listed checks are no longer current verification gaps.
- **Evidence:** Jared's explicit confirmation in this chat. Detailed command transcripts, selected recovery-point identifiers, and test artifacts were not supplied here; this entry deliberately does not invent them.
- **Outstanding:** The separate owner decision on direct LAN exposure/PVE firewall, PVE-only configuration details, direct PVE browser-login acceptance for Fran, certificate-renewal observation, and PVE hardware/maintenance follow-up remain as documented. Available Sources synchronization remains manual by Jared.

## 2026-10-14 — Verify Rotom operational follow-up gaps

- **Files changed:** `00-Rotom-Change-Log.md`, `02-Docker-Services.md`, `06-Maintenance-and-Automation.md`, `07-Users-and-Permissions.md`.
- **Status:** **Documentation only / Verified.** No live configuration, backup behavior, persistent data, network exposure, or account privilege was changed.
- **Changes:** Closed the Rotom-side verification gaps for Fran's effective Docker access, Remote Desktop Commander health after the `desktopcmd` shell change, and the current NAS recovery helper target list. The remaining running-workload Libraries-NFS-loss test is intentionally still unperformed.
- **Evidence:** Read-only 2026-10-14 inspection found Fran's direct `docker ps` succeeded and listed all 20 running containers; `desktop-commander.service` was enabled and active/running; and `/usr/local/sbin/rotom-nas-docker-recovery` was inspected without recording secret material. It validates the Libraries NFS mount plus `library/` and `paperless/`, then conditionally recovers only qBittorrentVPN, Radarr, Sonarr, Jellyfin, RomM, Paperless, and Nginx Proxy Manager after a matching NAS/mount startup failure. The guest continued to report zero failed units, five mounted read/write NFSv3 filesystems, and zero Docker restart counts.
- **Outstanding:** Direct PVE browser-login acceptance, Fran SSH-key setup (intentionally deferred), full backup restore/data-read verification, PVE-only configuration checks, NAS snapshot/recovery verification, owner decisions on direct LAN exposure, and a separately planned non-disruptive Libraries-NFS-loss test remain open. Available Sources synchronization remains manual by Jared.

## 2026-10-14 — Correct official backup system display names

- **Files changed:** `00-Rotom-Change-Log.md`, `01-Rotom-Server-Inventory.md`, `02-Docker-Services.md`, `03-Network-and-Domains.md`, `04-NAS-and-Storage.md`, `05-Backup-and-Restore.md`, `06-Maintenance-and-Automation.md`, `07-Users-and-Permissions.md`, `08-Rotom-Directory-Tree.txt`.
- **Status:** **Implemented / Verified.** No backup execution logic, script, unit, timer, schedule, retention, repository, NAS storage, credential, or recovery behavior was changed.
- **Changes:** Corrected current-state legacy documentation presentation terminology to **Rotom Restic Backup** (Rotom VM file/application-data backup), **PVE Restic Backup** (PVE host-configuration backup), and **Rotom VM Backup** (whole-VM backup using Proxmox VZDump). Retained VZDump in technical commands, archive/VMA references, verification procedures, and identifiers. Preserved older Guest/Host Restic and prior display-name records as historical evidence. Updated only the two stale Homepage display labels, then recreated Homepage to load its configuration.
- **Evidence:** Read-only LAN status APIs reported all three schedules active, enabled, and successful on 2026-10-14. Rotom preflight found `Rotom VM Backup` already correct and `Rotom Restic`/`PVE Restic` as the only outdated Homepage labels. The corrected live YAML rendered successfully; Homepage was recreated and `running healthy`; its API returned all three official names; `systemctl --failed` returned no units; and all three status APIs still reported successful scheduled runs. PVE's status endpoints were read successfully from Rotom; direct PVE configuration inspection remains Jared-executed under the established access procedure.
- **Outstanding:** Run the supplied read-only PVE inspection block if direct host-side display-label evidence is required. Available Sources synchronization remains manual by Jared.

## 2026-10-14 — Standardize backup system display names

- **Files changed:** `00-Rotom-Change-Log.md`, `01-Rotom-Server-Inventory.md`, `02-Docker-Services.md`, `03-Network-and-Domains.md`, `04-NAS-and-Storage.md`, `05-Backup-and-Restore.md`, `06-Maintenance-and-Automation.md`, `07-Users-and-Permissions.md`, `08-Rotom-Directory-Tree.txt`.
- **Status:** **Implemented / Verified.** No backup execution logic, script, unit, timer, schedule, retention, repository, NAS storage, credential, or recovery behavior was changed.
- **Changes:** Standardized current-state presentation terminology as **Rotom Restic** (guest file/application-data backup), **PVE Restic** (PVE host-configuration backup), and **Rotom VM Backup** (whole-VM backup). Updated only the three Homepage card labels to those exact names. Retained **VZDump** for the technical Proxmox mechanism, commands, VMA archives, verifiers, and identifiers. Historical records retain their original terminology as evidence. The legacy documentation has no current `Rotom-Architecture.md` or other current non-numbered Available Source.
- **Evidence:** Read-only Rotom checks on 2026-10-14 found `rotom-restic-backup.timer` and `rotom-weekly-maintenance.timer` active/enabled; guest, PVE Restic, and Rotom VM Backup status APIs each reported active/enabled schedules with successful 2026-10-14 runs. The guest Restic NFS mount was present. Homepage rendered the exact three official labels after its display-only YAML update, remained `running healthy`, and Rotom had zero failed systemd units. Jared-executed PVE search of the backup-status implementation, `/etc/pve/jobs.cfg`, and systemd definitions returned no matching legacy or alternate display terminology.
- **Outstanding:** Available Sources synchronization remains manual by Jared.

## 2026-10-14 — Add Fran as a Rotom and PVE administrator

- **Files changed:** `00-Rotom-Change-Log.md`, `01-Rotom-Server-Inventory.md`, `02-Docker-Services.md`, `03-Network-and-Domains.md`, `05-Backup-and-Restore.md`, `06-Maintenance-and-Automation.md`, `07-Users-and-Permissions.md`, `08-Rotom-Directory-Tree.txt`.
- **Status:** **Implemented / Verified.** Documentation updated from direct Rotom inspection and Jared-executed PVE output.
- **Changes:** Recreated Fran as a normal interactive Rotom administrator (`1002:1002`) with Zsh, Oh My Zsh, full `sudo`, `users`, and root-equivalent Docker-group access. Installed Oh My Zsh for the selected Rotom identities and changed `desktopcmd` from Bash to Zsh without unlocking it or adding privileges. Created PVE Linux/PAM administrator Fran (`1001:1001`), granted full sudo plus `systemd-journal`, added enabled `fran@pam` with propagated `Administrator` access at `/`, and installed Oh My Zsh. Existing Jared access and emergency root recovery remain unchanged.
- **Evidence:** Final Rotom NSS/group inspection showed Fran in `sudo`, `users`, and Docker GID `989`; `desktopcmd` and the five current service identities use `/usr/bin/zsh`, and their selected Oh My Zsh configurations were observed or confirmed by supplied shell tests. Jared-executed PVE verification showed Fran's password-set Linux account, private `0700` home, unrestricted sudo policy, `systemd-journal` membership, enabled PAM identity, propagated root Administrator ACL, effective Proxmox permissions, working Oh My Zsh, and successful journal read. No credential or key content was recorded.
- **Outstanding:** Fran's SSH public-key authentication is intentionally deferred on both Rotom and PVE; PVE `/home/fran/.ssh` was verified absent. Direct PVE web-login acceptance and a direct Rotom `docker ps` test as Fran were not supplied, although the corresponding effective ACL and group membership are verified. Remote Desktop Commander service health was not rechecked after changing `desktopcmd`'s shell. Fran has no separate current Rotom documentation ACL, GitHub identity, or Codex entry point recorded. Available Sources replacement remains manual by Jared.

## 2026-10-14 — Read-only Rotom and PVE audit reconciliation

- **Files changed:** `00-Rotom-Change-Log.md`, `01-Rotom-Server-Inventory.md`, `02-Docker-Services.md`, `03-Network-and-Domains.md`, `04-NAS-and-Storage.md`, `05-Backup-and-Restore.md`, `06-Maintenance-and-Automation.md`, `07-Users-and-Permissions.md`, `08-Rotom-Directory-Tree.txt`.
- **Status:** **Implemented / Documentation updated / Verified / Needs Verification.** Live changes were limited to removing two owner-approved cross-domain Smart Home ACL entries, repairing PVE's local Postfix hostname/alias database, and retiring explicitly reviewed rollback copies. No service restart, container, backup, NAS, network, firewall, package, proxy, DNS, certificate, repository, or application-content change occurred.
- **Changes:** Added dated Rotom guest and PVE host/VM baselines; reconciled the five live guest NFS contracts, current identities, active NPM routes/certificates, direct listener exposure, apex-only LAN DNS override, backup results, absent local backup-staging root, and Docker runtime. Removed the confirmed unintended `game-servers` write ACLs while preserving Smart Home/Jared access. Corrected the preliminary repository finding: current PVE sources are Debian plus PVE/CEPH no-subscription only, with no enabled enterprise source. Repaired Postfix's stale `proxmox.rotom.casa` identity to `pve.rotom.casa`, generated the missing alias database, and preserved the undeliverable queue without configuring a relay. At Jared's explicit direction, permanently removed the 32 inventoried unreferenced Rotom `.pre-*`/`.orig` rollback files plus the exact three-file PVE Postfix repair directory. Historical creation records remain historical; the files are no longer locally available.
- **Evidence:** Read-only 2026-10-14 Rotom inspection plus Jared-executed PVE collection completed at `2026-10-14T00:59:21-07:00`. PVE reported version `9.2.0` with `pve-manager 9.2.21`, zero currently failed units, running VM 100, active backup NFS mounts, eight current VM archives, ten PVE Restic snapshots, and a clean `restic check`. Privileged guest follow-up established 22 Docker objects (20 running and two stopped Palworld containers), three volumes, nineteen networks, zero restart counts, and 22 healthy Restic repository snapshots with latest `9494979d`. ACL verification passed. PVE repository/policy output proved only no-subscription Proxmox sources. Postfix verification showed `myhostname = pve.rotom.casa`, root-owned `0644` `/etc/aliases.db`, successful validation/reload, active service state, and the unchanged eleven-record queue. Cleanup verification found no matching backup-like files in the audited Rotom roots; active scripts parsed, Homepage Compose validated and remained healthy, relevant timers remained enabled/active, Postfix validation passed, and both hosts reported zero failed units.
- **Outstanding:** Confirm whether direct LAN application listeners—including NPM's host-networked API on TCP `3000`—apex-only split DNS, absent guest backup-staging root, retained deleted NPM rows, and disabled/ruleless PVE firewall are intentional. External PVE email remains unavailable without a relay or alternate target; eleven deferred records remain queued. Apply the reviewed PVE update transaction and reboot in a maintenance window; assess CPU/iGPU warnings; capture exact PVE storage configuration; decide whether to remove orphaned Docker volumes, the retired Syncthing image, and dangling images; prove Libraries/Paperless NAS recovery; and run full guest Restic data-read plus VMA verification/restore rehearsals. Available Sources replacement remains manual by Jared.

## 2026-10-13 — Persist Homepage backup-result color indicators

- **Files changed:** `00-Rotom-Change-Log.md`, `01-Rotom-Server-Inventory.md`, `02-Docker-Services.md`.
- **Status:** **Implemented / Verified.**
- **Changes:** Added a presentation-only Homepage customization in the persistent `/srv/rotom/appdata/platform/homepage/config` bind. Its `custom.js` marks only the three Backup Schedule **Last Result** blocks according to their refreshed custom-API value, and `custom.css` renders `success` green and `failed`/`failure` red. Backup schedules, status endpoints, retention, repositories, and backup data were not changed. Timestamped pre-change copies of both custom files remain beside the active files for rollback.
- **Evidence:** Homepage v2.5.0 is `running healthy`; Compose rendering and `node --check` of the active custom JavaScript passed; local and public Homepage checks returned `200`; all three status endpoints reported `last_result: success`; and the active configuration was verified as the persistent `/app/config` bind. Jared confirmed the visible behavior works.
- **Outstanding:** Available Sources replacement remains manual by Jared.

## 2026-10-13 — Restore Paperless in Libraries with NAS-resident media

- **Files changed:** `00-Rotom-Change-Log.md`, `01-Rotom-Server-Inventory.md`, `02-Docker-Services.md`, `03-Network-and-Domains.md`, `04-NAS-and-Storage.md`, `05-Backup-and-Restore.md`, `06-Maintenance-and-Automation.md`, `07-Users-and-Permissions.md`, `08-Rotom-Directory-Tree.txt`.
- **Status:** **Implemented / Verified.**
- **Changes:** Restored Paperless, PostgreSQL, and Valkey as Libraries (`127:5000`) workloads from the protected retained recovery set. The active Compose, appdata, and protected-input roots are now under `/srv/rotom/{stacks,appdata,secrets}/libraries/paperless`; its sole media bind is the new `/mnt/nas-libraries/paperless` subtree. The subtree is `127:5000`, mode `2770`, and is a non-creating Compose bind. The existing NPM route and Homepage Libraries card are now live. The NAS recovery helper validates the Paperless directory and conditionally recovers the Paperless container after a qualifying NAS startup failure. The recovered source set remains intact.
- **Evidence:** The retired Documents NFS export refused the temporary mount, so no bypass was attempted. The retained recovery media (five files / 384,771 bytes) was copied to Libraries with matching SHA-256 manifests. Compose rendered successfully; Paperless became healthy; loopback `127.0.0.1:8000` and `paperless.rotom.casa` each returned the expected `302` login redirect; Libraries could read the restored original and write the target directory; the recovery helper completed successfully with zero failed systemd units.
- **Outstanding:** Guest Restic protects the restored VM-local Paperless state but still excludes `/mnt`; effective Libraries NAS snapshot/restore protection remains Needs Verification. Perform authenticated upload/OCR/original-download acceptance and a separately planned isolated NAS recovery test before treating those outcomes as verified. Available Sources replacement remains manual by Jared.

## 2026-10-13 — Reconcile live NAS service boundaries and ownership

- **Files changed:** `00-Rotom-Change-Log.md`, `01-Rotom-Server-Inventory.md`, `02-Docker-Services.md`, `04-NAS-and-Storage.md`, `05-Backup-and-Restore.md`, `06-Maintenance-and-Automation.md`, `07-Users-and-Permissions.md`, `08-Rotom-Directory-Tree.txt`.
- **Status:** **Implemented / Verified.**
- **Changes:** Normalized every descendant of `/mnt/nas-libraries` to `libraries:libraries` (`127:5000`) and retained setgid on each directory. Verified the empty `/mnt/nas-game-servers`, `/mnt/nas-hosted-websites`, and `/mnt/nas-smart-home` boundaries create descendants as their respective `game-servers`, `hosted-websites`, and `smart-home` identities. Corrected the current-state layer to reflect the live `Hosted_Websites/.data` automount, the live `smart-home` identity/local roots, and the absence of the previously documented home NAS shortcuts. The retired `/mnt/nas-web` contract remains retired.
- **Evidence:** 2026-10-13 live `getent`, `stat`, fstab, NFS mount, Docker-mount, ownership, setgid, and service-account disposable-create checks. Libraries scan found 5,159 descendants, all `127:5000`; the three other shares were empty after their test objects were removed. qBittorrent local HTTP returned `200`; NPM returned its expected local `301` after the brief Libraries service stop/start.
- **Outstanding:** Guest Restic excludes `/mnt`; effective NAS snapshot/recovery policy remains Needs Verification. The live changes revealed a prior legacy documentation/live-state discrepancy; this entry corrects the supported current-state layer. Available Sources replacement remains manual by Jared.

## 2026-10-13 — Move Game Servers and Smart Home to renamed NAS Drives

- **Files changed:** `00-Rotom-Change-Log.md`, `01-Rotom-Server-Inventory.md`, `04-NAS-and-Storage.md`, `05-Backup-and-Restore.md`, `06-Maintenance-and-Automation.md`, `08-Rotom-Directory-Tree.txt`.
- **Status:** **Implemented / Verified.**
- **Changes:** Replaced Rotom's `Gameserver/.data -> /mnt/nas-gameserver` and `Smarthome/.data -> /mnt/nas-smarthome` guest contracts with fstab-backed systemd automounts for `Game_Servers/.data -> /mnt/nas-game-servers` and `Smart_Home/.data -> /mnt/nas-smart-home`. Replaced the matching `game-servers` and `smart-home` home shortcuts and removed the former empty local mountpoints and shortcuts. No container, Compose, application-state, backup-policy, or NAS-side data migration was performed.
- **Evidence:** 2026-10-13 read-only temporary NFS preflights and final live traversal both mounted the exact `Game_Servers/.data` and `Smart_Home/.data` sources as NFSv3 `sec=sys`; their automount units were active and systemd reported no failed units. Final Docker inspection found no running bind using either former path.
- **Outstanding:** Available Sources replacement remains manual by Jared. The retired NAS drive contents/retention were not inspected or removed.

## 2026-10-13 — Rename Library local identity and roots to Libraries

- **Files changed:** `00-Rotom-Change-Log.md`, `01-Rotom-Server-Inventory.md`, `02-Docker-Services.md`, `04-NAS-and-Storage.md`, `05-Backup-and-Restore.md`, `07-Users-and-Permissions.md`, `08-Rotom-Directory-Tree.txt`.
- **Status:** **Implemented / Verified.**
- **Changes:** Renamed the local Linux account and group `library` to `libraries`, retaining UID:GID `127:5000`, and moved its home to `/home/libraries`. Renamed the active local Compose, mutable-state, and protected-input roots to `/srv/rotom/{stacks,appdata,secrets}/libraries`; updated the affected Compose binds and recreated Jellyfin, Radarr, Sonarr, RomM, qBittorrentVPN, and Prowlarr. The NAS mount `/mnt/nas-libraries` and its internal `library/` data directory were intentionally unchanged. A transient singular appdata tree created during the first recreation was moved to `/srv/rotom/backup-staging/libraries-rename-transient-20261013` for reversible review rather than deleted.
- **Evidence:** 2026-10-13 final inspection confirmed `libraries:x:127:5000::/home/libraries:/usr/bin/zsh`, the former account/group and all four singular local roots absent, active Compose paths free of singular local-root references, and all eight affected containers running with plural appdata mounts. Jellyfin/Radarr/Sonarr/Prowlarr returned `302`; qBittorrent returned `200` with `wg0` at `10.2.0.2/32`; RomM and its database were running (database healthy); and systemd had no failed units.
- **Outstanding:** Available Sources replacement remains manual by Jared. Review and remove the retained transient staging tree only with separate authorization after confirming it is no longer needed.

## 2026-10-13 — Finalize Homepage Uptime Kuma retirement presentation

- **Files changed:** `00-Rotom-Change-Log.md`, `01-Rotom-Server-Inventory.md`, `02-Docker-Services.md`, `03-Network-and-Domains.md`, `06-Maintenance-and-Automation.md`, `08-Rotom-Directory-Tree.txt`.
- **Status:** **Implemented / Verified.**
- **Changes:** Removed the stale Uptime Kuma card and its `siteMonitor` from Homepage's Platform section, completing the presentation cleanup for the already-retired service. Renamed the Homepage service section and matching layout key from **Library** to **Libraries**. Timestamped rollback copies of the affected live YAML files were retained.
- **Evidence:** 2026-10-13 live YAML/API inspection found no Uptime Kuma card or `uptime.rotom.casa` monitor after the change and showed the **Libraries** key in both services and layout YAML. Homepage Compose validation passed; the container was `running healthy`; local-host and public HTTPS checks returned `200`.
- **Outstanding:** Available Sources replacement remains manual by Jared.

## 2026-10-13 — Retire local Media mountpoint remnant

- **Files changed:** `00-Rotom-Change-Log.md`, `01-Rotom-Server-Inventory.md`, `02-Docker-Services.md`, `04-NAS-and-Storage.md`, `05-Backup-and-Restore.md`, `06-Maintenance-and-Automation.md`, `08-Rotom-Directory-Tree.txt`.
- **Status:** **Implemented / Verified.**
- **Changes:** Removed the retired guest-local `/mnt/nas-media` directory after confirming that its fstab/systemd contract and active Compose references were already absent. The empty local `library/games` descendants were removed with guarded `rmdir`; the active Library contract remains `/mnt/nas-libraries`. Historical Media path records remain dated evidence and are not instructions to recreate the mount.
- **Evidence:** 2026-10-13 final inspection found `/mnt/nas-media` absent, no active fstab or systemd match, and `/mnt/nas-libraries` mounted from NAS `Libraries/.data`. Pre-removal inspection found only empty local directories and no active configuration reference.
- **Outstanding:** NAS-side Media export/data was not inspected or changed. Available Sources replacement remains manual by Jared.

## 2026-10-13 — Align Hosted Websites and Game Servers local domains

- **Files changed:** `00-Rotom-Change-Log.md`, `01-Rotom-Server-Inventory.md`, `02-Docker-Services.md`, `04-NAS-and-Storage.md`, `05-Backup-and-Restore.md`, `06-Maintenance-and-Automation.md`, `07-Users-and-Permissions.md`, `08-Rotom-Directory-Tree.txt`.
- **Status:** **Implemented / Verified.**
- **Changes:** Recorded the completed local rename from `web` to `hosted-websites` (`902:5004`) and from `gameserver` to `game-servers` (`995:5001`). Active website and Palworld Compose/state paths now use the matching hyphenated domains. Recorded retirement of Rotom's guest-only Web NFS fstab/automount/mountpoint and stale home symlink; NAS-side Web export/data was not changed. Preserved historical names, paths, and prior IDs as dated evidence rather than rewriting them as current state.
- **Evidence:** 2026-10-13 live identity, ownership, path, Compose-label/bind, and mount checks. Aloha was recreated from `/srv/rotom/{stacks,appdata}/hosted-websites` and its public HTTPS probe returned `200`. Palworld Jared and Fran were recreated without starting; persistent local file counts remained 301 and 212. `/mnt/nas-gameserver` and its retained home symlink remain; `/mnt/nas-web` is absent.
- **Outstanding:** Available Sources replacement remains manual by Jared. NAS-side Web export/data was intentionally not inspected; verify it separately before any NAS cleanup or recovery action.

## 2026-10-13 — Retire Documents local remnants

- **Files changed:** `00-Rotom-Change-Log.md`, `01-Rotom-Server-Inventory.md`, `05-Backup-and-Restore.md`, `07-Users-and-Permissions.md`, `08-Rotom-Directory-Tree.txt`.
- **Status:** **Implemented / Verified.**
- **Changes:** Removed the unused retired Documents local state roots `/srv/rotom/appdata/documents` and `/srv/rotom/secrets/documents`. No Documents account/group, home, local mount, Compose stack, container, or active Compose reference remains. Historical Paperless/Documents deployment and recovery records are retained, but neither local Documents appdata nor local Documents secrets are available for recovery.
- **Evidence:** 2026-10-13 preflight found each exact target was an empty 4 KiB directory, with no active Compose/container reference and no `documents` account/group. Post-removal checks found both paths absent; the active container set remained running.
- **Outstanding:** NAS Documents data/export and historical Restic evidence were not inspected or changed. Available Sources replacement remains manual by Jared.

## 2026-10-13 — Move Rotom legacy documentation checkout to Platform documentation

- **Files changed:** `00-Rotom-Change-Log.md`, `01-Rotom-Server-Inventory.md`, `06-Maintenance-and-Automation.md`, `07-Users-and-Permissions.md`, `08-Rotom-Directory-Tree.txt`.
- **Status:** **Implemented / Verified.**
- **Changes:** Recorded the current Rotom legacy documentation checkout and resolver fallback at `/home/platform/documentation/rotom-runbook`; updated current-state Codex, publisher, permissions, and directory-tree references. Dated `/home/infra/documentation` references remain historical evidence.
- **Evidence:** 2026-10-13 live `retired-helper path` and `/home/jared/.config/retired-helper/repository` both resolved the Platform path; `/home/infra` was absent; `stat` verified `/home/platform` `nobody:nogroup` mode `0750` and its documentation/repository directories `jared:jared` mode `0755`. A scoped live configuration search found no active old-path reference.
- **Outstanding:** Available Sources replacement remains manual by Jared.

## 2026-10-12 — Retire Customapps from Rotom

- **Files changed:** `00-Rotom-Change-Log.md`, `01-Rotom-Server-Inventory.md`, `02-Docker-Services.md`, `03-Network-and-Domains.md`, `04-NAS-and-Storage.md`, `05-Backup-and-Restore.md`, `06-Maintenance-and-Automation.md`, `07-Users-and-Permissions.md`, `08-Rotom-Directory-Tree.txt`.
- **Status:** **Implemented / Verified.**
- **Changes:** Retired the unused `customapps` (`904:5008`) Linux account/group; its absent configured `/home/apps` path and actual default-only `/home/customapps` tree; the `/mnt/nas-customapps` fstab/systemd automount contract and local mountpoint; and the empty `/srv/rotom/{stacks,appdata,secrets}/customapps` directories. The only stack file was the future-domain contract. No running process, active system/cron/stack reference, workload, Compose definition, or failed unit remained.
- **Evidence:** Root mounted `Customapps/.data` read/write and found it empty before retirement; its generated mount had zero tasks. The targeted fstab removal passed `findmnt --verify` with zero parse errors (two pre-existing unrelated `/media/cdrom0` warnings), generated units and local mountpoint were absent, and final checks found no account/group, home, local Customapps directory, active configuration reference, or failed unit.
- **Outstanding:** The UniFi NAS-side `Customapps` export/drive was not deleted or independently rechecked after the guest retirement because Rotom has no authorized NAS-management path. It was empty when mounted; remove it separately through the UniFi management plane if intended.

## 2026-10-12 — Grant Jared read access to local home trees

- **Files changed:** `00-Rotom-Change-Log.md`, `01-Rotom-Server-Inventory.md`, `07-Users-and-Permissions.md`.
- **Status:** **Implemented / Verified.**
- **Changes:** Added the named `jared` POSIX ACL with read/traverse access recursively to local service-home content and added the matching default named-user ACL to `/home` and local service directories for ordinary future descendants. Jared's own home is already readable through ownership, so its redundant named ACL was removed to preserve SSH-required private-key protections. The change does not apply to targets of `nas-*` shortcut symlinks: those are independent NFS permission boundaries that do not support the requested local POSIX ACL operation.
- **Evidence:** Live root inspection confirmed the access/default ACL on `/home` and representative service and `desktopcmd` directories; Jared-context local-tree checks found no unreadable regular files or inaccessible directories, and all service-home roots remained non-writable to Jared. The GitHub private key initially appeared group-readable through the ACL mask, then recovered to its required owner-only `0600` mode after removal of the redundant ACL from Jared's owner tree. Ownership and base owner/group ACL entries were retained; the required ACL mask is reflected as `r-x` in the conventional group-class mode display.
- **Outstanding:** Default ACL inheritance applies to ordinary future local content; a creating application can later restrict or replace it. NAS shortcut targets remain governed by their existing NAS permissions. This corrects the 2026-10-10 current-policy wording that said ACL application did not change displayed mode bits: POSIX ACL masks necessarily determine that display, without granting the base group new access.

## 2026-10-10 — Complete Available Sources documentation audit

- **Files changed:** `00-Rotom-Change-Log.md`, `01-Rotom-Server-Inventory.md`, `02-Docker-Services.md`, `03-Network-and-Domains.md`, `04-NAS-and-Storage.md`, `06-Maintenance-and-Automation.md`, `07-Users-and-Permissions.md`, `08-Rotom-Directory-Tree.txt`.
- **Status:** **Documentation only.** No live Rotom, PVE, Docker, NAS, network, backup, account, proxy, or external-service state was changed.
- **Changes:** Reviewed every current Available Sources member (`00`–`08`) a second time against the latest recorded evidence. Reconciled the current Docker inventory to the 2026-10-10 24-running-container record, aligned the directory-tree recovery-helper scope with the documented Downloader/Media/Documents/Filesync contract, removed orphaned headings, and clarified dated historical versus current state without rewriting historical evidence. `05-Backup-and-Restore.md` was reviewed and left unchanged because it remains the canonical supported backup/recovery record.
- **Evidence:** Complete cross-document legacy documentation review; no new live inspection was performed during this documentation-only audit.
- **Outstanding:** Existing Needs Verification items remain, including the next timer-triggered guest Restic run after repair, NAS snapshot recovery for Documents/Filesync before payload becomes authoritative, NAS metadata persistence, recovery rehearsals, alert/WOL delivery, certificate renewal, and exposure-policy review.

## 2026-10-10 — Extend NAS-backed Docker recovery to Documents and Filesync

- **Files changed:** `00-Rotom-Change-Log.md`, `01-Rotom-Server-Inventory.md`, `02-Docker-Services.md`, `06-Maintenance-and-Automation.md`.
- **Status:** **Implemented / Verified.**
- **Changes:** Extended the enabled root-owned `/usr/local/sbin/rotom-nas-docker-recovery` helper without changing any Compose restart policy. It now mounts and validates the Documents and Filesync NFS boundaries in addition to its retained Downloader/Media checks, then can recover `paperless`, `romm`, and `syncthing` alongside the existing covered consumers. The helper still leaves running containers untouched and starts a stopped container only when its policy is `unless-stopped` or `always` and Docker recorded a NAS/mount startup-failure signature.
- **Evidence:** A 2026-10-10 live run mounted `/mnt/nas-documents`, `/mnt/nas-media`, and `/mnt/nas-filesync`, recovered the three previously stopped containers, and completed successfully. Paperless and Syncthing reported healthy; local Paperless, RomM, and Syncthing endpoints returned `302`, `200`, and `200` respectively. Fresh `docker ps -a` showed 24 container objects, all running; `systemctl --failed` was empty.
- **Outstanding:** Normal future-boot observation remains useful, but the helper's live recovery path is verified.

## 2026-10-10 — Grant Jared read access to the Rotom v2 namespace

- **Files changed:** `00-Rotom-Change-Log.md`, `01-Rotom-Server-Inventory.md`, `07-Users-and-Permissions.md`.
- **Status:** **Implemented / Verified.**
- **Changes:** Added a named `jared` POSIX ACL with read/traverse access recursively to the existing `/srv/rotom` tree, including application state, protected inputs, and backup staging. Added the matching default named-user ACL to every existing directory so new descendants inherit the access policy. Ownership, group ownership, and mode bits were not changed.
- **Evidence:** Live root ACL inspection confirmed `user:jared:r-x` plus a matching default ACL on representative top-level and protected/service-owned directories. A Jared-context traversal check found no unreadable regular file or inaccessible directory in `/srv/rotom`; protected top-level `secrets/` and `backup-staging/` remained non-writable to Jared. One pre-existing descendant is owned by Jared and therefore remains writable through its owner permissions; it was not changed.
- **Outstanding:** Default ACL inheritance provides the policy for ordinary new content; a creating application can later restrict or replace an ACL/mode, which must be evaluated if Jared loses access to such content.

## 2026-10-05 — Verify PVE VM backup cadence and retain the 100 GiB VM disk baseline

- **Files changed:** `00-Rotom-Change-Log.md`, `01-Rotom-Server-Inventory.md`, `04-NAS-and-Storage.md`, `05-Backup-and-Restore.md`, `06-Maintenance-and-Automation.md`, `08-Rotom-Directory-Tree.txt`.
- **Status:** **Implemented / Verified.**
- **Changes:** A manual whole-VM VZDump completed before a temporary capacity assessment. VMID `100`'s thin VirtIO SCSI disk was briefly enlarged from `100 GiB` to `150 GiB`, but no guest partition or filesystem was changed. After the backup completed, the VM was cleanly stopped, its thin LV and Proxmox `scsi0` configuration were restored to `100 GiB`, and it booted successfully. The recorded current configuration therefore remains the original `100 GiB` disk. The PVE storage audit also records the current Samsung NVMe/LVM layout and distinguishes host-root free space, thin-pool free space, and unassigned VG capacity.
- **Evidence:** PVE reported `nvme0n1` at `232.9 GiB`; LVM root `67.75 GiB` with about `57 GiB` filesystem availability, swap `8 GiB`, thin pool `136.46 GiB` at `69.06%` allocated with about `42.2 GiB` free, and VG `VFree` `16 GiB`. Post-rollback `lvs` reported `vm-100-disk-1` at `100.00 GiB`; `qm config 100` reported `scsi0 ... size=100G`; and VMID `100` was running. The manual VZDump logged successful completion at `2026-10-05 23:00:53 PDT`; the subsequent PVE archive listing showed eight current VMID `100` archives, including six `05:00` scheduler-produced archives from 2026-09-30 through 2026-10-05, a separately listed 2026-09-29 archive, and manual `vzdump-qemu-100-2026_10_05-22_47_06.vma.zst`. `qm agent 100 ping` returned successfully.
- **Outstanding:** The 2026-10-05 archive listing proves archive availability and successful VZDump completion, but no new zstd or full VMA verification was supplied for those current archives. The earlier 2026-09-28 fully verified archive is historical evidence only and was absent from the current listing. Do not allocate the entire nominal thin-pool headroom without a separate capacity plan and margin.

## 2026-10-05 — Retire unused JDownloader service

- **Files changed:** `00-Rotom-Change-Log.md`, `01-Rotom-Server-Inventory.md`, `02-Docker-Services.md`, `05-Backup-and-Restore.md`, `06-Maintenance-and-Automation.md`, `07-Users-and-Permissions.md`, `08-Rotom-Directory-Tree.txt`.
- **Status:** **Implemented / Verified.**
- **Changes:** Retired the unused private JDownloader Compose module. Removed only its container, project network, image, Compose definition, 296 KiB VM-local configuration, and two dedicated protected MyJDownloader input files. The shared Media RomM inbox, its contents, and the independent Igir, qBittorrent importer, and browser-upload paths remain intact.
- **Evidence:** Pre-removal inspection verified that JDownloader had no host-published ports, no dependent containers, and only its dedicated local configuration/secret directories plus the shared `/mnt/nas-media/downloads/romm-inbox` bind. `docker compose down` removed `jdownloader` and `jdownloader_default`; the three dedicated paths are absent. After confirming no remaining container used it, the pinned JDownloader image was untagged and deleted. The shared inbox remains present at 7.5 GiB; RomM and qBittorrentVPN remain running, while `romm-igir.timer`, `romm-qbt-importer.timer`, and `romm-upload-bridge.service` remain active.
- **Outstanding:** None. Historical JDownloader records remain preserved as historical evidence.

## 2026-10-05 — Repair guest Restic NPM SQLite staging source

- **Files changed:** `00-Rotom-Change-Log.md`, `01-Rotom-Server-Inventory.md`, `05-Backup-and-Restore.md`, `06-Maintenance-and-Automation.md`.
- **Status:** **Implemented / Verified.**
- **Changes:** Corrected the root-only guest Restic worker's NPM SQLite source from retired `/home/infra/docker/nginx-proxy-manager/data/database.sqlite` to the active v2 database at `/srv/rotom/appdata/infra/nginx-proxy-manager/data/database.sqlite`.
- **Evidence:** Scheduled runs on 2026-10-02 through 2026-10-05 failed only at the stale-path preflight. The corrected worker passed `bash -n`; a manual service run created snapshot `8efea294` at 2026-10-05 21:45 PDT, completed normal `7 daily / 4 weekly / 12 monthly` retention/prune, and exited `0`. The prior failed-unit state was cleared; weekly maintenance remains enabled for its next scheduled run.
- **Outstanding:** Observe the next unattended guest Restic run after this repair. Existing PVE, NAS, router, WOL, and recovery-rehearsal gaps remain unchanged.

## 2026-10-01 — Restore Homepage Uptime Kuma monitor resolution

- **Files changed:** `00-Rotom-Change-Log.md`, `02-Docker-Services.md`, `06-Maintenance-and-Automation.md`.
- **Status:** **Implemented / Verified.**
- **Changes:** Homepage's Uptime Kuma `siteMonitor` was red because the Homepage container intermittently failed to resolve `uptime.rotom.casa` (`EAI_AGAIN`). Added the targeted `uptime.rotom.casa:192.168.1.69` `extra_hosts` mapping to `/srv/rotom/stacks/infra/homepage/compose.yaml` and recreated only Homepage. Uptime Kuma, Nginx Proxy Manager, public DNS, certificates, and the Uptime Kuma monitor configuration were unchanged.
- **Evidence:** The active Compose definition validated. The rebuilt Homepage was healthy, carried the exact mapping, resolved the hostname internally, and reached the Uptime Kuma TLS route, which returned its expected redirect followed by the dashboard response. Homepage's canonical local request returned HTTP `200`, and no new matching DNS error appeared in post-rebuild logs.
- **Outstanding:** The separate Jared Wines card remains intentionally unavailable because its website is intentionally undeployed.

## 2026-10-01 — Record boot-time Game NAS recovery limitation

- **Files changed:** `00-Rotom-Change-Log.md`, `01-Rotom-Server-Inventory.md`, `02-Docker-Services.md`, `04-NAS-and-Storage.md`, `06-Maintenance-and-Automation.md`, `08-Rotom-Directory-Tree.txt`.
- **Status:** **Verified / Documentation only.**
- **Changes:** Recorded the 2026-10-01 boot incident in which the initial Game and Filesync NFS mount attempts failed while the NAS network route was unavailable. Clarified that `/mnt/nas-game/.rotom-qbt-media-ready` is a qBittorrentVPN sentinel, not a torrent-payload location; the qBittorrent guard checks both Media and Game every 15 seconds, but does not restart containers. Corrected the recovery-helper scope: it covers Downloader and Media only. RomM and JDownloader have required Game bind mounts but no Game-specific sentinel, guard, or automatic restart/recovery path.
- **Evidence:** Root live inspection recorded `mount.nfs: Network is unreachable` for Game and Filesync during the 12:57 PDT boot; Docker then recorded mount-start errors for JDownloader, RomM, qBittorrentVPN, Radarr, Sonarr, and Jellyfin. After the NAS returned, the Game and Filesync NFS mounts, required Game/Media paths and markers, all six affected containers, the qBittorrent guard, and zero failed systemd units were verified. Active torrent payload remained `/mnt/nas-media/torrents`; no legacy service-home Docker-tree deletion caused the incident.
- **Outstanding:** The existing helper/guard design was documented, not changed. A future implementation decision is required before adding automatic Game recovery for RomM or JDownloader.

## 2026-10-01 — Organize repository-support files

- **Files changed:** `00-Rotom-Change-Log.md`, `01-Rotom-Server-Inventory.md`, `06-Maintenance-and-Automation.md`, `08-Rotom-Directory-Tree.txt`, `AGENTS.md`, `README.md`, `CONTRIBUTING.md` → `support/CONTRIBUTING.md`, `tooling/retired-helper` → `support/tooling/retired-helper`.
- **Status:** **Documentation only.**
- **Changes:** Kept the nine-file Core Numbered Reference Set, root `AGENTS.md`, root `README.md`, and `.gitignore` at the repository root. Moved repository-only contribution guidance and the canonical helper source into `support/`; root documentation and current-state references now use the new paths. `support/` is repository support material, not an legacy documentation membership boundary or an Available Sources destination.
- **Evidence:** Explicit user decision on 2026-10-01; repository path/reference review before the move.
- **Outstanding:** None. The identical `/usr/local/bin/retired-helper` installations on Mac and Rotom were unchanged; this task only moved their tracked canonical source path inside the repository.

## 2026-10-01 — Record JDownloader and current Docker inventory

- **Files changed:** `00-Rotom-Change-Log.md`, `01-Rotom-Server-Inventory.md`, `02-Docker-Services.md`, `06-Maintenance-and-Automation.md`, `08-Rotom-Directory-Tree.txt`.
- **Status:** **Verified / Documentation only.**
- **Changes:** Recorded the supplied root `docker ps -a` inventory: 25 container objects, 24 running, and Syncthing exited normally. Added the newly observed running `jdownloader` container; its bare TCP `3129` port is container-only in the supplied output. The two Palworld containers were running and healthy. Gamarr remains retired and absent.
- **Evidence:** User-supplied `sudo docker ps -a` output from 2026-10-01. It enumerated each current container/status and did not expose secret values.
- **Outstanding:** JDownloader's authoritative Compose path, persistent binds, service identity, network attachments, restart policy, and recovery/backup contract were not inspected; do not infer them from `docker ps -a` alone.

## 2026-10-01 — Add legacy documentation repository README and contribution guide

- **Files changed:** `README.md`, `CONTRIBUTING.md`, `00-Rotom-Change-Log.md`, `01-Rotom-Server-Inventory.md`.
- **Status:** **Documentation only / Verified.**
- **Changes:** Added repository-support `README.md` as the GitHub landing page and navigation index, plus `CONTRIBUTING.md` as the concise repository-facing change guide. Both direct readers to this document as the sole canonical legacy documentation maintenance contract. They document the current nine-file Core Numbered Reference Set and safety expectations, but neither file is an legacy documentation member or changes Available Sources membership.
- **Evidence:** Explicit user decision on 2026-10-01; the new files were created in the verified current legacy documentation Git checkout after reconciling its then-current GitHub `main` history.
- **Outstanding:** None.

## 2026-09-30 — Remove obsolete qBittorrent NAS readiness markers

- **Files changed:** `00-Rotom-Change-Log.md`, `08-Rotom-Directory-Tree.txt`.
- **Status:** **Implemented / Verified.**
- **Changes:** Removed the empty, unreferenced legacy directories `/mnt/nas-media/.rotom-qbt-nas-ready` and `/mnt/nas-game/.rotom-qbt-nas-ready` using non-recursive directory removal. The active Media qBittorrent safety marker `/mnt/nas-media/.rotom-qbt-media-ready` remains unchanged.
- **Evidence:** Live reference scans found neither removed path in `/etc`, `/usr/local`, or `/srv/rotom`; qBittorrentVPN mounts only the active Media marker at `/run/rotom-nas-media`. Both removed directories were verified empty, then absent after removal. The enabled active media-guard timer checks the retained Media marker and underlying NFS filesystem.
- **Outstanding:** None.

## 2026-09-30 — Retire unused Game Downloads bindfs view

- **Files changed:** `00-Rotom-Change-Log.md`, `01-Rotom-Server-Inventory.md`, `02-Docker-Services.md`, `03-Network-and-Domains.md`, `06-Maintenance-and-Automation.md`, `07-Users-and-Permissions.md`, `08-Rotom-Directory-Tree.txt`.
- **Status:** **Implemented / Verified.**
- **Changes:** Retired the unused read-only `/mnt/nas-downloads-game-ro` bindfs view, its enabled `rotom-downloads-game-ro.service`, and the view-specific branch of `rotom-nas-docker-recovery`. The helper retains its separate `/mnt/nas-game` NFS readiness check. No NAS data, Game NFS mount, Palworld path, or container bind was changed.
- **Evidence:** Live Docker inspection found no container mounted the view. The retired service was stopped/disabled and removed, its empty local mountpoint was removed after unmount confirmation, and the revised recovery helper passed syntax and healthy-state validation with success status. No active unit, helper reference, or local path remains.
- **Outstanding:** None.

## 2026-09-30 — Restore Jared Wines Homepage card

- **Files changed:** `00-Rotom-Change-Log.md`, `01-Rotom-Server-Inventory.md`, `02-Docker-Services.md`.
- **Status:** **Implemented / Verified.**
- **Changes:** Restored the existing **Jared Wines** card in Homepage's **Hosted Websites** section with its established `https://jaredwines.com` link and `siteMonitor`. The card is presentation/monitoring configuration only; the retained Jared Wines Compose module was not started and no NPM, DNS, TLS, container, or content change was made.
- **Evidence:** Homepage became healthy and returned local HTTP `200` after the targeted card restore. The public Jared Wines request returned HTTP `502`, matching the intended unstarted/no-container state.
- **Outstanding:** The card will report the target unavailable until Jared Wines is deliberately deployed; this task did not change that deployment decision.

## 2026-09-30 — PVE web UI NPM route and Homepage card

- **Files changed:** `00-Rotom-Change-Log.md`, `01-Rotom-Server-Inventory.md`, `02-Docker-Services.md`, `03-Network-and-Domains.md`, `06-Maintenance-and-Automation.md`, `08-Rotom-Directory-Tree.txt`.
- **Status:** **Implemented / Verified.**
- **Changes:** PVE's `pvedaemon` and `pveproxy` were started and enabled, and NPM proxy host `pve.rotom.casa` provides the PVE web UI through HTTPS to `192.168.1.68:8006`, with its existing certificate, forced TLS, WebSocket upgrade, and an enabled access list. Homepage now includes an unmonitored **PVE** link under **Rotom Management**. No DNS, certificate, firewall, WAN, or storage configuration was changed.
- **Evidence:** Supplied PVE output confirmed both services active and enabled, with the local PVE API responding. The live NPM record was enabled with HTTPS upstream `192.168.1.68:8006`, certificate ID `24`, access-list ID `1`, forced TLS, and WebSocket upgrade. Local-SNI `https://pve.rotom.casa` returned the Proxmox Virtual Environment page; direct PVE HTTPS also returned HTTP `200`. Homepage was healthy and its local canonical request returned HTTP `200` after the card change.
- **Outstanding:** Interactive PVE authentication and VM-console WebSocket use were not exercised because no administrator credentials were used by this task.

## 2026-09-29 — Confirm NAS Auth drive retirement

- **Files changed:** `00-Rotom-Change-Log.md`, `04-NAS-and-Storage.md`, `08-Rotom-Directory-Tree.txt`.
- **Status:** **Verified.**
- **Changes:** Recorded Jared's confirmation that the NAS `Auth` drive was deleted, completing the Auth account and guest-boundary retirement recorded below.
- **Evidence:** Jared explicitly confirmed the deletion. Rotom had already verified that no `auth` account, `/home/auth`, `/mnt/nas-auth`, Auth fstab/automount contract, or `Auth/.data` NFS export remained.
- **Outstanding:** None. Retained `Customapps` remains unchanged and must not be deleted.

## 2026-09-29 — Retire unused Auth account and guest boundary

- **Files changed:** `00-Rotom-Change-Log.md`, `01-Rotom-Server-Inventory.md`, `02-Docker-Services.md`, `04-NAS-and-Storage.md`, `05-Backup-and-Restore.md`, `06-Maintenance-and-Automation.md`, `07-Users-and-Permissions.md`, `08-Rotom-Directory-Tree.txt`.
- **Status:** **Implemented / Verified** for Rotom and the NFS export; NAS UI deletion was then unverified.
- **Changes:** Retired the unused `auth` Linux account/group (`905:5009`), its default-only `/home/auth` tree and `nas-auth` shortcut, plus the `Auth/.data -> /mnt/nas-auth` fstab/automount contract and local mountpoint. The separate `Customapps` identity and reserved mount remain unchanged.
- **Evidence:** No auth-owned process, deployed workload, Docker mount, or operational configuration reference was found. The Auth export was unavailable; `showmount` lists `Customapps/.data` but no `Auth/.data`. After targeted removal, the account/group/home/mountpoint and fstab entry were absent, Jellyfin remained up, and `systemctl --failed` reported zero failed units.
- **Outstanding:** NAS-side deletion confirmation was pending at the time; it is recorded in the newer entry above. `Customapps` remains retained and must not be deleted.

## 2026-09-29 — Retire stale Apps mount; retain Customapps boundary

- **Files changed:** `00-Rotom-Change-Log.md`, `01-Rotom-Server-Inventory.md`, `02-Docker-Services.md`, `04-NAS-and-Storage.md`, `05-Backup-and-Restore.md`, `07-Users-and-Permissions.md`, `08-Rotom-Directory-Tree.txt`.
- **Status:** **Implemented / Verified.**
- **Changes:** Corrected current terminology to `customapps` (`904:5008`) while preserving its compatibility home `/home/apps`. Retired only the stale `Apps/.data -> /mnt/nas-apps` Rotom fstab/automount contract, local mountpoint, and `/home/apps/nas-apps` shortcut; replaced the shortcut with `/home/apps/nas-customapps -> /mnt/nas-customapps`. The separate empty `Customapps/.data` boundary remains mounted and reserved.
- **Evidence:** Live `getent` identifies `customapps` with home `/home/apps`; `Customapps/.data` mounted successfully and was empty. The Apps export was unavailable, no workload configuration referenced either Apps or Customapps boundary beyond fstab, and the Apps mount was the sole failed unit. After targeted removal, `Customapps` remained mounted, the new compatibility shortcut was readable as `customapps`, Jellyfin remained up, and `systemctl --failed` reported zero failed units. Jared then confirmed that the NAS `Apps` drive was deleted.
- **Outstanding:** None. `Customapps` remains retained and must not be deleted.

## 2026-09-29 — Adopt Codex SSH and PVE execution lanes

- **Files changed:** `00-Rotom-Change-Log.md`, `01-Rotom-Server-Inventory.md`, `06-Maintenance-and-Automation.md`.
- **Status:** **Documentation only / Adopted operational policy.**
- **Changes:** Adopted the operational division of responsibility: Codex performs routine Rotom inspection and authorized changes through the `rotom` SSH alias as `jared`, using `sudo` only when needed; Jared manually executes every PVE check and change through `pve` from paste-ready, ticket-specific command blocks supplied by Codex. Each PVE block must distinguish preflight, targeted action, and verification, and Jared's output is the PVE evidence source.
- **Evidence:** Jared explicitly selected this execution model. Existing Mac key-only aliases for both `rotom` and `pve` are recorded as verified; this documentation update does not change SSH keys, account privileges, PVE, or Rotom.
- **Outstanding:** A future Rotom task must establish that Codex can use the `rotom` alias non-interactively before relying on the agent-operated lane; failure is a reported access blocker, not permission to fall back to PVE or change SSH configuration.

## 2026-09-29 — Retire empty Downloads NAS boundary

- **Files changed:** `00-Rotom-Change-Log.md`, `01-Rotom-Server-Inventory.md`, `04-NAS-and-Storage.md`, `08-Rotom-Directory-Tree.txt`.
- **Status:** **Implemented / Verified.**
- **Changes:** Retired the distinct empty UNAS `Downloads` drive and its unused Rotom `/mnt/nas-downloads` fstab/systemd-automount contract. The local mountpoint was removed after the mount was stopped. This does not affect active `Downloader/.data` at `/mnt/nas-downloaders`, or the retained `Game` rollback library.
- **Evidence:** A final mounted inspection found `Downloads/.data` contained 0 bytes and no entries; the supplied configuration-reference scan found no active workload reference. The exact fstab entry was removed, its generated automount was absent after daemon reload, the local directory was removed, `Downloader/.data` remained mounted, and `systemctl --failed` reported zero failed units. Jared then confirmed deletion of the empty NAS drive.
- **Outstanding:** `Game` remains retained rollback material and was not changed.

## 2026-09-29 — Retire superseded PVE rollback copies

- **Implemented / Verified:** With Jared's explicit authorization, retired inactive PVE rollback copies `/etc/fstab.pre-proxmox-restic-backup.20260927-152218`, `/etc/network/interfaces.pre-wol`, and `/etc/network/interfaces.pre-e1000e-offload-20260927` after confirming the active fstab/network replacements exist, differ as historical copies should, and have no active reference.
- **Verified:** PVE remained `running` with zero failed units; `pve-restic-backup.timer` remained active; `local`, `local-lvm`, and `nas-rotom-vm-backup` storage were active. No active PVE network configuration, backup worker, Restic repository/snapshot, VZDump archive, or recovery staging data was changed.
- **Documentation updated:** `06-Maintenance-and-Automation.md` retains the historical WOL/offload implementation evidence but records that its temporary pre-change copies are no longer retained.

## 2026-09-29 — Retire superseded Rotom backup rollback copies

- **Implemented / Verified:** With Jared's explicit authorization, retired two superseded `retired-helper` helper copies and ten inactive legacy Restic/backup rollback copies: historical `update-to-nas` sudoers, `unas-backup` units/status API, legacy backup helpers, and the pre-Restic-share-cutover fstab copy. Each had a current replacement and no active reference.
- **Verified:** The current legacy documentation helper/check remained healthy before and after the helper-copy removal. The active `rotom-restic-backup.timer` and `rotom-restic-backup-status-api.service` remain active; current fstab, worker, units, and status API files remain present; no failed systemd unit was reported.
- **Scope:** No Restic repository/snapshot, NAS data, current backup staging, credential, policy, timer schedule, or active recovery control was changed.
- **Documentation updated:** `08-Rotom-Directory-Tree.txt` removes the now-retired rollback-copy paths from the current filesystem topology.

## 2026-09-29 — Jared PVE backup-launcher access and journal visibility

- **Files changed:** `00-Rotom-Change-Log.md`, `01-Rotom-Server-Inventory.md`, `05-Backup-and-Restore.md`, `06-Maintenance-and-Automation.md`, `07-Users-and-Permissions.md`.
- **Status:** **Implemented / Verified.**
- **Changes:** The two root-owned PVE manual launchers, `/usr/local/bin/backup-rotom-vm-to-nas` and `/usr/local/bin/backup-restic-to-nas`, now re-execute themselves through `sudo` when invoked by a non-root user. This keeps their existing root-only workers, service ownership, backup scope, mounts, retention, and protected Restic credential boundary unchanged while allowing routine invocation by the PVE administrator `jared` through normal sudo authentication. `jared` was added to the PVE `systemd-journal` group so the account can directly follow system service logs, including `rotom-vm-vzdump-manual.service`.
- **Evidence:** Live read-only inspection on 2026-09-29 confirmed `jared` membership in `sudo` and `systemd-journal`, the group membership entry, and both launcher handoffs. Jared reconnected after the group change and confirmed direct `journalctl -fu rotom-vm-vzdump-manual.service` access.
- **Outstanding:** The manual backup jobs were intentionally not started solely to test access because each can write backup state and apply its existing retention behavior. No dedicated passwordless sudo rule for either PVE launcher was inspected or recorded.

## 2026-09-29 — Adopt Jared's routine PVE administration identity

- **Files changed:** `00-Rotom-Change-Log.md`, `01-Rotom-Server-Inventory.md`, `03-Network-and-Domains.md`, `06-Maintenance-and-Automation.md`, `07-Users-and-Permissions.md`, `08-Rotom-Directory-Tree.txt`.
- **Status:** **Implemented / Verified / Documentation policy.**
- **Changes:** Created PVE Linux account `jared`, added it to `sudo`, created enabled Proxmox identity `jared@pam`, and granted it propagated `Administrator` access at `/`. Moved the existing PVE SSH public key to Jared's PVE account, removed the matching root-authorized key, and changed the canonical Mac `pve` shortcut to use `jared@pve`. Adopted the policy that UniFi Gateway and UNAS routine administration uses UniFi roles; appliance SSH remains supported root-console access only for targeted troubleshooting, with no unsupported local Linux Jared account.
- **Evidence:** Supplied 2026-09-29 terminal output shows `jared` as UID/GID `1000:1000` with `sudo` membership, enabled `jared@pam`, its `/` Administrator ACL, and successful `sudo pveversion` output for PVE Manager `9.2.20` / kernel `7.0.14-19-pve`. Jared confirmed the PVE key is on the new account, the canonical shortcut targets Jared, and the root key was removed. No credential or key material was recorded.
- **Outstanding:** Zsh/Oh My Zsh installation for PVE Jared was requested but its completion was not supplied, so it is not recorded as implemented. No fresh direct configuration audit of the UniFi Gateway or UNAS was performed.

## 2026-09-28 — Verify universal legacy documentation helper and layered Codex instructions

- **Files changed:** `00-Rotom-Change-Log.md`, `01-Rotom-Server-Inventory.md`, `06-Maintenance-and-Automation.md`, `08-Rotom-Directory-Tree.txt`.
- **Status:** **Implemented / Verified / Documentation only.** The legacy documentation/Git/Codex integration is now in its final supported form; this entry documents the completed architecture and supersedes the current-state verification gaps recorded earlier on 2026-09-28 without rewriting those historical entries.
- **Changes:** The canonical `retired-helper` source is versioned as repository support tooling at `tooling/retired-helper` and the same script is installed at `/usr/local/bin/retired-helper` on both the Mac and Rotom. `retired-helper` now resolves the expected legacy documentation repository from the current working tree when possible and otherwise falls back to the per-user path file `~/.config/retired-helper/repository`; `retired-helper path` exposes the resolved checkout. The supported command set is `path`, `status`, `check`, `pull`, `diff`, `log [N]`, `commit "message"`, `push`, and `help`. The repository-root `AGENTS.md` is shared Git/Codex support metadata and carries common legacy documentation instructions; it is not an legacy documentation member unless intentionally added to Available Sources. The Mac global `~/.codex/AGENTS.md` is reduced to the command-line editor preference, while Rotom `/home/jared/.codex/AGENTS.md` contains Rotom machine/live-state safety rules and points Codex to `retired-helper path`, the repository `AGENTS.md`, and this document for canonical maintenance policy. Shared workflow instructions use `retired-helper path` rather than depending on a hard-coded checkout path; the verified physical checkout paths remain inventory facts.
- **Evidence:** Mac commit `152fd74` added repository `AGENTS.md` and `tooling/retired-helper`, was pushed successfully, and subsequent `retired-helper check` reported a clean `main` matching `origin/main`. The Mac installed helper and repository copy both hashed `42866ab6dbb5c47f996289d751cb26767dc79c756638cbeb9851c9e45fbdbe7b`. Rotom fast-forwarded to the same commit, installed the repository helper, passed `bash -n`, `retired-helper path`, `retired-helper status`, and `retired-helper check`, resolved the checkout successfully from `/srv` through the fallback config, and produced the same SHA-256 for `/usr/local/bin/retired-helper` and `tooling/retired-helper`. Fresh read-only Codex sessions on both Mac and Rotom correctly discovered the intended instruction hierarchy and canonical legacy documentation maintenance authority. Jared also confirmed the Mac global `AGENTS.md` cleanup.
- **Outstanding:** None for the helper/instruction architecture. Available Sources replacement and publication of this documentation update remain the normal manual completion steps for a ChatGPT-on-Mac `Update the legacy documentation` task.

## 2026-09-28 — Move Rotom legacy documentation checkout and refine ChatGPT handoff

- **Files changed:** `00-Rotom-Change-Log.md`, `01-Rotom-Server-Inventory.md`, `06-Maintenance-and-Automation.md`, `08-Rotom-Directory-Tree.txt`.
- **Status:** **Implemented / Documentation only.** Jared reports that the Rotom legacy documentation checkout moved from `/home/infra/documentation/retired-helper` to `/home/infra/documentation/rotom-runbook`. The legacy documentation also adopts an explicit ChatGPT-on-Mac handoff that ends with Jared publishing the delivered files from the Mac checkout.
- **Changes:** Current Rotom Codex/legacy documentation workflow references now use `/home/infra/documentation/rotom-runbook`. Historical entries that recorded `/home/infra/documentation/retired-helper` remain dated evidence rather than being silently rewritten. For ChatGPT on Mac, `Update the legacy documentation` still produces the materially changed replacement files plus the complete legacy documentation ZIP and performs no Git action itself; ChatGPT must now tell Jared to copy the changed files into `/Users/jared/Documents/ChatGPT/rotom-runbook`, manually replace the matching Available Sources files, then run `retired-helper commit "<relevant concise commit message>"`, `retired-helper check`, and `retired-helper push` on the Mac and verify success. Codex on Mac continues to work directly in `/Users/jared/Documents/ChatGPT/rotom-runbook` and Codex on Rotom now works directly in `/home/infra/documentation/rotom-runbook`.
- **Evidence:** User-reported checkout-path change and workflow decision in the current chat; no terminal output was supplied for the renamed Rotom checkout or helper after the move.
- **Outstanding:** Reverify the Rotom checkout, `/home/jared/.codex/AGENTS.md`, and any path-dependent Rotom `/usr/local/bin/retired-helper` helper against `/home/infra/documentation/rotom-runbook` before treating the renamed Rotom path/helper integration as freshly verified. Mac helper revalidation against `/Users/jared/Documents/ChatGPT/rotom-runbook` remains outstanding as already recorded.

## 2026-09-28 — Move Mac legacy documentation checkout to canonical repository directory

- **Files changed:** `00-Rotom-Change-Log.md`, `01-Rotom-Server-Inventory.md`, `06-Maintenance-and-Automation.md`, `08-Rotom-Directory-Tree.txt`.
- **Status:** **Implemented / Documentation only.** Jared reports that the Mac legacy documentation checkout moved from `/Users/jared/Documents/ChatGPT/Rotom-Home-Server` to `/Users/jared/Documents/ChatGPT/rotom-runbook`; this legacy documentation task records that new current path and makes no live Mac, Rotom, GitHub, or Available Sources change.
- **Changes:** Current Mac Codex/legacy documentation workflow references now use `/Users/jared/Documents/ChatGPT/rotom-runbook`. Historical entries and verification evidence that recorded the former `/Users/jared/Documents/ChatGPT/Rotom-Home-Server` checkout are preserved as dated history rather than silently rewritten. The Codex-on-Rotom checkout remains `/home/infra/documentation/retired-helper`, and the ChatGPT-versus-Codex execution policy is otherwise unchanged.
- **Evidence:** User-reported Mac path change in the current chat. No terminal output was supplied in this task to re-run `retired-helper check` against the renamed checkout.
- **Outstanding:** Reverify the Mac `/usr/local/bin/retired-helper` helper against `/Users/jared/Documents/ChatGPT/rotom-runbook` if its repository path is hard-coded or otherwise path-dependent; update the helper if needed before relying on Mac Codex commit/push from the new checkout.

## 2026-09-28 — Adopt environment-specific legacy documentation execution workflow

- **Files changed:** `00-Rotom-Change-Log.md`, `01-Rotom-Server-Inventory.md`, `06-Maintenance-and-Automation.md`, `08-Rotom-Directory-Tree.txt`.
- **Status:** **Documentation only.** The legacy documentation maintenance contract now distinguishes ChatGPT delivery from Codex direct-checkout execution; no live Rotom, Mac, GitHub, or Available Sources change is claimed by this documentation task.
- **Changes:** `Update the legacy documentation` now has three explicit execution modes. ChatGPT on Mac produces changed replacement files plus the complete legacy documentation ZIP for Jared to replace manually and does not commit/push. Codex on Mac updates `/Users/jared/Documents/ChatGPT/Rotom-Home-Server` directly; Codex on Rotom updates `/home/infra/documentation/retired-helper` directly. Both Codex modes finish the final legacy documentation state with `retired-helper commit` using a relevant concise message, `retired-helper check`, then `retired-helper push`, and verify success. Available Sources replacement remains manual in every mode. A revised Rotom `/home/jared/.codex/AGENTS.md` replacement was prepared separately to implement the Rotom-side rule while keeping document 00 canonical.
- **Evidence:** Jared explicitly selected the three-environment workflow in the current chat and supplied the current Rotom `AGENTS.md`; the Mac and Rotom checkout paths are already recorded in the legacy documentation. No helper execution, Git commit/push, agent installation, or Available Sources replacement was performed or verified by this documentation update.
- **Outstanding:** Install/replace the Rotom `AGENTS.md` and verify a fresh Codex session follows it. Rotom `/usr/local/bin/retired-helper` deployment and the final no-confirmation Mac helper revision remain subject to their previously recorded verification gaps until terminal evidence is supplied. If Mac Codex does not already have an instruction file that loads the canonical legacy documentation maintenance contract, add/verify that separately.

## 2026-09-28 — Adopt `retired-helper` helper workflow for routine legacy documentation Git operations

- **Files changed:** `00-Rotom-Change-Log.md`, `01-Rotom-Server-Inventory.md`, `06-Maintenance-and-Automation.md`, `08-Rotom-Directory-Tree.txt`.
- **Status:** **Implemented / Verified on Mac / Proposed / Needs Verification on Rotom / Documentation only.** A single `retired-helper` command namespace was adopted for routine legacy documentation Git operations. The Mac helper is installed and functionally exercised; the final no-confirmation revision and the Rotom-targeted deployment have not yet been reverified from supplied output.
- **Changes:** Adopted the supported interface `retired-helper status`, `retired-helper check`, `retired-helper pull`, `retired-helper diff`, `retired-helper log [N]`, `retired-helper commit "message"`, `retired-helper push`, and `retired-helper help`. The helper disables Git paging with `git --no-pager`; `status` stays local-only; `check` validates repository identity, the tracked core `00`–`08` set, `.DS_Store` state, filesystem access, GitHub reachability, and ahead/behind/divergence; `pull` requires a clean tree and only fast-forwards; `commit` stages all changed, deleted, and new non-ignored legacy documentation files before committing the supplied message; and `push` refuses dirty, behind, or diverged state. The final design deliberately removes Y/N confirmation prompts so the wrapper behaves more like normal Git while retaining legacy documentation-specific guardrails. The verified Mac checkout is `/Users/jared/Documents/ChatGPT/Rotom-Home-Server`; the Rotom-targeted helper uses `/home/infra/documentation/retired-helper` and includes the existing `/home/infra` traversal/access check.
- **Evidence:** Supplied Mac terminal output shows `/usr/local/bin/retired-helper` passed `bash -n`, was installed root-owned/executable, and successfully ran `retired-helper help`, `retired-helper status`, `retired-helper diff`, and `retired-helper check`; the check verified the expected SSH remote, `main`, `origin/main`, all nine core files tracked, no tracked `.DS_Store`, and a successful GitHub fetch. `retired-helper pull` correctly refused while seven intentional legacy documentation files were locally modified. The same output also demonstrates non-paged `retired-helper log`/`retired-helper diff` behavior. No post-change terminal evidence was supplied for the later no-confirmation revision or for the Rotom-targeted helper.
- **Outstanding:** Verify the final no-confirmation helper revision on Mac and install/verify the Rotom-targeted `/usr/local/bin/retired-helper`. Until Rotom verification is supplied, the already-verified Codex pull path remains `git -C /home/infra/documentation/retired-helper pull --ff-only`; after helper verification, update `/home/jared/.codex/AGENTS.md` to use `retired-helper pull`. Also verify an explicit Mac Git `user.name`/`user.email` configuration before relying on `retired-helper commit`; earlier supplied Git output showed an automatically derived commit identity.

## 2026-09-28 — Establish Git-backed legacy documentation checkout and Codex discovery

- **Files changed:** `00-Rotom-Change-Log.md`, `01-Rotom-Server-Inventory.md`, `03-Network-and-Domains.md`, `04-NAS-and-Storage.md`, `06-Maintenance-and-Automation.md`, `07-Users-and-Permissions.md`, `08-Rotom-Directory-Tree.txt`.
- **Status:** **Implemented / Verified / Documentation only.** Rotom now has a Git-backed local legacy documentation checkout and a verified Jared-scoped Codex discovery path. This documentation task records the already-completed live changes and also corrects four current document headers that still used the superseded physical host name `proxmox`; it makes no additional live-system change.
- **Changes:** Installed Debian package `acl`; restored narrow `jared` execute-only traversal on `/home/infra`; configured Jared's general GitHub SSH identity at `~/.ssh/d_ed25519_github` without documenting key material; cloned `git@github.com:jaredwines/rotom-runbook.git` to `/home/infra/documentation/retired-helper`; retained branch `main`; pulled the upstream `.gitignore`/`.DS_Store` cleanup with `--ff-only`; and created `/home/jared/.codex/AGENTS.md` so Codex starts from `01-Rotom-Server-Inventory.md`, reads the relevant legacy documentation, inspects live state before changes, treats the checkout as read-only during normal work, and reports live/legacy documentation discrepancies instead of silently forcing either side to match. `/home/jared/.codex` was tightened to mode `0700` and `AGENTS.md` to `0600`. Codex CLI updated from `0.157.1` to `0.158.0`. Current host labels in documents 03, 04, 06, and 07 were corrected to canonical PVE host `pve`.
- **Evidence:** Supplied Rotom terminal output shows package `acl` installed successfully; final `/home/infra` ACL `user:jared:--x`; `/home/infra/documentation` observed `root:root` mode `0755`; `/home/infra/documentation/retired-helper` observed `jared:infra` mode `0750`; successful GitHub SSH authentication as account `jaredwines`; successful clone and clean `main` working tree tracking the expected SSH remote; successful fast-forward pull that deleted tracked `.DS_Store` and added `.gitignore`; and two fresh Codex sessions, including after upgrade to `0.158.0`, correctly identifying `/home/infra/documentation/retired-helper`, `01-Rotom-Server-Inventory.md`, and the live-vs-legacy documentation discrepancy policy. No secret value or private-key content is recorded.
- **Outstanding:** The older top-level `/home/infra/documentation/AGENTS.md` and `README.md` described in pre-migration evidence were not re-inspected in this task; their current presence/content remains unverified and they are not required by the verified Jared-global Codex workflow. Fran is not recreated/configured for Codex. Jared must manually replace the corresponding Mac-folder and Available Sources copies with this legacy documentation update package.

## 2026-09-27 — mitigate Proxmox Intel I219-V / e1000e transmit hang

- **Files changed:** `00-Rotom-Change-Log.md`, `06-Maintenance-and-Automation.md`.
- **Status:** **Implemented / Verified / Monitoring / Documentation only.** A live and persistent Proxmox NIC workaround was applied after the physical Intel I219-V (`nic0`, `e1000e`) repeatedly reported `Detected Hardware Unit Hang` immediately before the Rotom VM and Proxmox host lost NAS/network reachability. This legacy documentation update records the verified final state and makes no additional live-system change.
- **Changes:** On Proxmox, `ethtool -K nic0 tso off gso off` was applied live and then made persistent by adding `post-up /usr/sbin/ethtool -K nic0 tso off gso off` to the existing `iface nic0 inet manual` stanza in `/etc/network/interfaces`, alongside the existing Wake-on-LAN `post-up /usr/sbin/ethtool -s nic0 wol g`. Pre-change rollback copy `/etc/network/interfaces.pre-e1000e-offload-20260927` was created. GRO, checksum offloads, EEE, bridge configuration, and other NIC features were intentionally left unchanged.
- **Evidence:** The failing boot logged repeated `e1000e 0000:00:1f.6 nic0: Detected Hardware Unit Hang` events from approximately `20:56:04` through the final pre-reboot kernel log at `20:59:46`; during the same interval Proxmox reported `nas-rotom-proxmox-backup` offline and the Rotom guest logged NFS server `192.168.1.70` not responding. After the mitigation, `ethtool -k nic0` reported TSO `off`, GSO `off`, and GRO `on`; `ethtool nic0` reported `1000Mb/s`, full duplex, `Wake-on: g`, and link detected; `ifquery --check nic0` and `ifquery --check vmbr0` passed. Older sampled boots `-2` through `-6` did not show the same transmit-hang signature, and boot `-7` ended with an orderly `systemd-shutdown` sequence.
- **Outstanding:** Treat the NIC workaround as **Implemented / Monitoring**, not a proven permanent fix. The `e1000e` transmit hang is the confirmed cause of the observed network/NFS outage immediately before the reset, but available evidence does not prove that the NIC hang directly caused the subsequent whole-Proxmox-host reboot. After a future normal reboot/power cycle, verify TSO/GSO remain disabled and continue checking the kernel journal for any new `Hardware Unit Hang` or `NETDEV WATCHDOG` events.

## 2026-09-27 — make manual Proxmox VM backup disconnect-safe

- **Files changed:** `00-Rotom-Change-Log.md`, `01-Rotom-Server-Inventory.md`, `04-NAS-and-Storage.md`, `05-Backup-and-Restore.md`, `06-Maintenance-and-Automation.md`, `08-Rotom-Directory-Tree.txt`.
- **Status:** **Implemented / Verified / Documentation only.** The manual whole-VM Proxmox backup path was changed from a foreground SSH-owned `exec vzdump` helper to a fixed systemd-owned manual service while the native `rotom-daily` scheduler, VZDump storage, retention policy, and both Restic layers were left unchanged. This legacy documentation update records the verified final state and makes no additional live-system change.
- **Changes:** `/usr/local/bin/backup-proxmox-to-nas` is now a root-only human launcher that checks `backup-proxmox-manual.service`, refuses to start a second manual backup while the service is active, starts the service with `systemctl start --no-block`, returns the shell promptly, and prints journal/status commands. New root-only worker `/usr/local/sbin/proxmox-vzdump-manual` (`0700`) retains VMID `100`, storage `nas-rotom-proxmox-backup`, snapshot mode, and zstd; it also holds non-blocking `flock` `/run/lock/proxmox-vzdump-manual.lock` as a second duplicate-manual-run guard. New `/etc/systemd/system/backup-proxmox-manual.service` is a manual `Type=oneshot` service using that worker with `Nice=10` and best-effort I/O priority 7; no timer was added. Rollback copy `/usr/local/bin/backup-proxmox-to-nas.pre-systemd.20260927-163449` preserves the previous foreground helper. Native `/etc/pve/jobs.cfg` job `rotom-daily` remains independent at `05:00`, snapshot + zstd, `repeat-missed=0`, retention `7 daily / 4 weekly / 6 monthly`.
- **Evidence:** The first new launcher invocation returned in about `0.042s`; systemd then owned VZDump PID `12067` with PPID `1` while the service remained `activating/start`. A second `backup-proxmox-to-nas` invocation reported that a manual backup was already running and did not create another VZDump. The SSH session was exited and reconnected; the same systemd-owned VZDump PID and its `zstd` child were still running and progress continued. The backup reached 100%, reported `42.31GB`, finished VM 100 in `00:08:40`, ended its PVE task `OK`, and systemd completed with `Result=success`, `ExecMainStatus=0`, `ActiveState=inactive`, `SubState=dead`; no backup processes remained and VM 100 remained `running`. The final observed storage listing contains archive/log pairs for `14_08_51`, `16_01_27`, and the new `16_38_06`. The `14_08_51` archive retains the explicit full `zstd -dc | vma verify -` exit-0 evidence; `16_38_06` has successful VZDump/service-completion evidence but was not separately full-VMA-verified in the supplied output.
- **Outstanding:** The first genuinely scheduler-triggered unattended `rotom-daily` `05:00` run still has not been observed. The `16_01_27` archive is present in the current listing but has no separate full-VMA-verification evidence in this chat. Archive protection/retention policy remains a separate decision; no Restic behavior was changed by this work.

## 2026-09-27 — deploy and verify Proxmox host-configuration Restic backup

- **Files changed:** `00-Rotom-Change-Log.md`, `01-Rotom-Server-Inventory.md`, `03-Network-and-Domains.md`, `04-NAS-and-Storage.md`, `05-Backup-and-Restore.md`, `06-Maintenance-and-Automation.md`, `07-Users-and-Permissions.md`, `08-Rotom-Directory-Tree.txt`.
- **Status:** **Implemented / Verified / Documentation only.** A third current recovery layer was added for Proxmox host configuration/reconstruction data, intentionally separate from guest Restic and whole-VM VZDump. This legacy documentation task records the verified final state and makes no additional live infrastructure change.
- **Changes:** NAS share `Proxmox_Restic_Backup/.data` is exported only to Proxmox `192.168.1.68` and mounted on the host at `/mnt/nas-proxmox-restic-backup` through a Proxmox `/etc/fstab` systemd automount. The encrypted Restic repository is `/mnt/nas-proxmox-restic-backup/proxmox-restic-backup` (repository `8ca0218c64`, format v2). Root-only `/usr/local/sbin/proxmox-restic-backup` rebuilds `/var/backups/proxmox-restic-recovery`, preserves selected Proxmox/network/boot/APT/SSH/systemd/`/usr/local` configuration plus reconstruction inventories, preserves a resolved copy of public `/root/.ssh/authorized_keys`, and deliberately excludes `/etc/pve/priv`, private `*.key` material, `/etc/restic/nas-password`, SSH private keys, VM disks, VZDump archives, and mounted NAS data. Manual operator command `/usr/local/bin/backup-restic-to-nas` runs the implementation directly so Restic output remains visible in the terminal. `proxmox-restic-backup.service` runs the same implementation with `HOME=/root`; `proxmox-restic-backup.timer` is enabled/active for daily `04:00`, `Persistent=true`, `AccuracySec=1min`. Retention is `7 daily / 4 weekly / 12 monthly`. Post-reboot testing exposed that the autofs trigger could exist without the underlying NFS mount, so the script now performs `timeout 35s ls -A` on the mount before its NFS/exact-source guard; the corrected manual path then triggered NFS and completed successfully from an initial autofs-only state.
- **Evidence:** The new UNAS export appeared in `showmount` restricted to `192.168.1.68`; the NFSv3 mount passed write/read/delete testing. `restic init` created repository `8ca0218c64`; initial `restic check` returned no errors. First snapshot `0cf1c62a` was created successfully, and an isolated restore recovered 284 files/directories; required PVE/network/scripts/inventory files were present, representative files compared identical, `/etc/pve/priv` and the Restic password were absent, and the restore scratch directory was removed. Service execution later returned `Result=success` / `ExecMainStatus=0`; adding `HOME=/root` removed the Restic cache warning. Final interactive execution created snapshot `a59fc03f` at `2026-09-27 15:57:03 PDT`, completed retention/prune, retained `0cf1c62a` plus `a59fc03f`, and removed redundant same-day snapshot `b1920314`. VMID 100 remained running and native PVE job `rotom-daily` remained unchanged at `05:00`.
- **Outstanding:** The first genuinely timer-triggered unattended `proxmox-restic-backup.timer` run at `04:00` has not yet been observed. Guest Restic and PVE `rotom-daily` first-unattended-run observations remain separate open checks. Off-site/failure-domain protection remains future recovery-policy work because all current NAS backup layers terminate on the same UNAS appliance.

## 2026-09-27 — enable persistent Proxmox Wake-on-LAN and verify power-cycle recovery

- **Files changed:** `00-Rotom-Change-Log.md`, `01-Rotom-Server-Inventory.md`, `02-Docker-Services.md`, `03-Network-and-Domains.md`, `04-NAS-and-Storage.md`, `06-Maintenance-and-Automation.md`, `08-Rotom-Directory-Tree.txt`.
- **Status:** **Implemented / Verified / Documentation only.** The live change made Proxmox Wake-on-LAN persistent on the physical NUC NIC and then exercised a complete host power-off/return cycle. This legacy documentation task records that verified state and makes no additional live infrastructure change.
- **Changes:** On Proxmox, physical `nic0` (Intel I219-V / `e1000e`, MAC `1c:69:7a:0e:f2:f7`) already reported `Supports Wake-on: pumbg`, `Wake-on: g`, and PCI power wake `enabled`. `/etc/network/interfaces` was backed up to `/etc/network/interfaces.pre-wol`, then the existing `iface nic0 inet manual` stanza gained `post-up /usr/sbin/ethtool -s nic0 wol g` so magic-packet WOL is reasserted whenever the interface is brought up. No bridge addressing, `vmbr0` membership, gateway, DNS, or VM network identity changed. A physical `systemctl poweroff` was then performed; after the host returned, Proxmox again reported `Wake-on: g`, VMID `100` was `running`, and `onboot: 1` remained set. The Rotom guest initially exposed transient failed `nas-downloaders`, `nas-game`, and `nas-media` mount units with only the 11 non-NAS-dependent containers running; the existing `rotom-nas-docker-recovery.service` then completed successfully and restored qBittorrentVPN, Radarr, Sonarr, Gamarr, and Jellyfin. Final guest state returned to zero failed systemd units and the exact 16-container production set.
- **Evidence:** `ifquery --check nic0` and `ifquery --check vmbr0` both passed with the new `post-up` line present; pre- and post-cycle `ethtool nic0` reported `Supports Wake-on: pumbg` / `Wake-on: g`. Post-return `qm status 100` reported `running` and `qm config 100` showed `onboot: 1`. Final Rotom verification showed `systemctl --failed` at zero, all 16 expected containers running, qBittorrentVPN `wg0` up at `10.2.0.2/32`, and genuine NFSv3 mounts for `/mnt/nas-downloaders` from `Downloader/.data`, `/mnt/nas-media` from `Media/.data`, and `/mnt/nas-game` from `Game/.data`. `rotom-nas-docker-recovery.service` ended `active (exited)` with status `0/SUCCESS` after logging recovery of the affected NAS-backed services.
- **Outstanding:** The supplied transcript proves persistent host-side WOL configuration and a successful physical power-cycle recovery, but it does **not** include a captured magic-packet sender invocation or otherwise prove that the NUC's return from the powered-off state was caused by Wake-on-LAN rather than another power-on method. End-to-end magic-packet wake therefore remains **Needs Verification**.

## 2026-09-27 — centralize and simplify legacy documentation maintenance governance

- **Files changed:** `00-Rotom-Change-Log.md`, `01-Rotom-Server-Inventory.md`, `06-Maintenance-and-Automation.md`, `07-Users-and-Permissions.md`.
- **Status:** **Documentation only.** No Rotom, Proxmox, Docker, NAS, networking, application, backup, or other live infrastructure state was changed.
- **Changes:** Made this file the sole canonical legacy documentation maintenance contract; replaced the former long-form documentation-update commands with the single canonical command `Update the legacy documentation`; defined that command around the final supported state established in the current chat; excluded superseded ideas, abandoned approaches, failed experiments, suggested-but-unrun commands, and temporary troubleshooting states unless they retain lasting historical, recovery, or diagnostic value; added a complete-legacy documentation contradiction check; retained the documentation-only authorization boundary; and changed delivery to materially changed files individually plus one ZIP containing the complete current legacy documentation set. `01-Rotom-Server-Inventory.md` now limits itself to legacy documentation membership/source mapping with a short pointer here, `06-Maintenance-and-Automation.md` no longer duplicates the maintenance contract, and the stale `07-Users-and-Permissions.md` maintenance cross-reference now points to `00`. Earlier changelog entries retain their original wording as historical evidence.
- **Evidence:** Explicit user decision in this chat plus a cross-document review of the current nine-file Available Sources set for maintenance-governance duplication and references. No live-system verification was required because this is a documentation-governance change only.
- **Outstanding:** Jared must manually replace the corresponding changed Available Sources/Mac-folder copies and the complete packaged set as appropriate. No live-system follow-up is created by this governance change.

## 2026-09-21 — Standardize dated legacy documentation ZIP filename

- **Files changed:** `00-Rotom-Change-Log.md`, `01-Rotom-Server-Inventory.md`, `06-Maintenance-and-Automation.md`.
- **Status:** **Documentation only / Adopted.** No live Rotom service, Docker container, NAS export, mount, account, permission, backup job, firewall rule, or application data was changed.
- **Changes:** Standardized the complete legacy documentation package filename as **`Rotom-Support-YYYY-MM-DD.zip`**, using the documentation-update date in Rotom's `America/Los_Angeles` project timezone. Individual legacy documentation filenames remain unchanged. Future canonical legacy documentation updates should use the dated ZIP filename instead of an undated `Rotom-Runbook.zip`.
- **Evidence:** Explicit user decision in this chat after the 2026-09-21 legacy documentation package was renamed to `Rotom-Runbook-2026-09-21.zip`.
- **Outstanding:** None.

## 2026-09-20 — Remove three non-numbered standards from Available Sources

- **Files changed:** `00-Rotom-Change-Log.md`, `01-Rotom-Server-Inventory.md`, `06-Maintenance-and-Automation.md`, `08-Rotom-Directory-Tree.txt`.
- **Status:** Documentation only. No live Rotom service, container, NAS export, mount, account, permission, network, proxy, backup job, automation, application data, derived Guide PDF, or derived Manual PDF was changed.
- **Changes:** Recorded the user's removal of `Rotom-Architecture-and-Deployment-Standard.md`, `Rotom-Home-Server-Guide-Maintenance.md`, and `Rotom-Home-Server-Manual-Maintenance.md` from the project's Available Sources. Because Available Sources defines legacy documentation set membership, the current maintained set is now exactly the nine-file Core Numbered Reference Set (`00`–`08`). Updated the current source map and documentation-workflow references accordingly. Historical change-log entries that mention the removed files or earlier 10/11/12-file source sets remain unchanged as historical records and are not current membership claims.
- **Evidence:** Explicit user statement in this chat that all three files were removed from legacy documentation set / Available Sources, followed by a cross-document review of the current numbered source set for current-state membership references. No live Rotom verification was required.
- **Outstanding:** The replacement `00`–`08` files still need to be installed in the user's normal Mac/Available Sources copies. The three removed files should remain outside Available Sources unless a future explicit decision adds them back.

## 2026-09-19 — Apply canonical fact-ownership documentation restructure

- **Files changed:** `00-Rotom-Change-Log.md`, `01-Rotom-Server-Inventory.md`, `02-Docker-Services.md`, `03-Network-and-Domains.md`, `04-NAS-and-Storage.md`, `05-Backup-and-Restore.md`, `06-Maintenance-and-Automation.md`, `07-Users-and-Permissions.md`, `08-Rotom-Directory-Tree.txt`, `Rotom-Architecture-and-Deployment-Standard.md`, `Rotom-Home-Server-Guide-Maintenance.md`, `Rotom-Home-Server-Manual-Maintenance.md`.
- **Status:** Documentation only. No live Rotom service, container, NAS export, mount, account, permission, network, proxy, backup job, automation, or application data was changed.
- **Changes:** Applied the accepted documentation-architecture design while preserving the `00`–`08` filenames and governance-file roles. Added compact document-role metadata, made canonical fact ownership explicit, reorganized current state ahead of historical material where needed, added reconstruction-critical and related-document sections, separated current/proposed/Needs Verification annotations in the directory-tree reference, and updated Guide/Manual/architecture-standard source-consumption rules to use the canonical subject documents rather than competing duplicated detail. Historical change-log entries were preserved.
- **Evidence:** Content-preserving migration of the complete current Available Sources set against `Rotom-Runbook-Restructure-Design.md`, followed by filename/link, source-membership, and semantic preservation checks. Existing Rotom-specific facts were not replaced with outside knowledge.
- **Factual corrections:** None discovered that required changing the recorded live Rotom state. Existing unresolved items remain Needs Verification or retain their prior evidence qualification.
- **Outstanding:** The restructure changes documentation organization only. Future edits should update the canonical subject file first, then only necessary contextual/index references plus this change log.

## 2026-09-19 — Make Guide diagram centering and arrow routing deterministic

- **Files changed:** `00-Rotom-Change-Log.md`, `Rotom-Home-Server-Guide-Maintenance.md`.
- **Status:** Documentation/governance refinement only; no live Rotom service, Docker container, NAS export, mount, backup job, account, network, proxy, storage configuration, or production Guide PDF was changed by this task.
- **Changes:** Strengthened the Guide diagram standard after review of the generated PDF showed two repeatable failures: text inside diagram bubbles/nodes could render visibly off-center, and some arrowheads could point in the wrong semantic direction. Node labels must now be laid out inside an inner label frame derived from the same final node bounds, with true two-axis centering; HTML/CSS generation should use a flex-style centering model, while SVG text must use a matching `foreignObject` label frame or measured rendered text bounds rather than baseline/`y`/`dy` placement. Connector geometry must now start from an explicit `source -> destination` relationship, choose source/destination edges from relative node position, recompute attachment points after node growth, place ordinary arrowheads at the destination end only, and use destination arrowheads on each branch of one-to-many flows. Added semantic-arrow QA, border/clearance checks, and corresponding Definition-of-Done requirements.
- **Evidence:** User review of the regenerated `Rotom-Home-Server-Guide.pdf` in this chat identified visibly misaligned bubble text and misdirected arrows. Review of the current maintenance standard showed that it required visual centering and general arrow consistency but did not define a deterministic construction algorithm for label frames, source/destination direction, attachment edges, or branch arrowheads. This is presentation/governance evidence, not live-system evidence.
- **Outstanding:** The production `Rotom-Home-Server-Guide.pdf` was not regenerated in this standards-only task. The next Guide regeneration should apply these deterministic node/connector rules and visually inspect every major diagram.

## 2026-09-19 — Reorder Guide for identity-first infrastructure and final documentation appendix

- **Files changed:** `00-Rotom-Change-Log.md`, `Rotom-Home-Server-Guide-Maintenance.md`; derived artifact `Rotom-Home-Server-Guide.pdf` regenerated with the same permanent filename.
- **Status:** Documentation/presentation reorganization only; no live Rotom service, Docker container, NAS export, mount, backup job, account, network, proxy, storage configuration, or application data was changed.
- **Changes:** Reordered the Guide so the reader moves from **System Overview** into **Identity & Infrastructure** before networking/storage details. The two-page **Rotom Linux Users** section now follows **Workload Ownership**, making the account model and `sudo -iu` administration workflow available before the infrastructure chapters that depend on those identities. Network, Docker, storage, Media/Game flows, backup, automation, status, and the Docker catalog follow in their existing logical sequence. **legacy documentation set & ChatGPT** is now the sole **Part V / Documentation Appendix** and is the final substantive section on pages 19–20. The Table of Contents, internal link destinations, page-level part eyebrows, preferred 20-page pacing map, workflow, appendix/section placement rules, and Definition of Done were updated to match.
- **Evidence:** Direct regeneration and inspection of the 20-page Guide in this chat, including the grouped page-2 Table of Contents and the reordered page sequence. This is presentation/governance evidence, not live-system evidence.
- **Outstanding:** None created by this reorganization. Future Guide regenerations should preserve the new order unless a later approved maintenance-standard change supersedes it.

## 2026-09-19 — Synchronize Guide maintenance standard with five-part PDF organization

- **Files changed:** `00-Rotom-Change-Log.md`, `Rotom-Home-Server-Guide-Maintenance.md`.
- **Status:** Documentation/governance synchronization; the production `Rotom-Home-Server-Guide.pdf` had already been reorganized in this chat. No live Rotom service, Docker container, NAS export, mount, backup job, account, network, proxy, storage configuration, or application data was changed by this documentation task.
- **Changes:** Updated the Guide maintenance standard to make the accepted five-part PDF organization a maintained rule: **Part I / System Overview**, **Part II / Infrastructure**, **Part III / Data Flows & Protection**, **Part IV / Status & Reference**, and **Part V / Appendices**. The standard now requires those exact group labels in the Table of Contents, matching part labels in substantive page eyebrows, no standalone part-divider pages, the corresponding 20-page pacing map, and QA/workflow checks that preserve the five-part grouping and navigation. It also explicitly replaces the older generic `ARCHITECTURE / REFERENCE / REQUIRED END MATTER` TOC grouping.
- **Evidence:** Direct inspection of the finished `Rotom-Home-Server-Guide.pdf` produced in this chat, including its page-2 grouped Table of Contents and the matching part labels on pages 3–20. This is presentation/governance evidence, not live-system evidence.
- **Outstanding:** None created by this synchronization. Future Guide regeneration should preserve the five-part organization unless a later approved maintenance-standard change supersedes it.

## 2026-09-19 — Lock Guide typography to the accepted old PDF

- **Files changed:** `00-Rotom-Change-Log.md`, `Rotom-Home-Server-Guide-Maintenance.md`.
- **Status:** Documentation/governance refinement only; no live Rotom service, Docker container, NAS export, mount, backup job, account, network, proxy, storage configuration, or production Guide PDF was changed by this task.
- **Changes:** Tightened the Guide typography standard so future regenerations match the accepted historical PDF by semantic role instead of using a looser small-text range. The standard now explicitly locks Arimo/Cousine Regular and Bold faces, upright style, CSS-equivalent weights 400/700, measured role-specific point sizes for ordinary paragraphs, card copy, callouts, tables, diagram labels, Docker Catalog cards, Project Documentation cards, commands, state pills, cover text, and footer text. It prohibits synthesized medium/semibold weights, italics, visible fallback families, global shrink-to-fit, and use of `6.05–6.45 pt` as an alternate general body scale. It also adds a ±0.05 pt role-size tolerance and requires extracted-font-span QA on the finished PDF.
- **Evidence:** Direct comparison of the user-supplied `Rotom-Home-Server-Guide(old).pdf` with the current generated `Rotom-Home-Server-Guide.pdf`. The old PDF embeds Arimo, Arimo-Bold, Cousine, and Cousine-Bold and uses the measured reference hierarchy now recorded in the Guide maintenance standard; the newer PDF retained the families but reduced ordinary page copy on several pages into smaller `6.2–6.45 pt` treatments. This is presentation/governance evidence, not live-system evidence.
- **Outstanding:** `Rotom-Home-Server-Guide.pdf` was not regenerated by this standards-only task. The next Guide regeneration should use the revised typography lock and compare representative finished-PDF spans against the accepted old PDF before delivery.

## 2026-09-19 — Establish evolving Manual visual design system

- **Files changed:** `00-Rotom-Change-Log.md`, `Rotom-Home-Server-Manual-Maintenance.md`.
- **Status:** Documentation/governance refinement only; no live Rotom service, Docker container, NAS export, mount, backup job, account, network, proxy, storage configuration, or derived PDF was changed by this task.
- **Changes:** Reworked the Manual presentation standard into an explicitly evolving visual design system. Established `MVS-1 — Technical Editorial / Navy + Teal` as the current baseline; added semantic color tokens, evidence-state styling, preferred typography, responsive type/spacing/page-grid guidance, cover and chapter grammar, table/card/callout standards, diagram integration, code/identifier treatment, TOC/navigation styling, page furniture, accessibility/print behavior, and a formal Visual Evolution Workflow. Added a Manual Visual System revision field to document control and expanded regeneration/Definition-of-Done rules so small visual corrections may refine the active revision while material changes to palette, typography, page grammar, cover language, card language, diagram language, or overall visual identity advance the MVS revision and supersede conflicting rules. The standard now explicitly favors controlled visual evolution over permanent pixel-level freezing.
- **Evidence:** User request in this chat to make the Manual maintenance file define a polished visual standard that can change over time, plus review of the existing Manual diagram, presentation, pagination, and Visual Correction Feedback Loop sections. This is presentation/governance evidence, not live-system evidence.
- **Outstanding:** `Rotom-Home-Server-Manual.pdf` was not regenerated as part of this standards-only change. The next Manual regeneration should apply `MVS-1` unless a newer visual revision is intentionally adopted first.

## 2026-09-19 — Require two-axis centering for Guide diagram labels

- **Files changed:** `00-Rotom-Change-Log.md`, `Rotom-Home-Server-Guide-Maintenance.md`.
- **Status:** Documentation/governance refinement only; no live Rotom service, container, NAS, mount, backup, account, network, proxy, storage configuration, or production Guide PDF was changed by this task.
- **Changes:** Strengthened the Guide visual standard after review of the generated PDF exposed bubble/node labels that were visibly out of line. Diagram labels must now be visually centered both horizontally and vertically as complete rendered text blocks; multiline labels must use balanced internal whitespace; node height must grow rather than pushing text off center; one-off baseline/`y`/`dy` nudges are disallowed as a general layout method; and rendered-PDF visual QA must reject labels that visibly ride high, low, left, or right. The component micro-geometry tokens, adaptive layout rules, page-by-page QA checklist, optical-alignment section, and Definition of Done were updated so the requirement is enforced throughout future regenerations.
- **Evidence:** User review of the current generated `Rotom-Home-Server-Guide.pdf` identified visibly misaligned text inside diagram bubbles/nodes. This is presentation/governance evidence, not a new live-system fact.
- **Outstanding:** The production `Rotom-Home-Server-Guide.pdf` was not regenerated in this documentation-only task; the revised standard governs the next regeneration.

## 2026-09-19 — Consolidate Guide visual history and clarify Shared Drive tree

- **Files changed:** `00-Rotom-Change-Log.md`, `08-Rotom-Directory-Tree.txt`.
- **Status:** Documentation cleanup only; no live Rotom service, container, NAS, mount, backup, account, network, proxy, storage configuration, Guide standard, or derived PDF was changed by this cleanup.
- **Changes:** Consolidated four adjacent same-task Guide visual-standard entries into the single historical summary immediately below so the change log follows its own rule to combine related work without losing substantive design decisions or measurement evidence. Added current `/mnt/nas-shared-drive` to the main `/mnt` topology in `08-Rotom-Directory-Tree.txt`; its displayed `Important` and `rotom` child names remain explicitly historical captured contents rather than a claim that those names are continuously current.
- **Evidence:** Cross-document consistency audit of the current twelve-file replacement set. `04-NAS-and-Storage.md` and the later Shared Drive section of `08-Rotom-Directory-Tree.txt` already record `/mnt/nas-shared-drive` as a current fstab-backed systemd automount with live NFSv3 verified on 2026-09-19. The four consolidated Guide entries all described successive refinements from the same accepted 20-page PDF design task on 2026-09-19.
- **Outstanding:** No new live-server verification was performed. The directory tree remains a preserved observed baseline plus targeted verified additions, not a continuously refreshed full filesystem scan. The production `Rotom-Home-Server-Guide.pdf` still requires separate regeneration if the preferred visual standard is to become the current production PDF.

## 2026-09-19 — Finalize Guide visual baseline and responsive design system

- **Files changed:** `00-Rotom-Change-Log.md`, `Rotom-Home-Server-Guide-Maintenance.md`.
- **Status:** Documentation/governance refinement only; no live Rotom service, container, NAS, mount, backup, account, network, proxy, storage configuration, or derived PDF was changed by this design-standard work.
- **Changes:** Consolidates the previously separate same-task entries for adopting the user-preferred 20-page editorial Guide, converting it into a deterministic measured production standard, adding responsive micro-geometry tokens, and locking the remaining reusable visual components. The maintenance standard preserves the US-Letter page model; dark navy/teal editorial cover; embedded Arimo/Cousine typography; `41.76–570.24 pt` body grid; measured title/footer hierarchy and palette; grouped TOC; spacious architecture-first pages; grid-based cards, callouts, diagrams, and orthogonal teal connectors; two-column Docker Container Catalog; two-page Project Documentation appendix; two-page Linux Users ending; preferred 20-page pacing; explicit do-not-drift/redesign rules; and visual-regression QA. Responsive tokens fix reusable spacing, line pitch, borders, radii, insets, connector/arrowhead geometry, catalog/source-card geometry, workload chips, state pills, diagram panels/nodes, TOC rules, and cover geometry while allowing content to wrap, grow vertically, reflow diagrams, or add pages instead of shrinking the design system. Final production output requires embedded Arimo/Cousine; catalog RUNNING/HEALTHY and STOPPED/EXITED pills preserve their measured treatments; TOC leaders are measured solid rules rather than dotted leaders; and the cover uses the locked upper-left-to-lower-right gradient recipe.
- **Evidence:** User comparison and preference in this chat plus direct measurement and visual review of the accepted `Rotom-Home-Server-Guide(old).pdf`. Recorded measurements include `612 × 792 pt` page size; `0.75 pt` card/table borders; `6.75 pt` standard card radius; `5.25 pt` source-card radius/gap; `3.75 pt` callout radius; `2.2 pt` diagram connectors with approximately `13.16 × 13.15 pt` arrowheads; `8.781 pt` state-pill height; `12.45 pt` workload-chip height with `#D5E0EA` border; diagram panel approximately `#F9FCFE`/`#E0E7EF`; primary Rotom node `#EEFAF7`/`#29B79F`; RUNNING/HEALTHY pill `#EAF8F4`/`#147562`; STOPPED/EXITED pill `#FCEBED`/`#A3414B`; TOC leader `#A8B6C5` with `5.25 pt` label/page-number gaps and `#E7EDF3` row rules; clipped `319.8 pt` cover ring; and cover corner checkpoints approximately `#08111F`, `#0D1D34`, `#112940`, and `#143A42`. This is presentation/governance evidence, not live-system evidence.
- **Outstanding:** The production `Rotom-Home-Server-Guide.pdf` was not regenerated as part of the design-standard work. Future regeneration should apply the locked visual system while allowing current Rotom content to reflow or add pages as needed.

## 2026-09-19 — Harden Guide structure, diagram, and PDF navigation standards

- **Files changed:** `00-Rotom-Change-Log.md`, `Rotom-Home-Server-Guide-Maintenance.md`.
- **Status:** Documentation/governance improvement only; no live Rotom service, Docker container, NAS export, mount, backup job, account, network, proxy, storage configuration, or derived PDF content was changed by this task.
- **Changes:** Incorporated the repeatable lessons from refining the current Guide: required an architecture-first section order; made a near-front Table of Contents with verified internal PDF links and final-page-number matching mandatory; formalized a complete Docker Container Catalog using consistent **Function / Method / Purpose** descriptions; standardized connector/arrow styling, explicit grid-based diagram geometry, connector-label spacing, and optical alignment; strengthened full-page visual QA and finished-PDF navigation QA; and required major structural/visual changes to be regenerated cleanly so successful corrections become maintained Guide design language rather than one-off PDF patches. Preserved the Guide/Manual boundary and the existing required end-matter order.
- **Evidence:** User decision in this chat after reviewing and refining the current derived Guide, plus a full review of the existing `Rotom-Home-Server-Guide-Maintenance.md` to consolidate the new rules into its existing role, workflow, content-priority, diagram, appendix-source-map, regeneration, and Definition-of-Done sections. No live Rotom verification was required.
- **Outstanding:** None created by this governance change. `Rotom-Home-Server-Guide.pdf` was intentionally not modified by this task; the updated standard governs future Guide regeneration. Existing unrelated operational verification gaps remain unchanged.

## 2026-09-19 — Add manual diagram geometry and visual-correction feedback standards

- **Files changed:** `00-Rotom-Change-Log.md`, `Rotom-Home-Server-Manual-Maintenance.md`.
- **Status:** Documentation only; no live Rotom service, Docker container, NAS export, mount, backup job, account, network, proxy, storage configuration, or derived PDF content was changed by this documentation task.
- **Changes:** Added a reusable Diagram Geometry and Connector Standard requiring visually centered node/bubble text, balanced multiline padding, consistent node alignment, and one uniform arrow/connector system for shaft weight, arrowheads, endpoint spacing, attachment points, bends, and relationship semantics. Added a Visual Correction Feedback Loop requiring accepted repeatable PDF presentation corrections to be generalized into `Rotom-Home-Server-Manual-Maintenance.md`, applied across the full manual, re-rendered and visually checked, and recorded in the change log rather than remaining one-off PDF fixes. Updated the recommended regeneration guidance and Definition of Done so this feedback loop is mandatory for future manual revisions.
- **Evidence:** User decision in this chat after reviewing the regenerated manual and correcting misaligned diagram bubble text and inconsistent arrows. This entry records the adopted maintenance/design rule; it does not assert a new live Rotom configuration fact.
- **Outstanding:** None created by this documentation change. Future manual regenerations should apply these standards and capture any additional repeatable presentation lessons through the same feedback loop.

## 2026-09-19 — Final strict-audit documentation fixes

- **Files changed:** `00-Rotom-Change-Log.md`, `01-Rotom-Server-Inventory.md`, `05-Backup-and-Restore.md`, `08-Rotom-Directory-Tree.txt`.
- **Status:** Documentation correction only; no live Rotom service, Docker container, NAS export, mount, backup job, account, network, proxy, or storage configuration was changed by this task.
- **Changes:** Corrected the remaining Homebridge backup-summary wording so only the known corrected `/home` files are asserted to be within normal Restic scope; the associated verification record's path and backup coverage remain unknown. Changed the later backup summary to describe all NAS source data under `/mnt`—including Media, Game, Shared Drive, and the backup mount itself—as outside the host Restic source scope rather than mentioning only Media/Game. Updated the inventory quick-reference description of `/home/rotom/documentation` so it is clearly the authoritative on-server Codex/control-document location, while Available Sources remains the membership boundary for legacy documentation set. Reconciled `08-Rotom-Directory-Tree.txt` with the current twelve-file governance model: none of the twelve Project Documentation files are deployed under `/home/rotom/documentation`, and `AGENTS.md`/`README.md` are separate on-server control/index files.
- **Evidence:** Final strict cross-document audit of the current twelve-file source set using the already recorded 2026-09-19 server, NFS, backup, Homebridge, and governance evidence. No new live Rotom verification was required.
- **Outstanding:** A post-Homebridge Restic snapshot containing the corrected Homebridge Compose file and `/home/jared/rotom-manual-verify.sh` has not yet been documented or path-verified. The associated verification record's storage path remains unspecified, so its backup coverage is unknown. Existing unrelated operational verification gaps remain unchanged.

## 2026-09-19 — Correct NFS summary and post-Homebridge backup wording

- **Files changed:** `00-Rotom-Change-Log.md`, `01-Rotom-Server-Inventory.md`, `02-Docker-Services.md`, `04-NAS-and-Storage.md`, `05-Backup-and-Restore.md`, `06-Maintenance-and-Automation.md`, `07-Users-and-Permissions.md`, `Rotom-Home-Server-Manual-Maintenance.md`.
- **Status:** Documentation correction only; no live Rotom service, Docker container, NAS export, mount, backup job, account, network, or proxy configuration was changed by this task.
- **Changes:** Updated the current NFS summaries to reflect the final 2026-09-19 verification that Media, Game, Backup, and Shared Drive all use NFSv3 with `sec=sys`. Clarified that Restic snapshot `f0d51eaa` at `2026-09-19 06:39:30 PDT` is the **latest verified snapshot in the documentation**, not proof of backup coverage for changes made later that day. The Homebridge Compose correction and `/home/jared/rotom-manual-verify.sh` change are within the normal `/home` Restic include scope, but the path of the associated verification record was not supplied and its backup scope should not be assumed. No post-change snapshot containing the known corrected `/home` files has yet been documented or path-verified. This supersedes the earlier Homebridge change-log entry's `Outstanding: None` wording only with respect to post-change backup verification; the Homebridge functional correction itself remains verified. Replaced the nonportable `chatgpt-conversation://` links with plain-text historical evidence references. A second consistency pass also corrected remaining `Current snapshot` wording in maintenance summaries, added the post-Homebridge backup-verification gap to the consolidated backup/verification sections, and brought `07-Users-and-Permissions.md` into line with the final four-mount NFSv3 evidence while preserving the fact that Shared Drive's detailed permission model remains unverified. A third pass corrected the remaining top-level `current path-verified snapshot` labels, clarified that `restic ls latest` referred to the snapshot that was latest at verification time, and restored Glances to the `rotom` account's complete current workload list in the permissions document. A fourth pass removed the unsupported assumption that the unspecified Homebridge verification-record path is covered by `/home`; only the known Compose file and `/home/jared/rotom-manual-verify.sh` are asserted to be in normal Restic scope. A fifth pass clarified the Manual-maintenance wording around the historical `/data` Media root so it cannot be misread as invalidating Jellyfin's current `/data/library` read-only mapping. A sixth pass narrowed the Backup document's opening verification claim so it distinguishes verified backup scope/path coverage through `f0d51eaa` from the still-unverified post-Homebridge snapshot state. A seventh pass removed one remaining shorthand phrase that could still imply the unspecified verification record is under `/home`; only the known Compose file and `/home/jared/rotom-manual-verify.sh` are asserted to be in normal Restic scope.
- **Evidence:** Existing final 2026-09-19 NFS verification recorded in `04-NAS-and-Storage.md`; documented Restic snapshot timestamp and coverage; and the later-in-day Homebridge correction evidence supplied by the user. No new backup run or live NFS check was performed.
- **Outstanding:** Run the normal Rotom backup and verify a resulting snapshot contains the corrected Homebridge Compose configuration and `/home/jared/rotom-manual-verify.sh` if a documented post-change recovery point is desired. If backup coverage of the associated verification record matters, first identify its path rather than assuming it is under `/home`. Existing unrelated operational verification gaps remain unchanged.

## 2026-09-19 — Final documentation consistency cleanup after Homebridge rename

- **Files changed:** `00-Rotom-Change-Log.md`, `01-Rotom-Server-Inventory.md`, `02-Docker-Services.md`, `03-Network-and-Domains.md`, `04-NAS-and-Storage.md`, `06-Maintenance-and-Automation.md`.
- **Status:** Documentation correction only; no live Rotom service, Docker container, NAS export, mount, network, backup, account, or proxy configuration was changed by this task.
- **Changes:** Added the previously omitted Radarr `172.18.0.0/16` bridge network to the current network summaries in the server inventory and Docker inventory. Refreshed the Docker, networking, and maintenance document update summaries to include the verified Homebridge `homebrige` → `homebridge` correction. Clarified the distinction between `/home/rotom/documentation` as the authoritative on-server Codex/control-document location and Available Sources as the membership boundary for legacy documentation set. Corrected the historical Shared Drive wording so its capacity figures are explicitly described as observations from the 2026-09-15 audit rather than current overview values. Also updated the documentation-definition paragraph in the server inventory to include the current Manual Maintenance standard in the non-numbered Project Documentation set.
- **Evidence:** Cross-document consistency review of the then-current twelve-file legacy documentation set, using the already recorded 2026-09-19 network and Homebridge verification evidence. No new live verification was required.
- **Outstanding:** None created by this cleanup. Existing unrelated operational verification gaps remain unchanged.

## 2026-09-19 — Correct Homebridge container-name typo

- **Files changed:** `00-Rotom-Change-Log.md`, `01-Rotom-Server-Inventory.md`, `02-Docker-Services.md`, `03-Network-and-Domains.md`, `06-Maintenance-and-Automation.md`.
- **Status:** Implemented and verified. The live Homebridge configuration was changed; no other Rotom service architecture, storage, networking, account, backup, or proxy configuration was intentionally changed.
- **Changes:** Corrected the Homebridge Docker container name from the historical misspelling `homebrige` to `homebridge` in `/home/smart-home/docker/homebridge/compose.yaml`. Updated `/home/jared/rotom-manual-verify.sh` and its associated verification record to use the corrected name. Homepage required no configuration change because its existing Homebridge service configuration was already correct and Docker discovery uses the socket. A whole-home scan found no remaining `homebrige` references. Homebridge started successfully after the change and restored its cached accessories.
- **Evidence:** User-supplied Codex completion output from Rotom reporting the Compose edit, verification-script/record update, whole-home reference scan, successful Homebridge startup, and cached-accessory restoration.
- **Outstanding:** None for the container-name correction. Existing unrelated verification gaps remain unchanged.

## 2026-09-19 — Confirm the 12-file source set and correct documentation-maintenance inconsistencies

- **Files changed:** `00-Rotom-Change-Log.md`, `01-Rotom-Server-Inventory.md`, `06-Maintenance-and-Automation.md`, `Rotom-Home-Server-Guide-Maintenance.md`, `Rotom-Home-Server-Manual-Maintenance.md`.
- **Status:** Documentation/governance correction only; no live Rotom service, Docker container, NAS export, mount, network, backup, account, or other server state was changed.
- **Changes:** Confirmed that the current Project-backed Available Sources set now contains twelve legacy documentation set files, including `Rotom-Home-Server-Manual-Maintenance.md`. Removed adoption-era wording that still described the Manual Maintenance standard as pending. Corrected the inventory's local-hostname/FQDN wording and its summary of legacy NPM database records. Clarified that none of the twelve Project Documentation files are currently deployed under `/home/rotom/documentation`, where only `AGENTS.md` and `README.md` were verified. Updated the Guide source-map wording to treat the twelve-file set as current. Corrected the Manual maintenance standard's source-authority wording, Game/Gamarr executive representation, Media/Jellyfin path diagram, disaster-recovery numbering, future-architecture evidence terminology, and Appendix L requirement.
- **Evidence:** Current Project-backed Available Sources membership in this project; cross-document consistency review against `01-Rotom-Server-Inventory.md`, `03-Network-and-Domains.md`, `04-NAS-and-Storage.md`, `06-Maintenance-and-Automation.md`, and both maintenance standards. No additional live Rotom verification was required because these corrections reconcile already documented evidence and governance.
- **Outstanding:** `Rotom-Home-Server-Guide.pdf` and `Rotom-Home-Server-Manual.pdf` are derived artifacts and were not regenerated by this documentation-only correction. Existing operational verification gaps remain unchanged.

## 2026-09-19 — Add Home Server Manual maintenance standard to Project Documentation

- **Files changed:** `00-Rotom-Change-Log.md`, `01-Rotom-Server-Inventory.md`, `06-Maintenance-and-Automation.md`, `Rotom-Home-Server-Guide-Maintenance.md`; new Project Documentation file `Rotom-Home-Server-Manual-Maintenance.md`.
- **Status:** Documentation/governance update only; no live Rotom service, Docker container, NAS export, mount, network, backup, account, or other server state was changed.
- **Changes:** Replaced the former one-off `Rotom-Systems-Architecture-and-Operations-Manual-Prompt.md` concept with the standing `Rotom-Home-Server-Manual-Maintenance.md` standard for the derived `Rotom-Home-Server-Manual.pdf`. Updated the Project Documentation source map and Guide source-map appendix requirements so the intended current Available Sources set contains twelve files: the nine-file Core Numbered Reference Set plus the Architecture/Deployment, Guide Maintenance, and Manual Maintenance standards. The Manual standard uses the complete current Available Sources set as its source of truth, preserves evidence-state distinctions, fixes the production PDF filename as `Rotom-Home-Server-Manual.pdf`, and updates stale manual-generation assumptions such as `game-server`, `/home/game-server`, the old `/data` Media path model, and omission of Gamarr/Game NAS architecture.
- **Evidence:** User decision in this chat; review of the current Project Documentation source map; and the newly prepared `Rotom-Home-Server-Manual-Maintenance.md`. No additional live Rotom verification was required because this change governs documentation generation rather than live configuration.
- **Outstanding:** Available Sources synchronization remains a manual project-maintenance action. After the replacement files are installed and `Rotom-Home-Server-Manual-Maintenance.md` is added to Available Sources, the twelve-file set described here becomes the current Project Documentation set. `Rotom-Home-Server-Manual.pdf` has not been regenerated by this documentation-only task.

## 2026-09-19 — Reconcile Guide end-matter governance after appendix expansion

- **Files changed:** `00-Rotom-Change-Log.md`, `01-Rotom-Server-Inventory.md`, `Rotom-Home-Server-Guide-Maintenance.md`.
- **Status:** Documentation only; no live Rotom account, sudo policy, Docker service, NAS, network, backup, or other server state was changed.
- **Changes:** Reviewed the complete current Project Documentation set after adding the Linux-user Guide appendix. Clarified the source-map role of `Rotom-Home-Server-Guide-Maintenance.md` so it explicitly covers both required Guide end-matter sections, updated the maintenance standard's self-description from a singular appendix reference to both required appendices, and made the **Rotom Linux Users** appendix an explicit narrow exception to the Guide's normal minimal-procedure rule so the required `sudo -iu ...` / `exit` examples cannot be dropped as procedural detail. No current Rotom architecture or account facts changed.
- **Evidence:** Cross-document review of the current eleven-file Available Sources set, especially `01-Rotom-Server-Inventory.md`, `07-Users-and-Permissions.md`, and the Guide maintenance standard. The existing account model and workload ownership were already documented and did not require another live Rotom check.
- **Outstanding:** None for this documentation-governance reconciliation. Existing operational verification items remain unchanged.


## 2026-09-19 — Add Linux-user appendix to Guide standard

- **Files changed:** `00-Rotom-Change-Log.md`, `Rotom-Home-Server-Guide-Maintenance.md`.
- **Status:** Documentation only; no live Rotom account, sudo policy, Docker service, NAS permission, SSH configuration, or other server state was changed.
- **Changes:** Added a required final **Rotom Linux Users** appendix to the Guide maintenance standard. The appendix defines the seven named operational accounts, their purposes and current workload roles, and the standard administrator workflow for switching into them on Rotom with `sudo -iu NAME_OF_USER` and returning with `exit`. The Guide regeneration workflow now requires the existing **legacy documentation set & ChatGPT** appendix followed by **Rotom Linux Users** as the final substantive section of `Rotom-Home-Server-Guide.pdf`.
- **Evidence:** User request in this chat plus the current named-account model in `07-Users-and-Permissions.md` and workload ownership recorded in `01-Rotom-Server-Inventory.md` / `02-Docker-Services.md`. No additional live Rotom verification was required because this change documents already-recorded account roles and Guide-generation behavior.
- **Outstanding:** The current production PDF was not regenerated by this documentation-only task; the Linux-user appendix will be added the next time the Guide is regenerated using the maintenance standard.


## 2026-09-19 — Add Project Documentation appendix to Guide standard

- **Files changed:** `00-Rotom-Change-Log.md`, `Rotom-Home-Server-Guide-Maintenance.md`.
- **Status:** Documentation only; no live Rotom, Docker, NAS, network, backup, account, or service configuration was changed.
- **Changes:** Added a required end-of-PDF **legacy documentation set & ChatGPT** appendix to the Guide maintenance standard. The appendix defines legacy documentation set, outlines the current eleven Project Documentation files with each file's purpose, role, and ChatGPT usage, explains Available Sources membership and source precedence, documents the ChatGPT update/synchronization model, and requires the appendix to be regenerated from the current source map whenever the Guide is rebuilt. The Guide workflow and Definition of Done now require this appendix as the final substantive section of `Rotom-Home-Server-Guide.pdf`.
- **Evidence:** User request in this chat plus the current eleven-file source map in `01-Rotom-Server-Inventory.md`. No live-system verification was needed because this is documentation/governance behavior only.
- **Outstanding:** The current production PDF was not regenerated by this documentation-only change. The new appendix requirement takes effect the next time `Rotom-Home-Server-Guide-Maintenance.md` is used to regenerate the Guide.


## 2026-09-19 — Correct post-audit documentation inconsistencies

- **Files changed:** `00-Rotom-Change-Log.md`, `03-Network-and-Domains.md`, `05-Backup-and-Restore.md`, `06-Maintenance-and-Automation.md`.
- **Status:** Documentation correction only; no live Rotom, Docker, NAS, network, backup, mount, or service configuration was changed.
- **Changes:** Replaced the remaining stale Gamarr LAN-only/NPM sentence with the already-verified active `gamarr.rotom.casa -> 192.168.1.69:6767` route and its verified TLS/access-list details; made the Restic boundary explicit that the `/mnt` exclusion places Media, Game, Shared Drive, and the Backup destination outside the host backup source scope; and expanded the deferred normal-reboot automount verification from Media/Game only to all four current fstab-backed NAS automounts.
- **Evidence:** Existing 2026-09-19 read-only manual-verification audit and the already-reconciled current inventory/storage records. No additional Rotom check was required because these were cross-document consistency corrections to facts already verified in this chat.
- **Outstanding:** The normal future reboot itself remains unobserved, so automount persistence across reboot is still a deferred verification item. Other previously recorded unresolved items are unchanged.

## 2026-09-19 — Comprehensive live verification and documentation-source reconciliation

- **Files changed:** `00-Rotom-Change-Log.md`, `01-Rotom-Server-Inventory.md`, `02-Docker-Services.md`, `03-Network-and-Domains.md`, `04-NAS-and-Storage.md`, `05-Backup-and-Restore.md`, `06-Maintenance-and-Automation.md`, `07-Users-and-Permissions.md`, `08-Rotom-Directory-Tree.txt`, `Rotom-Home-Server-Guide-Maintenance.md`. `Rotom-Architecture-and-Deployment-Standard.md` was reviewed and did not require a factual change.
- **Status:** Verified / documentation update only. The verification commands were read-only; no Rotom service, Docker container, NAS export, mount, firewall rule, account, database, backup repository, or other live configuration was changed by this documentation task.
- **Changes:** Incorporated the comprehensive 2026-09-19 manual-verification audit and the follow-up inspection of `/etc/cron.d/weekly-linux-update` and `/usr/local/sbin/weekly-linux-update`. Gamarr is now documented with its active NPM route `gamarr.rotom.casa -> 192.168.1.69:6767`, NPM certificate ID `24`, forced SSL, no access list, and working HTTPS response; its current Docker health is supplied by the image healthcheck even though no explicit Compose `healthcheck:` directive is present. Legacy Smart Hub/Portainer/OliveTin/PalTools NPM rows remain `enabled=1` in the NPM database but are absent from the current generated proxy-host configuration, so they are recorded as stale/unresolved database records rather than active generated routes. Fresh host evidence reconfirmed all four NAS mounts as live NFSv3 filesystems, the Media/Game/Backup ordinary-account access boundaries, hardlink-compatible Media/Game filesystem-device pairs, current Restic/timer/status-API state, current WOL NIC configuration, the failed `casper-md5check.service`, Docker log limits, and current service/container metadata. The authoritative `/home/rotom/documentation` top level is now explicitly recorded as containing only `AGENTS.md` and `README.md`; the numbered Project Documentation files are not deployed there. The current Available Sources membership is also reconciled to eleven files: the nine-file Core Numbered Reference Set plus `Rotom-Architecture-and-Deployment-Standard.md` and `Rotom-Home-Server-Guide-Maintenance.md`.
- **Evidence:** User-supplied `rotom-manual-verification.txt` from the 2026-09-19 read-only audit; follow-up output showing `/etc/cron.d/weekly-linux-update:3:0 4 * * 0 root /usr/local/sbin/weekly-linux-update`; and direct read of the update script confirming `apt-get update`, `apt-get -y upgrade`, `apt-get -y autoremove`, `apt-get -y autoclean`, logging to `/var/log/weekly-linux-update.log`, and reboot only when `/var/run/reboot-required` exists.
- **Outstanding:** UniFi control-plane implementation, final automount persistence through a normal future reboot, qBittorrent live-runtime NFS-loss behavior, full bare-metal disaster recovery, full end-to-end Palworld recovery, Backup/Game share permission persistence across a future UNAS/UniFi Drive restart/update, a future natural Let's Encrypt renewal, end-to-end alert delivery, end-to-end Wake-on-LAN, intended `jaredwines.com` state, exact intended public exposure for broad UFW/Docker-published services, current Arcane per-project qBittorrent update/auto-heal treatment, and VPN credential rotation after prior chat exposure remain unverified. Never expose VPN credential values while verifying rotation.

## 2026-09-19 — Correct Game NAS Docker dependency summary

- **Files changed:** `00-Rotom-Change-Log.md`, `03-Network-and-Domains.md`.
- **Status:** Documentation correction only; no live Rotom, Docker, NAS, network, or service change.
- **Changes:** Corrected the remaining stale Network Dependencies sentence that said no Docker workload depended on `/mnt/nas-game`. The current summary now records that qBittorrentVPN uses the Media and Game torrent trees, Gamarr uses the full Game share, and Docker as a whole remains independent of NAS availability.
- **Evidence:** Existing verified 2026-09-19 deployment documentation for central qBittorrentVPN and Gamarr, including the current Game NAS bind mounts and service-storage model.
- **Outstanding:** No new technical gap. Existing deferred checks remain unchanged.


## 2026-09-19 — Final cross-document current-state reconciliation

- **Files changed:** `00-Rotom-Change-Log.md`, `02-Docker-Services.md`, `03-Network-and-Domains.md`, `04-NAS-and-Storage.md`, `05-Backup-and-Restore.md`.
- **Status:** Documentation correction only; no live Rotom, Docker, NAS, network, backup, Palworld, or service change.
- **Changes:** Reconciled four remaining historical/current-state wording issues. The Prowlarr migration section now notes that the later full Docker-network audit resolved its initially uncaptured subnet/gateway; the Shared Drive section now treats the earlier directory-only observation as historical and records the later verified active NFSv3 automount; the NAS/storage Scope now explicitly includes `/mnt/nas-shared-drive`; and the Palworld recovery wording now distinguishes the successful representative `Level.sav` restore from the still-untested full end-to-end Palworld service/world recovery rehearsal.
- **Evidence:** Consistency review against the final 2026-09-19 evidence already recorded in the documentation set: `prowlarr_default` `172.22.0.0/16` with gateway `172.22.0.1` and Prowlarr `172.22.0.2`; active `/mnt/nas-shared-drive` NFSv3 automount; and successful isolated restoration of both current Palworld `Level.sav` files from Restic.
- **Outstanding:** No new technical gap. Existing deferred checks remain unchanged: normal post-change automount persistence through a future reboot, controlled qBittorrent live-NFS-loss behavior, full disaster-recovery and end-to-end Palworld recovery rehearsals, UNAS permission persistence after restart/update, UniFi router-side verification, observation of a future normal certificate renewal, end-to-end WOL/alert delivery, and the intended state of `jaredwines.com`.


## 2026-09-19 — Final deferred-test and storage-summary cleanup

- **Files changed:** `00-Rotom-Change-Log.md`, `02-Docker-Services.md`, `04-NAS-and-Storage.md`, `06-Maintenance-and-Automation.md`.
- **Status:** Documentation correction only; no live Rotom, Docker, NAS, network, certificate, backup, or service change.
- **Changes:** Marked the 2026-09-15 Docker container count/status as historical and explicitly superseded by the 2026-09-19 consolidated audit; added the verified `/mnt/nas-shared-drive` NFSv3 automount to the storage overview table; changed certificate follow-up from a forced renewal test to observing the next normal renewal unless troubleshooting requires intervention; and removed the unnecessary instruction to repeat the already-verified qBittorrent missing-sentinel startup test during future reboot validation.
- **Evidence:** Consistency review against the current 2026-09-19 documentation set and its already-recorded final verification evidence: 16 running containers plus exited `jaredwines.com`, Shared Drive active as an fstab-backed NFSv3 automount, qBittorrent missing-sentinel startup/recreation failure already verified, and the currently served Let's Encrypt certificate verified valid while a future natural renewal remains unobserved.
- **Outstanding:** Genuine deferred checks are unchanged: normal post-change reboot persistence of the final automount configuration, controlled qBittorrent behavior during live NFS loss, full disaster-recovery/Palworld restore rehearsals, UNAS permission persistence after restart/update, UniFi router-side verification, observation of a future normal certificate renewal, end-to-end WOL/alert delivery, and the intended state of `jaredwines.com`.


## 2026-09-19 — Final consistency cleanup of revised documentation set

- **Files changed:** `00-Rotom-Change-Log.md`, `02-Docker-Services.md`, `04-NAS-and-Storage.md`, `05-Backup-and-Restore.md`, `06-Maintenance-and-Automation.md`.
- **Status:** Documentation correction only; no live Rotom, Docker, NAS, network, backup, account, or service change.
- **Changes:** Removed the last stale current-state wording found during review of the revised source set. The Docker inventory now treats blank-port interpretation as a resolved caveat rather than an open verification item; NAS/storage now records Jared's final verified absence from media GID `5000`; backup migration notes now acknowledge that current snapshot `f0d51eaa` path-verifies Prowlarr, qBittorrentVPN, and Gamarr after the earlier migration-time gaps; and maintenance wording now clearly separates the original 2026-09-18 backup-protection checkpoint from the later 2026-09-19 current access matrix, snapshot verification, and successful timer-triggered backup run.
- **Evidence:** Consistency review of the current 10-file source set against the final 2026-09-19 verification evidence already recorded in these documents, including final `id`/group checks, current Compose/network reconciliation, snapshot `f0d51eaa`, and the latest successful scheduled backup service result.
- **Outstanding:** No new technical gap. Existing deferred operational tests remain unchanged: post-change reboot persistence, controlled qBittorrent live-NFS-loss behavior, full disaster-recovery/Palworld restore rehearsals, UNAS permission persistence after restart/update, UniFi router-side verification, future certificate renewal, end-to-end WOL/alert delivery, and the intended state of `jaredwines.com`.

## 2026-09-19 — Reconcile stale carry-forward wording after final verification

- **Files changed:** `00-Rotom-Change-Log.md`, `01-Rotom-Server-Inventory.md`, `02-Docker-Services.md`, `03-Network-and-Domains.md`, `05-Backup-and-Restore.md`, `06-Maintenance-and-Automation.md`, `08-Rotom-Directory-Tree.txt`.
- **Status:** Documentation correction only; no live Rotom, Docker, NAS, network, backup, or account change.
- **Changes:** Removed stale current-state wording that survived the final 2026-09-19 verification update. The inventory now records Jared's verified absence from media GID `5000`; Docker and network scope text now acknowledges the later full Compose/network reconciliation; backup coverage rows now mark Prowlarr, qBittorrentVPN, and Gamarr as path-verified in snapshot `f0d51eaa`; scheduled backup wording now records the successful timer-triggered run under backup-root mode `0700`; the historical September 18 backup section is explicitly superseded where later evidence applies; maintenance now distinguishes the successful representative isolated Restic restore from still-untested full-system and full Palworld recovery; and the directory tree notes the later Prowlarr snapshot verification while retaining rollback-source retirement as deferred.
- **Evidence:** Consistency review against the final 2026-09-19 verification evidence already recorded in the immediately following change-log entry, including final `id`/group checks, the full Docker-network/Compose audit, timer/service output, snapshot `f0d51eaa` path verification, `restic check --read-data`, and the isolated representative restore.
- **Outstanding:** No new technical gap created by this correction. Existing genuine deferred checks remain as recorded in the final verification entry: post-change reboot persistence, controlled qBittorrent live-NFS-loss behavior, full disaster-recovery/Palworld restore rehearsals, UNAS permission persistence after restart/update, UniFi router-side verification, future certificate renewal, end-to-end WOL/alert delivery, and the intended state of `jaredwines.com`.

## 2026-09-19 — Consolidate final Rotom verification audit and recovery evidence

- **Files changed:** `00-Rotom-Change-Log.md`, `01-Rotom-Server-Inventory.md`, `02-Docker-Services.md`, `03-Network-and-Domains.md`, `04-NAS-and-Storage.md`, `05-Backup-and-Restore.md`, `06-Maintenance-and-Automation.md`, `07-Users-and-Permissions.md`, `08-Rotom-Directory-Tree.txt`, `Rotom-Architecture-and-Deployment-Standard.md`.
- **Status:** Verified / documentation update only. The audit commands were read-only except for an isolated Restic restore under `/tmp`, which was deleted after verification; no running-service configuration was changed, no container was restarted, no NFS filesystem was unmounted, and no Restic snapshot was created/forgotten/pruned by the verification work.
- **Changes:** Reconciled the final 2026-09-19 read-only audits across hardware, Docker, networking, NAS, identities, Jellyfin GPU capability, Arcane, qBittorrentVPN, Nginx Proxy Manager, Restic, Wake-on-LAN, and current backup protection. Hardware is now recorded as a Wortmann_AG `1009664;1400107` / PC-MICRO system using an Intel `NUC8BEB` motherboard with Core i5-8259U and Iris Plus 655. Refreshed the complete live Docker bridge/subnet map and corrected Homepage/Glances runtime addresses. Verified `/mnt/nas-shared-drive` as an active NFSv3 automount, Jared's final absence from media GID 5000, current `game` denial on the backup share, qBittorrent NAS sentinels, Sonarr/Radarr root folders, Jellyfin process/device access, QSV/VAAPI functional encode capability, the current NPM wildcard certificate, the corrected Homepage backup-status UFW rule/listener, Wake-on-LAN magic-packet configuration, and current `jaredwines.com` Compose/container state. Arcane stale project records are now directly verified in `arcane.db`; Arcane has no notification-provider records. Restic path coverage was verified in current snapshot `f0d51eaa`; `restic check --read-data` read all 933 packs across 19 snapshots with no errors, and an isolated representative restore successfully recovered both Palworld `Level.sav` files plus Home Assistant and service configuration files before the 125 MiB scratch tree was deleted.
- **Important current-state findings:** Jellyfin's Intel GPU path and both QSV and VAAPI encode paths are functional, but Jellyfin application configuration currently has `HardwareAccelerationType=none`; hardware acceleration capability is verified but application use is disabled. `jaredwines.com` has a present Compose file and an exited container with exit code 0; whether it should be running is an administrator decision. qBittorrent's Media/Game sentinels are present as directories mode `2555`, UID `997`, with GIDs `5000` and `5001` respectively; an earlier unprivileged `test -e` false-negative demonstrated that existence checks through inaccessible parent directories must be repeated with a sufficiently privileged identity before declaring a path missing.
- **Evidence:** Supplied 2026-09-19 command output: `hostnamectl`/`dmidecode`/`lspci`; complete `docker network inspect` and Compose-label audit; `id`/`getent`; `findmnt`/systemd automount/showmount; Docker mounts and WireGuard; UFW and listener checks; read-only Sonarr/Radarr SQLite root-folder queries; Jellyfin process/GPU/FFmpeg tests with `QSV_TEST=PASS` and `VAAPI_TEST=PASS`; read-only Arcane SQLite inspection; TLS inspection; `restic check` and `restic check --read-data`; isolated Restic restore; current backup-share access matrix; `ethtool`; and root-level sentinel `stat`.
- **Outstanding:** Observe the current Media/Game automount configuration through a normal future Rotom reboot; test qBittorrent behavior during live NFS loss only in a controlled maintenance window; perform a full end-to-end Palworld server restore rehearsal and broader disaster-recovery rehearsal; verify backup-share mode persistence after a future UNAS/UniFi Drive restart/update; inspect UniFi DHCP reservation/VLAN/WAN-forward/router-firewall/local-DNS implementation; observe a real future Let's Encrypt renewal; configure/test an alert destination if desired; perform an end-to-end Wake-on-LAN delivery test; and decide whether `jaredwines.com` is intentionally stopped.

## 2026-09-19 — Correct Game NAS Docker-dependency wording

- **Files changed:** `00-Rotom-Change-Log.md`, `06-Maintenance-and-Automation.md`.
- **Status:** Documentation correction only; no live Rotom, Docker, NAS, account, mount, or service change.
- **Changes:** Corrected a stale sentence that said no Docker service depended on `/mnt/nas-game`. The current state is that central qBittorrentVPN bind-mounts `/mnt/nas-game/torrents`, Gamarr bind-mounts the full `/mnt/nas-game` tree at `/game`, and Palworld remains local under `/home/game`. The corrected paragraph also points to qBittorrent's verified NAS startup fail-closed bind/sentinel protection and retains the existing warning that host Restic excludes `/mnt`.
- **Evidence:** Documentation consistency review against the completed 2026-09-19 central qBittorrentVPN/Gamarr deployment already recorded in `02-Docker-Services.md`, `04-NAS-and-Storage.md`, and the preceding change-log entry. No new live command was run for this wording-only correction.
- **Outstanding:** Existing migration follow-up is unchanged: current Restic path-level verification for qBittorrentVPN/Gamarr/Prowlarr remains advisable; the specific Arcane qBittorrent project/update state remains uncaptured; VPN credential rotation after chat exposure was recommended but not verified; and no live runtime-NFS-loss watchdog test was performed.

## 2026-09-19 — Complete central qBittorrentVPN and Gamarr deployment

- **Files changed:** `00-Rotom-Change-Log.md`, `01-Rotom-Server-Inventory.md`, `02-Docker-Services.md`, `03-Network-and-Domains.md`, `04-NAS-and-Storage.md`, `05-Backup-and-Restore.md`, `06-Maintenance-and-Automation.md`, `07-Users-and-Permissions.md`, `08-Rotom-Directory-Tree.txt`, `Rotom-Architecture-and-Deployment-Standard.md`.
- **Status:** Implemented and verified for the functional deployment; documentation records remaining backup/security follow-up separately.
- **Changes:** Moved the active qBittorrentVPN project from `/home/media/docker/qbittorrentvpn` to `/home/rotom/docker/qbittorrentvpn`, changed its application identity from `127:5000` to `997:5000`, retained `UMASK=002`, port `8080`, ProtonVPN/WireGuard, and the existing local `/config` state, and changed the Media container path model from `/data` to `/media`. Sonarr and Radarr now mount `/mnt/nas-media` at `/media`; qBittorrent mounts only `/mnt/nas-media/torrents` at `/media/torrents` plus `/mnt/nas-game/torrents` at `/game/torrents`. Game torrent directories are `997:5001` mode `2775`. Added qBittorrent categories for Movies, Shows, and Games using the corresponding Media/Game completed and incomplete paths. Installed Gamarr at `/home/game/docker/gamarr` using `ghcr.io/gamarr-app/gamarr:latest`, `PUID=995`, `PGID=5001`, port `6767`, local `/config`, and `/mnt/nas-game -> /game`. Created the Game library/torrent layout under `/mnt/nas-game`, verified hardlink support, and verified the Gamarr → Prowlarr → qBittorrent → Game NAS → Gamarr import workflow with continued seeding. Added NAS startup fail-closed guards to qBittorrent using long bind syntax with `create_host_path: false` plus NAS-resident read-only sentinel directories at `/mnt/nas-media/.rotom-qbt-nas-ready` and `/mnt/nas-game/.rotom-qbt-nas-ready`; startup failed as intended when either sentinel was temporarily absent. VPN credentials were moved out of `compose.yaml` into `/home/rotom/docker/qbittorrentvpn/.env`, mode `0600`, and the stale pre-guard Compose copy that still contained credential variables was deleted. The old `/home/media/docker/qbittorrentvpn` rollback tree was also deleted after the user accepted the migration.
- **Evidence:** Docker inspection verified the final qBittorrent working directory, `PUID=997`, `PGID=5000`, `UMASK=002`, config bind, Media/Game torrent binds, and read-only sentinel binds. Disposable writes produced `997:5000` on Media and `997:5001` on Game. WireGuard showed an active `wg0` handshake and VPN egress; an earlier deliberate `wg0`-down test blocked Internet egress, verifying the VPN kill switch. Both missing-sentinel tests failed container creation with `bind source path does not exist`, and qBittorrent restarted normally after restoration. `findmnt -M`, `stat -f`, and `/proc/mounts` verified both Media and Game are active NFSv3 filesystems from `192.168.1.70`. Gamarr was verified listening on `6767`, using `/game`, writing as `995:5001`, querying Prowlarr through Torznab, handing a release to qBittorrent, importing to the Game library, hardlinking in the final commissioning test, and leaving the torrent available for seeding. The user subsequently confirmed the completed guide and that everything was working.
- **Important deviations/lessons:** The user intentionally cleared the existing qBittorrent torrent/download queue during the container-path rename, so historical torrents were not preserved through the final path migration. Gamarr appends `/api` to its Torznab URL; the working Prowlarr base is `http://192.168.1.69:9696/2`, not a value already ending in `/api`. Container-side account names can differ from host names; numeric UID/GID values are authoritative for NFS ownership. Hardlinks share inode metadata, so ownership changes through one pathname affect every hardlink to that inode.
- **Backup/cleanup:** The user deleted `/home/media/docker/qbittorrentvpn` before a fresh post-migration Restic path verification. The latest snapshot explicitly listed in this chat is automatic snapshot `02330a5e` from `2026-09-19 04:23:30 PDT`; its contents were not successfully queried because the first `restic ls` attempt used the literal placeholder `SNAPSHOT_ID`. Do not claim that snapshot contains the final qBittorrent/Gamarr state until checked. The Prowlarr rollback tree remains separately documented.
- **Outstanding:** A fresh Restic snapshot/path-level verification for `/home/rotom/docker/qbittorrentvpn`, `/home/game/docker/gamarr`, and preferably `/home/rotom/docker/prowlarr` is still advisable. The specific Arcane project/update treatment for the newly moved qBittorrent project was not separately captured. VPN credential rotation was recommended after credentials were exposed in chat, but completion was not verified; never record credential values in project documentation. A full live-NAS runtime-loss test while qBittorrent is already running was not performed; the verified protection is the container startup/recreation fail-closed path.

## 2026-09-19 — Migrate Prowlarr from media to rotom ownership

- **Files changed:** `00-Rotom-Change-Log.md`, `01-Rotom-Server-Inventory.md`, `02-Docker-Services.md`, `03-Network-and-Domains.md`, `04-NAS-and-Storage.md`, `05-Backup-and-Restore.md`, `06-Maintenance-and-Automation.md`, `07-Users-and-Permissions.md`, `08-Rotom-Directory-Tree.txt`. `Rotom-Architecture-and-Deployment-Standard.md` was reviewed and did not require a change.
- **Status:** Implemented and verified; old source retained temporarily for rollback.
- **Changes:** Migrated the active Prowlarr Compose project and persistent config/database from `/home/media/docker/prowlarr` to `/home/rotom/docker/prowlarr`. The target copy is owned `rotom:rotom`; the LinuxServer identity changed from `PUID=127` / `PGID=5000` to `PUID=997` / `PGID=986` while preserving `UMASK=002`, image, restart policy, published TCP port `9696`, reverse-proxy hostname, and the existing `/config` data. Prowlarr still has no `/mnt/nas-media` bind. The application process was verified running as `rotom:rotom`. Arcane recognizes the single current Prowlarr project under `/home/rotom/docker/prowlarr`; its UI showed auto-update enabled. The original `/home/media/docker/prowlarr` tree remains intact as the rollback source and is not the active Compose project.
- **Evidence:** Preflight captured the live Compose file, Docker metadata, source ownership/size, target absence, HTTP behavior (`302` locally and through `https://prowlarr.rotom.casa`), and unchanged Sonarr/Radarr/qBittorrentVPN/Jellyfin runtime state. Prowlarr was stopped cleanly; because Jared cannot traverse `/home/media`, the attempted direct `docker compose down` from Jared's shell could not enter the source directory, so `sudo docker stop prowlarr` was used instead. The stopped source was copied with `rsync -aHAX --numeric-ids`; `diff -qr` returned no differences before target ownership changed. The recreated container reported working directory `/home/rotom/docker/prowlarr`, config bind `/home/rotom/docker/prowlarr/config -> /config`, `PUID=997`, `PGID=986`, `UMASK=002`, and a live Prowlarr process as `rotom:rotom`. Local and proxied HTTP remained `302`; exactly one Prowlarr container was attached to `prowlarr_default`; the other media containers remained running. Prowlarr UI acceptance confirmed the existing indexers, history, Sonarr and Radarr applications, successful indexer/application tests, and no first-run or database/config corruption condition. The recreated container was observed at `172.22.0.2` on `prowlarr_default`; the network subnet/gateway were not captured by this targeted check.
- **Backup/rollback:** No new Restic/NAS backup was created by this migration guide. Both the old and new trees are beneath `/home` and therefore fall within the existing Restic include scope on a future run, but the latest verified Restic snapshot still predates this Prowlarr migration. The old media-owned source must remain until a separate retirement step. A path-only manifest `/home/jared/prowlarr-pre-migration-files.txt` was created during preparation; deletion was discussed after acceptance but was not confirmed in the supplied evidence.
- **Outstanding:** Run and verify a post-migration Restic snapshot containing `/home/rotom/docker/prowlarr` before retiring the old source if a durable recovery point is desired. Source-tree retirement and deletion of the temporary path-only manifest remain separate cleanup actions.

## 2026-09-19 — Correct final Game NFS protocol wording

- **Files changed:** `00-Rotom-Change-Log.md`, `04-NAS-and-Storage.md`.
- **Status:** Documentation correction only; no live Rotom, Docker, NAS, account, mount, or service change.
- **Changes:** Corrected the last over-broad NFS protocol sentence in `04-NAS-and-Storage.md`. The ownership/permissions section now states specifically that the **Media and Backup** mounts use NFSv3 with `sec=sys`, matching the evidence already recorded elsewhere and avoiding an unsupported claim about the permanently commissioned Game mount's negotiated NFS version.
- **Evidence:** Documentation consistency review against the verified 2026-09-19 Game commissioning output. The temporary Game mount explicitly used `vers=3`, but the permanent `findmnt` output did not capture the complete negotiated option list, so the documentation continues not to assert an unshown persistent `vers=` value. No new live command was run for this wording-only correction.
- **Outstanding:** Existing deferred checks are unchanged: observe `/mnt/nas-game` after a normal future Rotom reboot; verify Game and Backup share-root permission persistence after a future UNAS/UniFi Drive restart or reconfiguration; verify a new post-GID-migration Restic snapshot; and clean up the stale Jared Palworld `.env` identity values when separately reviewed.

## 2026-09-19 — Complete Game commissioning wording cleanup

- **Files changed:** `00-Rotom-Change-Log.md`, `04-NAS-and-Storage.md`.
- **Status:** Documentation correction only; no live Rotom, Docker, NAS, account, mount, or service change.
- **Changes:** Corrected the two remaining stale two-mount phrases in `04-NAS-and-Storage.md`. The Backup mount section now says specifically that the **Media and Backup** mounts use NFSv3 and `sec=sys`, avoiding an implication that Game was part of that older two-mount observation. The startup/dependency section now states that `docker.service` has no global `RequiresMountsFor=` dependency on **any NAS path** and is not globally coupled to NAS availability. This completes the two-mount wording cleanup described in the earlier 2026-09-19 documentation-correction entry.
- **Evidence:** Documentation consistency review against the already verified 2026-09-19 Game commissioning state. No new live command was run for this wording-only correction.
- **Outstanding:** Existing deferred checks are unchanged: observe `/mnt/nas-game` after a normal future Rotom reboot; verify Game and Backup share-root permission persistence after a future UNAS/UniFi Drive restart or reconfiguration; verify a new post-GID-migration Restic snapshot; and clean up the stale Jared Palworld `.env` identity values when separately reviewed.

## 2026-09-19 — Correct post-Game-commissioning documentation inconsistencies

- **Files changed:** `00-Rotom-Change-Log.md`, `01-Rotom-Server-Inventory.md`, `02-Docker-Services.md`, `03-Network-and-Domains.md`, `04-NAS-and-Storage.md`, `06-Maintenance-and-Automation.md`, `07-Users-and-Permissions.md`. `05-Backup-and-Restore.md`, `08-Rotom-Directory-Tree.txt`, and `Rotom-Architecture-and-Deployment-Standard.md` were reviewed and did not require changes.
- **Status:** Documentation correction only; no live Rotom, Docker, NAS, account, mount, or service change.
- **Changes:** Corrected the stale current-account row in `07-Users-and-Permissions.md` from `game` `995:985` to the verified current `995:5001`; added `/mnt/nas-game` to the front-page storage table in `01-Rotom-Server-Inventory.md`; refreshed the 2026-09-19 metadata/source notes in `02-Docker-Services.md` and `03-Network-and-Domains.md`; added `/mnt/nas-game` to the generated NFS mount/automount summary in `06-Maintenance-and-Automation.md`; and replaced stale two-mount wording in `04-NAS-and-Storage.md` with wording that covers all current NAS mounts. Historical `995:985` and `/mnt/nas-game-server` references remain where they explicitly describe earlier verified or proposed state.
- **Evidence:** Consistency review against the already supplied 2026-09-19 acceptance output: `id game` verified UID `995`, primary GID `5001`, and Docker supplementary GID `984`; both Palworld containers were healthy with explicit `PUID=995` / `PGID=5001`; `/etc/fstab` contained the exact Game export at `/mnt/nas-game`; `mnt-nas\x2dgame.automount` was active; the mounted Game share remained `988:5001` mode `2770`; and the service-user/negative access matrix passed. No new live command was run for this documentation-only correction.
- **Outstanding:** Existing deferred checks are unchanged: observe `/mnt/nas-game` after a normal future Rotom reboot; verify Game and Backup share-root permission persistence after a future UNAS/UniFi Drive restart or reconfiguration; verify a new post-GID-migration Restic snapshot; and clean up the stale Jared Palworld `.env` identity values when separately reviewed.

## 2026-09-19 — Commission dedicated Game NFS mount and migrate game service GID to 5001

- **Files changed:** `00-Rotom-Change-Log.md`, `01-Rotom-Server-Inventory.md`, `02-Docker-Services.md`, `03-Network-and-Domains.md`, `04-NAS-and-Storage.md`, `05-Backup-and-Restore.md`, `06-Maintenance-and-Automation.md`, `07-Users-and-Permissions.md`, `08-Rotom-Directory-Tree.txt`. `Rotom-Architecture-and-Deployment-Standard.md` was reviewed and did not require a change.
- **Status:** Implemented and verified on Rotom; normal post-change reboot persistence remains deferred.
- **Changes:** Migrated the existing `game` service group from GID `985` to dedicated primary GID `5001` while preserving UID `995` and `/home/game`. Targeted group ownership beneath `/home/game` was migrated from `985` to `5001`; Docker/containerd internal overlay objects under `/var/lib/containerd` were deliberately left untouched. Both Palworld Compose files were changed from `PUID=995` / `PGID=985` to `PUID=995` / `PGID=5001`, validated, and recreated against the same existing data trees. Commissioned the UniFi `Game` NFS share at `/mnt/nas-game`, changed only the Game share root from numeric `988:988` mode `0770` to `988:5001` mode `2770`, and added the verified Game export to `/etc/fstab` with the existing `_netdev,nofail,x-systemd.automount,x-systemd.device-timeout=30s` pattern. No game library directories or application data were moved to NAS.
- **Evidence:** Preflight confirmed `game` as `995:985`, GID `5001` unused on Rotom, the exact `Game/.data` export advertised to `rotom.casa`, and `/mnt/nas-game` absent from `fstab`. The temporary NFS mount exposed the new share as `988:988` mode `0770`; `game` was denied while Jared had access through the old group path. Before the GID change, 10,732 objects under `/home/game` carried GID `985`; the targeted migration left zero GID-985 objects under `/home/game`, while 1,014 old-GID objects outside the home were confined to `/var/lib/containerd` and were not modified. A stopped-state SHA-256 manifest covered 234 Palworld `.sav` files; the post-recreation manifest compared with no differences. Both Palworld containers became healthy with live `PUID=995` / `PGID=5001` and processes resolving as `game:game`. The Game share then verified as `988:5001` mode `2770`; `game` passed read/write/traverse, `jared`, `fran`, `media`, `rotom`, `smart-home`, and `web-host` all failed read/write/traverse, and a disposable file was created as `995:5001` mode `0664` and removed. `findmnt --verify --verbose` returned 0 parse errors and 0 errors; after `systemctl daemon-reload`, `mnt-nas\x2dgame.automount` was active and the permanent NFS mount resolved to the exact Game export.
- **Outstanding:** A normal future Rotom reboot has not yet been observed to re-establish `/mnt/nas-game`; no deliberate NAS-outage test was performed. No new post-GID-migration Restic snapshot was supplied or verified in this chat. The Jared Palworld `.env` still contains stale `PUID=1003` / `PGID=1003` values, but the current Compose files use explicit `995:5001` values; treat the `.env` entries as cleanup debt rather than current runtime identity.

## 2026-09-19 — Expand legacy documentation set to all Available Sources

- **Files changed:** `00-Rotom-Change-Log.md`, `01-Rotom-Server-Inventory.md`, `06-Maintenance-and-Automation.md`, `Rotom-Architecture-and-Deployment-Standard.md`.
- **Status:** Documentation policy only; no live Rotom change.
- **Changes:** Redefined **legacy documentation set** as every file intentionally kept in this project's Available Sources, regardless of filename, extension, format, document type, or purpose. The numbered `00`–`08` files are now the **Core Numbered Reference Set** within the larger documentation set. The canonical request **“Update the legacy documentation set using everything we changed, verified, and learned in this chat.”** now means review every Available Sources file, update only affected files, preserve unaffected files, record substantive changes in this log, return the complete current documentation set, and create one ZIP containing every current legacy documentation set file. The workflow explicitly preserves existing filenames, includes non-Markdown files, omits checksum/packaging extras unless requested, and keeps Mac-folder, Available Sources, browser, server-deployment, and live-service changes manual unless separately authorized.
- **Evidence:** User policy decision recorded on 2026-09-19. The Project-backed Available Sources set was verified during this update as exactly ten current files: the nine-file Core Numbered Reference Set (`00`–`08`) plus `Rotom-Architecture-and-Deployment-Standard.md`.
- **Outstanding:** Jared must manually replace the revised Available Sources/Mac-folder copies as desired. This policy update does not deploy files to `/home/rotom/documentation` or modify live Rotom state.

## 2026-09-18 — Refine the architecture and deployment standard from verified migration lessons

- **Files changed:** `00-Rotom-Change-Log.md`, `Rotom-Architecture-and-Deployment-Standard.md`.
- **Status:** Documentation policy only; no live Rotom change.
- **Changes:** Added durable guidance from the completed Palworld `game-server` → `game` migration: preserve numeric UID/GID during pure account renames unless the identity itself is changing; verify numeric ownership before using recursive ownership changes; separate independent identity, GID, storage, and NAS migrations; verify critical persistent data before restarting writers after path or identity changes; distinguish active old-path references from historical evidence; and treat backup retention/prune behavior as part of rollback design rather than assuming a manually created snapshot will remain available. The standard also clarifies that temporary migration manifests may be removed after acceptance when they are no longer required for rollback, while application backups and repository-managed backup data remain governed by their normal retention policies.
- **Evidence:** The verified 2026-09-18 Palworld account/home migration preserved UID/GID `995:985`, required no recursive `chown`, passed before/after save-integrity checks, separated the account rename from the still-proposed GID `5001` and `/mnt/nas-game-server` work, distinguished active configuration from historical old-name records, and showed that the later full Restic run removed stopped-state snapshot `53c989ec` under the normal retention policy after creating post-migration snapshot `0d64ab6d`.
- **Outstanding:** None. The numbered state documents `01`–`08` are unchanged by this methodology-only update.

## 2026-09-18 — Rename Palworld service account from game-server to game

- **Files changed:** `00-Rotom-Change-Log.md`, `01-Rotom-Server-Inventory.md`, `02-Docker-Services.md`, `03-Network-and-Domains.md`, `04-NAS-and-Storage.md`, `05-Backup-and-Restore.md`, `06-Maintenance-and-Automation.md`, `07-Users-and-Permissions.md`, `08-Rotom-Directory-Tree.txt`.
- **Status:** Implemented and verified. The proposed GID `5001` and `/mnt/nas-game-server` work remains separate and not deployed.
- **Changes:** Renamed the Palworld service group from `game-server` to `game` while preserving GID `985`, renamed the service user from `game-server` to `game` while preserving UID `995`, and moved the canonical home from `/home/game-server` to `/home/game`. Both Palworld Compose projects now run from `/home/game/docker/...`; no recursive ownership change was needed because numeric ownership stayed `995:985`. The Compose files themselves did not need path edits because each uses the relative bind `.:/palworld`. The active game-account Codex project entry was updated to the new Jared Palworld path. Migration-only temporary manifests and the temporary pre-edit Codex config copy were removed after verification; Palworld application backups and Restic data were retained.
- **Evidence:** Preflight verified `game-server` as `995:985`, no target `game` account/group or `/home/game`, both healthy Palworld containers, both live `/home/game-server/... -> /palworld` binds, no UID/GID ownership exceptions, no host configuration references in the inspected systemd/cron/sudo/local-script paths, and readable application archives containing `Level.sav` plus player saves. With both containers stopped, SHA-256 manifests covered 140 Jared `.sav` files and 112 Fran `.sav` files; after the account/home move both manifest comparisons were byte-for-byte identical. Post-migration checks verified `game:x:995:985::/home/game:/usr/bin/zsh`, group `game:x:985`, Docker group membership, absence of the old passwd/group names and `/home/game-server`, no ownership exceptions, Compose validation, new bind mounts and Compose working/config paths under `/home/game`, runtime processes as `game` UID/GID `995:985`, both containers healthy, and unchanged world IDs `DB40338954B844C28CEA21471A392F98` (Jared) and `396F5898378F4E9CAE89461F403653D9` (Fran). Active old-name checks were clean after updating `/home/game/.codex/config.toml`; historical shell/Codex cache records were intentionally not rewritten.
- **Backup evidence:** A stopped-state Rotom snapshot `53c989ec` existed at `2026-09-18 23:00:33 PDT`. The post-migration `backup-to-nas` run created snapshot `0d64ab6d` at `2026-09-18 23:08:43 PDT`, completed normal `7 daily / 4 weekly / 12 monthly` retention and prune, and removed the redundant same-day `53c989ec` snapshot. Snapshot `0d64ab6d` explicitly contains both current `/home/game/.../Level.sav` files. This demonstrates that manual full backups are subject to the same retention policy and may not remain as separate same-day rollback points.
- **Outstanding:** No migration-specific verification remains. Existing unrelated deferred checks remain unchanged, including the next timer-triggered backup under backup-root mode `0700`, persistence of the direct UNAS mode across a future NAS/Drive restart or reconfiguration, the final Jared media-group listing, restore rehearsals, and the firewall/status-API recheck.

## 2026-09-18 — Protect the UNAS backup share from ordinary access

- **Files changed:** `00-Rotom-Change-Log.md`, `01-Rotom-Server-Inventory.md`, `02-Docker-Services.md`, `03-Network-and-Domains.md`, `04-NAS-and-Storage.md`, `05-Backup-and-Restore.md`, `06-Maintenance-and-Automation.md`, `07-Users-and-Permissions.md`, `08-Rotom-Directory-Tree.txt`.
- **Status:** Implemented and verified; deferred timer, persistence, and firewall/status-API checks remain.
- **Changes:** Removed Glances' read-only `/mnt/nas-rotom-backup` bind and recreated the shared Homepage/Glances Compose project successfully. Changed only the UNAS backup-share root mode from `0770` to `0700`, preserving numeric ownership `988:988`, the NFSv3 export, Restic repository contents, backup scripts, timer, retention, and service identities. The resulting ordinary-filesystem policy denies direct read/write/traverse access to `jared`, `fran`, `rotom`, `media`, `game-server`, `smart-home`, and `web-host`, while the root-run backup retains access through the backup export's verified `no_root_squash` behavior. This remains an accident-prevention boundary, not a hard boundary against administrators with sudo or Docker-daemon control.
- **Evidence:** Supplied live output verified UNAS `rpc.mountd --manage-gids`; UID `1000` resolving to `jwines760` with primary GID `988` and supplementary GID `987`; the backup export using `no_root_squash,no_all_squash`; Btrfs mounted `noacl`; the share root changing from `988:988` mode `0770` to `988:988` mode `0700`; all seven ordinary accounts denied; root read/write/traverse access to both the mount root and `rotom-restic-backup`; Jared and Fran each completing `backup-to-nas`; snapshots `d22fbd7a` and then `ed244f4e` being created with retention/prune succeeding; `unas-backup.timer` enabled and active/waiting with the last service result successful; Glances running without the backup bind; and Homepage returning HTTP 200 both locally with the intended Host header and through `https://rotom.casa`. The live Homepage Docker network was also reverified as `172.24.0.0/16` with Homepage at `172.24.0.2`; this makes the older `172.18.0.0/16` network record stale and warrants a targeted firewall/status-API recheck.
- **Outstanding:** The next timer-triggered backup after the `0700` change has not yet been observed. Persistence of the direct UNAS share-root mode across a future UNAS reboot, UniFi Drive restart/update, or share reconfiguration is also unverified. Because the current Homepage network is `172.24.0.0/16` while the older audit recorded a UFW rule for backup-status API port 8787 from `172.18.0.0/16`, verify that rule and the Homepage backup-status path before treating the older firewall record as current.

## 2026-09-18 — Reconcile network and NAS documentation after backup-protection review

- **Files changed:** `00-Rotom-Change-Log.md`, `03-Network-and-Domains.md`, `04-NAS-and-Storage.md`.
- **Status:** Documentation correction only; no live Rotom or UNAS change.
- **Changes:** Marked the September 14 Arcane `172.24.0.0/16` subnet/IP and Homepage/Glances `172.18.0.x` DNAT destinations as historical rather than current because the live Homepage network was reverified on 2026-09-18 as `172.24.0.0/16`. Updated the NAS export history so the older `Shared_NAS` name is explicitly historical and the live 2026-09-18 `Shared_Drive` advertisement is current. Replaced the stale statement that the complete `unas-backup.service` was uninspected with the live verified root-run unit details from the protection work.
- **Evidence:** Documentation consistency review against the supplied 2026-09-18 Docker/network, `showmount`, and `systemctl cat unas-backup.service` output.
- **Outstanding:** Re-read the current full Docker network/NAT/firewall state to establish Arcane's present bridge allocation and confirm the backup-status API path; the older full-network audit remains historical where not separately refreshed.

## 2026-09-18 — Clean up documentation structure and companion-standard indexing

- **Files changed:** `00-Rotom-Change-Log.md`, `01-Rotom-Server-Inventory.md`, `Rotom-Architecture-and-Deployment-Standard.md`.
- **Status:** Documentation only; structure and indexing cleanup.
- **Changes:** Moved the two earlier Available Sources policy entries into the `Change history` section without changing their historical wording. Kept the numbered `00`–`08` files as the core legacy documentation set, added the Architecture and Deployment Standard to the server inventory as a maintained companion standard, and changed the standard's header so it no longer implies membership in the numbered set.
- **Evidence:** Documentation consistency review and user approval recorded on 2026-09-18.
- **Outstanding:** Jared must manually replace these three files in `/Users/jared/Documents/ChatGPT/Rotom-Home-Server` and in Available Sources. No live Rotom change is authorized or required.

## 2026-09-16 — Use manual Available Sources uploads

- **Files changed:** `00-Rotom-Change-Log.md`, `01-Rotom-Server-Inventory.md`.
- **Status:** Documentation policy.
- **Changes:** Restored the verified-replacement-file fallback and recorded that Jared will handle manual Available Sources uploads. Codex must not open or control a browser to synchronize Available Sources. Direct synchronization is allowed only if the project controls become accessible without browser automation; otherwise Codex provides verified replacement files and clearly states that manual upload is still needed.
- **Evidence:** User decision recorded on 2026-09-16.
- **Outstanding:** The updated `00` and `01` files require manual upload to Available Sources.

## 2026-09-16 — Restore the Available Sources fallback

- **Files changed:** `00-Rotom-Change-Log.md`, `01-Rotom-Server-Inventory.md`.
- **Status:** Documentation policy.
- **Changes:** Restored the standing rule that Codex synchronizes matching files to Available Sources when the ChatGPT project controls are accessible. If those controls are unavailable, Codex provides verified replacement files and clearly states that manual upload is still needed. Chrome's `ChatGPT` profile remains the preferred browser for synchronization.
- **Evidence:** User decision recorded on 2026-09-16.
- **Outstanding:** None.


## 2026-09-18 — Standardize the documentation-update request

- **Files changed:** `00-Rotom-Change-Log.md`, `01-Rotom-Server-Inventory.md`, `06-Maintenance-and-Automation.md`.
- **Status:** Documentation only; current workflow policy.
- **Changes:** Adopted **“Update the legacy documentation set using everything we changed, verified, and learned in this chat.”** as the canonical standing request for completing a Rotom documentation update from the current chat. The request updates only affected files in the maintained `00`–`08` set, records substantive changes in this change log, and produces verified replacement files using the existing filenames. Jared continues to manually replace both the Mac-folder copies and the matching Available Sources files.
- **Evidence:** User decision recorded on 2026-09-18.
- **Outstanding:** Jared must manually replace these three updated files in `/Users/jared/Documents/ChatGPT/Rotom-Home-Server` and in Available Sources. Do not mark either destination complete until Jared confirms it.


## 2026-09-16 — Make Mac documentation replacement manual

- **Files changed:** `00-Rotom-Change-Log.md`, `01-Rotom-Server-Inventory.md`, `06-Maintenance-and-Automation.md`.
- **Status:** Documentation only; current workflow policy.
- **Changes:** Removed automatic replacement of files in `/Users/jared/Documents/ChatGPT/Rotom-Home-Server` from the standing documentation-update instruction. ChatGPT now prepares verified replacement files only. Jared manually replaces both the matching Mac-folder files and the matching Available Sources files. Earlier entries describing automatic or conditional synchronization are retained as history and are superseded by this entry.
- **Evidence:** User decision recorded on 2026-09-16.
- **Outstanding:** After this update, Jared must manually replace these three files in the Mac documentation folder and Available Sources. Do not mark either destination complete until Jared confirms it.


## 2026-09-16 — Retire the ChatGPT browser workflow

- **Files changed:** `00-Rotom-Change-Log.md`, `01-Rotom-Server-Inventory.md`, `06-Maintenance-and-Automation.md`.
- **Status:** Documentation only; current workflow policy.
- **Changes:** Removed the active Chrome/ChatGPT-browser administration workflow from the server inventory and maintenance guidance. ChatGPT-controlled browser work is no longer part of the Rotom workflow, and Available Sources synchronization remains a manual Jared task using verified replacement files. Native macOS Terminal and `ssh rotom.casa` remain the administration workflow. Earlier Chrome and Safari entries below are retained as historical decisions and are superseded by this entry.
- **Evidence:** User decision recorded on 2026-09-16; the user also stated that Chrome will be removed from the Mac.
- **Outstanding:** Replace the matching files in `/Users/jared/Documents/ChatGPT/Rotom-Home-Server` and manually replace the affected Available Sources copies. This documentation update does not modify `/home/rotom/documentation/AGENTS.md`.


## 2026-09-16 — Consolidate four chats and adopt the Mac administration workflow

- **Files changed:** `00-Rotom-Change-Log.md`, `01-Rotom-Server-Inventory.md`, `02-Docker-Services.md`, `03-Network-and-Domains.md`, `06-Maintenance-and-Automation.md`.
- **Status:** Documentation update; Homepage cutover verified in supplied output; Mac workflow adopted by the user.
- **Changes:** Recorded `https://rotom.casa` as Homepage's canonical URL, NPM proxy host 9 with only `server_name rotom.casa;`, the selected title `Rotom` and description `Home automation and server management`, and wildcard DNS behavior. Adopted Chrome profile `ChatGPT` for assisted web work, Safari for personal browsing, Apple Passwords as the credential source, and native macOS Terminal for SSH. The user has removed Ghostty. This Chrome decision supersedes the earlier Safari synchronization policy below. The normal documentation-update request includes the Mac documentation folder and Available Sources synchronization. Preserved the previously incorporated authoritative-documentation ACLs and shared full-backup access for Jared and Fran.
- **Evidence:** “Create Rotom docs setup guide,” “Add Fran Backup Access,” “Change Homepage URL,” “Selection ChatGPT brower,” and the user's explicit Terminal correction. The Homepage chat includes generated NPM configuration, an HTTPS response with correct SNI (`200 OK`, `X-Served-By: rotom.casa`), and random-subdomain DNS output. This is not a new live server audit; the HTTPS test used `-k` and does not independently validate certificate trust. The ChatGPT project's operating instructions were also updated through Chrome to persist the Terminal and browser preferences.
- **Outstanding:** The presence of a separate explicit `homepage.rotom.casa` DNS record remains unverified; wildcard resolution alone does not establish one. The selected Homepage title/description and exact single-host environment value were not separately printed in the final verification. Deployment of numbered documents and updated operating instructions to `/home/rotom/documentation` remains a separate task; do not infer deployment from this documentation package.

## 2026-09-16 — Use Safari for Available Sources synchronization

- **Files changed:** `00-Rotom-Change-Log.md`, `01-Rotom-Server-Inventory.md`.
- **Status:** Documentation policy.
- **Changes:** Superseded the fallback-only synchronization wording. The standing documentation-update request now directs Codex to use Safari access to replace the matching Available Sources after preparing and verifying the revised files. This requires the user's Safari permission and any required confirmation before deleting existing cloud-source files.
- **Evidence:** User decision recorded on 2026-09-16.
- **Outstanding:** None.

## 2026-09-16 — Clarify the Available Sources synchronization fallback

- **Files changed:** `00-Rotom-Change-Log.md`, `01-Rotom-Server-Inventory.md`.
- **Status:** Documentation policy.
- **Changes:** At that time, clarified that the standing documentation-update request included Available Sources synchronization only when the ChatGPT project controls were accessible. That policy is superseded by the later Safari-access decision above. The local `sources/` directory remains a read-only project mirror and is not an alternate way to update cloud sources.
- **Evidence:** Current workspace access limits and the user’s requested documentation workflow.
- **Outstanding:** Available Sources must still be replaced through the ChatGPT project interface for this current update.

## 2026-09-16 — Define the documentation update-and-sync instruction

- **Files changed:** `00-Rotom-Change-Log.md`, `01-Rotom-Server-Inventory.md`.
- **Status:** Documentation policy.
- **Changes:** Defined the standing request “update the legacy documentation set using what we changed and learned from …” to include revising the affected numbered documents, recording the substantive change here, and syncing the matching filenames to the ChatGPT project's Available Sources list when its controls are accessible. Unrelated sources remain unchanged, and this instruction does not authorize a Rotom server change.
- **Evidence:** User decision recorded on 2026-09-16.
- **Outstanding:** None.

## 2026-09-16 — Add shared manual backup access for Jared and Fran

- **Files changed:** `00-Rotom-Change-Log.md`, `01-Rotom-Server-Inventory.md`, `05-Backup-and-Restore.md`, `06-Maintenance-and-Automation.md`, `07-Users-and-Permissions.md`.
- **Status:** Implemented and verified from supplied command output and the user's successful test.
- **Changes:** Recorded `/usr/local/bin/backup-to-nas` as the shared manual launcher for both human administrators. The launcher is `root:root` mode `0755` and invokes the protected `/usr/local/sbin/backup-to-unas` script through `sudo`. Jared retains the exact passwordless rule in `/etc/sudoers.d/update-to-nas`; Fran now has a separate exact-command rule in `/etc/sudoers.d/fran-backup-to-nas`. This grants Fran the same full Rotom backup operation without granting direct access to the NAS backup mount. The backup scope, repository, timer, retention, and protected script were not changed.
- **Evidence:** Supplied output confirms the shared launcher metadata, the Fran sudoers file as `root:root` mode `0440`, successful full sudoers validation, and a successful noninteractive permission check for Fran. The user subsequently confirmed that `backup-to-nas` worked for Fran. `/home/fran` was already included because the existing Restic job includes `/home`.
- **Outstanding:** Earlier per-user launchers were present during setup, but their final disposition was not shown. Treat `/usr/local/bin/backup-to-nas` as the canonical command and verify or remove redundant per-user copies in a separate reviewed cleanup if desired.

## 2026-09-16 — Establish authoritative on-server documentation controls

- **Files changed:** `00-Rotom-Change-Log.md`, `01-Rotom-Server-Inventory.md`, `06-Maintenance-and-Automation.md`, `07-Users-and-Permissions.md`, `08-Rotom-Directory-Tree.txt`.
- **Status:** Implemented and verified from supplied command output.
- **Changes:** Recorded `/home/rotom/documentation` as the authoritative on-server documentation directory. The directory contains `AGENTS.md` and `README.md`, owned by `rotom:rotom` with modes `0750` for the directory and `0640` for the files. Named and default ACLs give `jared` and `fran` read-only documentation access while preserving `rotom` as the writer. Recorded the separate `/home/jared/.codex/AGENTS.md` entry point used when Jared starts Codex outside the authoritative directory. The numbered legacy documentation set files remain expected content there; their presence on Rotom was not shown.
- **Evidence:** User-supplied `stat`, `getfacl`, and `sudo -u ... test` output from 2026-09-16. The output confirms the two control files, their ownership and modes, ACL entries, and successful read-only access tests for `jared` and `fran`. It also confirms `/home/jared/.codex/AGENTS.md` exists as `jared:jared` mode `0600`. No document contents or authentication material were used as evidence.
- **Outstanding:** Copy the numbered files `00` through `08` into `/home/rotom/documentation` only through a separate reviewed synchronization task, then verify their metadata and update this documentation from observed results. Configure and verify a per-user Codex entry point for `fran` only if Fran will run Codex.

## 2026-09-16 — Consolidate the complete legacy documentation set

- **Files changed:** All nine maintained files, `00-Rotom-Change-Log.md` through `08-Rotom-Directory-Tree.txt`.
- **Status:** Documentation only.
- **Changes:** Reissued the complete set with the proper name **legacy documentation set**, the agreed informal aliases, a consistent document index, and references to the change-log maintenance rules in every topic document. Retained the recorded media UID 127 / primary GID 5000 changes, isolated NFS findings, service-account administration policy, unchanged backup model, and clearly labeled future GIDs and mounts. Preserved valid source content and earlier dated history.
- **Evidence:** The existing project documents, the previously supplied command output, and the naming and documentation-maintenance decisions in this conversation. This consolidation does not claim a new server audit or live configuration change.
- **Outstanding:** Replace the uploaded numbered set with these nine files. Remove any superseded `00-UPDATE-NOTES.md` upload so `00-Rotom-Change-Log.md` is the single maintained change log. Previously documented live-verification gaps remain open.

## 2026-09-16 — Define “legacy documentation set”

- **Files changed:** `00-Rotom-Change-Log.md`, `01-Rotom-Server-Inventory.md`.
- **Status:** Documentation only.
- **Changes:** Established **legacy documentation set** as the proper name, with “project docs,” “rotom project docs,” and “project documentation” as informal aliases. Retained the earlier aliases “project documents” and “project reference files,” explicitly included the directory tree, and completed the source map with the server inventory itself. Clarified how supporting evidence and future documents relate to the set.
- **Evidence:** The user's request to establish a consistent reference name and subsequent clarification of its capitalization and aliases; no server changes or new live checks.
- **Outstanding:** Replace the uploaded copies of these two documents with the updated versions.

## 2026-09-16 — Establish the ongoing change log

- **Files changed:** Renamed `00-UPDATE-NOTES.md` to `00-Rotom-Change-Log.md`; updated `01-Rotom-Server-Inventory.md` with a link and maintenance reminder.
- **Status:** Documentation only.
- **Changes:** Adopted the agreed filename, added the maintenance guide and entry template, and retained the initial documentation update below as the first historical record.
- **Evidence:** The user's filename decision and this document revision; no server changes or new live checks.
- **Outstanding:** Add this file to the project's uploaded references and replace any previously uploaded `00-UPDATE-NOTES.md` copy, so there is only one active change log.

## 2026-09-16 — Media identity and NAS access documentation

**Status:** Documentation only, incorporating previously recorded implementation evidence and separately labeled proposals. **Files changed:** 01–08, listed below; originally accompanied by `00-UPDATE-NOTES.md`.

The initial package contained complete replacement copies of all eight affected project documents, using their original filenames.

The original synced files in `sources/` were left unchanged. These replacements preserve still-valid inventory, configuration, operating procedures, and historical audit evidence. This was a documentation task: no Rotom, NAS, account, container, backup, or network settings were changed or freshly audited.

### Recorded configuration at this update

- Rotom's `media` account is UID **127**, primary GID **5000**, replacing GID **129**. The UID did not change.
- All five media Compose files show `PUID=127`, `PGID=5000`, and `UMASK=002`. Actual qBittorrent, Radarr, and Sonarr processes were also observed as `127:5000`; equivalent process checks were not supplied for Jellyfin and Prowlarr.
- `/mnt/nas-media` is **988:5000**, mode **2770**. Its `library` and `torrents` trees use GID 5000, group-writable files, and group-writable setgid directories. Existing owner UIDs were preserved. New qBittorrent content was recorded as `127:5000`.
- Both media and backup were reported in UNAS Isolated Mode. UNAS `rpc.mountd --manage-gids` and its server-side lookup explain why client supplementary GID 5000 alone failed while primary GID 5000 worked. Numeric IDs matter across hosts; a local `fwupd-refresh` label for 988 does not identify the intended NAS data owner.
- The adopted policy keeps Jared outside the media group for ordinary use and uses `sudo -iu media` for administration on Rotom. The conversation confirms normal Jared access was denied, but does not include a final account listing after the requested group-membership removal. The documents preserve that distinction.
- `/mnt/nas-rotom-backup` remains **988:988**, mode **0770**, with its existing Jared access and root backup service. Restic repository contents and backup policy are unchanged.

### Proposed architecture — not deployed

| Account | Current UID:primary GID | Proposed primary GID | Proposed mount |
|---|---:|---:|---|
| game-server | 995:985 | 5001 | /mnt/nas-game-server |
| smart-home | 126:128 | 5002 | /mnt/nas-smart-home, only if needed |
| web-host | 128:130 | 5003 | /mnt/nas-web-host, only if needed |

The proposed GIDs must be checked for availability on both hosts before implementation. UIDs remain unchanged. No proposal implies moving Palworld worlds, Home Assistant configuration, website data, or databases from their current local service directories. Future NAS data would need an explicit backup review because the current host Restic job excludes `/mnt`.

This is a model for ordinary service-account access. Existing sudo and Docker-daemon privileges still allow administrators to cross those account boundaries.

### Affected documents

| File | Main changes |
|---|---|
| [01-Rotom-Server-Inventory.md](01-Rotom-Server-Inventory.md) | Current identity overview; future architecture; corrected media access summary |
| [02-Docker-Services.md](02-Docker-Services.md) | Compose settings, process evidence, existing mounts, future service identity constraints |
| [03-Network-and-Domains.md](03-Network-and-Domains.md) | NFS identity behavior, mount-state qualifications, proposed shares |
| [04-NAS-and-Storage.md](04-NAS-and-Storage.md) | Numeric ownership/modes, setgid, isolated NFS behavior, unchanged backup, future storage pattern |
| [05-Backup-and-Restore.md](05-Backup-and-Restore.md) | Reconcile old GID 129 snapshots with current GID 5000; preserve backup access; future NAS coverage gap |
| [06-Maintenance-and-Automation.md](06-Maintenance-and-Automation.md) | Preserve current service identity through updates; read-only checks; future mount and backup planning |
| [07-Users-and-Permissions.md](07-Users-and-Permissions.md) | Updated account records, current versus historical access, administration policy, proposed migrations |
| [08-Rotom-Directory-Tree.txt](08-Rotom-Directory-Tree.txt) | Current identity annotations; preserved captured paths; proposed mounts separated from observed tree |

The shared-drive mount and contents observed on September 15 are retained as historical evidence. The later directory listing confirms a mountpoint directory only; it does not prove the share is currently mounted or establish its current contents. No guessed paths were added to the observed tree.

### Evidence and verification limits

Primary evidence is the original project files and the supplied command output and decisions in the historical “Torrent Seeding Explanation” conversation. Unrelated inventory and health observations retain their original September 14–15 audit dates. September 16 is the documentation revision date.

The permission documents also reference the upstream [nfs-utils mountd manual](https://github.com/linux-nfs/nfs-utils/blob/master/utils/mountd/mountd.man) for the distinction between supplementary and primary groups under `--manage-gids`.

No fresh all-account NAS access matrix, Jellyfin/Prowlarr process identity check, post-removal Jared group listing, shared-drive mount check, restore rehearsal, or new backup run was performed for this update. GIDs 5001–5003 and their mounts remain proposals throughout the package.
