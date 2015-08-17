var twitter = require('ntwitter');
var auth = require('../auth_sga.js');

var now = new Date();

//oauth認証
var tw = new twitter({
    consumer_key: auth.consumer_key(),
    consumer_secret: auth.consumer_secret(),
    access_token_key: auth.access_token_key(),
    access_token_secret: auth.access_token_secret()
});

//時間のついっと
function time_post(){
    
    var post_word = now.getHours() + "時" + now.getMinutes() + "分" + now.getSeconds() + "秒";
    
    //ついっと
    tw.updateStatus(post_word, function(er, data){console.log("tweet success: " + data.text);});
}
