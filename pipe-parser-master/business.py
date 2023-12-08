import os
import json
import datasource
import database


def get_file_info(event):
    records = event["Records"]
    s3_info = records[0]["s3"]
    bucket_name = s3_info["bucket"]["name"]
    key_name = s3_info["object"]["key"]
    return bucket_name, key_name


schema = {
    "MH": [
        "Status",
        "TypeName",
        "Type",
        "Date",
        "Title",
        "Source",
        "Code",
        "Category",
        "CategoryId"
    ],
    "FI": [
        "Before",
        "Address",
        "Coding1",
        "Coding2",
        "Coding3",
        "Coding4",
        "Coding5",
        "CodingType",
        "After"
    ],
    "FT": [
        "Number",
        "Coding6",
        "Coding7"
    ]
}


def map(map, properties):
    data = {}
    i = 0
    for item in map:
        data[item] = properties[i]
        i = i + 1
    return data


def parse(data):
    lines = [_ for _ in data.split("~") if len(_) > 0]
    data = {}
    for line in lines:
        properties = line.split("|")
        type = properties[0]
        if type == "MT":
            continue
        properties.pop(0)
        properties.pop(0)
        data.update(map(schema[type], properties))
    return data


def run(event):
    bucket_name, key_name = get_file_info(event)
    data = datasource.read_file(bucket_name, key_name)
    parsed = parse(data)
    parsed["Filename"] = os.path.basename(key_name)
    print(json.dumps(parsed, indent=4))
    print("here")
    database.save(data)
    return {
        'bucket_name': bucket_name
    }
