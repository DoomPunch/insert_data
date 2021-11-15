import json
from get_path import get_config_path
import requests


config = get_config_path('config.json')
with open(config, encoding='utf-8') as file:
    configs = json.load(file)

headers = configs['headers']
headers['Authorization'] = 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJodHRwOi8vc2NoZW1hcy54bWxzb2FwLm9yZy93cy8yMDA1LzA1L2lkZW50aXR5L2NsYWltcy9uYW1lIjoi5bmz5Y-w566h55CG5ZGYIiwiaHR0cDovL3NjaGVtYXMueG1sc29hcC5vcmcvd3MvMjAwNS8wNS9pZGVudGl0eS9jbGFpbXMvbmFtZWlkZW50aWZpZXIiOiIxIiwibmJmIjoxNjM2OTYyMjA1LCJleHAiOjE2MzcwNDg2MDUsImlzcyI6Imh0dHA6Ly9sb2NhbGhvc3Q6NTAwMCIsImF1ZCI6Imh0dHA6Ly9sb2NhbGhvc3Q6NTAwMCJ9.QTNxBmX3ykPTCASNiJbQabgwz81puLFMPmBQ3dkDlS4'

url = configs['base_url']['local'] + configs['path']['syscode']


cd = json.loads(requests.post(url, headers=headers).text)
# cd = requests.post(url, headers=headers).text
print(cd)

code = ['TBA', 'AST', 'CL', 'K', 'UA', 'HCY', 'PHO', 'ALB', 'TP', 'FE']


rules = []


for i in code:
    srule = {
        "aId": 0,
        "type": "区间范围",
        "itemCode": code,
        "operations": "",
        "formula": "",
        "range": code+"({}~{})",
        "minRange": "1",
        "maxRange": "100",
        "risk": "大了",
        "id": 0,
        "isActive": True
    }
    rules.append(srule)


rule_path = get_config_path('json/rule.json')


with open(rule_path, encoding='utf-8') as file:
    rule = json.load(file)

rule['ruleList'] = rules

rule = json.dumps(rule)
# print(a)


# res = requests.post(url, headers=headers)
# print(res.text)
