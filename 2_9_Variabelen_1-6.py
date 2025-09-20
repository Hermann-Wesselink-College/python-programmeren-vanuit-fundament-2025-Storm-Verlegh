# opdrachten 1 tot en met 6 van paragraaf 2.9
totaalprijs = 100
kortingsBon = 25
nieuweprijs = totaalprijs - kortingsBon
print(nieuweprijs)
	cijfer1 = 7.2
cijfer2 = 8.6
gemiddelde = (cijfer1 + cijfer2) / 2
print(gemiddelde)
prijsExclBtw = float(input("Voer een prijs in:"))
prijsInclBtw = prijsExclBtw * 1.21
print(prijsInclBtw)
	totaalprijs = float(input("Totaalprijs van de producten:"))
verzendkosten = 3.95
teBetalen = totaalprijs + verzendkosten
print("Totaalprijs: " + str(totaalprijs) + " EUR.")
print("Verzendkosten: " + str(verzendkosten) + " EUR.")
print("TOTAAL: " + str(teBetalen) + " EUR.")
bedrag = float(input("Voer een bedrag in euros in"))
wisselkoers = 1.1648
prijsDollar = bedrag * wisselkoers
totaalPrijs = float(input("Geef een totaalprijs:"))
kortingsPercentage = float(input("Geef een kortingspercentage:"))
nieuwePrijs = (1 - (kortingsPercentage / 100)) * totaalPrijs
print(nieuwePrijs)
''git commit''
print("$" + str(prijsDollar))
