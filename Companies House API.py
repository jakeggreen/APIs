import requests
import json
import pandas as pd

#define class for each company and their officers

class Company:
	def __init__(self, officer, company):
		self.officer = officer
		self.company = company
	def getOfficer(self):
		return self.officer
	def getCompany(self):
		return self.company

#setup

#pull in API key from text file
APIKey_file = open('Companies House Key.txt', 'rt')
APIKey = APIKey_file.read()

#get list of company numbers from text file
CompanyNumber_file = open('Company Numbers.txt', 'rt')
company_file = CompanyNumber_file.read()
company_number = company_file.split('\n')

url = 'https://api.company-information.service.gov.uk/company/' 

payload = {}

headers = {'Authorization': APIKey}

company_list = list();

#end setup

for company in company_number:
	# parameters = {'register_view': 'true', 'register_type': 'directors'}
	full_url = url + company + '/officers'
	response = requests.request('GET', full_url, headers=headers, data=payload)
	company_officers = response.json()
	company = company
	for name in company_officers.get('items'):
		if not name.get('resigned_on') and name.get('officer_role') == 'director':
			try:
				API_name = name['name'] #takes the name in the API formatted (surname, first_names other_names)
				temp_name = API_name.replace(',','') #removes the comma from the API name format
				end = len(temp_name) #finds the length of the full name
				surname_end_location = temp_name.find(' ') #finds the location of the end of the surname
				surname = temp_name[0:surname_end_location] #sets the surname
				other_names = temp_name[surname_end_location + 1:end] #sets the other names
				officer = other_names.upper() + ' ' + surname.upper() #creates new name	
				company_list.append(Company(officer, company))
			except ValueError:
				pass

for company in company_list:
	print(Company.getOfficer(company) + ', ' + Company.getCompany(company))