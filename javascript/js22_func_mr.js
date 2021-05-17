// Functional (w/ Array.map() and Array.reduce())
function add(a, b) {
	return a + b;
}

function average(arr) {
	return arr.reduce(add) / arr.length;
}

function grabAtt(att) {
	return function(item) { return item[att]; };
}

function combiner(arr1, arr2) {
	function combmap(e, i) {
		return [e, arr2[i]];
	}
	const result = arr1.map(combmap);
	return result;
}

function func_mr_main(data) {
	const names = data.map(grabAtt("name"));
	const points = data.map(grabAtt("points"));
	const avgs = points.map(average);
	const pairs = combiner(names, avgs, []);

	console.log(JSON.stringify(pairs));
}
