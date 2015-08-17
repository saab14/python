#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Execute as cgi-skript and send a correct HTTP header.
Send result as HTML.
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


# Store my ascii image in a separat variabel as a raw string
meImage = r"""
          ,     ,
         (\____/)
          (_oo_)
            (O)
          __||__    \)
       []/______\[] /
       / \______/ \/
      /    /__\ 
     (\   /____\ 
"""
# Here comes the content of the webpage 
content = """<!doctype html>
<meta charset="utf-8">
<title>Min me-sida</title>
<pre>
Min Me-sida
==============================================================================
Hej, 
Mitt namn är Sama och jag är student i datavetenskap vid Göteborgs universitet.
{image} 
Jag bodde i stockholm med familj förut, sedan flyttade jag till Göteborg när jag blev antagen till dess högskola.

Det som intresserar mig mest att skapa genom programmering är webbplatser.
I Göteborg universitet studerade jag Haskell och objektorienterad programmering i Java. Där hittade inte jag någon 
webbprogrammering kurs, därför valde jag att studera några fristående kurser vid olika universitet.

På fritiden brukar jag förutom programmera, spela piano, rita, kolla på nya filmer och syssla med Photoshop. 
Dessutom tycker jag om att photografera olika saker ute när vädret är bra.
</pre>
"""
# Write page content
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
sys.stdout.write(content.format(image=meImage))
