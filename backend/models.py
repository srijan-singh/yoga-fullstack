from bson import ObjectId
from pydantic import BaseModel
import datetime

# Member
class Member(BaseModel):
    id      : str = None
    name    : str = None
    age     : int = None
    gender  : str = None
    address : str = None
    pin     : int = None
    mobile  : int = None

# Batch
class Batch(BaseModel):
    id   : str   = None
    slot : str   = None
    cost : float = None

# Order
class Order(BaseModel):
    member_id : str 
    batch_id  : str
    fee       : float = 500.00
    timestamp : datetime.datetime 

class Payment(BaseModel):
    member_id : str
    batch_id  : str
    fee_paid  : bool = False 
