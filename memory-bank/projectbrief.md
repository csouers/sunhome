# Project Brief: Sun Home Bluetooth Light Bar Control

## Overview
This project aims to reverse engineer the Bluetooth protocol of the "Sun Home" Light Bar and provide a Python interface for control. The ultimate goal is Home Assistant integration.

## Scope
- Reverse engineering the BLE protocol for the `iStar&5B13` device.
- Implementing a Python library to control the device.
- Initial focus: White LED On/Off control.
- Future focus: RGB control, effects, and Home Assistant integration.

## Goals
1. Establish reliable connection via Python (Bleak).
2. Identify protocol structure (Commands for On/Off, Color, etc.).
3. Create a stable control script.
