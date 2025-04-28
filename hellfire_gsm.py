import serial
import time

def find_port():
    # You can modify this if your adapter shows up on a different port
    return "/dev/ttyUSB0"

def send_sms(port, number, message, count, delay):
    try:
        print(f"\n📡 Connecting to GSM modem on {port}...")
        ser = serial.Serial(port, baudrate=9600, timeout=5)
        time.sleep(2)  # Allow modem to initialize

        # Initialize modem
        ser.write(b'AT\r')
        time.sleep(1)
        ser.write(b'AT+CMGF=1\r')  # Set SMS mode to text
        time.sleep(1)

        for i in range(count):
            full_message = f"{message} #{i+1}"
            print(f"\n📨 Sending SMS [{i+1}/{count}] -> {number}")
            ser.write(f'AT+CMGS="{number}"\r'.encode())
            time.sleep(1)
            ser.write(full_message.encode() + b"\x1A")  # Ctrl+Z to send
            time.sleep(3)
            print("✅ Sent!")

            if i < count - 1:
                print(f"⏳ Waiting {delay} seconds before next message...")
                time.sleep(delay)

        ser.close()
        print("\n🔥 All messages sent successfully! Hellfire complete.")

    except Exception as e:
        print(f"\n❌ Error: {e}")

if __name__ == "__main__":
    print("\n🔥 HELLFIRE GSM - Scammer Tears Mode Activated 🔥")
    port = find_port()

    number = input("📲 Enter target phone number (e.g. +1234567890): ")
    message = input("💬 Enter SMS message content: ")

    try:
        count = int(input("🔁 How many times to send it? "))
        delay = float(input("⏱️ Delay between messages (in seconds)? "))
    except ValueError:
        print("❌ Invalid input. Exiting.")
        exit()

    send_sms(port, number, message, count, delay)
