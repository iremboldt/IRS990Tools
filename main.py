import os
import xml.etree.ElementTree as ET
import zipfile
import pandas as pd
import requests
import urllib.request
import IRS990Tools.py

directory=input("Enter target directory: ")
IRSTools=IRS990Tools(directory)
#print("Would you like to enter more than one year? Y/N")
#choice=input("")
#if choice == "Y" or "N":
# if choice == "Y":
years=input("Enter target year: ")
IRSTools.get990s(years)
IRSTools.extractzip():
statecode=input("Enter target state code: ")
statecode=statecode.upper()
if statecode.len() > 2:
 statecode=input("State code must be two characters, try again: ")
IRSTools.removeStates(statecode)
citycode=input("Enter target city: ")
IRSTools.removeCity(citycode)
IRSTools.xmltocsv()
