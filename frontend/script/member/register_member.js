const registerMember = async (register_form) => {
    let options = {
        method : "POST",
        headers : {
            "Content-Type":"application/json",
        },
        body : JSON.stringify(register_form)

    }
    let response = await fetch("https://yoga-backend.deta.dev/register_member", options);
    let json = response.json();
    return json;
}

const mainFunc = async() =>{
    var _id = document.getElementById("id").value;
    var _name = document.getElementById("name").value;
    var _age = document.getElementById("age").value;
    var _gender_option = document.getElementById("gender").selectedIndex;
    var _gender = document.getElementsByTagName("option")[_gender_option].value;
    var _address = document.getElementById("address").value;
    var _pin = document.getElementById("pin").value;
    var _mobile = document.getElementById("pin").value;

    console.log(_address)

    let register_form = {
        id: _id,
        name: _name,
        age: _age,
        gender: _gender,
        address: _address,
        pin: _pin,
        mobile: _mobile,
    }

    console.log(register_form)

    let response = await registerMember(register_form);
    console.log(response);

    alert(response["response"]); 
}

