import json
def wr(basa_auto_parts, file_name):
    basa_auto_parts = json.dumps(basa_auto_parts)
    basa_auto_parts = json.loads(str(basa_auto_parts))

    with open(file_name, 'w', encoding="utf-8") as file:
        json.dump(basa_auto_parts, file, indent=4)


#wr(basa_auto_parts,"basa.json")


def read_inf(file_name):
    with open(file_name, 'r', encoding="utf-8") as file:
        return json.load(file)