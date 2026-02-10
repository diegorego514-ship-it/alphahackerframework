import socket
import sys
import os
import argparse

# AlphaHackerFramework - V0.1.0 (IPv4 & Penetration Testing Dual Hacker Framework IPSec Version)

SERVER_HOST = "192.168.87.149"
SERVER_PORT = 1024
SERVER_LIST = SERVER_HOST, SERVER_PORT

s = socket
s.socket(socket.AF_INET, socket.SOCK_STREAM);
s.setdefaulttimeout(10) # Set time in seconds to avoid false positives from antivirus

try:
    print("[*] Your System is under penetration tests, there's no need to worry");
except:
    print("[*] Recommendation - always update your devices and remember to update your antivirus softwares regularly to avoid new potential vulnerabilities");
else:
    print("[*] Your system has been compromised, too bad. Want to try again?");
