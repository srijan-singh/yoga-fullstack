import uvicorn
from fastapi import FastAPI, HTTPException
# an HTTP-specific exception class  to generate exception information
from fastapi.middleware.cors import CORSMiddleware

from models import Member, Batch, Order, Payment

from bson import ObjectId

#Payment Gateway
def CompletePayment(response):
    return response


from databases import(
    #Member
    getAllMember,
    getOneMember,
    postMember,
    putMember,
    deleteMember,

    #Batch
    getAllBatch,
    getOneBatch,
    postBatch,
    putBatch,
    deleteBatch,

    #Order
    postOrder,
    getRecipient,
    getAllOrder
)

app = FastAPI()

origins = [
    "*",
]

# what is a middleware? 
# software that acts as a bridge between an operating system or database and applications, especially on a network.

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def index():
    return {"Yoga":"Backend"}

#   Member
@app.post("/register_member")
async def register_member(request : Member):
    response = postMember(request)
    return request

@app.get("/member/{id}")
async def show_one_member(id:str):
    response = getOneMember(id)
    return response

@app.put("/member/{id}/update")
async def update_member(id : str, member : Member):
    response = putMember(id, member.name, member.age, member.gender, member.address, member.pin, member.mobile)
    return response

@app.delete("/member/{_id}/delete")
async def remove_member(_id : str):
    
    response = deleteMember(_id)

    if (response): 
        return {200 : "User Deleted"}

    return {500 : "User doesn't exist"}

#   Batch
@app.get("/batch/*")
async def show_all_batch():
    response = getAllBatch()
    return response

@app.get("/batch/{_id}")
async def show_one_batch(_id : str):
    
    response = getOneBatch(_id)
    return response

#   Order
@app.post("/payfee/payment_gateway/")
async def pay_fee(payment : Payment):

    if(CompletePayment(payment.fee_paid)):
        return postOrder(payment.member_id, payment.batch_id)

    return {"response": "Transaction Failed"}

@app.get("/order/{id}")
async def show_recipient(id:str):
    _id = ObjectId(id)

    return getRecipient(_id)

############################################Admin Access#################################################

#   Member
@app.get("/admin/member/*")
async def show_all_member(access_id : str):
    if(access_id != "admin123"):
        return {400 : "Forbiden!"}
    response = getAllMember()
    return response

#   Batch
@app.post("/admin/add_batch")
async def add_batch(access_id : str, batch:Batch):
    if(access_id != "admin123"):
        return {"response" : "Forbiden!"}
    response = postBatch(bacth.id, batch.slot, batch.cost)
    return response

@app.put("/admin/batch/{_id}/update")
async def update_batch(access_id : str, _id : str, batch:Batch):
    if(access_id != "admin123"):
        return {400 : "Forbiden!"}

    response = putBatch(batch.id, batch.slot, batch.cost)
    return response
    
@app.delete("/admin/batch/{id}/delete")
async def delete_batch(access_id : str, _id:str):
    if(access_id != "admin123"):
        return {400 : "Forbiden!"}
    
    response = deleteBatch(_id)

    if (response): 
        return {200 : "Batch Deleted"}

    return {500 : "Batch doesn't exist"}

#   Order
@app.get("/admin/order/*")
async def show_all_order(access_id : str):
    if(access_id != "admin123"):
        return {"response" : "Forbiden!"}

    return getAllOrder()

if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)

