const memberLogin = async (_id) => {
    let response = await fetch("https://yoga-backend.deta.dev/member?id="+_id, { method: 'GET' });
    let json = response.json();
    return json;
}

const mainFunc = async() =>{
    var input_id = document.getElementById("id").value;

    console.log(input_id)

    let response = await memberLogin(input_id);

    if(response["response"] == "error")
    {
        alert("Member Not Found!");     
    }

    else
    {
        document.location.href = "../../pages/member/home.html?member_id="+input_id;
    }
    
}