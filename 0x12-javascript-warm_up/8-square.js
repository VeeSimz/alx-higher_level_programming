#!/usr/bin/node

const len = process.argv[2];

if (len && parseInt(len)) {
	  let i = 0;
	  while (i < len) {
		      const x = 'X'.repeat(len);
		      console.log(x);
		      i++;
		    }
} else {
	  console.log('Missing size');
}
