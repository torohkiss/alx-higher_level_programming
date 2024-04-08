#!/usr/bin/node

const al = process.argv.length;  
if (al === 2) {
	console.log('No argument');
} else if (al === 3) {
	console.log('Argument found');
} else {
	console.log('Arguments found');
}
