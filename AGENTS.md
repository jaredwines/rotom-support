# Rotom Support Agent

This repository is the Git working copy for the Rotom Support (RS).

## Documentation authority

**Terminology:** Within Rotom work, **RC** means **Rotom Compose**: the reviewed non-secret deployment configuration in `/srv/rotom/stacks` and its Git history. “Update RC” means follow the canonical **Update Rotom Compose Configuration** procedure in `runbook/02-Docker-Services.md`; it does not itself authorize a service lifecycle change or an RS update unless the verified Compose change changes RS-documented state.

- Rotom Support (RS) is all intentionally tracked content in this repository. Local untracked files, ignored files, temporary artifacts, generated output, and Git's internal metadata are not part of RS merely because they exist inside the checkout.
- `runbook/` is the primary authority for Rotom's documented current state, operation, troubleshooting, configuration, maintenance, migration, recovery, Docker, networking, storage, backups, permissions, and services.
- `runbook/00-Rotom-Change-Log.md` is the canonical RS maintenance contract.
- `runbook/01-Rotom-Server-Inventory.md` is the starting index when unsure which RS document applies.
- Follow the current RS rather than duplicating its detailed procedures in this file.
- Preserve historical entries as historical evidence. Do not silently rewrite old records to match current state.

The current numbered runbook files `00`–`08` live under `runbook/` in the checkout resolved by `rs path`. They are the Core Numbered Reference Set within RS. Relative links between these files remain within that directory.

Other tracked repository areas are RS components with narrower roles:

- `architecture/` explains system relationships and orientation; it does not replace current runbook facts or procedures.
- `guide/` contains supplementary task and recovery guidance; it is outside the Core Numbered Reference Set and does not become a canonical operational fact owner. Validate it with `internals/tooling/test-guides`.
- `internals/` contains agent support, repository tooling, validation, and publication implementation; it is not an operational runbook collection.
- Root-level tracked files provide repository governance, navigation, and Git metadata or configuration appropriate to their individual purpose.

Do not infer authority from RS membership alone. If another RS component conflicts with the applicable current runbook about Rotom's operation or documented current state, preserve and report the discrepancy, investigate it, and resolve the current guidance in favor of the runbook authority rather than silently rewriting either source.

Available Sources is a separate, manually maintained publication or reference destination. It does not define RS membership and must not be treated as the complete repository. Jared remains responsible for manually replacing its contents.

## RS Git workflow

Use the `rs` helper for normal RS Git operations.

On Rotom, when the sandbox restricts `.git` or GitHub access, request the needed execution access **before** running `rs check`, `rs commit`, `rs push`, or other affected Git operations. Do not first run them in the restricted sandbox. Follow the stop-on-failure rules in `runbook/00-Rotom-Change-Log.md`.

- Use `rs path` to resolve the active local checkout.
- Use `rs status`, `rs check`, `rs pull`, `rs diff`, `rs log`, `rs commit`, and `rs push` rather than bypassing the helper's guardrails.
- Do not hard-code Mac or Rotom checkout paths in shared workflow instructions.
- Do not commit unrelated changes, temporary files, or secrets.
- If an `rs` safety check fails, stop and report the problem rather than automatically resetting, cleaning, merging, rebasing, force-pushing, or otherwise bypassing the guardrail.

When an RS update is authorized, follow `runbook/00-Rotom-Change-Log.md` for the environment-specific completion workflow.

## Safety

Never place passwords, API tokens, SSH private keys, VPN credentials, WireGuard private keys, cookies, Home Assistant secrets, Restic passwords, or other authentication material in this repository.

Use `vim` instead of `nano` for command-line text editing.
