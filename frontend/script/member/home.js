let _params = (new URL(document.location)).searchParams;
var _member_id = _params.get("member_id");
// api url
const api_url =
    'https://yoga-backend.deta.dev/member/transaction/*?id='+_member_id;

// Defining async function
async function getapi(url) {
	
	// Storing response
	const response = await fetch(url);
	
	// Storing data in form of JSON
	var data = await response.json();
	if (response) {
		hideloader();
	}
	show(data);
}
// Calling that async function
getapi(api_url);

// Function to hide the loader
function hideloader() {
	document.getElementById('loading').style.display = 'none';
}
// Function to define innerHTML for HTML table
function show(database) {
	let tab = ""

    console.log(database);
	i=1;
	// Loop to access all rows
	for (let data of database) {
		tab +=
		`
        <tr><th></th></tr>
        <tr><td colspan="2">Recipient ${i++}</td></tr>
        <tr>
		<th>Order Id</th>
        <td>${data.order_id} </td>
        </tr>
		<th>Fee of</th><td>${data.timestamp}</td>         <th>Fee Paid</th><td>${data.batch_cost}</td></tr>
        <th>Name</th><td>${data.name}</td>                <th>Age</th><td>${data.age}</td></tr>
        <th>Batch ID</th><td>${data.batch_id}</td>        <th>Batch Slot</th><td>${data.batch_slot}</td></tr>        
        <th>Mobile</th><td>${data.mobile}</td>            <th>Pin</th><td>${data.pin}</td></tr>
        <tr><th></th></tr>
        `;
	}

    console.log(tab);

	// Setting innerHTML as tab variable
    document.getElementById("h4").innerHTML = "Transaction History";
    document.getElementById('recipient').bgColor = '#FFF'; 
    document.getElementById("recipient").style = "height:220px; width:100%;";
    document.getElementById("recipient").scrollIntoView({
        behavior: 'smooth',
        block: 'end',
        inline: 'start'
     }); 
	document.getElementById("recipient").innerHTML = tab;
    
}
