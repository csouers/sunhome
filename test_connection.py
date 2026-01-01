import asyncio
from bleak import BleakClient

from bleak import BleakScanner

# "2B:80:03:E4:5B:13"
TARGET_NAME = "iStar&5B13"

async def main():
    print(f"Scanning for {TARGET_NAME}...")
    device = await BleakScanner.find_device_by_name(TARGET_NAME)
    
    if not device:
        print(f"Device {TARGET_NAME} not found. Ensure it is not connected to another device.")
        return

    print(f"Found device: {device.address}")
    
    print(f"Connecting to {device.address}...")
    try:
        async with BleakClient(device) as client:
            print(f"Connected: {client.is_connected}")
            
            print("\nServices:")
            for service in client.services:
                print(f"[Service] {service.uuid} ({service.description})")
                for char in service.characteristics:
                    print(f"  [Characteristic] {char.uuid} ({','.join(char.properties)})")
                    
                    if "read" in char.properties:
                        try:
                            value = await client.read_gatt_char(char.uuid)
                            print(f"    Value: {value.hex()}")
                        except Exception as e:
                            print(f"    Read failed: {e}")

            print("\nDisconnecting...")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    asyncio.run(main())
