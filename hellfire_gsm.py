import serial
import time

def print_banner():
    print(r"""
   _   _   _   _   _   _   _   _  
  / \ / \ / \ / \ / \ / \ / \ / \ 
 ( H | E | L | L | F | I | R | E )
  \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ 
         by ek0ms savi0r    
    """)

def find_port():
    return "/dev/ttyUSB0"

def send_sms(port, number, message, count, delay):
    try:
        print(f"\n[+] Connecting to GSM modem on {port}...")
        ser = serial.Serial(port, baudrate=9600, timeout=5)
        time.sleep(2)

        # Initialize modem
        ser.write(b'AT\r')
        time.sleep(1)
        ser.write(b'AT+CMGF=1\r')
        time.sleep(1)

        for i in range(count):
            full_message = f"{message} #{i+1}"
            print(f"[{i+1}/{count}] {full_message}")
            ser.write(f'AT+CMGS="{number}"\r'.encode())
            time.sleep(0.25)  # Bare minimum for modem to accept number
            ser.write(full_message.encode() + b"\x1A")
            time.sleep(delay)

        ser.close()
        print("\n[✔] All messages sent successfully. Hellfire operation complete.")

    except Exception as e:
        print(f"\n[!] Error: {e}")

if __name__ == "__main__":
    print_banner()
    port = find_port()

    number = input("Enter target phone number (e.g. +1234567890): ")
    message = input("Enter SMS message content: ")

    try:
        count = int(input("How many times to send it? "))
        delay = float(input("Delay between messages (in seconds, can be decimal): "))
    except ValueError:
        print("[!] Invalid input. Exiting.")
        exit()

    send_sms(port, number, message, count, delay)
