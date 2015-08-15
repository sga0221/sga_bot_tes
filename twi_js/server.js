var express = require('express')
, app = express()
, server = require('http').createServer(app)
, io = require('socket.io').listen(server);

//port: Heroku || AppFog || 3000
var port = process.env.PORT || process.env.VMC_APP_PORT || 3000;
server.listen(port);

app.use(express.static(__dirname + '/public'));

var twitter = require('ntwitter');
var auth = require('./auth_sga.js');

var tw = new twitter({
    consumer_key: auth.consumer_key(),
    consumer_secret: auth.consumer_secret(),
    access_token_key: auth.access_token_key(),
    access_token_secret: auth.access_token_secret()
});

tw.stream('statuses/sample', function(stream) {
    stream.on('data', function (data) {
	io.sockets.emit('message', {
	    'text': data
	});
    });
});
