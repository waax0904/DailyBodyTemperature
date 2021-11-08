import requests
from requests.api import request
import datetime
import random

my_info = {'employeeId': '●●●●●', 'mobileNo': '●●●●●'}
loginUrl = requests.post("https://wits-healthy.wistronits.com/healthy-tp/login", data=my_info)

todayDate = datetime.date.today().strftime("%Y%m%d")

input_tmp = random.uniform(36.0 , 36.6)
fixtmp = str( round(input_tmp, 1) )

my_data={'reportDate': todayDate,
'workProvince': '35',
'workCity': '3384',
'projectTeam': '',
'temperatureType': '1',
'temperature': fixtmp,
'symptomList': '0',
'attentionKb': '0',
'causeKbSelf': '04',
'symptomDetail': '',
'familyStatusKb': '0',
'causeKbFamily': '04',
'familyStatusDetail': '',
'familyAbroad': '',
'contactHistory': '',
'returnBackDate': ''}

r = requests.post(loginUrl.url, data=my_data)

print('tmp input done')