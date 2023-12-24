import json

basa_auto_parts = {
    "shop_name": "Velo Bike",
    "address": "Tekstilshchikov, 26",
    "workers": [
        {
            "id": 1,
            "name": "Andry Popov",
            "age": 46,
            "emai": "andry_pop@mail.com",
            "class_id": 1
        },
        {
            "id": 2,
            "name": "Oleg Linal",
            "age": 65,
            "email": "oleg65@gmail.com",
            "class_id": 2
        },
        {
            "id": 3,
            "name": "Ivan Sorokin",
            "age": 25,
            "email": "sorok_iv@gmail.com",
            "class_id": 1
        },
        {
            "id": 4,
            "name": "Marina Raspytina",
            "age": 27,
            "email": "marishka.r@mail.ru",
            "class_id": 2
        }
    ],   
    "classes": [
        {
            "id": 1,
            "name": "seller",
            "class_nachalnik_id": 1,
            "worker_id": [
                1,
                3
            ],
        },
        {
            "id": 2,        
            "name": "consultant",
            "class_nachalnik_id": 2,
            "worker_id": [
                2,
                4
            ],            
        }
    ],    
    "nachalniks": [
    {
        "id": 1,
        "name": "Elena Obyhova",
        "email": "elena_obyhova@example.com",
    },
    {
        "id": 2,
        "name": "Katy Popova ",
        "email": "katerina1263.p@gmail.com",
    }
    ]
}

def wr(basa_auto_parts, file_name):
    basa_auto_parts = json.dumps(basa_auto_parts)
    basa_auto_parts = json.loads(str(basa_auto_parts))

    with open(file_name, 'w', encoding="utf-8") as file:
        json.dump(basa_auto_parts, file, indent=4)

#wr(basa_auto_parts,"basa.json")
      
def read_inf(file_name):
    with open(file_name,'r',encoding="utf-8") as file:
        return json.load(file)

def get_one_to_id(id,elem):
    basa = read_inf("basa.json")

    for e in basa[elem]:
        if e["id"] == id:
            return e

    return {"message": f"Element with {id} not found"}

def up_for_id(id,person,name):
    basa = read_inf("basa.json")
    for i, e in enumerate(basa[name]):
        if e["id"] == id:
            e["name"] = person["name"]
            e["age"] = person["age"]
            e["email"] = person["email"]
            wr(basa,"basa.json")
            return e

    return {"message": f"Element with {id} not found"}

def cread_one_to_id(person,status):
    basa = read_inf("basa.json")

    last_id = len(basa[status])
    basa[status].append({"id": last_id + 1, **person})
    wr(basa,"basa.json")
    
def delete_one_to_id(id,person):
    basa = read_inf("basa.json")
    for i, e in enumerate(basa[person]):
        if e["id"] == id:
            delete = basa[person].pop(i)
            wr(basa,"basa.json")
            return delete

    return {"message": f"Element with {id} not found"}

b = 10
while b > 0:
    while True:
        sp = 1,2,3,4
        try:
            print("what do you want to do with the data? create (1), read (2), update (3), delete (4)")
            zap = int(input())
            if zap in sp:
                break
            else: print("Try again:")
        except ValueError:
            print("Try again:")
            
    if zap == 2:
        basa = read_inf("basa.json")
        print("display the readings of one element(1) or all(2)")
        zap1 = int(input()) 
        if zap1 == 2:
            print(read_inf("basa.json"))
        if zap1 == 1:
            print("display what element readings shop name(1), address(2), workers(3), classes(4),nachalniks(5)")
            zap2 = int(input())
            if zap2 == 1: print(basa["shop_name"])
            if zap2 == 2: print(basa["address"])
            if zap2 == 3: 
                print("all workers(1) or one(2)")
                zap3 = int(input())
                if zap3 == 1: print(basa["workers"])
                if zap3 == 2:
                    print("wich worker")
                    zap4 = int(input())
                    print(get_one_to_id(zap4,"workers"))
            if zap2 == 4: 
                print("all classes(1) or one(2)")
                zap3 = int(input())
                if zap3 == 1: print(basa["classes"])
                if zap3 == 2:
                    print("wich class")
                    zap4 = int(input())
                    print(get_one_to_id(zap4,"classes"))
            if zap2 == 5: 
                print("all nachalniks(1) or one(2)")
                zap3 = int(input())
                if zap3 == 1: print(basa["nachalniks"])
                if zap3 == 2:
                    print("wich nachalnik")
                    zap4 = int(input())
                    print(get_one_to_id(zap4,"nachalniks"))
                    
    if zap == 3:
        basa = read_inf("basa.json")
        print("display update workers(1) or nachalniks(2)")
        zap1 = int(input()) 
        if zap1 == 1:
            print("wich worker")
            zap2 = int(input())
            new_n = input("new name ")
            new_a = input("new age ")
            new_e = input("new email ")
            print(up_for_id(zap2,{"name": new_n,"age": new_a,"email": new_e},"workers"))
        if zap1 == 2:
            print("wich nachalnik")
            zap2 = int(input())
            new_n = input("new name ")
            new_a = input("new age ")
            new_e = input("new email ")
            print(up_for_id(zap2,{"name": new_n,"age": new_a,"email": new_e},"nachalniks"))
            
    if zap == 1:
        print("display create workers(1) or nachalniks(2)")
        zap1 = int(input()) 
        if zap1 == 1:
            new_n = input("name ")
            new_a = input("age ")
            new_e = input("email ")
            cread_one_to_id({"name": new_n,"age": new_a,"email": new_e},"workers"),"basa.json"
            print(read_inf("basa.json")["workers"])
        if zap1 == 2:
            new_n = input("name ")
            new_a = input("age ")
            new_e = input("email ")
            cread_one_to_id({"name": new_n,"age": new_a,"email": new_e},"nachalniks"),"basa.json"
            print(read_inf("basa.json")["nachalniks"])
    
            
    if zap == 4:
        print("display delete workers(1) or nachalniks(2)")
        zap1 = int(input()) 
        if zap1 == 1:
            print("wich worker")
            zap2 = int(input())
            delete_one_to_id(zap2,"workers")
            print(read_inf("basa.json")["workers"])
        if zap1 == 2:
            print("wich nachalnik")
            zap2 = int(input())
            delete_one_to_id(zap2,"nachalniks")
            print(read_inf("basa.json")["nachalniks"])
            
            

            
                    

                    

                    
                
            
                
        
