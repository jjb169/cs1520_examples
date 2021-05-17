// Functional
function totalAcrossArray(arr, curTotal) {
	if (arr.length > 0) {
		const newTotal = curTotal + arr[0];
		const remaining = arr.slice(1);
		return totalAcrossArray(remaining, newTotal);
	}
	else {
		return curTotal;
	}
}

function avgAcrossArray(arr) {
	return totalAcrossArray(arr, 0) / arr.length;
}

function avgAllSubarrays(arr, oldList) {
	if (arr.length > 0) {
		const remaining = arr.slice(1);
		// use of Array.concat() to generate a new Array
		const newList = oldList.concat([avgAcrossArray(arr[0])]);
		// had typo here, tried to reference "resmaining"
		return avgAllSubarrays(remaining, newList);
	}
	else {
		return oldList;
	}
}

function grab(arr, oldList, att) {
	if (arr.length > 0) {
		const remaining = arr.slice(1);
		// again, use Array.concat()
		const newList = oldList.concat([arr[0][att]]);
		return grab(remaining, newList, att);
	}
	else {
		return oldList;
	}
}

function combineArrays(arr1, arr2, oldList) {
	if (arr1.length > 0 && arr2.length > 0) {
		const newPair = [arr1[0], arr2[0]];
		// again, use Array.concat()
		const newList = oldList.concat([newPair]);
		const rem1 = arr1.slice(1);
		const rem2 = arr2.slice(1);
		return combineArrays(rem1, rem2, newList);
	}
	else {
		return oldList;
	}
}

function func_main(data) {
	// had typo here, mentioned the att as "names" instead of "name"
	const names = grab(data, [], "name");
	const points = grab(data, [], "points");
	// had a bug here, did not provide empty array to avgAllSubarrays()
	const avgs = avgAllSubarrays(points, []);
	const pairs = combineArrays(names, avgs, []);

	console.log(JSON.stringify(pairs));
}
