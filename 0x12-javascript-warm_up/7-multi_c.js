#!/usr/bin/node

const phrase = 'C is fun';

if (process.argv.length >= 3) {
  let i = process.argv[2];
  while (i > 0) {
    console.log(phrase);
    i--;
  }
} else {
  console.log('Missing number of occurrences');
}
