-module(client1).
-behaviour(gen_server).

-export([init/1, handle_call/3, handle_cast/2, handle_info/2,terminate/2, code_change/3]).

%%% Server functions
init([]) ->
	 {ok, []}. %% no treatment of info here!




