# ⚠️ WiFi Jammer (Local Use Only)

This is a **WiFi deauthentication tool** built in Python for **educational and testing purposes only**. It allows you to scan nearby WiFi networks, list connected clients, and perform deauth attacks to test network resilience.

> ❗ This tool only works in **Kali Linux** or other Linux distributions with wireless adapter support in **monitor mode**.

---

## 🚨 Disclaimer

> 🛑 This tool is intended for **educational use only**.  
> 🔒 Use it **only on your own network** or with **explicit permission**.  
> ❗ Unauthorized use of this tool is **illegal** and against ethical hacking guidelines.  
> ⚠️ The author is not responsible for misuse or damage caused.

---

## 📦 Requirements

- Python 3.x
- `aircrack-ng` tools:
  - `airmon-ng`
  - `airodump-ng`
  - `aireplay-ng`
- Root access (sudo)

---

## 🔧 Setup Instructions

1. Clone this repository or copy the script:

   ```bash
   git clone https://github.com/your-username/wifi-jammer.git
   cd wifi-jammer
Run with root privileges:

bash
Copy
Edit
sudo python3 wifi_jammer.py
📋 How to Use
Enter wireless interface (e.g., wlan0)

Start monitor mode (script will attempt automatically)

Scan for networks

Press CTRL+C when your target appears

Enter target BSSID and channel

Scan for clients

Press CTRL+C when clients appear

Enter client MAC address

Use FF:FF:FF:FF:FF:FF to target all clients

Confirm deauth attack

Deauth packets will be sent continuously

🛠️ Helpful Commands (Manual)
bash
Copy
Edit
# Show available interfaces
iwconfig

# Start monitor mode manually
sudo airmon-ng start wlan0

# Scan for WiFi networks
sudo airodump-ng wlan0mon

# Scan for clients
sudo airodump-ng --bssid <BSSID> -c <CHANNEL> wlan0mon
📌 Tips
Use iwconfig to verify if your interface is in Monitor Mode

If wlan0 remains the same in monitor mode, do not append mon (e.g., use wlan0, not wlan0mon)

Some clients only appear if they're actively using the network

If errors appear related to permissions or socket(PF_PACKET), ensure you're running as root

✅ Author & Credits
Developed by [Nasim Khan / Nasim7045]

Contributions and feedback welcome!

🧠 Reminder
"With great power comes great responsibility."
