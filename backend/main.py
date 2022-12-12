import uvicorn
from fastapi import FastAPI, HTTPException
# an HTTP-specific exception class  to generate exception information
from fastapi.middleware.cors import CORSMiddleware

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
    getOrder
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

#Member
@app.post("/register_member")
async def register_member(_id:str, name : str, age : int, gender : str, address : str, pin : int, mobile : int):
    response = postMember(_id, name, age, gender, address, pin, mobile)
    return response

@app.get("/member/{_id}")
async def show_one_member(_id:str):
    response = getOneMember(_id)
    return response

@app.put("/member/{_id}/update")
async def update_member(_id:str, name : str = None, age : int = None, gender : str = None, address : str = None, pin : int = None, mobile : int = None):
    response = putMember(_id, name, age, gender, address, pin, mobile)
    return response

@app.delete("/member/{_id}/delete")
async def remove_member(_id : str):
    
    if (response): 
        return {200 : "User Deleted"}

    return {500 : "User doesn't exist"}

#Batch
@app.get("/batch/*")
async def show_all_batch():
    response = getAllBatch()
    return response

@app.get("/batch/{_id}")
async def show_one_batch(_id : str):
    
    response = getOneBatch(_id)
    return response

#Order
@app.post("/member/{member_id}/batch/{batch_id}/order")
async def pay_fee(member_id: str, batch_id: str, payment:bool = False):
    
    if(payment):
        return postOrder(member_id, batch_id)

    return {500: "Transaction Failed"}

@app.get("/order/{id}")
async def show_recipient(id:str):
    _id = ObjectId(id)

    return getOrder(_id)

#Admin Access

#Member
@app.get("/admin/member/*")
async def show_all_member(access_id : str):
    if(access_id != "admin123"):
        return {400 : "Forbiden!"}
    response = getAllMember()
    return response

#Batch
@app.post("/admin/add_batch")
async def add_batch(access_id : str, _id : str, batch_slot : str, batch_cost : float):
    if(access_id != "admin123"):
        return {400 : "Forbiden!"}
    response = postBatch(_id, batch_slot, batch_cost)
    return response

@app.put("/admin/batch/{_id}/update")
async def update_batch(access_id : str, _id : str, batch_slot : str = None, batch_cost : float = None):
    if(access_id != "admin123"):
        return {400 : "Forbiden!"}

    response = putBatch(_id, batch_slot, batch_cost)
    return response
    
@app.delete("/admin/batch/{id}/delete")
async def delete_batch(access_id : str, _id:str):
    if(access_id != "admin123"):
        return {400 : "Forbiden!"}
    
    response = deleteBatch(_id)

    if (response): 
        return {200 : "Batch Deleted"}

    return {500 : "Batch doesn't exist"}



if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)
    