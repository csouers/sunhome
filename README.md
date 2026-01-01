# Sun Home Light Bar Control

This python project provides control of a Bluetooth RGB Light Bar by sun home. The lightbar features two light bars, one downward/desk facing (adjustable white), and the other ceiling facing (rgb). It also features a microphone that enables sound-controlled light effects. 

## Requirements

- Python 3.12+
- `bleak` library

## Setup

1. Create a virtual environment:
   ```bash
   pyenv virtualenv 3.12.9 sunhome-ble
   pyenv local sunhome-ble
   ```
2. Install dependencies:
   ```bash
   pip install bleak
   ```

## Usage

Control the main white light:

```bash
# Turn ON
python control.py on

# Turn OFF
python control.py off
```

## Protocol Details

**Device Name**: `iStar&5B13`

| Function | Command (Hex) |
|----------|--------------|
| ON       | `CC 23 33`   |
| OFF      | `CC 24 33`   |

- **Write Char**: `FFD9`
- **Notify Char**: `FFD4`
