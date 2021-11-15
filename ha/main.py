import requests
import json
from get_path import get_config_path


config = get_config_path('config.json')
with open(config, encoding='utf-8') as file:
    configs = json.load(file)

headers = configs['headers']
headers['Authorization'] = 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJodHRwOi8vc2NoZW1hcy54bWxzb2FwLm9yZy93cy8yMDA1LzA1L2lkZW50aXR5L2NsYWltcy9uYW1lIjoi5bmz5Y-w566h55CG5ZGYIiwiaHR0cDovL3NjaGVtYXMueG1sc29hcC5vcmcvd3MvMjAwNS8wNS9pZGVudGl0eS9jbGFpbXMvbmFtZWlkZW50aWZpZXIiOiIxIiwibmJmIjoxNjM2OTYyMjA1LCJleHAiOjE2MzcwNDg2MDUsImlzcyI6Imh0dHA6Ly9sb2NhbGhvc3Q6NTAwMCIsImF1ZCI6Imh0dHA6Ly9sb2NhbGhvc3Q6NTAwMCJ9.QTNxBmX3ykPTCASNiJbQabgwz81puLFMPmBQ3dkDlS4'

url = configs['base_url']['local'] + configs['path']['item']
url2 = ''

print(headers)
# system_code = json.loads(requests.get(url=url, headers=headers).text)
# sys_codes = system_code['Payload']
# sys_path = get_config_path('json/sys.json')
# with open(sys_path, encoding='utf-8') as file:
#     system_code = json.load(file)

post_path = get_config_path('json/post.json')
with open(post_path, encoding='utf-8') as file:
    post_code = json.load(file)


with open(get_config_path('json/refer.json'), encoding='utf-8') as file:
    refer = json.load(file)
a = []

for i in refer:
    post_code['itemsCode_Request_Name'] = i
    post_code['itemsName_LIS'] = i
    post_code['itemsCode_Request'] = i
    post_code['itemsCode_LIS'] = i
    post_code['itemsrangelists'][0]['range'] = '[{}~{}]'.format(refer[i]['reference_range'][0], refer[i]['reference_range'][1])
    post_code['itemsrangelists'][0]['minRange'] = str(refer[i]['reference_range'][0])
    post_code['itemsrangelists'][0]['maxRange'] = str(refer[i]['reference_range'][1])
    data = json.dumps(post_code)
    print(data)
    print(requests.post(url=url, headers=headers, data=data).text)


# for code in sys_codes:
#     # if code['id'] in [106, 104, 148]:
#     #     continue
#     post_code['itemsCode_Request_Name'] = code['itemNameCN']
#     post_code['itemsName_LIS'] = code['itemNameCN']
#     post_code['systemId'] = code['id']
#     post_code['itemsCode_Request'] = code['itemCode'].split('~')[0]
#     post_code['itemsCode_LIS'] = code['itemCode'].split('~')[0]
#     data = json.dumps(post_code)

#     res = requests.post(url=url2, headers=headers, data=data)

#     print(res.text)

#     print(data)
#     a.append(code['itemCode'].split('~')[0])
