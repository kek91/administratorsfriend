#! python

# WMI query to list all properties and values of the root/cimv2:Win32_ComputerSystem class.
# To use WMI in Python, install the Python for Windows extensions:
# http://sourceforge.net/projects/pywin32/files/pywin32/
# This Python script was generated using the WMI Code Generator, Version 9.02
# http://www.robvanderwoude.com/wmigen.php

import sys
import win32com.client

def bytesto(bytes, to, bsize=1024):
    # Ex: print('mb= ' + str(bytesto(314575262000000, 'm')))
    a = {'k' : 1, 'm': 2, 'g' : 3, 't' : 4, 'p' : 5, 'e' : 6 }
    r = float(bytes)
    for i in range(a[to]):
        r = r / bsize
    numstring = str(r)
    return float(numstring[:numstring.find('.')+3])

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
colItems = objSWbemServices.ExecQuery( "SELECT * FROM Win32_ComputerSystem" )

for objItem in colItems:
    print( " Domain                    : " + str( objItem.Domain ) )
    print( " User                      : " + str( objItem.UserName ) )
    print( " Computer                  : " + str( objItem.Model ) )
    print( " RAM                       : " + str(bytesto(int(objItem.TotalPhysicalMemory), 'g') ) + " GB" )
