let _params = (new URL(document.location)).searchParams;
var _member_id = _params.get("member_id");
console.log(_member_id);




const payMemberFee = async (fee_form) => {
    let options = {
        method : "POST",
        headers : {
            "Content-Type":"application/json",
        },
        body : JSON.stringify(fee_form)

    }

    let response = await fetch("https://yoga-backend.deta.dev/payfee/payment_gateway/", options);
    let json = response.json();
    return json;
}

const mainFunc = async() =>{

    var _id = _member_id;
    var _batch_option = document.getElementById("batch").selectedIndex;
    var _batch = document.getElementsByTagName("option")[_batch_option].value;
    var _status = document.getElementById("feeStatus").value;


    let fee_form = {
        member_id : _id,
        batch_id : _batch,
        fee_paid : true
    }

    console.log(fee_form)

    let response = await payMemberFee(fee_form);
    
    console.log(response);

    if(response["response"] == "error"){
        alert(response["response"]);
    }
    else{
        console.log(response);
        show(response);
    }
        
}

function show(data) {
	let tab =
		`
        <br>
        <tr>
		<th>Order Id</th>
        <td>${data.order_id} </td>
        </tr>
		<th>Fee of</th><td>${data.timestamp}</td>         <th>Fee Paid</th><td>${data.fee}</td></tr>
        <th>Name</th><td>${data.name}</td>                <th>Age</th><td>${data.age}</td></tr>
        <th>Batch ID</th><td>${data.batch_id}</td>        <th>Batch Slot</th><td>${data.batch_slot}</td></tr>        
        <th>Mobile</th><td>${data.mobile}</td>            <th>Pin</th><td>${data.pin}</td></tr>
        <br>`;

        console.log(data);      
        	
	// Setting innerHTML as tab variable
    document.getElementsByClassName("column")

    document.getElementById("h1").innerHTML = "Payment Recipient";

    document.getElementById('recipient').bgColor = '#FFF';
    document.getElementById("recipient").style = "height:100%; width:100%;";  

	document.getElementById("recipient").innerHTML = tab;

    document.getElementById("btn").innerHTML = String.raw`<button onclick="print_recipient()">Print</button>`;

}

function print_recipient() {
    var divToPrint=document.getElementById("recipient");
    newWin= window.open("home.html", "../../style/style.css", "width=800px, height=600px");
    newWin.document.write(String.raw`<h1 style="color: #5161ce;">Payment Recipient</h1>`+divToPrint.outerHTML);
    newWin.print();
    newWin.close();
}
