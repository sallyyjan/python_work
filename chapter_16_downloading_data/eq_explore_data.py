import json

# Explore the structure of the json formatted data
filename = 'data/eq_data_1_day_m1.json'
with open(filename) as f:
    all_eq_data = json.load(f) # a giant dictionary

# Create readable version of the json data
readable_file = 'data/readable_eq_data.json'
with open(readable_file, 'w') as f:
    json.dump(all_eq_data, f, indent=4)

all_eq_dicts = all_eq_data['features'] 

mags = []
for eq_dict in all_eq_dicts:
    mags.append(eq_dict['properties']['mag'])

print(mags)