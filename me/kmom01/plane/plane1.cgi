#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Execute as cgi-skript and send a correct HTTP header.
"""


# To write pagecontent to sys.stdout as bytes instead of string
import sys
import codecs


#Enable debugging of cgi-.scripts
import cgitb
cgitb.enable()


# Send the HTTP header
print("Content-Type: text/html;charset=utf-8")
print("Content-Type: text/plain;charset=utf-8\n")
print("")

"""Function plane beräknar din höjd, hastighet och temperatur utanför ett flygplan"""
def plane():
    """
    Funktionen plane ger höjd, hastighet och temperatur som resultat
    """
    height = 1100 * 3.28084
    print("Din hojd over havet ar ", height, "feet\n")
    velocity = 1000 /1.609344
    print("Din hastighet ar ", velocity, "mph\n")
    temperature = (-50 * 9) / 5 + 32
    print("Temperaturen utanfor flygplanet ar ", temperature, "farenheit")
plane()
