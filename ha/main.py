import requests
import json
from get_path import get_config_path


token = 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJodHRwOi8vc2NoZW1hcy54bWxzb2FwLm9yZy93cy8yMDA1LzA1L2lkZW50aXR5L2NsYWltcy9uYW1lIjoi5bmz5Y-w566h55CG5ZGYIiwiaHR0cDovL3NjaGVtYXMueG1sc29hcC5vcmcvd3MvMjAwNS8wNS9pZGVudGl0eS9jbGFpbXMvbmFtZWlkZW50aWZpZXIiOiIxIiwibmJmIjoxNjM1OTkwMDEyLCJleHAiOjE2MzYwNzY0MTIsImlzcyI6Imh0dHA6Ly9sb2NhbGhvc3Q6NTAwMCIsImF1ZCI6Imh0dHA6Ly9sb2NhbGhvc3Q6NTAwMCJ9.avSGuZ_HoDlm8syrRF_eGeNO7ZbLDdWlgax-an4o0LA'

headers = {'Content-Type': 'application/json;charset=utf-8',
           'Authorization': token}

# url = 'http://52.131.241.143/aivalidation/api/v1/ConfigItem/getSystemList'
# url = 'http://139.217.234.156/aivalidation/api/v1/ConfigItem/getSystemList'
url = 'http://192.168.11.105:53218/api/v1/ConfigItem/getSystemList'

system_code = json.loads(requests.get(url=url, headers=headers).text)


sys_codes = system_code['Payload']


# post
# url2 = 'http://52.131.241.143/aivalidation/api/v1/ConfigItem'
url2 = 'http://192.168.11.105:53218/api/v1/office/create'
# url2 = 'http://139.217.234.156/aivalidation/api/v1/ConfigItem'


sys_path = get_config_path('json/sys.json')
post_path = get_config_path('json/post.json')

# with open(sys_path, encoding='utf-8') as file:
#     system_code = json.load(file)

with open(post_path, encoding='utf-8') as file:
    post_code = json.load(file)

a = []

for code in sys_codes:
    # if code['id'] in [106, 104, 148]:
    #     continue
    post_code['itemsCode_Request_Name'] = code['itemNameCN']
    post_code['itemsName_LIS'] = code['itemNameCN']
    post_code['systemId'] = code['id']
    post_code['itemsCode_Request'] = code['itemCode'].split('~')[0]
    post_code['itemsCode_LIS'] = code['itemCode'].split('~')[0]
    data = json.dumps(post_code)

    # res = requests.post(url=url2, headers=headers, data=data)

    # print(res.text)

    # print(data)
    a.append(code['itemCode'].split('~')[0])

print(a)
