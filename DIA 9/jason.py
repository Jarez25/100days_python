import json

json_file = open("DIA 9/json.json", "w+")

json_text = {"nombre":"jairo","apellido":"medina","edad":24, "lenguaje":"python"}

json.dump(json_text, json_file,indent= 4)

json_file.close()

with open("DIA 9\json.json") as my_other_file:
    for line in my_other_file.readlines():
        print(line)


json_dict = json.load(open("DIA 9\json.json"))
print(json_dict)
print(type(json_dict))
print(len(json_dict))
print(json_dict['nombre'])