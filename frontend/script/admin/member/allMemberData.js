let fetchAPI = async (id) => {
    let response = await fetch("http://127.0.0.1:8000/admin/member/*?access_id="+id);
    let json = await response.json();
    console.log(json);
    return json;
}

let tableFromJson = async () => {

    var memberList = await fetchAPI("admin123");

    const tableData = memberList.map(member => {
    return (
        `<tr>
        <td>${member.id}</td>
        <td>${member.name}</td>
        <td>${member.age}</td>
        <td>${member.gender}</td>
        <td>${member.address}</td>
        <td>${member.pin}</td>  
        <td>${member.mobile}</td>          
        </tr>`
    );
    }).join('');

    const tableBody = document.querySelector("#tableBody");
    tableBody.innerHTML = tableData;
}
