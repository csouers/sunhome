# Product Context

## The Problem
The Sun Home light bar is controlled via a proprietary app. The user wants to integrate it into a smart home system (Home Assistant), requiring a reverse-engineered Python controller.

## The Solution
A Python script/library that interfaces with the device over Bluetooth Low Energy (BLE), mimicking the official app's commands.

## Device Details
- **Name**: `iStar&5B13`
- **MAC**: `2B:80:03:E4:5B:13`
- **Known Services**: `FFD0`, `FFD5`
- **Known Characteristics**:
    - `FFD4` (Service `FFD0`): Status Notification (Read/Notify).
    - `FFD9` (Service `FFD5`): Command Write.
- **Commands identified**:
    - ON: `CC 23 33`
    - OFF: `CC 24 33`

## User Experience Goals
- Simple CLI or Python API to toggle the light.
- Reliable connection and state management.
