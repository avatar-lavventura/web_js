import json


with open("ex.json", "r") as jsonFile:
    data = json.load(jsonFile)

#print(data["clusters"]['0x4e4a0750350796164D8DefC442a712B7557BF282'])


#print(data["clusters"]['0x4e4a0750350796164D8DefC442a712B7557BF282'][0]['coreNumber'])
#print(data["clusters"]['0x4e4a0750350796164D8DefC442a712B7557BF285'][0]['coreNumber'])

# print(data["clusters"])

for make in data["clusters"]:
	for model in data["clusters"][make]:
		print(make)
		print(model)
# data["clusters"]['0x4e4a0750350796164D8DefC442a712B7557BF285'][0]['coreNumber'] = 100

with open("ex.json", "w") as jsonFile:
    json.dump(data, jsonFile)


'''
with open("ex.json", "r+") as jsonFile:
	data = json.load(jsonFile)
	data["clusters"]['0x4e4a0750350796164D8DefC442a712B7557BF285'][0]['coreNumber'] = 999
	data["clusters"]['0x4e4a0750350796164D8DefC442a712B7557BF282'][0]['coreNumber'] = 77
	
	jsonFile.seek(0)  # rewind
	json.dump(data, jsonFile)
	jsonFile.truncate()
'''
