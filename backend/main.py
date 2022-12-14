from fastapi import FastAPI, HTTPException
# an HTTP-specific exception class  to generate exception information
from fastapi.middleware.cors import CORSMiddleware

from models import Member, Batch, Order, Payment

from bson import ObjectId
import uvicorn

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
    getTransactionHistory,

    #Batch
    getAllBatch,
    getOneBatch,
    postBatch,
    putBatch,
    deleteBatch,

    #Order
    postOrder,
    getOneOrder,
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
    if(getOneMember(request.id)):
        return {"response":"Already Registered!"}
    response = postMember(request)
    return {"response":"Successfully Registered!"}

@app.get("/member")
async def show_one_member(id:str):
    response = getOneMember(id)

    if(not response):
        return {"response" : "error"}

    return response

@app.put("/member/update")
async def update_member(id : str, member : Member):
    response = putMember(id, member.name, member.age, member.gender, member.address, member.pin, member.mobile)
    
    if(not response):
        return {"response" : "error"}

    return {"response" : "Successfully Updated!"}

@app.delete("/member/delete")
async def remove_member(id : str):
    response = deleteMember(id)

    if (not response): 
        return {"response" : "error"}

    return response

@app.get("/member/transaction/*")
async def transaction_history(id : str):
    return getTransactionHistory(id)

#   Batch
@app.get("/batch/*")
async def show_all_batch():
    response = getAllBatch()
    return response

@app.get("/batch")
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

    return getOneOrder(_id)

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

