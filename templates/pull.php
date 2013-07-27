<?php

require_once('pull-test/TwitterAPIExchange.php');

/** Set access tokens here - see: https://dev.twitter.com/apps/ **/
$settings = array(
    'oauth_access_token' => "1326156804-MslnVzYvO8OvH5Fmq1H8Va3h70aYGRU9ZVN6EgD",
    'oauth_access_token_secret' => "N7bC3OwTKne0tc8kUar4MUbzeeGkO54M2Xz2oflu1I",
    'consumer_key' => "AbbrPn8EMnXIEkPUewBg",
    'consumer_secret' => "zY3M6NwuU9Su1n6BuND76fedD6TuUsigjcIZ5bBm4Y"
);


$url = 'https://api.twitter.com/1.1/search/tweets.json';
$getfield = '?q=%23freebandnames&result_type=recent&count=100';
$requestMethod = 'GET';
$twitter = new TwitterAPIExchange($settings);
echo $twitter->setGetfield($getfield)
             ->buildOauth($url, $requestMethod)
             ->performRequest();