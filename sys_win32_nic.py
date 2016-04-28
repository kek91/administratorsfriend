#! python

# WMI query to list all properties and values of the root/cimv2:Win32_ComputerSystem class.
# To use WMI in Python, install the Python for Windows extensions:
# http://sourceforge.net/projects/pywin32/files/pywin32/
# This Python script was generated using the WMI Code Generator, Version 9.02
# http://www.robvanderwoude.com/wmigen.php

import sys
import win32com.client
import socket

try:
    strComputer = sys.argv[1]
except IndexError:
    strComputer = "."

try:
    strUsername = sys.argv[2]
except IndexError:
    strUsername = ""

try:
    strPassword = sys.argv[3]
except IndexError:
    strPassword = ""

objWMIService = win32com.client.Dispatch( "WbemScripting.SWbemLocator" )
objSWbemServices = objWMIService.ConnectServer( strComputer, "root/cimv2", strUsername, strPassword )
colItems = objSWbemServices.ExecQuery( "SELECT * FROM Win32_NetworkAdapter" )

ip_address = socket.gethostbyname_ex(strComputer)
ip_address = repr(ip_address[2]).strip("[]'")

for objItem in colItems:

    if objItem.NetConnectionStatus == 2: # 2 = Connected
        #print(" NIC                       : " + str(objItem.Name) + " (Label: " + str(objItem.NetConnectionID) + ")")
        print(" " + str(objItem.NetConnectionID) + " - " + str(objItem.Name))
        print(" MAC address               : " + str(objItem.MACAddress))
        print(" IP address                : " + str(ip_address) )
        print
