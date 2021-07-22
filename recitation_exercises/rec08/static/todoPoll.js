let timeoutID;
let timeout = 10000;

function setup() {
	document.getElementById("theButton").addEventListener("click", makePost);
	timeoutID = window.setTimeout(poller, timeout);
}

function makePost() {
	console.log("Sending POST request");
	const name = document.getElementById("todo_name").value
	
	fetch("/todos", {
			method: "post",
			headers: { "Content-type": "application/json" },
			body: JSON.stringify({task : name})
		})
		.then((response) => {
			return response.json();
		})
		.then((result) => {
			updateTable(result);
			clearInput();
		})
		.catch(() => {
			console.log("Error posting new items!");
		});
}

function poller() {
	console.log("Polling for new items");
	fetch("/todos")
		.then((response) => {
			return response.json();
		})
		.then(updateTable)
		.catch(() => {
			console.log("Error fetching items!");
		});
}

function updateTable(result) {
	console.log("Updating the table");
	const info = JSON.parse(result);
	console.log(info);
	const tab = document.getElementById("theTable");
	while (tab.rows.length > 0) {
		tab.deleteRow(0);
		console.log("deleted row");
	}
	
	for (let i in info) {
		console.log("going to add row");
		addRow(i);
		console.log("added row");
	}
	
	timeoutID = window.setTimeout(poller, timeout);
}

function addRow(row) {
	const tableRef = document.getElementById("theTable");
	const newRow = tableRef.insertRow();

	const newCellOne = newRow.insertCell();
	const newTextOne = document.createTextNode(row);
	newCellOne.appendChild(newTextOne);
	
	const newCellTwo = newRow.insertCell();
	const newTextTwo = document.createTextNode(row[newTextOne]);
	newCellTwo.appendChild(newTextTwo);
	
}

function clearInput() {
	console.log("Clearing input");
	document.getElementById("a").value = "";
	document.getElementById("b").value = "";
	document.getElementById("c").value = "";
}

window.addEventListener("load", setup);
