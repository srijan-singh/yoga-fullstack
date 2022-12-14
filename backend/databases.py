import pymongo
# Model
from models import Member, Batch, Order, Payment
import datetime

# Access Key
from setting import access_key

from bson import ObjectId

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

    for member in buffer:

        json = {
            "id"    : member["_id"],
            "name"   : member["name"],
            "age"    : member["age"],
            "gender" : member["gender"],
            "address": member["address"],
            "pin"    : member["pin"],
            "mobile" : member["mobile"]
        }

        member_list.append(json)

    return member_list

def getOneMember(id : str):
    try:
        member = member_collection.find_one({"_id":id})

        json = {
            "id"    : member["_id"],
            "name"   : member["name"],
            "age"    : member["age"],
            "gender" : member["gender"],
            "address": member["address"],
            "pin"    : member["pin"],
            "mobile" : member["mobile"]
        }

        return json

    except:

        return False

def postMember(member : Member):

    if(member_collection.find_one({"_id":member.id})):
        return {"response" : "Email aLready in use!"}
    
    data = {
        "_id"    : member.id,
        "name"   : member.name,
        "age"    : member.age,
        "gender" : member.gender,
        "address": member.address,
        "pin"    : member.pin,
        "mobile" : member.mobile
    }

    member_collection.insert_one(data)

    return {"response" : "Member Added Successfully!"}

def putMember(_id: str, name : str = None, age : int = None, gender : str = None, address : str = None, pin : int = None, mobile : int = None):

    try:

        if(name):
            update_data = {
                "$set":{
                    "name":name
                }
            }

            member_collection.update_one({"_id":_id}, update_data) 

        if(age!=0):
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

        if(pin!=0):
            update_data = {
                "$set":{
                    "pin":pin
                }
            }

            member_collection.update_one({"_id":_id}, update_data)  

        if(mobile!=0):
            update_data = {
                "$set":{
                    "mobile":mobile
                }
            }

            member_collection.update_one({"_id":_id}, update_data) 

        return True

    except:
        return False

def deleteMember(_id : str):
    try:
        response = member_collection.find_one_and_delete({"_id":_id})
        return response
    except:
        return {"response" : "Invalid Credential"}

def getTransactionHistory(_id : str):
    transaction_list = list(order_collection.find({"member_id":_id}))
    #print(transaction_list)

    buffer = [transaction for transaction in transaction_list]

    transaction_list = []

    for transaction in buffer:

        order_id = transaction["_id"]

        json = getRecipient(order_id)

        transaction_list.append(json)

    return transaction_list

#Batch
def getAllBatch():
    batch_list = list(batch_collection.find({}))
    
    buffer = [batch for batch in batch_list]

    batch_list = []

    for batch in buffer:

        json = {
            "id" : batch["_id"],
            "slot": batch["slot"],
            "cost": str(batch["cost"])
        }

        batch_list.append(json)

    return batch_list

def getOneBatch(_id : str):
    try:
        batch = batch_collection.find_one({"_id":_id})

        json = {
            "id" : batch["_id"],
            "slot": batch["slot"],
            "cost": str(batch["cost"])
        }

        return json
    except:
        return {"response" : "Invalid Credential"}

def postBatch(_id : str, batch_slot : str, batch_cost : float):

    if(batch_collection.find_one({"_id":_id})):
        return {"response" : "Batch aLready exist!"}

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

        return {"response" : "Invalid Credential"}

def deleteBatch(_id : str):
    try:

        response = batch_collection.find_one_and_delete({"_id":_id})

        return response

    except:
        return {"response" : "Invalid Credential"}

#Order
def getAllOrder():
    order_list = list(order_collection.find({}))

    buffer = [order for order in order_list]

    order_list = []

    for order in buffer:

        json = {
            "id" : str(order["_id"]),
            "member_id" : order["member_id"],
            "batch_id" :order["batch_id"],
            "fee": order["fee"],
            "timestamp" : order["timestamp"]
        }

        order_list.append(json)

    return order_list

def getOneOrder(_id : ObjectId):

    order = order_collection.find_one({"_id":_id})

    json = {
        "_id"       : str(order["_id"]),
        "member_id" : order["member_id"],
        "batch_id"  : order["batch_id"],
        "fee"       : order["fee"],
        "timestamp" : order["timestamp"]
    }

    return json


def getRecipient(_id : ObjectId):


    order = getOneOrder(_id)
    member = getOneMember(order["member_id"])
    batch = getOneBatch(order["batch_id"])

    order_recipient = {
        "order_id"  : str(order["_id"]),
        "timestamp" : order["timestamp"],

        "batch_cost": batch["cost"],
        "batch_id"  : batch["id"],
        "batch_slot": batch["slot"],
        
        "member_id" : member["id"],
        "name"      : member["name"],
        "age"       : member["age"],
        "gender"    : member["gender"],
        "address"   : member["address"],
        "pin"       : member["pin"],
        "mobile"    : member["mobile"],

    }

    return order_recipient
"""
    except:
        return {"response" : "Invalid Credential"}
"""
def postOrder(member_id : str, batch_id : str):

    member = getOneMember(member_id)
    batch = getOneBatch(batch_id)
    time = datetime.datetime.now()

    list_of_months = {'1': 'January', '2': 'February', '3': 'March',
                            '4': 'April', '5': 'May', '6': 'June', '7': 'July',
                            '8': 'August', '9': 'September', '10': 'October',
                            '11': 'November', '12': 'December'}

    timestamp = list_of_months[str(time.month)] +" "+ str(time.year)

    order_data = {
        "member_id" : member["id"],
        "batch_id"  : batch["id"],
        "fee"   : batch["cost"],
        "timestamp" : timestamp
    }

    _id = order_collection.insert_one(order_data).inserted_id

    order_recipient = {
        "order_id"  : str(_id),
        "timestamp" : str(timestamp),

        "fee"       : batch["cost"],
        "batch_id"  : batch["id"],
        "batch_slot": batch["slot"],
        
        "member_id" : member["id"],
        "name"      : member["name"],
        "age"       : member["age"],
        "gender"    : member["gender"],
        "address"   : member["address"],
        "pin"       : member["pin"],
        "mobile"    : member["mobile"],

    }

    return order_recipient


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