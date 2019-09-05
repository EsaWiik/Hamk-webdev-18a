#assign4 
#prog asks URL from user.
#if URL can be opened, writes the URL 
#into a local file path defined by user.
#Use binary mode and check that file writing succeeds.
#The program shound not fail if given URL cannot be found.

import urllib.request ###nettiesimerkki
...
asking = True

while asking == True:    
    urli = input("Gimme an URL: ")
    #urli = "https://yle.fi/uutiset" #automaattinen testiURL
    try:   
         response = urllib.request.urlopen(urli)
         asking = False
    except:
         print("Loading URL failed!")
         asking = True
             
data = response.read()
text = data.decode("utf-8")
print(text[:1000])

filename = "urlfilex.txt"
urlfile = open(filename, "wb") #Tallennus binäärimuodossa
urlfile.write(data)
urlfile.close
print ( filename + " saved." )


