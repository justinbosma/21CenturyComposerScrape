import requests
from bs4 import BeautifulSoup
 
req = requests.get('https://en.wikipedia.org/wiki/List_of_21st-century_classical_composers', verify=False)
soup = BeautifulSoup(req.text, "html.parser")
tbl = soup.find_all('table')[2]
#need to append tbl.a to "https://en.wikipedia.org"
#req1 = requests.get(tbl.a, verify=False)
#soup1 = BeautifulSoup(req1.text, "html.parser")
print(tbl.a)