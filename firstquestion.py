import yaml
import json
json_data = {}
with open("sample1.yaml", "r") as f, open("sample1.json", "w") as c:
    data = yaml.safe_load(f)
    json.dump(data, c)
