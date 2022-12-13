let _params = (new URL(document.location)).searchParams;
var _member_id = _params.get("member_id");
console.log(_member_id);


function processInt(val){
    if(val=="")
        return 0;
    return val
}

const updateMemberData = async (update_form) => {
    let options = {
        method : "PUT",
        headers : {
            "Content-Type":"application/json",
        },
        body : JSON.stringify(update_form)

    }

    email = member_id.split('@')

    user = email[0];

    domain = email[1];

    let response = await fetch("https://yoga-backend.deta.dev/member/update?id="+user+"%40"+domain, options);
    let json = response.json();
    return json;
}

const mainFunc = async() =>{

    var _id = _member_id;
    var _name = document.getElementById("name").value;
    var _age = document.getElementById("age").value;
    var _gender_option = document.getElementById("gender").selectedIndex;
    var _gender = document.getElementsByTagName("option")[_gender_option].value;
    var _address = document.getElementById("address").value;
    var _pin = processInt(document.getElementById("pin").value);
    var _mobile = processInt(document.getElementById("mobile").value);

    if (_age!="" && (_age<18 || _age>65)){
        window.alert("Member can't be younger than 18 and older than 65!");
        return;
    }

    _age = processInt(_age);

    console.log(_address)

    let update_form = {
        id: _id,
        name: _name,
        age: _age,
        gender: _gender,
        address: _address,
        pin: _pin,
        mobile: _mobile,
    }

    console.log(update_form)

    let response = await updateMemberData(update_form);
    
    console.log(response);

    alert(response["response"]);
    
    
}