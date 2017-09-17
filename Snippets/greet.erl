-module(greet).
-export([greet/2]).

greet(male,Name)->
	io:format("Hello Mr. ~p!~n",[Name]),
	io:format("~s~n",["Hello"]),
	io:format("~s~n",[<<"Hello">>]),
	io:format("~p~n",[<<"Hello">>]),
	io:format("~~~n"),
	io:format("~f~n",[4.1]),
	io:format("~100f~n",[5.0]);
greet(female,Name)->
	io:format("Hello Mrs. ~s!~n",[Name]);
greet(_, Name)->
	io:format("Hello ~s!~n",[Name]).
