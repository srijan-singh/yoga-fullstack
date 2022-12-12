import pymongo
# Model
from models import Member, Batch, Order
from bson import ObjectId
import datetime

# Access Key
from setting import access_key

client = pymongo.MongoClient(access_key)
database = client["Yoga"]

member_collection = database["Member"]
batch_collection = database["Batch"]
order_collection = database["Order"]

#Member
def getAllMember():
    member_list = list(member_collection.find({}))

    buffer = [member for member in member_list]

    member_list = []

    for MemberResponse in buffer:

        member = Member(MemberResponse)

        json = {
            "_id"    : str(member._id),
            "name"   : str(member.name),
            "age"    : str(member.age),
            "gender" : str(member.gender),
            "address": str(member.address),
            "pin"    : str(member.pin),
            "mobile" : str(member.mobile)
        }

        member_list.append(json)

    return member_list

def getOneMember(_id : str):
    try:
        member = Member(member_collection.find_one({"_id":_id}))

        json = {
                "_id"    : str(member._id),
                "name"   : str(member.name),
                "age"    : str(member.age),
                "gender" : str(member.gender),
                "address": str(member.address),
                "pin"    : str(member.pin),
                "mobile" : str(member.mobile)
            }

        return json

    except:
        return {400 : "Invalid Credential"}

def postMember(_id : str, name : str, age : int, gender : str, address : str, pin : int, mobile : int):

    if(member_collection.find_one({"_id":_id})):
        return {302 : "Email aLready in use!"}
    
    data = {
        "_id"    : _id,
        "name"   : name,
        "age"    : age,
        "gender" : gender,
        "address": address,
        "pin"    : pin,
        "mobile" : mobile
    }

    member_collection.insert_one(data)

    return getOneMember(_id)

def putMember(_id: str, name : str = None, age : int = None, gender : str = None, address : str = None, pin : int = None, mobile : int = None):

    try:

        if(name):
            update_data = {
                "$set":{
                    "name":name
                }
            }

            member_collection.update_one({"_id":_id}, update_data) 

        if(age):
            update_data = {
                "$set":{
                    "age":age
                }
            }

            member_collection.update_one({"_id":_id}, update_data) 

        if(gender):
            update_data = {
                "$set":{
                    "gender":gender
                }
            }

            member_collection.update_one({"_id":_id}, update_data) 

        if(address):
            update_data = {
                "$set":{
                    "address":address
                }
            }

            member_collection.update_one({"_id":_id}, update_data)

        if(pin):
            update_data = {
                "$set":{
                    "pin":pin
                }
            }

            member_collection.update_one({"_id":_id}, update_data)  

        if(mobile):
            update_data = {
                "$set":{
                    "mobile":mobile
                }
            }

            member_collection.update_one({"_id":_id}, update_data) 

        return getOneMember(_id)

    except:
        return {400 : "Invalid Credential"}

def deleteMember(_id : str):
    try:
        response = member_collection.find_one_and_delete({"_id":_id})
        return response
    except:
        return {400 : "Invalid Credential"}

#Batch
def getAllBatch():
    batch_list = list(batch_collection.find({}))
    
    buffer = [batch for batch in batch_list]

    batch_list = []

    for BatchResponse in buffer:

        batch = Batch(BatchResponse)

        json = {
            "_id" : str(batch._id),
            "slot": str(batch.slot),
            "cost": str(batch.cost)
        }

        batch_list.append(json)

    return batch_list

def getOneBatch(_id : str):
    try:
        batch = Batch(batch_collection.find_one({"_id":_id}))

        json = {
                "_id" : str(batch._id),
                "slot": str(batch.slot),
                "cost": str(batch.cost)
            }

        return json
    except:
        {400: "Invalid Credential"}

def postBatch(_id : str, batch_slot : str, batch_cost : float):

    if(batch_collection.find_one({"_id":_id})):
        return {302 : "Batch aLready exist!"}

    data = {
        "_id" : _id,
        "slot":batch_slot,
        "cost":batch_cost
        }

    batch_collection.insert_one(data)

    return data

def putBatch(_id : str, batch_slot : str = None, batch_cost : float = None):

    try:

        if(batch_slot):
            update_data = {
                "$set":{
                        "slot":batch_slot
                        }
            } 

            batch_collection.update_one({"_id":_id}, update_data) 

        if(batch_cost):
            update_data = {
                "$set":{
                        "cost":batch_cost
                        }
            } 

            batch_collection.update_one({"_id":_id}, update_data) 

        return getOneBatch(_id)

    except:

        return {400 : "Invalid Credential"}

def deleteBatch(_id : str):
    try:

        response = batch_collection.find_one_and_delete({"_id":_id})

        return response

    except:
        return {400 : "Invalid Credential"}

#Order
def getOneOrder(_id : ObjectId):
    
    try:
        order = Order(order_collection.find_one({"_id":_id}))


        json = {
            "_id"       : str(_id),
            "member_id" : str(order.member_id),
            "batch_id"  : str(order.batch_id),
            "fee"       : str(order.fee),
            "timestamp" : str(order.timestamp)
        }

        return json

    except:
        return {400 : "Order Don't exist!"}

def getOrder(_id : ObjectId):

    try:
        order = getOneOrder(_id)
        member = getOneMember(ObjectId(order["member_id"]))
        batch = getOneBatch(ObjectId(order["batch_id"]))

        order_recipient = {
            "order_id"  : order["_id"],
            "timestamp" : order["timestamp"],

            "batch_cost": batch["cost"],
            "batch_id"  : batch["_id"],
            "batch_slot": batch["slot"],
            
            "member_id" : member["_id"],
            "name"      : member["name"],
            "age"       : member["age"],
            "gender"    : member["gender"],
            "address"   : member["address"],
            "pin"       : member["pin"],
            "mobile"    : member["mobile"],

        }

        return order_recipient
    
    except:
        return {400 : "Invalid Credential"}

def postOrder(member_id : str, batch_id : str):
    
    try:

        member = getOneMember(member_id)
        batch = getOneBatch(batch_id)
        timestamp = datetime.datetime.now()

        order_data = {
            "member_id" : member["_id"],
            "batch_id"  : batch["_id"],
            "fee"   : batch["cost"],
            "timestamp" : timestamp
        }

        _id = order_collection.insert_one(order_data).inserted_id

        order_recipient = {
            "order_id"  : str(_id),
            "timestamp" : timestamp,

            "fee"       : batch["cost"],
            "batch_id"  : batch["_id"],
            "batch_slot": batch["slot"],
            
            "member_id" : member["_id"],
            "name"      : member["name"],
            "age"       : member["age"],
            "gender"    : member["gender"],
            "address"   : member["address"],
            "pin"       : member["pin"],
            "mobile"    : member["mobile"],

        }

        return order_recipient

    except:
        return {400: "Invalid Credential"}


if __name__ == "__main__":

    #member_id = ObjectId("6395b6ec14fdf993bb7a17da")
    #batch_id = ObjectId("639586591f71f7951080c3dc")

    #order_id = "6395fd733dfb479cdce28d85"

    #print(getOrder(ObjectId(order_id)))

    #print(postOrder(member_id, batch_id))

    #print(putBatch("7-9 PM", 500.00))

    #_id = ObjectId("639586591f71f7951080c3dc")

    #print(updateBatch(_id, "9-10 AM", 500.00))

    #print(deleteBatch(_id))

    #print(postMember("Ramdhari Singh Dinkar3", 128, "Male", "Bihar", 201005, 869934562))

    """
    batch = getOneBatch(_id)
    print("Batch: ",batch._id, " Slot: ", batch.slot, " Cost: ", batch.cost)
    print(allBatch())"""