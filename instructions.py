# ================================================================
# WiFi Jammer - LOCAL USE ONLY (for testing and educational use)
# ================================================================
# 
# 💡 How to Find Required Details Before Running:
# 
# 1. 🔍 Find Your Wireless Interface Name:
#     - Run: `iwconfig` or `ip a`
#     - Look for something like `wlan0` (your WiFi adapter)
#
# 2. 📡 Enable Monitor Mode (if not using auto mode from script):
#     - Run: `sudo airmon-ng start wlan0`
#     - Monitor mode interface will usually be `wlan0mon` or still `wlan0`
#     - Check: `iwconfig` again to verify mode = "Monitor"
#
# 3. 📶 Scan for Nearby WiFi Networks:
#     - Run: `sudo airodump-ng wlan0mon`
#     - Wait for networks to populate
#     - Note down:
#         - BSSID: MAC address of the target router (e.g., 10:27:F5:68:EB:82)
#         - CH: Channel number (e.g., 5)
#         - ESSID: Network name (for identification only)
#
# 4. 🧑‍💻 Scan for Connected Clients:
#     - Run: `sudo airodump-ng --bssid <BSSID> -c <channel> wlan0mon`
#     - Note down:
#         - Station MAC (client MACs connected to the router)
#         - These are targets for the deauth attack
#
# 5. ⚠️ Important Notes:
#     - Use sudo/root to run this script
#     - Make sure NetworkManager doesn't interfere (stop/restart as needed)
#     - Some clients (e.g., phones) only appear when actively using WiFi
#     - This script is for **local network testing** and **educational use only**
#
# ================================================================
