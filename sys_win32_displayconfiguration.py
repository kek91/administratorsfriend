#! python

# WMI query to list all properties and values of the root/cimv2:Win32_DisplayConfiguration class.
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
colItems = objSWbemServices.ExecQuery( "SELECT * FROM Win32_DisplayConfiguration" )

for objItem in colItems:
	print( " GPU                       : " + str( objItem.DeviceName ) )
	print
