# Tech Context

## Development Environment
- **OS**: macOS
- **Language**: Python 3.12.9
- **Virtual Env**: pyenv virtualenv `sunhome-ble`
- **Dependencies**:
    - `bleak`: BLE client library.

## Bluetooth Tools
- **PacketLogger**: macOS built-in for capturing traffic.
- **Wireshark**: For analyzing `.pklg` or `.pcap` files.
- **nRF Connect**: Mobile app for inspecting BLE services.

## Device constraints
- **Single Connection**: Device stops advertising when connected.
- **Services**: `FFD0`, `FFD5`.
