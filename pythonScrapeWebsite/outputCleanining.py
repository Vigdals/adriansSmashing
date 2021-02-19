import re

f = open("lottoTallOutputRaw.txt")
filtekst = f.read()
filtekst = filtekst[:-1] #removes the last character of the string ]
lottolinjer = filtekst.split(",") #splits the string into a list on every comma

for x in range(len(lottolinjer)): #loops through the list we made
	#lottolinjer[x].strip(">")
	#print(lottolinjer[x].strip("</span>"))
	lottolinjer[x] = lottolinjer[x].strip("</span>") #removes the </span> text at the end of each line
	lottolinjer[x] = re.findall(r'\d+', lottolinjer[x])[-1] #gets the last whole number in each line
	
for x in range(len(lottolinjer)): #loops through the list we made
	print(lottolinjer[x])

f.close()