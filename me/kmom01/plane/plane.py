"""Functionen plane beräknar din höjd, hastighet och temperatur utanför ett flygplan"""
def plane():
    """
    Functionen plane ger höjd, hastighet och temperatur som resultat
    """

    Höjd = input("Skriv höjden över havet(meter)")
    HöjdP = int(Höjd) * 3.28084
    Hastighet = input("Skriv hastighet(km/h)")
    hastighetP = int(Hastighet) /1.609344
    Temperatur = input("Skriv temperatur utanför flygplanet(Celsius)")
    temperaturP = (int(Temperatur) * 9) / 5 + 32

    print("Höjd över havet"+str(HöjdP)+"feet\n", "Hastighet "+str(hastighetP)+ \
          " mph\n", "Temperatur utanför flygplanet"+str(temperaturP)+"farenheit"
         )
