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
        - `56 R G B F0 00 00 64 00 AA`: Set RGB Color (Length 10 bytes).
          - `R`, `G`, `B`: 0-255 (00-FF).
          - `F0` (Byte 4): RGB Mode.
          - `0F` (Byte 4): White Mode.
          - `FF` (Byte 5): Warm White (00 to FF).
          - `FF` (Byte 6): Cool Mode (00 to FF).
          - `64` (Byte 7): Brightness (0x03-0x64).
          - `00` (Byte 8): Fixed.
          - `AA` (Byte 9): Fixed.

## Design Patterns
- **Discovery**: Locate device by MAC.
- **Connection**: Maintain connection or connect-on-demand (BLE limit).
- **Command Pattern**: Encapsulate device commands (On, Off, SetColor) into a class.
