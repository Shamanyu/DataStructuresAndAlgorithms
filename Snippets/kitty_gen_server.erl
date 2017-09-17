
-module(kitty_gen_server).
-behaviour(gen_server).

-export([start_link/0, order_cat/2, return_cat/2, close_shop/1]).
-export([init/1, handle_call/3, handle_cast/2, handle_info/2,
         terminate/2, code_change/3]).

start_link() ->
	gen_server:start_link(?MODULE, [], []).

order_cat(Pid, Name) ->
	io:format("asdasd"),
	gen_server:call(Pid, {order, Name}).

return_cat(Pid, Cat) ->
	io:format("inside kitty gen server return cat~n"),
	gen_server:cast(Pid, {return, Cat}).

close_shop(Pid) ->
	gen_server:call(Pid, terminate).

init([]) ->
	{ok, []}.

handle_call({order, Name}, _From, Cats)->
	if 
		Cats =:= [] ->
			{reply, make_cat(Name), Cats};
		Cats =/= [] ->
			{reply, hd(Cats), tl(Cats)}
	end;

handle_call(terminate, _From, Cats) ->
    {stop, normal, ok, Cats}.

handle_cast({return, Cat}, Cats) ->
	io:format("inside handle_cast for return cat for cat ~p and cats ~p~n", [Cat, Cats]),
	{noreply, [Cat|Cats]}.

handle_info(Msg, Cats) ->
	io:format("Unexpected Message: ~p~n", [Msg]),
	{noreply, Cats}.

terminate(normal, Cats) ->
	[io:format("~p was set free.~n", [C]) || C <- Cats],
	ok.

code_change(_OldVsn, State, _Extra) ->
	{ok, State}.

make_cat(Name) ->
	Name.