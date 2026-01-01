import asyncio
from bleak import BleakScanner, BleakClient

TARGET_NAME = "iStar&5B13"
CMD_UUID = "0000ffd9-0000-1000-8000-00805f9b34fb"

# Commands
CMD_ON = bytes.fromhex("CC 23 33")
CMD_OFF = bytes.fromhex("CC 24 33")

async def main():
    print(f"Scanning for {TARGET_NAME}...")
    device = await BleakScanner.find_device_by_name(TARGET_NAME)
    
    if not device:
        print("Device not found. Is it connected to another device?")
        return
        
    print(f"Connecting to {device.address}...")
    async with BleakClient(device) as client:
        print(f"Connected: {client.is_connected}")
        
        print("Sending ON...")
        await client.write_gatt_char(CMD_UUID, CMD_ON)
        print("Sent ON command")
        
        await asyncio.sleep(3)
        
        print("Sending OFF...")
        await client.write_gatt_char(CMD_UUID, CMD_OFF)
        print("Sent OFF command")
        
        print("Disconnecting...")

if __name__ == "__main__":
    asyncio.run(main())
