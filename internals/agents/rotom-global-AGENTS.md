> Reference backup of the active global Codex instructions at `~/.codex/AGENTS.md`. Keep this copy in sync when the active file changes.

# Rotom Agent

This machine is the Rotom Debian VM.

## Rotom administration

Use the Rotom Support (RS) as the primary reference for Rotom administration, troubleshooting, configuration, migration, recovery, Docker, networking, storage, backups, permissions, maintenance, and services.

Resolve the local RS checkout with:

`rs path`

RS is all intentionally tracked content in the repository. The numbered documents `00`–`08` in the checkout's `runbook/` directory are the primary authority for Rotom's documented current state and operations. Other tracked areas, including `guide/`, are RS components with narrower roles and do not override the runbook.

Before changing Rotom:

1. Resolve the RS checkout with `rs path`.
2. Read the repository `AGENTS.md`.
3. Read the relevant RS. Start with `runbook/01-Rotom-Server-Inventory.md` when unsure which document applies.
4. Inspect the current live configuration.
5. Compare live state with the documented state.
6. Make the smallest targeted change.
7. Verify the result.

If live state conflicts with the RS, report and investigate the discrepancy. Do not silently change either side merely to make them match.

## Safety

Preserve existing service ownership, UID/GID contracts, Docker volumes, networks, NAS paths, and persistent data.

Inspect an existing `compose.yaml` before editing it.

Treat NAS data, Palworld saves, Home Assistant configuration, websites, Docker databases/configuration, certificates, and Restic repositories as critical persistent data.

Never expose passwords, tokens, SSH private keys, VPN credentials, WireGuard private keys, cookies, Home Assistant secrets, Restic passwords, or other authentication material.

Never use `chmod 777`.

Before destructive actions, verify the exact target and impact first.

Use `vim` instead of `nano`.

Use `sudo` only when needed.

## RS maintenance

Treat the RS checkout as read-only during normal Rotom work unless RS or Git maintenance is explicitly authorized.

For an authorized RS update:

- follow the repository `AGENTS.md`;
- follow the canonical maintenance contract in `runbook/00-Rotom-Change-Log.md`;
- use `rs` for routine Git operations;
- do not bypass an `rs` safety failure with reset, clean, merge, rebase, force-push, or ad-hoc Git operations;
- do not commit unrelated changes, temporary files, or secrets.

Available Sources replacement remains manual by Jared.

## GitHub

Run normal GitHub operations as `jared`.

Do not copy Jared's GitHub private key into service accounts.
