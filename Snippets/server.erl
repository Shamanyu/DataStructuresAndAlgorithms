-module(server).

%%% Client API
start() ->
    gen_server:start_link(client1,[say_hey,say_bye], []).
    gen_server:start_link(client2,[say_heyy,say_byee],[]).

%%% Server functions
%init([]) ->
%	gen_server:start_link(client1,[say_hello],[]).
%	gen_server:start_link(client2,[say_bye],[]). 
%	{ok, []}. %% no treatment of info here!

