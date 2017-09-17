-define(RIAK_BUCKET(A), list_to_binary(application:get_env(butler_server, riak_prefix, "") ++ binary_to_list(A)) ).

-define(COMPARTMENTS_DBNAME, compartment).
-define(ORDERS_DBNAME, orderrec).
-define(AUDIT_DBNAME, auditrec).
-define(AUDITLINE_DBNAME, auditlinerec).
-define(RACKS_DBNAME, rackinfo).
-define(RACKTYPES_DBNAME, racktype_rec).
-define(RACKBINTYPES_DBNAME, rackbintype_rec).
-define(MAP_DBNAME, gridinfo).
-define(MAPDET_DBNAME, mapdet).
-define(PPSTASKS_DBNAME, ppstaskrec).
-define(AUDITTASKS_DBNAME, audittaskrec).
-define(BUTLERTASKS_DBNAME, movetaskrec).
-define(RESERVATION_DBNAME, reservationinfo).
-define(BUTLERS_DBNAME, butlerinfo).
-define(CHARGETASKS_DBNAME, chargetaskrec).
-define(CHARGERS_DBNAME, chargerinfo).
-define(ITEMAFFINITY_DBNAME, itemaffinity_info).
-define(STORAGEMAP_DBNAME, storage_info).
-define(INVENTORY_BASE_DBNAME, inventory_base).
-define(ORDERS_BASE_DBNAME, orders_base).
-define(PPSBIN_DBNAME, ppsbin).
-define(PPSBINTYPE_DBNAME, ppsbin_type).
-define(PPS_DBNAME, ppsinfo).
-define(FREESPACES_DBNAME, freespacesinfo).
-define(PATHINFO_DBNAME, pathinfo).
-define(PUT_OUTPUT_DBNAME, put_output).
-define(PUT_OUTPUT1_DBNAME, put_output1).
-define(ZIGBEE_DBNAME, zigbeeinfo).
-define(TOTAL_SPACE_DBNAME, total_space).
-define(SLOTINFO_DBNAME, storage_node).
-define(RESOURCEINFO_DBNAME, resourceinfo).
-define(RACKREF_DBNAME, rackref).
-define(ZIGBEEREC_DBNAME, zigbeerec).
-define(ZONEREC_DBNAME, zonerec).

-define(SQL_TABLE_SPEED_LOGS, ?RIAK_BUCKET(<<"speed_logs">>)).
-define(SQL_TABLE_DEBUG_INT, ?RIAK_BUCKET(<<"debug_int">>)).
-define(SQL_TABLE_DEBUG_STR, ?RIAK_BUCKET(<<"debug_str">>)).
-define(SQL_TABLE_ORDER_LOGS, ?RIAK_BUCKET(<<"order_logs">>)).
-define(SQL_TABLE_ITEM_LOGS, ?RIAK_BUCKET(<<"item_logs">>)).
-define(SQL_TABLE_ITEM_DETAILS, ?RIAK_BUCKET(<<"item_details">>)).
-define(SQL_TABLE_SERVER_EVENTS, ?RIAK_BUCKET(<<"server_events">>)).
-define(SQL_TABLE_PPS_EVENTS, ?RIAK_BUCKET(<<"pps_events">>)).
-define(SQL_TABLE_CHARGER_EVENTS, ?RIAK_BUCKET(<<"charger_events">>)).
-define(SQL_TABLE_BUTLER_EVENTS, ?RIAK_BUCKET(<<"butler_events">>)).
-define(SQL_TABLE_CALC_LOGS, ?RIAK_BUCKET(<<"calc_logs">>)).
-define(SQL_TABLE_BUTLER_DETAILS, ?RIAK_BUCKET(<<"butler_details">>)).

-record(subtask,{
          name               :: subtask_name(),
          label                  :: subtask_name(),
          parameters             :: list()
       }).
-record(bmrec,{
          manager_pid            :: pid(),
          butler_id              :: butler_id()
         }).
-record(butlerinfo,{
          id=null                :: butler_id(),
          direction=null         :: direction(),
          position=null          :: barcode(),
          status=null            :: butler_taskstatus(),
          navstatus=undefined    :: butler_navstatus(),
          paused={true, manual}  :: butler_paused_status(),
          taskkey=null           :: null|taskkey(),
          tasktype=null          :: null|tasktype(),
          deltas={0,0,0}         :: deltas(),
          voltage=0              :: number(),
          address=null           :: string() | null,
          display_id             :: display_id()
         }).
-record(gridinfo,{
          coordinate={0,0}       :: coordinate(),
          barcode=null           :: barcode(),
          botid=null             :: butler_id(),
          neighbours=0           :: neighbours(),
          blocked=false          :: boolean() | list(),
          zone                   :: binary(),
          proximity              :: list({coordinate(), number()}),
          absolute_position      :: {number(), number()}
         }).

-record(mapdet,{
          coordinate={0,0}       :: coordinate(),
          sizeinfo=[]            :: list()
         }).

-record(reservationinfo,{
          coordinate={0,0}       :: coordinate(),
          reservationtype=empty  :: reservationtype(),
          reservation_count      :: integer(),
          reserved_by            :: list({butler_id(), reservationtype(), res_timeout()}),
          time_out               :: res_timeout()
         }).
-record(orderrec,{
          order_id                          :: order_id(),
          completion_status                 :: order_status(),
          possible_items                    :: list({list(item_order_info()), number()}),
          possible_uids                     :: list(list({binary(),number(),number()})),
          tags                              :: order_tag(),
          items                             :: undefined | {list(item_order_info()), number()},
          selected_pps                      :: pps_id() | null,
          selected_ppsbin                   :: ppsbin_id() | null,
          order_date                        :: calendar:datetime(),
          options                           :: order_options(),
          doc_ready                         :: boolean()
         }).

-record(orderlinerec , {
          orderline_id                       :: orderline_id(),
          order_id                           :: order_id(),
          quantity                           :: number(),
          options,
          possible_uids                      :: list({item_id() , number() , number()}),
          selected_combination = undefined   :: {item_id() , number() , number()}
  }).

-record(rackrec,{
          rack_id                :: rack_id(),
          rack_face              :: rack_face()
         }).
-record(racktype_rec,{
          racktype_id            :: racktype_id(),
          rack_barcodes          :: rack_barcodes(),
          rack_initial_mass      :: mass(),
          initial_cm_of_rack     :: xyz(),
          density_profile        :: list({floor_id(), {number(), number()}})
          }).

-record(rackbintype_rec,{
          type_id                :: rackbin_type_id(),
          dimension              :: dimension(),
          tag                    :: rackbin_type_tag()
         }).

-record(taskkeyrec,{
          rack                   :: rackrec(),
          pps_id                 :: pps_id()
         }).

-record(ppstaskrec,{
          task_key               :: taskkey(),
          pps_id                 :: pps_id(),
          rack                   :: rackrec(),
          ppsbin_orders          :: list(ppsbinorderrec()),
          status                 :: picktask_status(),
          type                   :: ppstask_type()
         }).

-record(ppsbinorderrec,{
          ppsbin                 :: ppsbin_type_id() | ppsbin_id(),
          task_orders            :: list(taskorderrec()) | list(taskputplan())
         }).

-record(taskorderrec,{
          order_id               :: order_id(),
          % items_list             :: list(item_details())
          items_list             :: list(item_details1())
         }).

-record(movetaskrec,{
          task_key               :: taskkey(),
          butler_id              :: butler_id() | undefined,
          details                :: movetask_details(), 
          task_time              :: integer(),
          status                 :: movetask_status(),
          type                   :: goto_barcode | lift | rackloop | rack_restore
         }).

-record(chargetaskrec, {
          task_key               :: taskkey(),
          butler_id              :: butler_id(),
          charger_id             :: charger_id(),
          charger_entry_point    :: {barcode(), direction()},
          task_time              :: integer(),
          status                 :: chargetaskstatus()
          }).

-record(audittaskrec, {
          task_key               :: taskkey(),
          pps_id                 :: pps_id(),
          rack                   :: rackrec(),
          slot_audits            :: list(slotauditrec()),
          status                 :: picktask_status()
          }).

-record(slotauditrec, {
          slot_rec               :: slotrec(),
          details                :: list({compartment_key(), list(audit_id())})
          }).

-record(rackinfo,{
          id                            :: rack_id(),
          direction                     :: direction(),
          position                      :: barcode(),
          last_store_position           :: barcode(),
          is_stored                     :: boolean(),
          reserved_store_position       :: barcode(),
          lifted_butler_id              :: butler_id() | null,
          racktype                      :: racktype_id() | null,
          centre_of_mass                :: centreofmass(),
          mass_distribution             :: list({{rack_face(), floor_id()}, mass()})
         }).

-record(slotrec, {
          rack_id                :: rack_id(),
          rack_face              :: rack_face(),
          floor_id               :: floor_id(),
          barcode_list           :: list(barcode()),
          height                 :: number(),
          breadth                :: number(),
          barcode_length         :: number()
         }).

-record(freespacesinfo, {
          freespace_key          :: freespace_key(),
          cuboid                 :: cuboid(),
          slot_rec               :: slotrec(),
          barcodes               :: list(barcode()),
          item_list              :: list(item_id())
         }).

% -record(slot_info, {
%             slot_id              :: uid(),
%             properties           :: slot_properties(),
%             type                 :: atom(),
%             storage_node_list    :: list(storage_node()),
%                    }).
-record(itemrec, {
          item_id                :: item_id(),
          amount                 :: integer(),
          pick_reserved          :: integer(),
          put_reserved           :: integer(),
          amount_possible        :: integer()
         }).

-record(compartment,{
          compartment_key        :: compartment_key(),
          entity_type            :: put_types(),
          rack                   :: rackrec(),
          item_id                :: item_id(),
          slot_rec               :: slotrec(),
          box_id=undefined       :: item_id() | undefined,
          item_amount            :: integer(),
          box_amount             :: integer(),
          item_pick_reserved     :: integer(),
          box_pick_reserved      :: integer(),
          item_put_reserved      :: integer(),
          box_put_reserved       :: integer(),
          item_amount_possible   :: integer(),
          box_amount_possible    :: integer(),
          exception_qty          :: integer(), %% TODO : change this too
          audit_marked           :: boolean(),
          x                      :: integer(),
          y                      :: integer(),
          barcodes               :: list(barcode()),
          compartment_type       :: compartment_type(),
          base_height            :: float(),
          height                 :: number(),
          rackbin_id             :: rackbin_id(),
          item_mass              :: mass(),
          positions_possible     :: list(stacking()) | undefined,
          positions_occupied     :: list(stacking()) | undefined,
          stacking               :: stacking() | undefined,
          putting_style          :: {putting_order(), putting_style()}
         }).

-record(ppsmrec,{
          ppsm_pid               :: pid(),
          pps_id                 :: pps_id()
         }).

-record(ppsinfo, {
          pps_id                 :: pps_id(),
          location               :: barcode(),
          status                 :: pps_mode(),
          queue_barcodes         :: list(barcode()),
          pick_position          :: barcode(),
          pick_direction         :: direction(),
          paused                 :: boolean()
         }).

-record(itemstats, {
          item_id                :: item_id(),
          quantity               :: integer(),
          timestamp              :: integer()
         }).

-record(ppsbin, {
          ppsbin_record_id       :: ppsbin_record_id(),
          pps_id                 :: pps_id(),
          ppsbin_id              :: ppsbin_id(),
          reserved_rack_list     :: list({rackrec(), order_id()}),
          type_id                :: ppsbin_type_id()
         }).

-record(ppsbin_type,{
          type_id                :: ppsbin_type_id(),
          dimension              :: dimension(),
          tag                    :: ppsbin_type_tag()
         }).

-record(rack_detail, {
          rack              :: rackrec(),
          item_id           :: item_id(),
          have              :: integer(),
          compartment       :: compartment()
         }).
-record(rack_detail1, {
          rack              :: rackrec(),
          item_uid          :: uid(),
          have              :: integer(),
          slotref           :: slotref()
         }).
-record(taskputplan, {
          put_data          :: put_output(),
          status            :: put_plan_status()
         }).

-record(put_output, {
           put_output_key        :: put_output_key(),
           put_id                :: put_id(),
           scan_entity           :: scan_entity(),
           min_put_quantity      :: integer(),
           status                :: put_status(),
           scan_status           :: scan_status(),
           compartment           :: list(compartment()) | compartment_key() | undefined
          }).

-record(put_output1, {
           put_output_key        :: put_output_key(),
           put_id                :: put_id(),
           pps_info              :: {pps_id(), ppsbin_id()},
           storage_node_list     :: list(storage_node()),
           ref_uid_list          :: list(uid()),
           put_quantity          :: quantity(),  
           status                :: put_status(),
           scan_status           :: scan_status(),
           slotref               :: uid() | undefined
          }).
-record (storage_node, {
           storage_node_id       :: uid(),
           node_type             :: node_types1(),
           properties            :: free_space_properties() | container_properties() | undefined | slot_properties(),
          % can be either parent entity or children entity
           node_entity           :: list(storage_node()) | undefined
          }).
-record (container_properties, {
                                  storage_node_serial  :: uid(),
                                  mass                 :: mass(),
                                  dimension            :: cuboid(),
                                  details              :: json_text() | undefined | any(),
                                  quantity             :: undefined | integer(),
                                  put_status           :: undefined | reserved | put_complete,
                                  pick_properties      :: list(pick_properties()) | undefined,
                                  barcodes             :: list(barcode()) | undefined,
                                  base_height          :: float(),
                                  height               :: number(),
                                  positions_occupied   :: list(stacking()) | undefined,
                                  stacking             :: stacking() | undefined,
                                  scan_required        :: true|false|none
                                }).
-record (slot_properties, {
                            rack_id              :: rack_id(),
                            rack_face            :: rack_face(),
                            floor_id             :: floor_id(),
                            barcode_list         :: list(barcode()),
                            height               :: number(),
                            breadth              :: number(),
                            barcode_length       :: number(),
                            pick_properties      :: list(pick_properties()) | undefined
                          }).
-record (free_space_properties, {
                                  cuboid               :: cuboid(),
                                  barcodes             :: list(barcode()),
                                  item_list            :: list(item_id()),
                                  slot_rec             :: slotrec() | undefined 
                                }).
-record(total_space, {
           total_volume          :: float(),
           volume_available      :: float()
          }).

-record(put_entity, {
           put_id                :: put_id(),
           scan_entity           :: scan_entity(),
           min_put_quantity      :: integer()
          }).

-record(put_entity1, {
           pps_info              :: {pps_id(), ppsbin_id()},
           put_id                :: put_id(),
           entity_list           :: list(storage_node()),
           details               :: any()
          }).
-record(scan_entity, {
           quantity              :: integer(),
           item_entity           :: item_entity(),
           details               :: any()
          }).

-record(item_entity, {
           type                  :: put_types(),
           details               :: item_details_rec() | box_details_rec() | rackbin_details_rec()
          }).

-record(item_details_rec, {
           item_uid              :: uid(),
           dimension             :: cuboid(),
           mass                  :: mass(),
           parent_entity         :: box_details_rec() | rackbin_details_rec() | undefined,
           item_details          :: json_text() | undefined
          }).

-record(box_details_rec, {
           box_uid               :: uid(),
           box_serial            :: uid(),
           dimension             :: cuboid(),
           max_quantity          :: integer(),
           mass                  :: mass(),
           scan_entity           :: list(scan_entity())
          }).

-record(rackbin_details_rec, {
           rackbin_id            :: rackbin_id(),
           dimension             :: cuboid(),
           scan_entity_list      :: list(scan_entity()),
           mass                  :: mass()
          }).

-record(dimension, {
          length            :: number(),
          breadth           :: number(),
          height            :: number()
         }).

-record(inventory_base, {
          item_id           :: item_id(),
          max_quantity      :: integer(),
          batch_quantity    :: integer(),
          dimension         :: dimension(),
          category          :: category(),
          sub_category      :: sub_category()
         }).

-record(orders_base, {
          order_id          :: order_id(),
          items_list        :: list(orders_item_base()),
          status            :: orders_base_status()
         }).

-record(orders_item_base, {
          item_id           :: item_id(),
          quantity          :: integer()
         }).

-record(rackbinrec,{
          id                :: rackbin_id(),
          type_id           :: rackbin_type_id()
         }).

-record(chargerinfo, {
          charger_id        :: charger_id(),
          charger_location  :: {barcode(), direction()},
          entry_point       :: {barcode(), direction()},
          reinit_point      :: {barcode(), direction()},
          status            :: connected | disconnected,
          mode              :: manual | auto | emergency,
          charge=0          :: number()
         }).

-record (itemaffinity_info, {
           items            :: list(item_id()),   %% sorted
           affinity         :: number()
          }).

-record(storage_info, {
          coordinate        :: coordinate(),
          storable          :: storable(),
          status            :: storage_map_status()
         }).

-record(pathinfo,{
          coordinate        :: coordinate(),
          butler_list=[]    :: list({butler_id(), direction()})
         }).

-record(zigbeeinfo,{
          butler_id         :: butler_id(),
          line_5v           :: integer(),
          line_12v          :: integer(),
          line_48v          :: integer(),
          nuc_power         :: integer(),
          nuc_connection    :: integer(),
          nuc_pong          :: integer(),
          bb_power          :: integer(),
          bb_pong           :: integer(),
          bb_pong_rec       :: integer(),
          ods_front         :: integer(),
          ods_back          :: integer()
         }).

%% Data format to send to PPS - As pps interface

-record(pi_rack_compartment,{
          x                    :: integer(),
          y                    :: integer(),
          barcodes             :: list(barcode()),
          stacking             :: stacking(),
          positions_reserved   :: list(stacking()),
          positions_occupied   :: list(stacking()),
          racktype_details     :: racktype_rec()
         }).

-record(centreofmass,{
          centre            ::  xyz(),
          mass              ::  mass()
        }).

-record(auditrec, {
          audit_id          :: audit_id(),
          details           :: {audit_type(), list(item_id()) | barcode()},
          status            :: audit_order_status()
    }).

-record(auditlinerec, {
          auditline_key     :: auditline_key(),
          compartment_key   :: compartment_key(),
          audit_id          :: audit_id(),
          selected_pps      :: pps_id(),
          status            :: auditline_status(),
          item_id           :: item_id(),
          expected_qty      :: integer(),
          actual_qty        :: integer()
    }).

-record(boxserialrec, {
          box_serial        :: uid(),
          item_quantity     :: integer(),
          compartment_list  :: list({compartment_key(), item_id()})
    }).

-record(pi_rack_slot, {
          x                    :: integer(),
          y                    :: integer(),
          barcodes             :: list(barcode()),
          racktype_details     :: racktype_rec()
    }).

-record(inventory, {
        item_uid               :: uid(),
        slotref_list           :: list()
  }).

-record(resourceinfo, {
    resource_name                :: binary(),
    type                         :: atom(),
    path                         :: undefined | list({float(),float()}), %% list(direction, distance) %% direction range [0.00,4.00)
    geometry                     :: {cirle, float()} | {rectangle, float(), float(), float()},  %% {circle, radius} | {rectangle, length, breadth, rotation}
    reference                    :: coordinate(),
    direction                    :: float(), %% direction relative to reference , range [0.00, 4.00)
    distance                     :: float()  %% distance relative to reference
  }).

-record(rackref,{
          rack_id                :: rack_id(),
          info                   :: any()
         }).
         
-record(zigbeerec, {
        zigbee_id                 :: zigbee_id(),
        type                      :: zigbee_type(),
        last_seen                 :: calendar:datetime(),
        last_seen_by = undefined  :: undefined | zigbee_id(),
        dio_states = undefined    :: undefined | list(),
        zone_id = undefined       :: undefined | zone(),
        butler_id = undefined     :: undefined | butler_id()
  }).

-record(zonerec, {
  zone_id                         :: zone(),
  blocked                         :: boolean(),
  paused                          :: boolean(),
  paused_butlers = []             :: list(butler_id())
  }).

-define(SEGMENT_LEN, 9).

-type display_id()               :: binary() | undefined.
-type taskkey()                  :: binary() | undefined.
-type tasktype()                 :: picktask | movetask | chargetask | audittask.
-type taskid()                   :: {tasktype(), taskkey()}.
-type taskrec()                  :: ppstaskrec() | movetaskrec() | chargetaskrec() | audittaskrec().
-type movetaskrec()              :: #movetaskrec{}.
-type ppstaskrec()               :: #ppstaskrec{}.
-type audittaskrec()             :: #audittaskrec{}.
-type rackref()                  :: #rackref{}.
-type ppstask_type()             :: pick | put.

-type taskstatus()               :: picktask_status() | chargetaskstatus().
-type tasksubstatus()            :: created | assigned | started | rack_picked | pps_complete.
-type taskstatusindices()        :: pending | tasksubstatus() | cancelled | complete.

-type picktask_status()          :: {pending, tasksubstatus()} |% pending |
                                    cancelled | complete.
-type movetask_status()          :: {pending, tasksubstatus()} |% pending |
                                    created | cancelled | complete.
-type movetask_details()         :: {{barcode(), direction()}, direction()} |
                                    liftdirection() |
                                    undefined |
                                    {true | false,
                                     {
                                       {rack_id(), rack_face()} | undefined ,
                                       pps_id() | undefined, 
                                       undefined | {barcode(), direction()}}} |
                                    rack_id().

-type chargetaskstatus()         :: pending | {pending, assigned | started} |
                                    reached_entry_point | complete.

-type taskkeyrec()               :: #taskkeyrec{}.
-type taskorderrec()             :: #taskorderrec{}.
-type ppsbinorderrec()           :: #ppsbinorderrec{}.
-type rackrec()                  :: #rackrec{}.
-type butlerinfo()               :: #butlerinfo{}.
-type zigbeeinfo()               :: #zigbeeinfo{}.
-type gridinfo()                 :: #gridinfo{}.
-type mapdet()                   :: #mapdet{}.
-type reservationinfo()          :: #reservationinfo{}.
-type orderrec()                 :: #orderrec{}.
-type orderlinerec()             :: #orderlinerec{}.
-type rackinfo()                 :: #rackinfo{}.
-type itemrec()                  :: #itemrec{}.
-type compartment()              :: #compartment{}.
-type ppsinfo()                  :: #ppsinfo{}.
-type itemstats()                :: #itemstats{}.
-type ppsbin()                   :: #ppsbin{}.
-type ppsbin_type()              :: #ppsbin_type{}.
-type rack_detail()              :: #rack_detail{}.
-type rack_detail1()             :: #rack_detail1{}.
-type taskputplan()              :: #taskputplan{}.
-type dimension()                :: #dimension{}.
-type inventory_base()           :: #inventory_base{}.
-type orders_base()              :: #orders_base{}.
-type orders_item_base()         :: #orders_item_base{}.
-type rackbinrec()               :: #rackbinrec{}.
-type chargetaskrec()            :: #chargetaskrec{}.
-type storage_info()             :: #storage_info{}.
-type pi_rack_compartment()      :: #pi_rack_compartment{}.
-type pi_rack_slot()             :: #pi_rack_slot{}.
-type slotrec()                  :: #slotrec{}.
-type boxserialrec()             :: #boxserialrec{}.
-type pathinfo()                 :: #pathinfo{}.
-type subtask()                  :: #subtask{}.
-type auditrec()                 :: #auditrec{}.
-type auditlinerec()             :: #auditlinerec{}.
-type slotauditrec()             :: #slotauditrec{}.
-type racktype_id()              :: string().
-type rack_barcodes()            :: list({FloorId :: string(),
                                          list({list(Barcode :: string()),number(),number()})}).
-type racktype_rec()             :: #racktype_rec{}.

-type rackbintype_rec()          :: #rackbintype_rec{}.
-type compartment_type()         :: string().
-type compartment_key()          :: binary().
-type butler_id()                :: integer() | null.
-type coordinate()               :: {integer(), integer()}.
-type deltas()                   :: {integer(), integer(), integer()}.
-type order_id()                 :: binary().
-type audit_id()                 :: binary().
-type audit_type()               :: location | uid.
-type audit_value()              :: binary().
-type orderline_id()             :: binary().
-type order_tag()                :: list(binary()).
-type order_options()            :: list({binary(), term()}).
-type order_status()             :: pending | created | running | complete.
-type audit_order_status()       :: audit_pending | audit_started | audit_calculated | audit_completed.
-type auditline_status()         :: audit_pending | audit_tasked | audit_completed.
-type auditline_key()            :: binary().
-type direction()                :: 0 | 1 | 2 | 3 | null | undefined.
-type movecmd()                  :: {direction(), Steps :: integer()}.
-type pps_id()                   :: integer().
-type pps_mode()                 :: disconnected | pick_mode | put_mode | audit_mode.
-type barcode()                  :: string() | null | undefined.
-type butlerstatus()             :: empty | moving | idle.
-type reservationtype()          :: empty | moving | idle | turn | safety.
-type res_timeout()              :: inf | integer().
-type rack_id()                  :: undefined | binary().
-type item_id()                  :: undefined | binary().
-type liftstate()                :: up | down.
-type liftdirection()            :: 0 | 1.     %% 0 is up, 1 is down.
-type transportinfo()            :: list(integer()).
-type neighbours()               :: list(transportinfo()).
%% one for each direction
-type coordinate_distances()     :: list(integer()).
%% [ ItemId | Required | Have ]
-type item_order_info()          :: [ item_id()| integer() ].
-type item_details()             ::
        {
          ItemId                 :: item_id(),
          Required               :: integer(),
          Have                   :: integer(),
          CompartmentKey         :: compartment_key(),
          X                      :: integer(),
          Y                      :: integer(),
          Barcodes               :: list(barcode())
        }.
-type item_details1()             ::
        {
          ItemId                 :: item_id(),
          Required               :: integer(),
          Slotref                :: slotref()
        }. 

-type storage_details()          ::
        {
          compartment_type(),
          Capacity               :: integer()
        }.
-type pptl_id()                  :: integer().
-type rack_face()                :: 0 | 1 | undefined.
-type pptl_status()              :: idle | open | complete.
-type butler_taskstatus()        :: initializing | dead | ready | processing| null| assigned.
-type butler_navstatus()         :: undefined | init | info | error | warning.
-type butler_paused_status()     :: false | {true, manual | low_charge}.
-type ppsbin_id()                :: string().
-type ppsbin_status()            :: idle | open | complete.
-type ppsbin_position()          :: coordinate().
-type ppsbin_record_id()         :: {pps_id(), ppsbin_id()}.
-type ppsbin_type_tag()          :: list(binary()).
-type ppsbin_type_id()           :: binary() | undefined.

-type seat_name()                :: atom().
-type put_id()                   :: binary() | undefined.
-type pps_preference()           :: {status, pps_mode()} | {selected_pps, pps_id()}.

-type put_plan_status()          :: tentative | scanned | undefined.
-type mass()                     :: number().
-type xyz()                      :: {float(), float(), float()}.
-type centreofmass()             :: #centreofmass{}.
-type category()                 :: binary().
-type sub_category()             :: binary().
-type orders_base_status()       :: created | forwarded.
-type rackbin_id()               :: binary() | undefined.
-type rackbin_type_id()          :: binary() | undefined.
-type rackbin_type_tag()         :: standard.

%% 0 means not storable, 1 means store position (storable)
-type storable()             :: 0 | 1 .

-type json_text()                :: binary().

%% For database stuff

-type value()                    :: term().
-type charger_id()               :: number() | null.
-type charger_mode()             :: auto | manual | emergency.
-type chargerinfo()              :: #chargerinfo{}.
-type key()                      :: term().
-type bucket()                   :: atom().
-type metadata()                 :: list().
-type output()                   :: term().
-type db_operator()              :: atom().
-type db_whereclauselist()       :: list({atom(),db_operator(),term()}).
-type db_columnlist()            :: list(atom()).
-type db_columnname()            :: atom(). 
-type subtask_name()             :: start_random | stop_random | start_rackloop | stop_rackloop | append_subtasks |
                                    goto_barcode | check_rack_tasks | check_audit_rack_tasks | goto_store | lift |
                                    turn_out_direction | pps_control | delay | abandon_task | set_task_complete |
                                    assign_same_rack_task | assign_same_rack_audit_task | abandon_subtask | self.

-type storage_map_status()       :: undefined | available | {rack_id(), reserved} | {rack_id(), stored}.
-type floor_id()                 :: string().
-type cuboid()                   :: {number(), number(), number() | not_required}.
-type rack()                     :: {rack_id(), rack_face()}.
-type freespacesinfo()           :: #freespacesinfo{}.
-type put_entity()               :: #put_entity{}.
-type put_entity1()              :: #put_entity1{}.
-type put_output()               :: #put_output{}.
-type put_output1()              :: #put_output1{}.
-type scan_entity()              :: #scan_entity{}.
-type storage_node()             :: #storage_node{}.
-type item_entity()              :: #item_entity{}.
-type item_details_rec()         :: #item_details_rec{}.
-type box_details_rec()          :: #box_details_rec{}.
-type rackbin_details_rec()      :: #rackbin_details_rec{}.
-type uid()                      :: undefined | binary().
-type put_types()                :: item | box | rackbin.
-type node_types1()              :: item | container | free_space | slot |compartment | rackbin.
-type calculation_status()       :: {fulfillable | partially_fulfillable | unfulfillable, integer()}.
-type put_status()               :: calculation_pending | calculating | calculated | completed.
-type scan_status()              :: scan_pending | {scanned | completed, {pps_id(), ppsbin_id(), atom()}}.
-type scan_sub_status()          :: scan_pending | scanned | completed.
-type put_output_key()           :: binary().
-type volume_key()               :: binary().
-type freespace_key()            :: freespace_key().
-type putting_style_types()      :: back_to_front | front_to_back | left_to_right | right_to_left |
                                    top_to_bottom | bottom_to_top.
-type putting_order_types()      :: depth | width | height.
-type putting_order()            :: {putting_order_types(), putting_order_types(), putting_order_types()}.
-type putting_style()            :: {putting_style_types(), putting_style_types(), putting_style_types()}.
-type stacking()                 :: {number(), number(), number()}.
-type pick_properties()          :: {item_id() , {integer() , integer()} , integer()}.
-type total_space()              :: #total_space{}.
-type container_properties()     :: #container_properties{}.
-type slot_properties()          :: #slot_properties{}.
-type free_space_properties()    :: #free_space_properties{}.
-type slotref()                  ::string().
-type quantity()                 :: number().                     
-type inventory()               :: #inventory{}.
-type zone()                     :: binary().
-type resourceinfo()             :: #resourceinfo{}.
-type mac_address()              :: string().
-type zigbee_id()                :: mac_address().
-type zigbee_type()              :: emerbee | zonalbee | butlerbee | serverbee.
-type zigbeerec()                :: #zigbeerec{}.
-type zonerec()                  :: #zonerec{}.
