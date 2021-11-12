import requests
from get_path import get_config_path
import json


token = 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJodHRwOi8vc2NoZW1hcy54bWxzb2FwLm9yZy93cy8yMDA1LzA1L2lkZW50aXR5L2NsYWltcy9uYW1lIjoi5qOA6aqM566h55CG5ZGYIiwiaHR0cDovL3NjaGVtYXMueG1sc29hcC5vcmcvd3MvMjAwNS8wNS9pZGVudGl0eS9jbGFpbXMvbmFtZWlkZW50aWZpZXIiOiI0NTYiLCJuYmYiOjE2MzYzNDIyMzIsImV4cCI6MTYzNjQyODYzMiwiaXNzIjoiaHR0cDovL2xvY2FsaG9zdDo1MDAwIiwiYXVkIjoiaHR0cDovL2xvY2FsaG9zdDo1MDAwIn0.Kttt9KYnLT3P0-9kT1cNl9THS7-X8wVDjELpe2IB4rY'

headers = {'Content-Type': 'application/json;charset=utf-8',
           'Authorization': token}

url = 'http://52.131.241.143/aivalidation/api/v1/ConfigItem/getSystemList'
# url = 'http://139.217.234.156/aivalidation/api/v1/ConfigItem/getSystemList'
# url = 'http://192.168.11.105:53218/api/v1/ConfigItem/getSystemList'

# system_code = json.loads(requests.get(url=url, headers=headers).text)


# sys_codes = system_code['Payload']


# post
# url2 = 'http://52.131.241.143/aivalidation/api/v1/office/create'
# url2 = 'http://192.168.11.105:53218/api/v1/office/create'
url2 = 'http://139.217.234.156/aivalidation/api/v1/office/create'


depart = {"id": 0, "officeCode": "01", "officeName": "测试科室01", "isValid": True}

for i in range(1, 21):
    depart['officeCode'] = '{:02d}'.format(i)
    depart['officeName'] = '测试科室' + '{:02d}'.format(i)
    requests.post(url2, headers=headers, json=depart)
