import requests
import json
import pandas as pd
import csv
import os

#setup

#read in API key from text file
APIKey_file = open('Companies House Key.txt', 'rt')
APIKey = APIKey_file.read()

#import the list of company numbers from csv file
with open('Company Numbers.csv') as csvfile:
    company_number = csvfile.read().split('\n')
    company_number.remove('')

#change URL head depending on search being used - top for company number, bottom for company name

url = 'https://api.company-information.service.gov.uk/company/' 

url_name = 'https://api.company-information.service.gov.uk/search/companies?q=' 

#change URL ending depending on information required, listed officers of the company or persons with significant control

url_officers = '/officers'

url_psc = '/persons-with-significant-control'

payload = {}

headers = {'Authorization': APIKey}

companies_house_data = list()

#end setup

def get_info():

	for company in company_number:
		full_url = url + company + url_psc
		response = requests.request('GET', full_url, headers=headers, data=payload)
		data = response.json()
		company = company

		try:
			for name in data['items']:
				psc_name = name.get('name')
				psc_id = name.get('identification').get('registration_number')
				name_search_url = url_name + psc_name
				name_response = requests.request('GET', name_search_url, headers=headers, data=payload)
				name_data = name_response.json()
				for com_num in name_data['items']:
					if com_num.get('title') == psc_name.upper():
						psc_id = com_num.get('company_number')
						companies_house_data.append([company, psc_id, psc_name])
					else:
						pass
		except Exception:
			pass


if __name__ == '__main__':

	get_info()

	ch_excel_data = pd.DataFrame(companies_house_data, columns = ['Company', 'PSC ID', 'PSC Name'])
	print(ch_excel_data)
	ch_excel_data.to_excel('companies_house_data.xlsx', index = False, header = True)
