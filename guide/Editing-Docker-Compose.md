# Editing Docker Compose on Rotom

**Artifact class:** Supplementary RS guide; outside the Core Numbered Reference Set

A Compose file describes how Docker runs an application. Use this map and walkthrough to plan a focused change; the [Docker runbook](../runbook/02-Docker-Services.md) and live state remain authoritative. Commands below are examples, not authorization to change a service.

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

The former `platform/rotom-docs` rollback stack was removed on 2026-10-18; `platform/mkdocs-rr` serves Rotom Support.

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

## Editing walkthrough

This example uses the Aloha Millworks website to show how to locate and validate a project. It does not prescribe a particular change. The [Docker runbook](../runbook/02-Docker-Services.md#diagnose-and-recover-a-container-or-docker-backed-website) records its current deployment and checks; its website recovery procedure does not authorize Compose edits. Use the relevant runbooks and service-specific checks for other projects.

1. **Define the change and impact.** Identify the exact setting, expected result, affected service and potential interruption. Confirm authorization and the current service contract in the [Docker runbook](../runbook/02-Docker-Services.md), and consult the network, storage and permissions runbooks as applicable. Check existing Compose inputs, including overrides, environment files, mounts, project name and working directory. Do not print secret inputs or a rendered configuration that could contain them.

2. **Inspect and compare.** For this example, identify the existing container and its recorded Compose file, then inspect the file with an editor without exposing protected values. Substitute the exact project and container for another service.

   **Read-only**

   ```bash
   sudo docker inspect alohamillworks.com \
     --format 'status={{.State.Status}} compose={{index .Config.Labels "com.docker.compose.project.config_files"}}'
   sudo vim -R /srv/rotom/stacks/hosted-websites/alohamillworks.com/compose.yaml
   ```

   Compare the actual file, inputs, mounts, image, ports, ownership and service state with the relevant runbooks. Stop and investigate any mismatch or unclear scope; do not change either side simply to make them agree. Do not create a missing NAS bind source as a local directory.

3. **Prepare recovery.** Identify and verify an appropriate recovery point for the configuration and any affected persistent data before editing. A copy of Compose alone does not back up application data or guarantee a usable image. Follow [Backup and Restore](../runbook/05-Backup-and-Restore.md) for selecting and verifying recovery points. Record the original state and plan how to restore it without overwriting newer data. Stop if recovery is uncertain.

4. **Make the smallest change.** Edit the confirmed file with `vim`, using the permissions required for that file. Preserve existing service ownership, UID/GID, volumes, networks, paths and protected inputs unless the specific change explicitly requires otherwise. Review the resulting difference without displaying secrets.

5. **Validate before applying.** From the correct project context, use the same Compose files and other inputs as the live project. For this example, only after confirming that this file and its context are the complete inputs:

   **Read-only**

   ```bash
   sudo docker compose -f /srv/rotom/stacks/hosted-websites/alohamillworks.com/compose.yaml config --quiet
   ```

   A successful exit validates the configuration; it does not prove the application will work. If validation fails, fix or restore the configuration before proceeding. Errors may contain sensitive values; review them privately before sharing.

6. **Apply only the authorized change.** Select the precise service and an appropriate application method after assessing its dependencies and downtime. Compose can recreate containers; do not assume applying a file is interruption-free. The command and recovery steps depend on the project and change, so do not reuse a website recovery command blindly. Avoid `down`, volume removal, image cleanup or broad restarts as routine editing steps.

7. **Verify and recover if needed.** Check the affected container's status and logs, expected listener and service-specific behavior; for this example, use the direct and proxied checks in the [website procedure](../runbook/02-Docker-Services.md#diagnose-and-recover-a-container-or-docker-backed-website). Check that unrelated services were not affected and persistent mounts still point to the intended sources. If verification fails, preserve evidence and stop; restore the prior configuration or image only from the verified recovery point and within the confirmed scope. Do not delete containers, volumes or data as an automatic rollback. Document the outcome and any remaining discrepancy.
