import os
import subprocess

def run_nmap_scan(target):
    print("Running Nmap scan...")
    subprocess.run(["nmap", "-sV", target])

def check_firewall_status():
    print("Checking firewall status...")
    os.system("sudo ufw status")

def main():
    print("1. Run Nmap Scan")
    print("2. Check Firewall Status")
    choice = input("Select an option: ")
    if choice == "1":
        target = input("Enter target IP: ")
        run_nmap_scan(target)
    elif choice == "2":
        check_firewall_status()
    else:
        print("Invalid option")

if __name__ == "__main__":
    main()
