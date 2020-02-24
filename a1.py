"""
MODULE a1.py

Name: Dushyant Panchal
  Roll No: 2018033
Section: A    Group: 1

"""

#Required predefined modules
import urllib.request
import datetime

# function to get weather response
def weather_response(location, API_key):
	
	urlString='http://api.openweathermap.org/data/2.5/forecast?q=' + location + '&APPID=' + API_key
	#Create string for complete url

	siteData=urllib.request.urlopen(urlString)
	#Opening the URL

	data=str(siteData.read())
	#Bringing in data from the site

	return data[2:]	#Returning after removing '\b' from the string



# function to check for valid response 
def has_error(location,json):
	#Check whether <location> string is a part of the <json> string or not
	return not (json.find(location) > -1)




###############Function to get index to required record################
#function to find the record corresponding to given day and hour
def findMatchingRecord(json, n=0, t="3:00:00"):

	temp=datetime.datetime.now() + datetime.timedelta(days=n)	#Current date + 'n' days
	Hour=int(t[:t.find(':')])	#Extract hour from variable 't'
	toFind=datetime.datetime(temp.year,temp.month,temp.day,Hour);
					#Date Time record To be found
	
	
	dateFind=str(toFind)	#Convert datetime object to string

	recFound=json.find(dateFind)
	#Finding required date and time record in the json

	if(recFound>-1):	#If record found
		recFound-=360
		recFound=json.find('\"dt\":',recFound)+5
	
		return recFound	#Return index to the beginning of the record

	else:				#If record not found
		return -1
######################################################################




####### function to get attributes on nth day ########
def get_temperature (json, n=0, t="3:00:00"):
	
	index=findMatchingRecord(json, n=n, t=t)	#Get index to beginning of the required record
	if(index==-1):		#If record does not exist
		print('Record Not Found')
		return -1
	index=json.find('\"temp\":',index)+7	#Find the string '"temp":' (start the search from 'index')
	T=float(json[index:json.find(',',index)])	
	print(T)
	return T   			#Return as float data


def get_humidity(json, n=0, t="3:00:00"):
	
	index=findMatchingRecord(json, n=n, t=t)	#Get index to beginning of the required record
	if(index==-1):		#If record does not exist
		print('Record Not Found')
		return -1
	index=json.find('\"humidity\":',index)+11	#Find the string '"humidity":' (start the search from 'index')
	H=float(json[index:json.find(',',index)])
	#print(H)
	return H   			#Return as float data

def get_pressure(json, n=0, t="3:00:00"):
	
	index=findMatchingRecord(json, n=n, t=t)	#Get index to beginning of the required record
	if(index==-1):		#If record does not exist
		print('Record Not Found')
		return -1
	index=json.find('\"pressure\":',index)+11	#Find the string '"pressure":' (start the search from 'index')
	P=float(json[index:json.find(',',index)])
	#print(P)
	return P   			#Return as float data

def get_wind(json, n=0, t="3:00:00"):
	
	index=findMatchingRecord(json, n=n, t=t)	#Get index to beginning of the required record
	if(index==-1):		#If record does not exist
		print('Record Not Found')
		return -1
	index=json.find('\"wind\":',index)+16	#Find the string '"wind":' (start the search from 'index')
	W=float(json[index:json.find(',',index)])
	#print(W)
	return W   			#Return as float data

def get_sealevel(json, n=0, t="3:00:00"):
	
	index=findMatchingRecord(json, n=n, t=t)	#Get index to beginning of the required record
	if(index==-1):		#If record does not exist
		print('Record Not Found')
		return -1
	index=json.find('\"sea_level\":',index)+12	#Find the string '"sealevel":' (start the search from 'index')
	S=float(json[index:json.find(',',index)])
	#print(S)
	return S   			#Return as float data

#######################################################
