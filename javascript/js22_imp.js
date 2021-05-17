function imp_main(data) {
	// Imperative
	let avgs = [], total = 0, avg = 0;

	for (let i=0; i < data.length; i++) {
		total = 0;
		for (let j=0; j < data[i].points.length; j++) {
			total += data[i].points[j];
		}
		avg = total / data[i].points.length;
		avgs.push([data[i].name, avg]);
	}

	console.log(JSON.stringify(avgs));
}
