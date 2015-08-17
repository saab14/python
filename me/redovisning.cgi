#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Update this.

"""


# To write pagecontent to sys.stdout as bytes instead of string
import sys
import codecs


#Enable debugging of cgi-.scripts
import cgitb
cgitb.enable()


# Send the HTTP header
#print("Content-Type: text/plain;charset=utf-8")
print("Content-Type: text/html;charset=utf-8")
print("")


# Here comes the content of the webpage 
content = """<!doctype html>
<meta charset="utf-8">
<title>Min redovisnings-sida</title>
<pre>
Min Redovisnings-sida
==============================================================================
Kmom02
======
Jag har inte programmerat med python tidigare men syntaxen i Python gör att 
koden blir väldigt lättläst. Indenteringen som är obligatorisk hjläper att 
läsa koden ännu lättare fast jag tyckte inte att den är obligatorisk. 
Ibland när jag osäker på att jag har gjort rätt, vill jag snabb testa 
koden utan att bryr mig om indenteringen och även kommentar.

Jag tyckte inte heller om semikolon som man kan skriva det men pylint varnar. 
Det känns onödigt. När det gäller långa rad, det är bra att pylint varnar om. 
Validering för mig var enkelt den här gången eftersom jag redan har förstått 
från förre momentet vad den klagar på. 

Båda answer och marvin uppgifter var ganska enkla när del gäller koden men jag 
fick kolla upp ett par formler för Marvin som jag har glömt. Det ända som tog 
lite längre tid än vad det krävs är skillnaden mellan de programmerings språk
som jag kan och python. T.ex. vi kan inte skriva if sats i en annan if sats. 
Det tog lite long tid för mig att förstå det på den sista uppgiften som till sist 
var det mycket enklare att lösa.

==============================================================================

Kmom01
======
Min utvecklingsmiljö är Windows 8. Som webbläsare använder jag Chrome men jag
brukar verifiera att sidan ser bra ut både på Firefox och IE också. Som editor
har jag installerat Python 3.4 IDLE. Däremot 
har jag installerat Cygwin utan problem.

Jag är inte så bekant med python. Jag har testat det en gång bara för länge
sedan så att jag inte kommer ihåg någonting nu. Däremot jag är bekant med
programmering och problemlösning. Jag har läst mer 
än 30hp på A och B nivå. Jag har erfarenhet inom olika programmerings språk
vilka är Java, javascript, php, lite c++ och lite haskell.

Jag är ganska bekant med terminalen och kommandon då förre terminen har jag
klarat en kurs i Linux. Även om det är lite olika på windows men man känner sig
bekant ändå. För att logga in på BTH server genom Cygwin, har jag redan gjort
förut på andra kurser.

Det tog lite tid för mig att förstå allt innan jag började komma igång.
För första moment gick det väldigt bra att klara det utan svårigheter.

Jag skummade över kursmaterialet som verkar att det har mycket läsningar.
Jag har inte använt något av materialet den här gången men jag föredra videor
än att läsa en bok. Jag tycker att videor förklarar bättre då de visar hur man gör.
Boken är viktig också för nybörjare som behöver förstå grunder av programmeringen
eller själva språket. Jag tänker att använda mig av både videor och böcker på 
kommande moment.

</pre>
"""


# Write page content
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
sys.stdout.write(content)
