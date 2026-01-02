# Active Context

## Current Focus
Implementing RGB Strip On/Off control based on reverse-engineered logs.

## Recent Changes
- Initialized Memory Bank.
- Identified target device: `iStar&5B13` (`2B:80:03:E4:5B:13`).
- Added RGB control support to `control.py`.
- **New**: Identified commands for separate RGB Strip control: `C1 23 1C` (ON) and `C1 24 1C` (OFF).

## Next Steps
- [x] Implement `rgb_on` and `rgb_off` commands in `control.py`.
- [x] Verify if these commands trigger specific notifications (confirmed: No).
- [x] Update `control.py` CLI to support `rgb_on` and `rgb_off`.
- [ ] Refine error handling for disconnected states.

## Active Decisions
- Using `bleak` for BLE interface.
- Python 3.12.9 as the runtime.
- Focusing strictly on White LED On/Off first to validate control.
- Device UUID on macOS confirmed as `C74BD8CC-1FE7-8A1B-A243-1A382EF2E31B`.
- Protocol confirmed: `CC 23 33` (ON) and `CC 24 33` (OFF). Note: Device returns "Invalid Length" error for these commands but executes them. Warning must be suppressed in code.
- State Confirmation: Listening to notifications on `FFD4` allows confirming ON (`23`) vs OFF (`24`) state.
- **New Protocol**: RGB Strip uses `C1` prefix instead of `CC`.
    - `C1 23 1C`: RGB ON (No notification)
    - `C1 24 1C`: RGB OFF (No notification)
