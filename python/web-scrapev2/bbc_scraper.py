# Juan Rodriguez
# This script scrapes the BBC news website for headlines related to Ukraine.
import os 
folder = os.path.join(os.path.dirname(os.path.abspath(__name__)), 'headlines') # makes the file path in the same folder as the script
os.makedirs(folder, exist_ok=True) # makes the folder
import requests
import bs4
import time 

if requests.get()