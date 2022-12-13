// api url
const api_url =
    'https://yoga-backend.deta.dev/batch/*';

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
function show(data) {
	let tab =
		`<tr>
		<th>Batch Id</th>
		<th>Slot</th>
		<th>Cost</th>
		</tr>`;

        console.log(data);
	
	// Loop to access all rows
	for (let r of data) {
		tab += `<tr>
	<td>${r.id} </td>
	<td>${r.slot}</td>
	<td>${r.cost}</td>		
</tr>`;
	}
	// Setting innerHTML as tab variable
    document.getElementById('batch').bgColor = '#FFF';
    document.getElementById("batch").style = "height:100%; width:100%;";    
	document.getElementById("batch").innerHTML = tab;
    
}
