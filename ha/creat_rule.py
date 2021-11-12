import json
from get_path import get_config_path
import requests


token = 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJodHRwOi8vc2NoZW1hcy54bWxzb2FwLm9yZy93cy8yMDA1LzA1L2lkZW50aXR5L2NsYWltcy9uYW1lIjoi5bmz5Y-w566h55CG5ZGYIiwiaHR0cDovL3NjaGVtYXMueG1sc29hcC5vcmcvd3MvMjAwNS8wNS9pZGVudGl0eS9jbGFpbXMvbmFtZWlkZW50aWZpZXIiOiIxIiwibmJmIjoxNjM1OTkwMDEyLCJleHAiOjE2MzYwNzY0MTIsImlzcyI6Imh0dHA6Ly9sb2NhbGhvc3Q6NTAwMCIsImF1ZCI6Imh0dHA6Ly9sb2NhbGhvc3Q6NTAwMCJ9.avSGuZ_HoDlm8syrRF_eGeNO7ZbLDdWlgax-an4o0LA'

headers = {'Content-Type': 'application/json;charset=utf-8',
           'Authorization': token}


url = 'http://192.168.11.105:53218/api/v1/rule/GetLisCodeName'
url2 = 'http://192.168.11.105:53218/api/v1/rule/create'

# url = 'http://52.131.241.143/aivalidation/api/v1/ConfigItem/getSystemList'
# url2 = 'http://52.131.241.143/aivalidation/api/v1/ConfigItem'

# url = 'http://139.217.234.156/aivalidation/api/v1/ConfigItem/getSystemList'
# url2 = 'http://139.217.234.156/aivalidation/api/v1/ConfigItem'


cd = json.loads(requests.post(url, headers=headers).text)
# cd = requests.post(url, headers=headers).text
print(cd)

code = ['TP', 'ALB', 'ALP', 'ALT', 'AST', 'GGT', 'BIL-T', 'BIL-D', 'PALB', 'CHE', 'UREA', 'BUN',
        'CREA', 'UA', 'B2MG', 'mALB', 'CYSC', 'A1MG', 'TPUC', 'TRANS', 'CK', 'CKMB', 'LDH', 'Hs-CRP', 'HCY',
        'LP(a)', 'TRIG', 'TRIGB', 'CHOL', 'Apo A I', 'Apo B', 'HDL-C', 'LDL-C', 'FERR', 'UIBC', 'Iron', 'sTfR',
        'CRP', 'D-Dimer', 'KAPP', 'LAMB', 'C3C', 'C4', 'HAPT', 'MYO', 'PHNO', 'PHNY', 'VALP', 'CARB', 'LI', 'SALI',
        'VANC', 'MPA', 'ETOH', 'HbA1c', 'GLU', 'FRUC', 'TSH', 'T3', 'T4', 'FT3', 'FT4']


srule = {
        "aId": 0,
        "type": "区间范围",
        "itemCode": "T3",
        "operations": "",
        "formula": "",
        "range": "T3(1~100)",
        "minRange": "1",
        "maxRange": "100",
        "risk": "大了",
        "id": 0,
        "isActive": True
    }


rules = []


for i in range(0, 20):
    srule = {
        "aId": 0,
        "type": "区间范围",
        "itemCode": code[i],
        "operations": "",
        "formula": "",
        "range": code[i]+"(1~100)",
        "minRange": "1",
        "maxRange": "100",
        "risk": "大了",
        "id": 0,
        "isActive": True
    }
    rules.append(srule)


rule_path = get_config_path('json/rule.json')
# code_path = get_config_path('json/it_code.json')

with open(rule_path, encoding='utf-8') as file:
    rule = json.load(file)

# with open(code_path, encoding='utf-8') as file:
#     code = json.load(file)

rule['ruleList'] = rules

rule = json.dumps(rule)
# print(a)


# res = requests.post(url, headers=headers)
# print(res.text)
