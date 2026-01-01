import asyncio
import sys
from bleak import BleakScanner, BleakClient

TARGET_NAME = "iStar&5B13"
CMD_UUID = "0000ffd9-0000-1000-8000-00805f9b34fb"

# Commands
CMD_ON = bytes.fromhex("CC 23 33")
CMD_OFF = bytes.fromhex("CC 24 33")

async def control_light(command):
    print(f"Scanning for {TARGET_NAME}...")
    device = await BleakScanner.find_device_by_name(TARGET_NAME)
    
    if not device:
        print(f"Error: {TARGET_NAME} not found. Ensure it is not connected to another device.")
        return False
        
    print(f"Connecting to {device.address}...")
    try:
        async with BleakClient(device) as client:
            print(f"Connected: {client.is_connected}")
            
            try:
                if command == "on":
                    print("Sending ON...")
                    await client.write_gatt_char(CMD_UUID, CMD_ON)
                elif command == "off":
                    print("Sending OFF...")
                    await client.write_gatt_char(CMD_UUID, CMD_OFF)
            except Exception as e:
                if "The value's length is invalid" in str(e):
                    # This error is expected but the command still works
                    pass
                else:
                    raise e
            
            print("Done.")
            return True
    except Exception as e:
        print(f"Error: {e}")
        return False

def main():
    if len(sys.argv) != 2 or sys.argv[1].lower() not in ["on", "off"]:
        print("Usage: python control.py [on|off]")
        sys.exit(1)
        
    asyncio.run(control_light(sys.argv[1].lower()))

if __name__ == "__main__":
    main()
