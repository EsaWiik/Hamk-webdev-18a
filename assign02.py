#Number list and editing with the almighty REGEX!!!

import re 
import statistics


print(" ")
print("Kirjoita merkkijono, jossa on kokonaislukuja")
print("erotettuna millä tahansa muilla merkeillä.")
print("Miinusmerkki kokonaisluvun edessä merkitsee")
print("Negatiivista kokonaislukua:")
origx = input(">>> ")
print ("Alkuperäinen syöte: " + origx + "\n")

rexlist = re.findall(r"-?\d+",origx) #!!! Tässä REGEX:ointi     

print ("Regex:in löytämä lista: " + str(rexlist) + "\n")
intlist = list( map(int,rexlist) )
print ("Edellinen lista kokonaislukuina: " + str(intlist) + "\n")
print ("Kokonaislukujen summa: " + str(sum(intlist))) 
keskiarvo = (round(statistics.mean(intlist)*10)) /10
print ("Kokonaislukujen keskiarvo, noin: " + str(keskiarvo))
print ("Kokonaislukujen mediaani: " + str((statistics.median(intlist))) + "\n")    