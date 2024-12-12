
from header import *
import portscan
import os

def displayHomeText():
    global ip
    print(f"{color(col='yellow', text=str('IP Set as ->'))} {color(col='green', text=str(ip))}")
    colPr(col='white', text="Please choose an option:")
    colPr(col='white', text="1. Set Ip")
    colPr(col='white', text="2. Run Port Scan")
    colPr(col='white', text="3. Track Network Connections")
    colPr(col='white', text="4. Analyze Network Traffic")
    colPr(col='white', text="5. Full Security Scan (All Options)")
    colPr(col='white', text="6. Exit")

def setIP():
    pp = input("Enter IP >> ")
    clearScreen()
    return pp

def netScan():
    global ip
    if ip == "EMPTY":
        colPr(col="red", text="Error: Please set an IP address first!")
        return
    scan = portscan.PortScanner(ip)
    scan.scanResults()

def clearScreen(): 
    os.system('cls' if os.name == 'nt' else 'clear')

ip = "EMPTY"

def main():
    global ip 
    displayHomeText()
    colPr(col='yellow', text="Please enther the option you'd like to use")
    choice = input(">> ")
    if choice == 'clear': clearScreen()
    elif choice in ['1', 'set ip']:
        ip = setIP()
    elif choice in ['2', 'port scan']:
        scan = netScan()
    elif choice in ['6', 'exit', 'end', 'terminate']:
        colPr(col='yellow', text="Exiting");
        return True
    else:
        colPr(col='red', text='Error - not an option')


colPr(col='white', text="\nWelcome to the Home Security System")
while True:
    if main():
        break
