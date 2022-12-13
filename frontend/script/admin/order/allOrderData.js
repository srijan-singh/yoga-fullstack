let fetchAPI = async (id) => {
    let response = await fetch("http://127.0.0.1:8000/admin/order/*?access_id="+id);
    let json = await response.json();
    console.log(json);
    return json;
}

let tableFromJson = async () => {

    var orderList = await fetchAPI("admin123");

    const tableData = orderList.map(order => {
    return (
        `<tr>
        <td>${order.id}</td>
        <td>${order.member_id}</td>
        <td>${order.fee}</td>      
        <td>${order.timestamp}</td>  
        </tr>`
    );
    }).join('');

    const tableBody = document.querySelector("#tableBody");
    tableBody.innerHTML = tableData;
}
