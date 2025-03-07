/*
The purpose of this exercise is to get you familiarized with promises.
*/


/*
1) 
Write a promise that resolves after waiting for 2 seconds
You can verify this by printing something to the console
after waiting for 2 seconds. Look into setTimeout function.
*/

const taskOnePromise = new Promise((resolve, reject) => {
	setTimeout(() => {
		resolve("foo");
		}, 2000);
	});
	
taskOnePromise.then(() => {console.log("task 1");});	

/*
2) 
Imagine you're programming a two player game. For this
purpose we need to write a promise that resolves when
both the players join the game. Your task is to write
a promise that resolves when the number of players is 2
otherwise it rejects. For now, you can declare a variable
that holds the number of players. Again you can print
stuff to the console to verify your implementation works
*/
let numplayers = 0;
const playerPromise = new Promise((resolve, reject) => {
	setInterval(() => { 
		if (numplayers == 2){
			resolve();
		}
	}, 200);
	});

playerPromise.then(() => {console.log("task 2");});
/*
3) 
Now we will try to chain promises together. Notice
that a promise when resolved can return a value or
another promise object. Imagine that you have to
fetch two files from the internet and then merge
the files together. Here we wont be doing any
fetching rather we'll try to emulate this by
setting timeouts. Assume it takes 3 seconds to
fetch the first file and 4 to fecth the second.
Again you can print stuff to the console to verify
your implementation works and use timeouts.
*/

const downloadOnePromise = new Promise((resolve, reject) => {
	setTimeout(() => {
		resolve("foo");
		}, 2000);
	});

downloadOnePromise.then(() => {
		console.log("First File");
	});
	
const downloadTwoPromise = downloadOnePromise.then(((resolve, reject) => {
	setTimeout(() => {
		resolve("foo");
		}, 4000);
	}));
	
downloadTwoPromise.then(() => {console.log("Second File");});





/*
After implementing the above promises. Look at the console output see if it makes sense.
Some promises might have resolved before others even though they were declared afterwards.
*/


