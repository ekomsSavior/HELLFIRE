( H | E | L | L | F | I | R | E )
 
   open-source weaponry 

   _by ek0ms savi0r_

![hellfire](https://github.com/user-attachments/assets/6b036330-ca42-4f47-b38c-116390887824)

## What is Hellfire?

**Hellfire** is a real-world SMS flooding tool built for cybersecurity research, counter-scamming, and hacker education.  
It uses your own SIM card and GSM modem — not Twilio, not Nexmo, and **no third-party nonsense**.  
If a scammer hits your phone, **this is what hits back**.

Use cases

- SMS alert stress-testing

- Ethical counter-scamming

- OSINT and reply honeypots

- Spoof detection research (coming soon)

---

## 🛠 What You’ll Need

- **SIM800C USB GSM Modem**  

  Plug-and-play USB dongle with antenna.  

  [Amazon link](https://a.co/d/cWa05mU) or search: `SIM800C GSM USB dongle`

- **Prepaid M2M / IoT SIM Card (REQUIRED — standard phone SIMs often fail!)**  
  → These are designed for modems and work reliably:
  
    • Hologram.io Global IoT SIM  
    • 1NCE IoT SIM  
    • Things Mobile SIM  
    • Air Global Plan01s IoT SIM (Amazon)  

  → Must support **outgoing SMS** (not just data)  
  → Activate SIM at provider site  
  → **Wait up to 24 hours after activation** for SMS to work  
  → Format numbers like: `+1XXXXXXXXXX`

- **Kali Linux or any Debian-based distro**  

  - Just clone and run it

  - your SIM800C USB will be auto detected by kali if that is your host os.
    
  - if you are running a vm you have to attach the sim800c usb to the vm in > settings> USB> + ... before you start your vm. 

---

##  Installation & Execution

git clone https://github.com/ekomsSavior/HELLFIRE.git

cd HELLFIRE

- Activate your sim card

( buy it with cash and use a prepaid giftcard and anonymous creds to remain anonymous also use tails, tor and or proxies)

Insert your SIM card into the GSM dongle, then plug it in via USB.

Run Hellfire

sudo python3 hellfire_gsm.py

Example Run

Enter target phone number (e.g. +1234567890): +13332224444
Enter SMS message content: HACK THE PLANET
How many times to send it? 100
Delay between messages (in seconds, can be decimal): 0.001

[1/10] HACK THE PLANET #1
[2/10] HACK THE PLANET #2
...
[✔] All messages sent successfully. Hellfire operation complete.

![FOURTYONE](https://github.com/user-attachments/assets/ec9febfb-3481-456d-bfe2-4d44869f8b95)


Tips for Success-

  Use full number format (+1...)

  Use short delays (e.g. 0.05) for rapid bursts   
  

🛡 Disclaimer

This tool is for ethical cybersecurity research only.

By using Hellfire, you agree to-

Only target systems and numbers you control or have permission to test.

the user assumes full responsibility of thier actions when using HELLFIRE choose your path wisely.


**Coming Soon**

  SMS origin tracing

  Honeypot reply traps

  Scam message fingerprinting

  Integration with Phish Hunter and Info Glow

Made with light and love by
ek0ms savi0r

https://github.com/ekomsSavior

https://instagram.com/ekoms.is.my.savior

https://medium.com/@ekoms1

