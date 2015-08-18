var express = require('express')
var app = express();
var server = require('http').Server(app);
var io = require('socket.io')(server);

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

io.on('connection' , function(socket){
    //接続の開始
    console.log('connection start');

    //stream apiからついっとを取得
    tw.stream('statuses/sample', function(stream) {
	stream.on('data', function (data) {
	    io.sockets.emit('message', {
		'text': data.text ,
		'name': data.user.name ,
		'screen_name': data.user.screen_name,
		'retweet_count': data.retweet_count,
		'favorite_count': data.favorite_count
	    });
	    
	});
    });

    //ついっと内容をconsoleへ出力
    //socket.on('chat message', function(msg){
    //console.log('message: ' + msg);
    //});
    
    //接続の終了
    socket.on('disconnect', function(){
	console.log('connection close');
    });

});
