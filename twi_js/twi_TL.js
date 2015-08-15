//ntwitterの呼び出し
var twitter = require('ntwitter');

//auth認証のためのデータは外部においてます
var auth = require('./auth_sga.js');

var tw = new twitter({
    consumer_key: auth.consumer_key(),
    consumer_secret: auth.consumer_secret(),
    access_token_key: auth.access_token_key(),
    access_token_secret: auth.access_token_secret()
});

tw.stream('statuses/sample', function(stream) {
    stream.on('data', function (data) {
	//標準出力へ出力
	console.log(data);
    });
});



////以下、auth_sga.jsの中身////
// exports.consumer_key = function (){
//     return "aaa";
// }

// exports.consumer_secret = function(){
//     return "bbb";
// }
// exports.access_token_key = function (){
//     return "ccc";
// }

// exports.access_token_secret = function(){
//     return "zzz";
// }
