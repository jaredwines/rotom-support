# Rotom Guides

Rotom Guides provide practical starting points for specific tasks and recovery situations. They bring together the relevant steps and references to help administrators find their way through more involved work.

For recovery after the loss of both PVE and Rotom, see [PVE and Rotom Total-Loss Recovery](pve-and-rotom-total-loss-recovery.md). The [Runbook](../runbook/index.md) remains the authoritative source for current operational facts and procedures.

## RS commands

Use `rs` in a terminal on Rotom or the Mac to manage the Rotom Support checkout.

| Command | Purpose |
| --- | --- |
| `rs path` | Show the checkout selected by the helper. |
| `rs status` | Show the local working tree and cached upstream status without contacting GitHub. |
| `rs pull` | Update a clean checkout from its upstream when a fast-forward is safe. |
| `rs check` | Validate the checkout and compare it with GitHub. |
| `rs help` | Show all supported commands and their safeguards. |

For documentation changes, follow the [RS maintenance contract](../runbook/00-Rotom-Change-Log.md#current-documentation-maintenance-rules). If `rs` reports that its repository is missing, first verify the checkout's location and GitHub origin. The helper uses the current RS checkout when run inside it; otherwise, configure the checkout path in `${XDG_CONFIG_HOME:-$HOME/.config}/rs/repository` (or the legacy `rr/repository` file when the RS configuration is absent). Run `rs path` from outside the checkout and then `rs status` to verify the selection. Do not bypass a failed helper safety check.

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
