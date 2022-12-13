let _params = (new URL(document.location)).searchParams;
var _member_id = _params.get("member_id");
console.log(_member_id);

const memberDeletion = async (member_id) => {
    let response = await fetch("https://yoga-backend.deta.dev/member/delete?id="+member_id, { method: 'DELETE' });
    let json = response.json();
    return json;
}

const mainFunc = async() =>{
    var input_id = _member_id;

    console.log(input_id)

    let response = await memberDeletion(input_id);

    if(response["response"] == "error")
    {
        alert("Member Not Found!");     
    }

    else
    {
        document.location.href = "../../pages/auth/login.html";
    }
    
}