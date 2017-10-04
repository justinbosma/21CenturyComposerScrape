import requests
import re
from bs4 import BeautifulSoup
#Go to wikipedia page. Verify=False for https
req = requests.get('https://en.wikipedia.org/wiki/List_of_21st-century_classical_composers', verify=False)
#create soup object with wiki page and html parser
soup = BeautifulSoup(req.text, "html.parser")
#Grab the table which lists all names and nationalities
tbl = soup.find_all('table')[2]
# initialize arrays for distributing composers to regions based on birth place
midwest = []
south = []
east = []
west = []
#Grab all rows in the table of composers - each row is a composer, birthdate, deathdate, nationality, 
rows = tbl.find_all('tr')
#create file object from composer.txt in write mode
file_obj = open("composer.txt", "w")
#create file obj for testing the re search
#file_obj_test = open("file_test.txt", "w")
#count for watching console and making sure things are moving
count = 1
#go through each row in the list of rows
for row in rows:
	#increment count per row. Used to make sure things are moving in console
	count = count + 1
	#print count to console
	print(count)
	#grab all cells in row
	cells = row.find_all('td')
	#some cells were failing. This assures only rows with data are grabbed and accessed
	if(len(cells) > 4):
		#checks if the 4th cell has value 'American'
		if(cells[3].text.strip() == 'American'):
			#If the Nationality is American, append the link to the wiki base link. 
			link = ("https://en.wikipedia.org" + row.a['href'])
			#follow new link and make request
			reqNew = requests.get(link, verify=False)
			#make soup object of new request
			newSoup = BeautifulSoup(reqNew.text, "html.parser");
			#grab the birthplace of the composer
			birthPlace = re.search('born .*?, [A-Z][a-z]+\s{0,1}[A-Z]*[a-z]*', newSoup.getText())

			if birthPlace != None:

			#Check the birthplace text for the state name. Put in the associated region list
				if("Connecticut" in birthPlace.group(0) or "Maine" in birthPlace.group(0) or "Massachusetts" in birthPlace.group(0) or "New Hampshire" in birthPlace.group(0) or "Rhode Island" in birthPlace.group(0) or "Vermont" in birthPlace.group(0) or "New Jersey" in birthPlace.group(0) or "New York" in birthPlace.group(0) or "Pennsylvania" in birthPlace.group(0)):
					east.append(cells[0].a.text.strip())
				elif("Illinois" in birthPlace.group(0) or "Indiana" in birthPlace.group(0) or "Michigan" in birthPlace.group(0) or "Ohio" in birthPlace.group(0) or "Wisconsin" in birthPlace.group(0) or "Iowa" in birthPlace.group(0) or "Kansas" in birthPlace.group(0) or "Minnesota" in birthPlace.group(0) or "Missouri" in birthPlace.group(0) or "Nebraska" in birthPlace.group(0) or "North Dakota" in birthPlace.group(0) or "South Dakota" in birthPlace.group(0)):
					midwest.append(cells[0].a.text.strip())
				elif("Delaware" in birthPlace.group(0) or "Florida" in birthPlace.group(0) or "Georgia" in birthPlace.group(0) or "Maryland" in birthPlace.group(0) or "North Carolina" in birthPlace.group(0) or "South Carolina" in birthPlace.group(0) or "Virginia" in birthPlace.group(0) or "District of Columbia" in birthPlace.group(0) or "West Virginia" in birthPlace.group(0) or "Alabama" in birthPlace.group(0) or "Kentucky" in birthPlace.group(0) or "Mississippi" in birthPlace.group(0) or "Tennessee" in birthPlace.group(0) or "Arkansas" in birthPlace.group(0) or "Louisiana" in birthPlace.group(0) or "Oklahoma" in birthPlace.group(0) or "Texas" in birthPlace.group(0)):
					south.append(cells[0].a.text.strip())
				elif("Arizona" in birthPlace.group(0) or "Colorado" in birthPlace.group(0) or "Idaho" in birthPlace.group(0) or "Montana" in birthPlace.group(0) or "Nevada" in birthPlace.group(0) or "New Mexico" in birthPlace.group(0) or "Utah" in birthPlace.group(0) or "Wyoming" in birthPlace.group(0) or "Alaska" in birthPlace.group(0) or "California" in birthPlace.group(0) or "Hawaii" in birthPlace.group(0) or "Oregon" in birthPlace.group(0) or "Washington" in birthPlace.group(0)):
					west.append(cells[0].a.text.strip())
	
#For each list write region to txt. After loop through all names of that region and write to txt
			
file_obj.write("East \n")
for name in east:
	file_obj.write(name + "\n")
file_obj.write("\n")
file_obj.write("Midwest \n\n")
for name in midwest:
	file_obj.write(name + "\n")
file_obj.write("\n")
file_obj.write("West \n\n")
for name in west:
	file_obj.write(name + "\n")
file_obj.write("\n")
file_obj.write( "South \n\n")
for name in south:
	file_obj.write(name + "\n")
			#if(re.search('born .*, Minnesota', newSoup.get_text())):
			#	file_obj.write(cells[0].a.text.strip() + "\n")

file_obj.close()
#file_obj_test.close()