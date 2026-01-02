# WARNING: VIBE CODED AI SLOP

# Sun Home Light Bar Control

## Tools used
- PacketLogger on MacOS via iPhone over USB with Bluetooth Debug profiles from Apple (requires dev account)
- Cline inside VSCode
- LLM; mostly Gemini 3 Pro Preview via openrouter. Actually economical in my opinion. Project cost was maybe a couple of dollars in compute.

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

# Turn RGB Strip ON
python control.py rgb_on

# Turn RGB Strip OFF
python control.py rgb_off

# Set RGB Color
python control.py rgb 255 0 0

# Listen for manual changes
python control.py listen
```

## Protocol Details

**Device Name**: `iStar&5B13`

| Function | Command (Hex) |
|----------|--------------|
| ON       | `CC 23 33`   |
| OFF      | `CC 24 33`   |
| RGB ON   | `C1 23 1C`   |
| RGB OFF  | `C1 24 1C`   |

- **Write Char**: `FFD9`
- **Notify Char**: `FFD4`
