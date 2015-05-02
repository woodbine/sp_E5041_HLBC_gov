# -*- coding: utf-8 -*-

import scraperwiki
import urllib2
from datetime import datetime
from bs4 import BeautifulSoup
import re

# Set up variables
entity_id = "E5041_HLBC_gov"
url = "http://www.hillingdon.gov.uk/index.jsp?articleid=21085"

# Set up functions
def convert_mth_strings ( mth_string ):
	month_numbers = {'JAN': '01', 'FEB': '02', 'MAR':'03', 'APR':'04', 'MAY':'05', 'JUN':'06', 'JUL':'07', 'AUG':'08', 'SEP':'09','OCT':'10','NOV':'11','DEC':'12' }
	#loop through the months in our dictionary
	for k, v in month_numbers.items():
		#then replace the word with the number
		mth_string = mth_string.replace(k, v)
	return mth_string

def check_regex(txt):
	rg = re.compile(re1+re2+re3+re4+re5+re6+re7+re8+re9+re10+re11+re12+re13+re14+re15,re.IGNORECASE|re.DOTALL)
	m = rg.search(txt)
	print m
	if m:
		w1=m.group(1)
		int1=m.group(2)
		c1=m.group(3)
		word1=m.group(4)
		c2=m.group(5)
		word2=m.group(6)
		c3=m.group(7)
		d1=m.group(8)
		d2=m.group(9)
		d3=m.group(10)
		d4=m.group(11)
		c4=m.group(12)
		int2=m.group(13)
		c5=m.group(14)
		word3=m.group(15)
    		print "regex check :" + "("+w1+")"+"("+int1+")"+"("+c1+")"+"("+word1+")"+"("+c2+")"+"("+word2+")"+"("+c3+")"+"("+d1+")"+"("+d2+")"+"("+d3+")"+"("+d4+")"+"("+c4+")"+"("+int2+")"+"("+c5+")"+"("+word3+")"+"\n"

# set up the regex check
# URL that generated this code:
# http://txt2re.com/index-python.php3?s=E5017_LLBC_gov_2015_02.csv&17&5&-52&-53&9&-54&-31&-27&-30&34&-55&11&-36&-8&7


re1='([a-z])'	# 1st letter - Any Single Word Character (Not Whitespace) 1
re2='(\\d+)'	# following digits - Any digits allowed
re3='(_)'	# underscore
re4='((?:[A-Z][A-Z]+))'	# any word (hoping to force uppercase)
re5='(_)'	# underscore
re6='((?:[a-z][a-z]+))'	# any word (usually gov)
re7='(_)'	# underscore
re8='(2)'	# start of YYYY must be a '2'
re9='(0)'	# 2nd digit of YYYY must be a '0'
re10='(1)'	# 3rd digit of YYYY must be a '1'
re11='(\\d)'	# 4th digit of YYYY must be a digit
re12='(_)'	# underscore
re13='(\\d+)'	# MM can be any two digits (we don't restrict to < 12)
re14='(\\.)'	# full stop
re15='(csv)'	# csv



# pull down the content from the webpage
html = urllib2.urlopen(url)
soup = BeautifulSoup(html)

# find all entries with the required class
links = soup.findAll('a', href=True)

for link in links:
	url = link['href']
	if '&type=csv' in url:
		title = link['title'].split()[2] # get third word in the title
		# create the right strings for the new filename
		title = title.replace(')','').replace('(','')
		csvYr = title.split('/')[-1]
		csvMth = title.split('/')[0]
		if len(csvMth) == 1:
			csvMth = '0'+csvMth # handle single digit months
		filename = entity_id + "_" + csvYr + "_" + csvMth + ".csv"
		check_regex(filename)
		todays_date = str(datetime.now())
		#scraperwiki.sqlite.save(unique_keys=['l'], data={"l": url, "f": filename, "d": todays_date })
		print filename
