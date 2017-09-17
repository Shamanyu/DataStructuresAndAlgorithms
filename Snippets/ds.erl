-module(ds).
%-export([first_robot/0]).
-compile(export_all).

-record(robot,{name,type=industrial,hobbies,details=[]}).
-record(sorter,{name,type=industrial,company,details=[]}).

first_robot()->
	#robot{name="Michael",details=["Moved by gunda"]}.

first_sorter()->
	FlipkartSorter1=#sorter{name="Ramu Bhai",company="Flipkart",details=["kuch nahi","bas aise hi"]},
	FlipkartSorter1#sorter.name.
