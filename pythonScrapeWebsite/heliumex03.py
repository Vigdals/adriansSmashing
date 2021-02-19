from helium import *
from selenium.webdriver import FirefoxOptions


options = FirefoxOptions()
options.add_argument('--start-maximized')
start_firefox(options=options)

go_to("https://www.norsk-tipping.no/lotteri/lotto/resultater")

#selectorSearch = find_all(S(".winnernumbersContainer--3gVxG")) Denne traff på noko
selectorSearch = find_all(S(".number--3Cvhn"))
selectorFind = [item.web_element.text for item in selectorSearch]

print(selectorSearch)
print("")
print('[%s]' % ', '.join(map(str, selectorSearch)))

f= open("lottoTallOutputRaw.txt","w+")
f.write('[%s]' % ', '.join(map(str, selectorSearch)))
f.close() 

kill_browser()

print("Finished getting lottotall. Invoking outputCleanining:\"")

import re

f = open("lottoTallOutputRaw.txt" ,"r") #read only is the "r" thingy
filtekst = f.read()
filtekst = filtekst[:-1] #removes the last character of the string ]
lottolinjer = filtekst.split(",") #splits the string into a list on every comma


for x in range(len(lottolinjer)): #loops through the list we made
	#lottolinjer[x].strip(">")
	#print(lottolinjer[x].strip("</span>"))
	lottolinjer[x] = lottolinjer[x].strip("</span>") #removes the </span> text at the end of each line
	lottolinjer[x] = re.findall(r'\d+', lottolinjer[x])[-1] #gets the last whole number in each line


outputFile = open('cleanLottotall.txt', 'w') #overwrite the file due to the "w"
for x in range(len(lottolinjer)): #loops through the list we made and prints it
	outputFile.write(lottolinjer[x])
	outputFile.write("\n")
	print(lottolinjer[x])

f.close()
outputFile.close()