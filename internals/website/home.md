# Rotom Support

Rotom Support is the private operations portal for people who administer, troubleshoot, or recover Rotom. It combines the authoritative numbered Runbook with supplementary architecture context and task-oriented guides.

## Choose a section

- [Runbook: current state and operating procedures](runbook/index.md) contains the approved numbered source set for configuration, maintenance, security, troubleshooting, and recovery.
- [Architecture: systems and relationships](architecture/index.md) explains how the PVE host, Rotom VM, applications, network, NAS storage, and protection layers fit together.
- [Guides: choose a task](guides/index.md) routes common administration and recovery work to the controlling Runbook procedure.

## What is authoritative

The numbered Runbook is the sole operational authority. Architecture and Guides explain and route the material; they do not replace Runbook procedures, expand Rotom Support membership, or establish a separate maintenance contract.

This portal is a read-only view generated from a verified Git revision. Make documentation changes in the canonical repository, update the Runbook first when operational facts or procedures change, and then reconcile affected supplementary pages.

## RS commands

Use `rs` in a terminal on Rotom or the Mac to manage the Rotom Support checkout.

| Command | Purpose |
| --- | --- |
| `rs path` | Show the checkout selected by the helper. |
| `rs status` | Show the local working tree and cached upstream status without contacting GitHub. |
| `rs pull` | Update a clean checkout from its upstream when a fast-forward is safe. |
| `rs check` | Validate the checkout and compare it with GitHub. |
| `rs help` | Show all supported commands and their safeguards. |

For documentation changes, follow the [RS maintenance contract](runbook/00-Rotom-Change-Log.md#current-documentation-maintenance-rules). If `rs` reports that its repository is missing, first verify the checkout's location and GitHub origin. The helper uses the current RS checkout when run inside it; otherwise, configure the checkout path in `${XDG_CONFIG_HOME:-$HOME/.config}/rs/repository` (or the legacy `rr/repository` file when the RS configuration is absent). Run `rs path` from outside the checkout and then `rs status` to verify the selection. Do not bypass a failed helper safety check.

On the Mac, if the verified checkout is `$HOME/Documents/ChatGPT/rotom-support` and its origin is the expected SSH URL, this updates the resolver and checks the result:

```sh
repo="$HOME/Documents/ChatGPT/rotom-support"
if [ -d "$repo/.git" ] && [ "$(git -C "$repo" remote get-url origin)" = "git@github.com:jaredwines/rotom-support.git" ]; then
  mkdir -p "${XDG_CONFIG_HOME:-$HOME/.config}/rs"
  printf '%s\n' "$repo" > "${XDG_CONFIG_HOME:-$HOME/.config}/rs/repository"
  (cd /tmp && rs path && rs status)
else
  echo "Checkout or expected GitHub origin not found; no configuration changed."
fi
```
