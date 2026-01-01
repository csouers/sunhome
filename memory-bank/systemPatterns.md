# System Patterns

## Architecture
- **Controller**: Python script running on macOS (using `bleak`).
- **Communication**: Bluetooth Low Energy (BLE).
- **Protocol**: Unidentified proprietary protocol (likely similar to Magic Home/Keepads).
    - **Write Command** (UUID `FFD9`): 3-byte structure `CC XX 33`.
        - **IMPORTANT**: Must use **Write Request** (`response=True`), but suppress the "Invalid Length" error.
    - **Notifications** (UUID `FFD4`): 12-byte status starting with `66` and ending with `99`.
        - Byte 2 (Index 2): State (`23` = ON, `24` = OFF).
    - **Commands**:
        - `CC 23 33`: ON
        - `CC 24 33`: OFF

## Design Patterns
- **Discovery**: Locate device by MAC.
- **Connection**: Maintain connection or connect-on-demand (BLE limit).
- **Command Pattern**: Encapsulate device commands (On, Off, SetColor) into a class.
