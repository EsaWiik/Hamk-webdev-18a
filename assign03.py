# Dictionary
import json


#dicty = { "koira" : "dog" , "kissa" : "cat", "hiiri" : "mouse" }
#filen testitallennus (alkuperäisen dicty.txt:n luominen)
#with open("dictyx.txt","w") as outfile:
#    json.dump(dicty,outfile)

    
#Ladataan tiedostosta dictyx.txt #Errorilla luo oman 3 sanan dicty:n
try:   
    with open("dictyx.txt") as json_file:
        dicty = json.load(json_file)
except:
    print("ERROR loadin dictyx.txt!!! Default dicty in use.")
    dicty = { "koira" : "dog" , "kissa" : "cat", "hiiri" : "mouse" }
    
bigloop= True  #looppi päälle

def finder(eläin):
    """ muokkaa annetun syötteen ja etsii dicty:stä 
    ,jos sanaa ei löydy, ottaa uuden syötteen ja lisää elukan"""
    global bigloop
    findthis = str(eläin)
    found = dicty.get(findthis,"0")
    if found != "0" :
        print("="+found)
    else:
        print("Eläintä ei löytynyt")
        uusielukka = str(input("Kirjoita määritelmä eläimelle %s: " %(findthis)))

        if len(uusielukka) == 0:
            bigloop = False
        else:
            dicty[findthis] = uusielukka.lower()
            print(dicty)

#toistaa ohjelmaa, kunnes saa tyhjän syötteen
while bigloop == True:

    print ("Kirjoita eläimen nimi")
    kirjoitettu = (input (":")).lower()
    if len(kirjoitettu) > 0:
        finder(kirjoitettu)
    else:
        bigloop = False

##Tähän dicty:n tallennus fileen
with open("dictyx.txt", "w") as outfile:
    json.dump(dicty, outfile)
        
print("Hyvästi!")

