from bson import ObjectId
import datetime

#Member
class Member:
    def __init__(self, MemberResponse):
        self._id     : ObjectId = MemberResponse["_id"]
        self.name    : str = MemberResponse["name"]
        self.age     : int = MemberResponse["age"]
        self.gender  : str = MemberResponse["gender"]
        self.address : str = MemberResponse["address"]
        self.pin     : int = MemberResponse["pin"]
        self.mobile  : int = MemberResponse["mobile"]

#Batch
class Batch:
    def __init__(self, BatchResponse):
        self._id  : ObjectId  = BatchResponse["_id"]
        self.slot : str = BatchResponse["slot"]
        self.cost : float = BatchResponse["cost"]

#Order
class Order():
    def __init__(self, OrderResponse):
        self._id       : ObjectId = OrderResponse["_id"]
        self.member_id : int = OrderResponse["member_id"]
        self.fee       : float = OrderResponse["fee"]
        self.batch_id  : int = OrderResponse["batch_id"]
        self.timestamp : datetime.datetime = OrderResponse["timestamp"]
