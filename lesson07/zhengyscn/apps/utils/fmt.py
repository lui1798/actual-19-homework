import json

from prettytable import PrettyTable

def Println(data):
	print(json.dumps(data, indent=4))
	

def PrintTable(data):
	x = PrettyTable()
	if isinstance(data, list):
		x.field_names = data[0].keys()
		for dicinfo in data:
			x.add_row(dicinfo.values())
	elif isinstance(data, dict):
		x.field_names = data.keys()
		x.add_row(data.values())
	else:
		return '', False
	return x, True
		
		
		