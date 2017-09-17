
-module(human_gen_server).
-behaviour(gen_server).

-export([start_link/0, say_hello/2, say_whatsup/1, say_bye/2]).
-export([init/1, handle_call/3, handle_cast/2, handle_info/2,
         terminate/2, code_change/3]).

start_link() ->
	gen_server:start_link(?MODULE, [], []).

say_hello(Pid, Name) ->
	gen_server:call(Pid, {hello, Name}).

say_whatsup(Pid) ->
	gen_server:call(Pid, whatsup).

say_bye(Pid, Name) ->
	gen_server:cast(Pid, {bye, Name}).

init([]) ->
	{ok, Pid} = kitty_gen_server:start_link(),
	io:format("~p~n", [Pid]),
	{ok, Pid}.

handle_call({hello, Name}, _From, Pid)->
	kitty_gen_server:order_cat(Pid, cat1),
	{reply, hello, Name};
handle_call(whatsup, _From, Pid) ->
	kitty_gen_server:return_cat(Pid, test),
    {reply, whatsup, test}.

handle_cast({bye, Name}, _From) ->
	{noreply, bye, Name}.

handle_info(Msg, _) ->
	io:format("Unexpected Message: ~p~n", [Msg]),
	{noreply, []}.

terminate(normal, _) ->
	ok.

code_change(_OldVsn, State, _Extra) ->
	{ok, State}.