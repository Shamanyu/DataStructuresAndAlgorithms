-module(concurrency).
-export([dolphin1/0,dolphin2/0,dolphin3/0]).
%-compile(export_all).

dolphin1()->
	receive
		do_a_flip->
			io:format("How about a No?~n");
		fish->
			io:format("So long and how about a fish?~n");
		_->
			io:format("Hey, we are smarter than you humans.~n")
	end.

dolphin2()->
	receive
		{From,do_a_flip}->
			From ! "How about no?!";
		{From,fish}->
			From ! "So long and thanks for all the fish!";
		_->
			io:format("Heh, we are smarter than humans.~n")
	end.

dolphin3()->
	receive
		{From,do_a_flip}->
			From ! "How about no?!",
			dolphin3();
		{From,fish}->
			From ! "So long and thanks for all the fish!";
		_->
			io:format("Heh, we are smarter than humans.~n"),
			dolphin3()
	end.

