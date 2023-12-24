from json_servise import read_inf, wr
def get_one_to_id(id, elem):
    basa = read_inf("basa.json")

    for e in basa[elem]:
        if e["id"] == id:
            return e

    return {"message": f"Element with {id} not found"}


def up_for_id(id, person, name):
    basa = read_inf("basa.json")
    for i, e in enumerate(basa[name]):
        if e["id"] == id:
            e["name"] = person["name"]
            e["age"] = person["age"]
            e["email"] = person["email"]
            wr(basa, "basa.json")
            return e

    return {"message": f"Element with {id} not found"}


def cread_one_to_id(person, status):
    basa = read_inf("basa.json")

    last_id = len(basa[status])
    basa[status].append({"id": last_id + 1, **person})
    wr(basa, "basa.json")


def delete_one_to_id(id, person):
    basa = read_inf("basa.json")
    for i, e in enumerate(basa[person]):
        if e["id"] == id:
            delete = basa[person].pop(i)
            wr(basa, "basa.json")
            return delete

    return {"message": f"Element with {id} not found"}
