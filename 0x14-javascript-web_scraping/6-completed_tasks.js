#!/usr/bin/node

const request = require('request');
const url = 'https://jsonplaceholder.typicode.com/todos';

request(url, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    const completedTasks = {};
    const tasks = JSON.parse(body);

    tasks.forEach((task) => {
      if (task.completed) {
        if (completedTasks[task.userId]) {
          completedTasks[task.userId]++;
        } else {
          completedTasks[task.userId] = 1;
        }
      }
    });
    console.log(completedTasks);
  }
});
