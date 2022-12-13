# Yoga Backend

<img src ="https://img.shields.io/tokei/lines/github/srijan-singh/yoga-fullstack?label=Line%20of%20Code"> <img src ="https://img.shields.io/github/repo-size/srijan-singh/yoga-fullstack?color=succeess&label=Size"> <img src="https://img.shields.io/github/directory-file-count/srijan-singh/yoga-fullstack/backend?color=yellow&label=%20Backend%20File"> <img src="https://img.shields.io/github/directory-file-count/srijan-singh/yoga-fullstack/frontend/pages/auth?color=pink&label=Authorization%20Page"> <img src="https://img.shields.io/github/directory-file-count/srijan-singh/yoga-fullstack/frontend/pages/member?color=violet&label=Member%20Page">


## Technology

- FastAPI : API Framework
- MongoDB : Database

## Schema

- ### Member

    - _id     : varchar (Primary Key)
    - name    : varchar 
    - age     : int 
    - gender  : varchar 
    - address : varchar 
    - pin     : int 
    - mobile  : int 

- ### Batch

    - _id  : varchar (Primary Key)
    - slot : varchar
    - cost : decimal 

- ### Order

    - _id       : varchar (Primary Key)
    - member_id : int (Foreign Key)
    - batch_id  : int (Foreign Key)
    - fee       : decimal
    - timestamp : datetime

- ### ER Diagram
    <img src="https://github.com/srijan-singh/yoga-fullstack/blob/main/res/img2.png">


## Querries

- ### Member
    - getAllMember
    - getOneMember
    - postMember
    - putMember
    - deleteMember

- ### Batch
    - getAllBatch
    - getOneBatch
    - postBatch
    - putBatch
    - deleteBatch

- ### Order
    - getAllOrder
    - getOneOrder
    - getRecipient
    - postOrder


## API

- ### User Interface
    <img src="https://github.com/srijan-singh/yoga-fullstack/blob/main/res/img1.png">

- ### Requests

    #### Member (General)
        - register_member
        - show_one_member
        - update_member
        - remove_member

    #### Batch (General)
        - show_all_batch
        - show_one_batch

    #### Order (General)
        - pay_fee
        - show_recipient

    #### Member (Admin Access)
        - show_all_member

    #### Batch (Admin Access)
        - add_batch
        - update_batch
        - delete_batch

    #### Order (Admin Access)
        - show_all_order



