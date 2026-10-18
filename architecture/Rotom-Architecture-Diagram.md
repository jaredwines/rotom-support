# Rotom Architecture Diagram

Rotom is the Debian application VM running on the Proxmox host `pve`. Its applications use both VM-local storage and a separate UniFi NAS. These diagrams explain the documented architecture as of 2026-10-17; they are an orientation, not an operational procedure or a new live audit. The [server inventory](../runbook/01-Rotom-Server-Inventory.md) and numbered runbooks own current facts and procedures.

## 1. Systems and services

The host runs Rotom as VM 100. Docker Compose organizes its applications into five service domains. The NAS is a separate system on the LAN.

```mermaid
flowchart TB
    PVE["Proxmox VE host · pve<br/>192.168.1.68"]
    ROTOM["Rotom · Debian VM 100<br/>192.168.1.69"]
    NAS["UniFi NAS<br/>192.168.1.70"]
    PVE -->|"hosts"| ROTOM
    ROTOM -->|"NFS storage"| NAS
    PVE -->|"backup destinations"| NAS
    ROTOM --> PLATFORM["Platform<br/>Proxy, Homepage, Glances,<br/>Arcane, DDNS, Rotom Support"]
    ROTOM --> LIBRARIES["Libraries<br/>Jellyfin, Radarr, Sonarr, Prowlarr,<br/>qBittorrentVPN, RomM, Paperless"]
    ROTOM --> WEBSITES["Hosted Websites<br/>Aloha Millworks, Jared Wines"]
    ROTOM --> GAMES["Game Servers<br/>Palworld · Jared and Fran"]
    ROTOM --> SMART["Smart Home<br/>Home Assistant, Homebridge"]
```

## 2. How requests reach services

DNS answers a name lookup; it does not carry the application request. The solid arrows show request paths, while dotted arrows show DNS lookups or updates.

```mermaid
flowchart LR
    LAN["LAN users and devices"]
    PUBLIC["Internet users"]
    DNS["Cloudflare DNS"]
    LOCALDNS["LAN DNS"]
    GATEWAY["UniFi gateway"]
    NPM["Nginx Proxy Manager<br/>on Rotom"]
    WEB["Web applications<br/>and hosted websites"]
    PRIVATE["Rotom Support and PVE UI<br/>trusted-LAN proxy routes"]
    DIRECT["Selected direct LAN listeners<br/>and Palworld UDP ports"]
    DDNS["Cloudflare DDNS<br/>on Rotom"]
    PUBLIC -. "DNS lookup" .-> DNS
    LAN -. "DNS lookup" .-> LOCALDNS
    DDNS -. "updates DNS" .-> DNS
    PUBLIC -->|"where forwarding allows"| GATEWAY
    GATEWAY -->|"web requests"| NPM
    LAN -->|"web requests"| NPM
    LAN -->|"direct access"| DIRECT
    NPM -->|"hostname routes"| WEB
    NPM -->|"trusted-LAN access list"| PRIVATE
```

A DNS answer or proxy route alone does not establish public access: gateway forwarding, NPM rules, and application controls also matter. Some LAN services have direct listeners; Palworld uses UDP rather than NPM. See [network and domains](../runbook/03-Network-and-Domains.md) for exact routes and boundaries.

## 3. Data and protection

Each arrow describes a different protection path. The NAS holds both application data and backup destinations; these are separate roles.

```mermaid
flowchart LR
    LOCAL["Rotom VM-local data<br/>including /srv/rotom"]
    LIB["NAS Libraries data<br/>including Paperless media"]
    PVEHOST["PVE host configuration<br/>and recovery material"]
    RESTIC["Rotom Restic Backup<br/>selected guest-local data"]
    VM["Rotom VM Backup<br/>PVE VZDump · VM 100"]
    PVER["PVE Restic Backup"]
    SNAP["NAS snapshots"]
    RREPO["NAS: Rotom Restic repository"]
    VREPO["NAS: VM backup archives"]
    PREPO["NAS: PVE Restic repository"]
    LOCAL --> RESTIC --> RREPO
    LOCAL -->|"VM disk"| VM --> VREPO
    PVEHOST --> PVER --> PREPO
    LIB --> SNAP
```

- **Rotom Restic** protects selected guest-local paths; it excludes `/mnt` and does not back up the external Libraries data.
- **Rotom VM Backup** protects the VM disk, not the contents of external NFS mounts.
- **NAS snapshots** protect NAS-resident Libraries data. Paperless media and its VM-local database need compatible recovery points.
- **PVE Restic** protects selected PVE host configuration and recovery material separately from the Rotom VM.

Game Servers, Smart Home, and Hosted Websites also have empty NAS service-boundary mounts; their current application state remains VM-local. NAS snapshot protection was owner-confirmed, while exact NAS control-plane settings were not exported during the documented review. See [backup and restore](../runbook/05-Backup-and-Restore.md), [NAS and storage](../runbook/04-NAS-and-Storage.md), and the detailed [architecture system overview](Rotom-Architecture-System.md).
