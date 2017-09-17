-spec create_or_update(seat_name(), pps_seat(), metadata()) ->
                               {ok, Key :: key()} | {error, term()}.
create_or_update(SeatName, SeatRecord, Metadata)->
    PpsSeat =
      case SeatRecord#pps_seat.details of
          undefined -> #pps_seat{seat_name = SeatRecord#pps_seat.seat_name,
                      pps_id = SeatRecord#pps_seat.pps_id,
                      seat_type = SeatRecord#pps_seat.seat_type,
                      details = #{tote_id => undefined,put_expectation_id => undefined, group_map => undefined}};
          _ -> SeatRecord
      end,
    Ret = baseinfo:create(?MODULE, SeatName, PpsSeat, Metadata),
    case Ret of
        {ok, _} ->
            send_pps_seat_data_to_interface(PpsSeat, post);
        {error, _Reason} -> ok
    end,
    Ret.

-spec send_pps_seat_data_to_interface(any(), any()) -> any().
send_pps_seat_data_to_interface(SeatRecord, Method) ->
    PpsId = SeatRecord#pps_seat.pps_id,
    SeatName = SeatRecord#pps_seat.seat_name,
    SeatType = atom_to_binary(SeatRecord#pps_seat.seat_type, utf8),
    PpsSeatData = [
                    {<<"pps_id">>, erlang:list_to_binary(
                                                 erlang:integer_to_list(PpsId))},
                    {<<"seat_name">>, atom_to_binary(SeatName, utf8)},
                    {<<"seat_type">>, SeatType}
                  ],
    lager:info("ppsdata for ~p method is ~p", [Method, jsx:encode(PpsSeatData)]),
    pps_client_interface:send_pps_seat_data(PpsId, PpsSeatData).


send_to_client({send_pps_seat_data, Data}, AuthToken) ->
    {ok, BaseUrl} = application:get_env(butler_server, api_baseurl),
    {ok, SeatEndpoint} = application:get_env(butler_server, seat_endpoint),
    EndPoint = BaseUrl ++ SeatEndpoint,
    lager:debug("Sending seat data = ~p", [Data]),
    PpsSeatData = jsx:encode([{<<"pps_seats">>, [Data]}]),
    Request = {EndPoint,
               [{"Authentication-Token", AuthToken}],
               "application/json",
               PpsSeatData
               },
    HTTPOptions = [{timeout, 30000}],
    Options = [],
    butler_client_httpc:httpc_retry(post, Request, HTTPOptions, Options, ?RETRYTIME);