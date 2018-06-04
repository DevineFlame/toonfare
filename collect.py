from urllib.request import urlopen
from bs4 import BeautifulSoup
from collections import defaultdict
import time


sites=['http://www.amul.com/','https://timesofindia.indiatimes.com/cartoons.cms','http://indianexpress.com/']
site_map={'amul':'http://www.amul.com/','indianexpress':'http://indianexpress.com/','toi':'https://timesofindia.indiatimes.com/cartoons.cms'}
final_links=[]
local_links = defaultdict(list)


def waiter(page_url,ele,attr,delay_time,skip_text):
	page=""
	soup=""
	while True:
		page = urlopen(page_url)
		soup = BeautifulSoup(page, 'html.parser')
		name_box = soup.find(ele, attrs=attr)
		links=name_box.find_all('img')
		flag=0
		print("waiting for ->" +str(page_url) )
		for link in links:
			link=link.get('src')
			if str(link)!= skip_text:
				flag=1
				break
		if flag==1:
			break

		time.sleep(delay_time)
	return soup

for site in sites:

	quote_page = site
	print(quote_page)

	page = urlopen(quote_page)
	soup = BeautifulSoup(page, 'html.parser')
	#for amuls cartoons
	if site_map['amul']==quote_page:
		name_box = soup.find('div', attrs={'id': 'topicalbox2'})
		links=name_box.find_all('img');
		for link in links:
		    x=link.get('src')[1:]
		    link=str(site_map['amul'])+str(x)
		    local_links["amul"].append(link)
	
	# if site_map['hindu']==quote_page:
	# 	name_box = soup.find('div', attrs={'class': 'main'})
	# 	links=name_box.find_all('img');
	# 	for link in links:
	# 	    link=link.get('src')            
	# 	    local_links["hindu"].append(link)


	if site_map['indianexpress']==quote_page:
		name_box = soup.find('div', attrs={'class': 'usual'})
		links=name_box.find_all('img');
		for link in links:
		    link=link.get('src')  
		    link=str("http:")+str(link)          
		    local_links["indianexpress"].append(link)

	if site_map['toi']==quote_page:
		
		name_box = soup.find('ul', attrs={'class': 'crt_slides'})
		links=name_box.find_all('img');
		for link in links:
		    link=link.get('src')
		    if 'photo' not in str(link):
		    	continue

		    link='https://timesofindia.indiatimes.com'+str(link)
		             
		    local_links["toi"].append(link)


print(local_links)

