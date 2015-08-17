#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Funktionen plane beräknar din höjd, hastighet och temepratur utanför ett flygplan"""
def plane():
    """
    Functionen plane ger höjd, hastighet och temperatur som resultat
    """
    height = 1100 * 3.28084
    velocity = 1000 /1.609344
    temperature = (-50 * 9) / 5 + 32

    
    print("Din hojd over havet ar ", height, "feet", "Din hastighet ar ", velocity, \
    "mph", "Temperaturen utanfor flygplanet ar ", temperature, "farenheit")

    plane()
