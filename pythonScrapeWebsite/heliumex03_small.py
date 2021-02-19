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