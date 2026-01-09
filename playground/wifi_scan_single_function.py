
from os import waitstatus_to_exitcode
import subprocess
import sys
import re
import time

def scan_networks():

    try:
        if sys.platform.startswith('win'):
            # time.sleep(1)
            command = ['netsh', 'wlan', 'show', 'networks', 'mode=bssid']
            output = subprocess.check_output(
                command,
                stderr=subprocess.STDOUT,
                text=True,
                encoding='utf-8')

            ssids = set()
            ssid_pattern = re.compile(r"^SSID\s+\d+\s*:\s*(.+)$")

            for line in output.splitlines():
                if "SSID" in line:
                    print("DEBUG: ", line)

                line = line.strip()
                match = ssid_pattern.match(line)

                if match:
                    ssid = match.group(1).strip()
                    if ssid and ssid != "<Hidden Network>":
                        ssids.add(ssid)
                        print(f"Found network: {ssid}")

            for ssid in sorted(ssids):
                self.wifi_networks.append(ssid)

    except subprocess.CalledProcessError as e:
        self.wifi_networks.append(f"Error scanning: {e.output}")
    except Exception as e:
        self.wifi_networks.append(f"An error occurred: {e}")

scan_networks()