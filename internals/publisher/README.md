# Rotom Publisher Overview

This directory contains the implementation and checks for the private Rotom Support repository mirror. It is an RS component supporting publication; the runbook remains the primary authority for Rotom operations and current state.

## Files

- [`build-input.py`](build-input.py) prepares the site input and navigation from tracked repository files, excluding paths with a component beginning with `.git`. The same paths are excluded from raw downloads.
- [`sync`](sync) synchronizes the deployment checkout, builds and validates the site, and publishes it.
- [`publish-source`](publish-source) is the compatibility entry point for the updater.
- [`rotom-support-sync.service`](rotom-support-sync.service) and [`rotom-support-sync.timer`](rotom-support-sync.timer) define the scheduled update.
- [`test-publisher.py`](test-publisher.py) tests source selection, navigation, and rejection of symlinks in an isolated fixture.

For the documented publication workflow, verification, and recovery guidance, see [Documentation and Synchronization Workflow](../../runbook/06-Maintenance-and-Automation.md#6-documentation-and-synchronization-workflow). Follow the [RS maintenance contract](../../runbook/00-Rotom-Change-Log.md#current-documentation-maintenance-rules) when changing this implementation; installed copies and live publication are separate from repository edits.
