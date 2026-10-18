# Editing Docker Compose on Rotom

**Artifact class:** Supplementary repository guide; not a Rotom Support or Available Sources member
**Document role:** Beginner's companion to the authoritative Docker, storage, and identity runbooks
**RS index:** [01 - Rotom Server Inventory](../runbook/01-Rotom-Server-Inventory.md)
**Docker authority:** [02 - Docker Services](../runbook/02-Docker-Services.md)

This guide helps an administrator prepare and review a small, authorized Compose change. It does not authorize a change or replace a service-specific procedure. A Compose file describes containers and their settings; Docker runs those containers. A *project* can contain multiple services, so one command may affect more than the service you intended. A volume or bind mount connects a container to persistent data. Losing a container does not necessarily remove that data, but changing a mount can make the application use the wrong data or fail.

**Before starting:** Identify the requested change and its expected effect, the exact service and project, who uses it, a suitable interruption window, and a verified recovery point. If these are unclear, stop and investigate with an administrator. Changes to data, identities, networks, ports, images, secrets, or shared services need their own scoped review. Docker administration is root-equivalent; do not grant Docker group membership just to follow this guide. Never share passwords, tokens, environment-file contents, logs containing credentials, or rendered configuration containing secrets.

## 1. Find and understand the target

In a terminal on Rotom, run the following to locate the authoritative checkout. A command is entered by typing it and pressing Enter; the resulting path is output, not another command.

**Read-only**

```bash
rs path
```

Expect the checkout path. Open its `runbook/01-Rotom-Server-Inventory.md` for the subject index and [02, Current Service Contracts](../runbook/02-Docker-Services.md#2-current-service-contracts) for the service. The runbook records supported Compose definitions under `/srv/rotom/stacks/<domain>`, application data under `/srv/rotom/appdata/<domain>`, and protected inputs under `/srv/rotom/secrets/<domain>`. These are different purposes; do not assume a service account's home directory is its deployment directory. The inventory is dated evidence, so check the live target too.

Use the exact container name and path established from RS; placeholders below are not literal names. Jared normally needs `sudo` for Docker; an authorized Docker-group administrator may omit it. Docker commands can reveal sensitive information, so use the restricted formats shown and do not paste unredacted output into tickets or chat.

**Read-only**

```bash
sudo docker compose ls --all
sudo docker inspect CONTAINER --format 'compose={{index .Config.Labels "com.docker.compose.project.config_files"}} project={{index .Config.Labels "com.docker.compose.project"}} running={{.State.Running}}'
```

The first lists projects; the second shows the container's recorded Compose file(s), project and running state. Replace `CONTAINER` with the exact known container name. If it is absent, labels are missing, multiple files are listed, or the path differs from RS, stop and investigate; do not guess which file is authoritative. Overrides, an `.env` file, a project name, or a different working directory can affect the result. Determine all inputs and the original invocation before proceeding. Do not print environment files or use unrestricted `docker inspect`.

Inspect the existing Compose file locally using `sudo vim -R /absolute/path/to/compose.yaml` if needed for read access; `-R` opens it read-only. Press `Esc`, type `:q`, then press Enter to exit. Replace the path with the confirmed one. Do not copy its sensitive contents into a report. Compare its service names, image, ports, mounts, network mode or networks, environment variable *names*, user settings and other relevant values with [02, Service Contracts](../runbook/02-Docker-Services.md#2-current-service-contracts), [02, Docker Networking](../runbook/02-Docker-Services.md#3-docker-networking), and the specific storage and identity runbooks. Environment variables configure an application; their values can be credentials. `user`, `PUID`, `PGID` and `UMASK` have image-specific meanings; their absence does not imply a default identity you can safely change. Check the service's documented contract, not another service's numbers. A bind mount maps a host path to a container path; a named volume is managed by Docker. Note read-only flags and whether an expected NAS mount is actually the correct filesystem; a local directory alone is not proof. See [02, NAS-Backed Container Safety](../runbook/02-Docker-Services.md#4-nas-backed-container-safety) and [07, Ownership and Permission Contracts](../runbook/07-Users-and-Permissions.md#2-ownership-and-permission-contracts).

**Read-only**

```bash
stat -c '%u:%g %a %n' /absolute/path/to/compose.yaml
getfacl -cp /absolute/path/to/compose.yaml
```

These show numeric owner/group, mode and access rules. Use `sudo` only if access requires it. Record them privately for comparison after editing. If access is denied, a mount is missing, or live state conflicts with RS, stop and investigate the discrepancy; do not fix ownership or create missing mount directories to make it match. Preserve existing owners, modes, ACLs, UID/GID values, mounts, networks and persistent data. See [07, Current Identity and Access Model](../runbook/07-Users-and-Permissions.md#1-current-identity-and-access-model).

## 2. Prepare recovery and inspect the baseline

Before editing, identify a verified, accessible prior copy of the **exact** Compose file and any required companion files, and a recovery procedure appropriate to the service. Confirm its source, date, scope, and metadata; a Compose copy alone is not a backup of databases or application data. Use the applicable [05 - Backup and Restore](../runbook/05-Backup-and-Restore.md) procedure to establish a recovery point; do not improvise a restore. Keep sensitive copies protected. Record the target, approved change, existing service health, and recovery location without recording secrets. If a verified recovery point or the restoration scope is unknown, stop.

With the exact original inputs and working directory established, validate the baseline. Substitute the verified path, and add any confirmed original options or additional files in their original order; otherwise stop. `config --quiet` checks the configuration without printing the rendered model, which could expose secrets.

**Read-only**

```bash
sudo docker compose -f /absolute/path/to/compose.yaml config --quiet
```

Success normally prints nothing and returns to the prompt. An error or warning about missing variables, files, or invalid configuration is a stop: investigate before editing. This check does not prove the application works, the mount is correct, or the service can start. For a known supported website, [02, Read-only preflight](../runbook/02-Docker-Services.md#5-read-only-preflight) describes additional scoped checks. Other services require their own checks.

## 3. Make one small edit in Vim

Only after the target, permissions and recovery are confirmed, open the exact file. For a root-owned file where your account cannot write, use `sudo`; do not change ownership or permissions to make editing easier.

**Changes Rotom**

```bash
sudo vim /absolute/path/to/compose.yaml
```

Vim opens in **Normal mode**. Use arrow keys to move. Press `i` to enter **Insert mode** and type the intended change; look for `-- INSERT --`. Press `Esc` to return to Normal mode. Type `:wq` and press Enter to save and exit. To discard **unsaved** edits, press `Esc`, type `:q!` and press Enter. `:q!` cannot undo a previous save. If Vim warns about an existing swap file, an unexpected new file, or a permission problem, stop and investigate rather than overriding it. Saving changes the file on disk but does not apply it to running containers.

### Fictional example — do not apply to Rotom

This imaginary excerpt illustrates only a small change to a non-sensitive application setting. It is not a verified Rotom service or a recommendation to deploy it. Change `LOG_LEVEL: "info"` to `LOG_LEVEL: "debug"` only in a disposable practice file, if practicing; the application would need to support that setting.

```yaml
services:
  example:
    image: example.invalid/app:1
    environment:
      LOG_LEVEL: "info"
    volumes:
      - example-data:/data
    networks:
      - example-net
volumes:
  example-data:
networks:
  example-net:
```

`services:` contains a service named `example`. Its `image` identifies the software; `environment` contains a setting; the dash begins each item in the volume and network lists. The top-level definitions name the volume and network. This example contains no real paths, identities, or credentials.

## 4. YAML essentials

- Indent with spaces, never tabs. Items at the same level must align; nested settings must be indented consistently under their parent. Follow the existing file's spacing.
- A colon separates a key from its value. List entries start with `- ` and align with other entries in that list. A misplaced dash or space can change structure or cause an error.
- Quote values that could be mistaken for numbers, booleans, or YAML syntax, such as `"002"` or `"true"`; preserve existing quoting and variable references. Compose also interprets `$` expressions, so do not change them casually. Quoting does not make a secret safe to publish.
- Do not duplicate keys or rename services, mounts, networks, or paths as an incidental edit. YAML may parse while expressing the wrong configuration.

## 5. Review, validate, apply and verify

Compare the edited file with the verified prior copy using a private local review. A diff can display credentials: do not share it unredacted. Confirm that only the intended lines changed, indentation and variable references remain correct, and ownership, mode and ACLs match the baseline. Repeat the `stat` and `getfacl` checks above. Stop if anything unexpected changed.

Repeat the baseline `docker compose ... config --quiet` command with the **same complete inputs and context**. Expect no output on success; correct an error in Vim or restore the prior file using the verified recovery procedure. Do not apply an invalid file. Even a valid file can have the wrong values, so review both syntax and intent.

Applying a saved edit is a separate state-changing action. [02, Impact and authorization](../runbook/02-Docker-Services.md#3-impact-and-authorization) warns that `docker compose up -d` can create or replace a project. Its [procedure](../runbook/02-Docker-Services.md#7-procedure) is specifically for an absent, confirmed-active supported website with matching inputs; it does **not** authorize arbitrary edits or prescribe a universal deployment command. For a planned edit, first establish an authorized, service-specific application and rollback procedure, exact project/files and affected services. If that procedure is not available, stop and obtain it rather than guessing. A targeted `up -d` may recreate containers, interrupt connections and affect dependencies or other project services; agree on the impact and window first. Never use `down`, volume removal, image deletion, or a broad restart as an automatic rollback.

After the authorized procedure, check the selected container's status and restart count, relevant sanitized logs, and the service's documented health or user-facing test. For the two websites, [02, Verification](../runbook/02-Docker-Services.md#8-verification) gives the specific checks and expected responses; do not substitute its ports for other applications. A running container alone is not proof the application works. Check that the intended data and dependencies are accessible and that no unrelated service was affected. Record sanitized evidence and report any mismatch.

## 6. If something fails

- **Validation fails before application:** Do not apply. Read the error and line number, inspect indentation, list markers, quotes and variable references. Re-edit or restore the exact verified prior file using the applicable recovery procedure, then validate again. Existing containers continue using their previous configuration until separately changed.
- **Startup or health fails after application:** Stop further changes; preserve the container and relevant sanitized logs. Follow [02, Rollback or recovery](../runbook/02-Docker-Services.md#9-rollback-or-recovery). Restore a prior configuration or image only from a verified applicable recovery point with explicit scope; restoring a file alone does not revert an already recreated container. Follow the service-specific recovery and verification procedure. Do not delete volumes, containers, images or data as a shortcut.
- **Permission denied:** Check the exact file and access rules; use only the necessary authorized privilege. Do not use `chmod 777` or change service ownership.
- **Mount or data missing:** Stop; check the documented filesystem and source. Do not create a replacement directory or rewrite NAS ownership.
- **Unexpected project, network, port, identity, or other discrepancy:** Stop and compare live evidence with RS; investigate before proceeding.
- **Still uncertain:** Preserve sanitized errors, target, baseline, change and checks performed; ask an administrator. Never include authentication material.
