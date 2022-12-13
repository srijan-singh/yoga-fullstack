let params = (new URL(document.location)).searchParams;
var member_id = params.get("member_id");
console.log(member_id);

function login(){
    document.location.href = "../../pages/auth/login.html";
}

function register(){
    document.location.href = "../../pages/auth/register.html";   
}

function home(){
    document.location.href = "../../pages/member/home.html?member_id="+member_id;
}

function payFee(){
    document.location.href = "../../pages/member/payfee.html?member_id="+member_id;
}

function showBatch(){
    document.location.href = "../../pages/member/batch.html?member_id="+member_id;
}

function updateMember(){
    document.location.href = "../../pages/member/update.html?member_id="+member_id;
}

function deleteMember(){
    document.location.href = "../../pages/member/delete.html?member_id="+member_id;
}

function logout(){
    document.location.href = "../../pages/auth/login.html";
}