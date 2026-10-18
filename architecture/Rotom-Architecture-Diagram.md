# Rotom Architecture Diagram

This overview shows the documented relationships between Rotom, its services, storage, and backup systems. It is supplementary orientation, not an operational procedure. The [server inventory](../runbook/01-Rotom-Server-Inventory.md) and linked numbered runbooks are authoritative. Evidence is drawn from the documented state as of 2026-10-17; this diagram is not a new live audit.

```mermaid
flowchart TB
    Users["LAN users and devices"]
    Internet["Internet users"]
    DNS["Cloudflare DNS"]
    Gateway["UniFi gateway / LAN DNS"]
    NAS["UniFi NAS"]

    subgraph PVE["Proxmox VE host · pve"]
        VMBackup["Rotom VM Backup<br/>VZDump · VMID 100"]
        PVERestic["PVE Restic Backup"]
        subgraph Rotom["Rotom · Debian VM 100"]
            NPM["Nginx Proxy Manager"]
            Platform["Platform<br/>Homepage, Glances, Arcane,<br/>Cloudflare DDNS, Rotom Support"]
            Libraries["Libraries<br/>Jellyfin, Radarr, Sonarr, Prowlarr,<br/>qBittorrentVPN, RomM, Paperless"]
            Websites["Hosted Websites<br/>Aloha Millworks, Jared Wines"]
            Smart["Smart Home<br/>Home Assistant, Homebridge"]
            Games["Game Servers<br/>Palworld Jared and Fran"]
            Local["VM-local application state<br/>and deployment files · /srv/rotom"]
            GuestRestic["Rotom Restic Backup"]
        end
    end

    subgraph Storage["NAS storage and protection"]
        LibData["Libraries NFS<br/>including Paperless media"]
        Snapshots["NAS snapshots"]
        GuestRepo["Rotom Restic repository"]
        VMRepo["VM backup archives"]
        PVERepo["PVE Restic repository"]
    end

    Users --> Gateway
    Internet --> DNS --> Gateway
    Gateway -->|"Named web routes"| NPM
    Users -->|"Selected direct LAN ports"| Rotom
    Users -->|"Game traffic"| Games
    NPM --> Platform & Libraries & Websites & Smart
    NPM -->|"Trusted-LAN route"| PVE
    Platform -. "DDNS updates" .-> DNS
    Platform & Libraries & Websites & Smart & Games --> Local
    Libraries --> LibData
    NAS --- LibData & Snapshots & GuestRepo & VMRepo & PVERepo
    LibData --> Snapshots
    Local --> GuestRestic --> GuestRepo
    Rotom --> VMBackup --> VMRepo
    PVE --> PVERestic --> PVERepo
```

Rotom Restic protects selected guest-local data and excludes `/mnt`; the VM backup protects the VM disk, not external NFS data. NAS snapshots protect NAS-resident Libraries data. These layers are complementary; see [backup and restore](../runbook/05-Backup-and-Restore.md). The NAS also has empty service-boundary mounts for Game Servers, Smart Home, and Hosted Websites; their application state remains VM-local. Access depends on DNS, gateway forwarding, proxy rules, and application controls; a diagrammed route alone does not establish public exposure. See [network and domains](../runbook/03-Network-and-Domains.md) and the [architecture system overview](Rotom-Architecture-System.md) for details and evidence qualifications.
