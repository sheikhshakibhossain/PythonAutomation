import os
import sys
import time
import getpass
import subprocess

import asyncio
import pyrcrack
from rich.console import Console
from rich.prompt import Prompt

import pywifi
from pywifi import const



def get_wifi_interfaces():
    interfaces = []
    iwconfig_output = subprocess.check_output(['iwconfig'])
    iwconfig_output = iwconfig_output.decode('utf-8')
    for line in iwconfig_output.split('\n'):
        if 'IEEE 802.11' in line:
            interface = line.split()[0]
            interfaces.append(interface)
    return interfaces


def set_monitor_mode(interface):
    try:
        subprocess.check_call(['sudo', 'ifconfig', interface, 'down'])
        subprocess.check_call(['sudo', 'iwconfig', interface, 'mode', 'monitor'])
        subprocess.check_call(['sudo', 'ifconfig', interface, 'up'])
        print(f'Successfully set {interface} to monitor mode')
    except subprocess.CalledProcessError as e:
        print(f'Error setting {interface} to monitor mode: {e}')


def set_managed_mode(interface):
    cmd = ['sudo', 'ifconfig', interface, 'down']
    subprocess.run(cmd, check=True)
    cmd = ['sudo', 'iwconfig', interface, 'mode', 'managed']
    subprocess.run(cmd, check=True)
    cmd = ['sudo', 'ifconfig', interface, 'up']
    subprocess.run(cmd, check=True)
    print(f"{interface} set to managed mode")


async def scan_for_targets():
    """Scan for targets, return json."""
    console = Console()
    console.clear()
    console.show_cursor(False)
    airmon = pyrcrack.AirmonNg()

    interface = Prompt.ask(
	'Select an interface',
	choices=[a['interface'] for a in await airmon.interfaces])

    async with airmon(interface) as mon:
        async with pyrcrack.AirodumpNg() as pdump:
            async for result in pdump(mon.monitor_interface):
                console.clear()
                console.print(result.table)
                await asyncio.sleep(2)


# asyncio.run(scan_for_targets())


def scan_wifi():
    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[1] # get the first wireless interface
    iface.scan() # scan for available Wi-Fi networks
    results = iface.scan_results()

    ssids = []
    for result in results:
        if result.ssid:
            ssids.append(result.ssid)

    return ssids

print(scan_wifi())

# def main():
#     # Check if user has root privileges
#     if os.geteuid() != 0:
#         print("This program requires root privileges to run.")
#         print("Please run the program with 'sudo'.")
#         sys.exit(1)

#     wifi_interfaces = get_wifi_interfaces()
#     print(wifi_interfaces)
#     set_monitor_mode(wifi_interfaces[1])
#     set_managed_mode(wifi_interfaces[1])


# if __name__ == '__main__':
#     main()

