import json
write_csv = open('processed/kick.csv','w')
json_file_path = '/home/rh0101/accion-dev/j-books/pydata-talk/data/Kickstarter_2017-10-15T10_20_38_271Z.json'

headers= 'id,deadline,launched_at,state,category_type_subtype,location_type,backers_count,currency,goal,pledged,spotlight,static_usd_rate,usd_pledged,country,country_state\n'

write_csv.write(headers)

for line in open(json_file_path):
  obj = json.loads(line)
  temp_data = []
  try :
    temp_data.append(str(obj["data"]["id"]))
    temp_data.append(str(obj["data"]["deadline"]))
    temp_data.append(str(obj["data"]["launched_at"]))
    temp_data.append(str(obj["data"]["state"]))
    temp_data.append(str(obj["data"]["category"]["slug"]))
    try :
        temp_data.append(str(obj["data"]["location"]["type"]))
    except Exception as e:
        temp_data.append('None')
    temp_data.append(str(obj["data"]["backers_count"]))
    temp_data.append(str(obj["data"]["currency"]))
    temp_data.append(str(obj["data"]["goal"]))
    temp_data.append(str(obj["data"]["pledged"]))
    temp_data.append(str(obj["data"]["spotlight"]))
    temp_data.append(str(obj["data"]["static_usd_rate"]))
    temp_data.append(str(obj["data"]["usd_pledged"]))
    temp_data.append(str(obj["data"]["country"]))
    try:
        temp_data.append(str(obj["data"]["location"]["localized_name"]))
    except Exception as e:
        temp_data.append('None')
    write_csv.write(','.join(temp_data) + '\n')
  except Exception as e:
    print('error', e)

write_csv.close()
