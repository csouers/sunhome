# Active Context

## Current Focus
Initial setup and reverse engineering of the White LED On/Off command.

## Recent Changes
- Initialized Memory Bank.
- Identified target device: `iStar&5B13` (`2B:80:03:E4:5B:13`).

## Next Steps
[Completed] Capture and analyze On/Off packets.
[Completed] Implement toggle control.
[Completed] Fix "Invalid Length" error in `control.py` (must suppress error).
[Completed] Implement feedback verification via Notifications (`FFD4`).
[Completed] Add `listen` mode to monitor manual changes.
[Completed] Document usage in README.

## Active Decisions
- Using `bleak` for BLE interface.
- Python 3.12.9 as the runtime.
- Focusing strictly on White LED On/Off first to validate control.
- Device UUID on macOS confirmed as `C74BD8CC-1FE7-8A1B-A243-1A382EF2E31B`.
- Protocol confirmed: `CC 23 33` (ON) and `CC 24 33` (OFF). Note: Device returns "Invalid Length" error for these commands but executes them. Warning must be suppressed in code.
- State Confirmation: Listening to notifications on `FFD4` allows confirming ON (`23`) vs OFF (`24`) state.
