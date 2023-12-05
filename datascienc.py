import json 
file_path= 'D:\programming\Python\data2.json'

with open (file_path,'r') as json_file:
    json_data =json.load(json_file)
    formatted_json = json.dumps(json_data, indent=4)  # Indentation for better readability
    print(formatted_json)