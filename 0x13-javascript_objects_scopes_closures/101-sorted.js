#!/usr/bin/node

const dict = require('./101-data.js');

const newDict = {};
const logs = dict.dict;

for (const key in logs) {
  if (newDict[logs[key]] === undefined) {
    newDict[logs[key]] = [key];
  } else {
    newDict[logs[key]].push(key);
  }
}

console.log(newDict);
