#! python

# WMI query to list all properties and values of the root/cimv2:Win32_OperatingSystem class.
# To use WMI in Python, install the Python for Windows extensions:
# http://sourceforge.net/projects/pywin32/files/pywin32/
# This Python script was generated using the WMI Code Generator, Version 9.02
# http://www.robvanderwoude.com/wmigen.php

import sys
import win32com.client

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
colItems = objSWbemServices.ExecQuery( "SELECT * FROM Win32_OperatingSystem" )

for objItem in colItems:

    print( " OS                        : " + str(objItem.Caption) + str(objItem.Version) + " " + str(objItem.CSDVersion) + " (" + str(objItem.OSArchitecture) + ")" )
    print( " Serial Number             : " + str( objItem.SerialNumber ) )
    print( " Last Bootup               : " + str(objItem.LastBootUpTime)[0:14] )
    print( " Organization              : " + str(objItem.Organization) )
    print
