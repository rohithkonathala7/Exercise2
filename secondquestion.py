import yaml
import json
json_data = {}
with open("sample2.yaml", "r") as s, open("sample1.yaml", "r") as f, open("sample1.json", "w") as c, open("sample2.json", "w") as d:
    try:
        data1 = yaml.safe_load(s)
        json.dump(data1, d)
    except:
        print("There is some error in sample2.yaml file.")
        data2 = yaml.safe_load(f)
        json.dump(data2, c)
