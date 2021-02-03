/*jshint node:true */
/*global require */
'use strict';

var http = require('http'),
    express = require('express'),
    app = express(),
    port = 5000;

//app.use(bodyParser.json());
//app.use(bodyParser.urlencoded({extended: true}));

app.get('/health', function(request, response, next){
	response.send('{"status": "healthy"}');
})

app.use(express.static('../dashboard'));

app.listen(port, function() {
  console.log(`Web service listening on port ${port}!`);
})
