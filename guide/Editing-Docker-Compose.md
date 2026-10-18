# Editing Docker Compose on Rotom

**Artifact class:** Supplementary RS guide; outside the Core Numbered Reference Set

A Compose file describes how Docker runs an application. This is a quick map; check the [Docker runbook](../runbook/02-Docker-Services.md) and live state before making changes.

## Where things live

| Purpose | Path |
|---|---|
| Compose files | `/srv/rotom/stacks/<domain>/<project>/compose.yaml` |
| Application data and configuration | `/srv/rotom/appdata/<domain>/` |
| Protected inputs and secrets | `/srv/rotom/secrets/<domain>/` |
| Library content | `/mnt/nas-libraries/` |

Not every project has a matching secrets directory. Keep secret contents private. Application data may also live on the NAS or in Docker volumes; check the project's existing mounts before editing.

## Workload domains and containers

These domains are folders that group related applications. For each project below, substitute its folder name into the Compose path above. The inventory is a snapshot; check current state before relying on it.

| Domain | Project folder | What it runs |
|---|---|---|
| `platform` | `nginx-proxy-manager` | Nginx Proxy Manager routes web traffic and manages TLS. |
| `platform` | `homepage` | Homepage is the dashboard; Glances supplies system monitoring. |
| `platform` | `arcane` | Arcane manages Docker applications. |
| `platform` | `cloudflare-ddns` | Cloudflare DDNS updates DNS when the public address changes. |
| `platform` | `mkdocs-rr` | Rotom Support serves the documentation site. |
| `libraries` | `jellyfin` | Streams media. |
| `libraries` | `radarr`, `sonarr` | Manage movies and TV shows. |
| `libraries` | `prowlarr` | Manages indexers for library applications. |
| `libraries` | `qbittorrentvpn` | Downloads torrents through a VPN. |
| `libraries` | `romm` | Manages the game library; its database and Valkey containers support it. |
| `libraries` | `paperless` | Organizes documents; its database and broker containers support it. |
| `hosted-websites` | `alohamillworks.com`, `jaredwines.com` | Serve the two websites. |
| `game-servers` | `palworld-jared`, `palworld-fran` | Run the two Palworld servers. |
| `smart-home` | `home-assistant`, `homebridge` | Provide home automation and smart-home integrations. |

The `platform/rotom-docs` Compose file is an inactive rollback stack, not an active service.

## Website addresses

| Address | Purpose |
|---|---|
| `rotom.casa` | Homepage dashboard. |
| `support.rotom.casa` | Private Rotom Support documentation. |
| `docs.rotom.casa` | Legacy address that redirects to the Support runbook. |
| `pve.rotom.casa` | Restricted access to the Proxmox interface. |
| `alohamillworks.com` | Aloha Millworks website. |
| `jaredwines.com` | Jared Wines website. |

Other application routes and access restrictions are maintained in [Network and Domains](../runbook/03-Network-and-Domains.md#2-current-access-paths); a DNS name alone does not prove a route is active.

## Before editing

Confirm the exact project and its existing Compose inputs, inspect the file, and compare live state with the runbook. Establish a verified recovery point first. Preserve existing ownership, networks, mounts, and persistent data. If live state differs from the runbook, stop and investigate. Use `vim` to edit, validate the exact configuration without printing secrets, and verify the affected service afterward. See [Docker Services](../runbook/02-Docker-Services.md) and [Backup and Restore](../runbook/05-Backup-and-Restore.md) for the applicable procedures.
