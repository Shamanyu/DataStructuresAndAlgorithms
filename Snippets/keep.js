/* System Configurator App
    This app displays the existing information of pps(ppsinfo table),
    pps bin types(ppsbin_type table), pps bins(ppsbinrec table) and
    pps bin groups(bingrouprec table) on the server. It allows the user to edit,
    update, delete or create new information.
 */

//Renders a button given its id, name and onClick handler
var Button = React.createClass({
    render: function() {
        return (
            <button className="btn btn-default btn-sm"
              id={this.props.id}
              onClick={this.props.onClickEvent}>
                {this.props.name}
            </button>
        );
    }
});

/*Renders a button group on the UI given its primary identifier(model name),
  secondary identifier(element id), and a dictionary containing individual
  button names and onClick handlers*/
var Buttons = React.createClass({
    render: function() {
        var buttons = [];
        for (var button in this.props.buttons) {
            buttons = buttons.concat(<Button id={this.props.primary
              +this.props.secondary+this.props.buttons[button]["name"]}
              name={this.props.buttons[button]["name"]}
              onClickEvent={this.props.buttons[button]["onClickEvent"]} />)
        }
        return (
            <div className="btn-group col-md-3" role="group"
              id={this.props.primary+this.props.secondary+'ButtonGroup'}>
                {buttons}
            </div>
        );
    }
});

/*Renders one field of an element of a model given its id, name, value,
 disabled status and onChange handler*/
var Field = React.createClass({
    render: function() {
        return (
            <div className="row">
                <div className="col-sm-1">
                    <label className="label label-default"
                      for={this.props.id + this.props.name}>
                          {this.props.name}
                      </label>
                </div>
                <div className="col-sm-11">
                    <input type="text" name={this.props.id + this.props.name}
                      value={this.props.value}
                      disabled={this.props.disabled}
                      onChange={this.props.onChange}
                      /><br />
                </div>
            </div>
        );
    }
});

/*Renders one element of a model given its unique identifier(index), name,
  list of relevant fields and their corresponding expected data types.
  This class receives updated values from the server every 5 seconds but
  chooses to update the display only if the user isn't currently editing
  the existing value. It supports editing existing fields, adding a new element
  on the server, updating an existing element on the server and deleting an
  existing element on the server*/
var Element = React.createClass({
    getInitialState: function() {
        return {
            disabled: true,
            data: this.props.data
        };
    },
    handleChange: function(id, e) {
        var newStateData = this.state.data;
        newStateData[id] = e.target.value;
        this.setState({
            data: newStateData
        });
        this.props.onUpdate(this.props.index, newStateData);
    },
    handleEditEvent: function() {
        if (this.state.disabled === false) {
            var newState = {};
            newState["disabled"] = true;
            newState["data"] = this.props.data;
            this.setState(newState);
            this.props.onUpdate(this.props.index, newState["data"]);
        } else {
            this.setState({
                disabled: false
            });
        }
    },
    handlePutEvent: function() {
        var dataToPut = {};
        var DataToBuild = {};
        for (var field in this.state.data) {
            DataToBuild[field] =
              this.props.typeConverter(this.state.data[field],
              typeof(this.state.data[field]),
              this.props.field_types[field]);
        }
        dataToPut[this.props.model] = DataToBuild;
        $.ajax({
            type: 'PUT',
            url: this.props.url,
            dataType: 'json',
            data: JSON.stringify(dataToPut),
            contentType: 'application/json'
        });
    },
    handleAddEvent: function() {
        var dataToAdd = {};
        var dataToAddKey = this.props.model + this.props.model_suffix;
        dataToAdd[dataToAddKey] = [];
        var DataToBuild = {};
        for (var field in this.state.data) {
            DataToBuild[field] =
              this.props.typeConverter(this.state.data[field],
              typeof(this.state.data[field]),
              this.props.field_types[field]);
        }
        dataToAdd[dataToAddKey].push(DataToBuild);
        $.ajax({
            type: 'POST',
            url: this.props.head_url+'?clear=false',
            dataType: 'json',
            data: JSON.stringify(dataToAdd),
            contentType: 'application/json'
        });
        this.handleRemoveEvent(this.props.index);
    },
    handleDeleteEvent: function() {
        this.handleRemoveEvent();
        $.ajax({
            type: 'DELETE',
            url: this.props.url
        });
    },
    handleRemoveEvent: function() {
        this.props.onRemove(this.props.index);
    },
    render: function() {
        var fields = [];
        var buttons = {};
        for (var field in this.state.data) {
            fields = fields.concat(<Field id={this.props.index} name={field}
              value = {this.state.data[field]}
              disabled={this.state.disabled}
              onChange={this.handleChange.bind(this, field)} />)
        }
        buttons['edit'] = {};
        buttons['edit']['name'] = 'edit';
        buttons['edit']['onClickEvent'] = this.handleEditEvent;
        if (this.props.type == 'existing') {
            buttons['put'] = {};
            buttons['put']['name'] = 'put';
            buttons['put']['onClickEvent'] = this.handlePutEvent;
            buttons['delete'] = {};
            buttons['delete']['name'] = 'delete';
            buttons['delete']['onClickEvent'] = this.handleDeleteEvent;
        } else if (this.props.type == 'created') {
            buttons['add'] = {};
            buttons['add']['name'] = 'add';
            buttons['add']['onClickEvent'] = this.handleAddEvent;
            buttons['remove'] = {};
            buttons['remove']['name'] = 'remove';
            buttons['remove']['onClickEvent'] = this.handleRemoveEvent;
        }
        return (
            <div>
                <a data-toggle="collapse"
                  href={'#Collapse'+this.props.name+this.props.index+'Data'}>
                    <div className="panel panel-default col-md-3"
                      id={this.props.index}
                      style={{"clear":"both"}}>
                        {this.props.index}
                    </div>
                </a>
                <Buttons primary={this.props.name} secondary={this.props.index}
                  buttons={buttons} />
                <div id={'Collapse'+this.props.name+this.props.index+'Data'}
                  className="panel-collapse collapse indent-right"
                  style={{"clear":"both"}}>
                      <form>
                          {fields}
                      </form>
                </div>
            </div>
        );
    }
});

/*This class requests the server for the latest information of its corresponding
  database table every 5 seconds. It then passes this information down to the
  'Element' class which does some processing on it to display the relevant data.
  It also supports posting all the displayed data onto the server at any given
  point of time, and adding a new database table entry on the server*/
var Model = React.createClass({
    getInitialState: function() {
        return {
            modelExistingInfo: {},
            modelCreatedInfo: {},
            modelUpdatedInfo: {},
            nextCreateKey: 1
        };
    },
    convertToRequiredType: function(value, current_type, expected_type) {
        if (current_type == expected_type) {
            return value;
        } else {
            if (current_type == "string" && expected_type == "number") {
                return parseInt(value);
            } else if (current_type == "string" && expected_type == "object") {
                return value.split(",");
            } else if(current_type == "string" && expected_type == "boolean") {
                return value == "true"
            } else {
                return value;
            }
        }
    },
    componentDidMount: function() {
          this.loadModelFromServer();
          setInterval(this.loadModelFromServer, this.props.pollInterval);
    },
    loadModelFromServer: function() {
        $.get(this.props.url, function(data) {
            var newData = {};
            var receivedDataKey = this.props.model + this.props.model_suffix;
            for(var counter1=0; counter1<data[receivedDataKey].length;
              counter1++) {
                var filteredData = {};
                for (var field in this.props.fields) {
                    filteredData[this.props.fields[field]] =
                      data[receivedDataKey][counter1]
                      [this.props.fields[field]];
                }
                newData[filteredData[this.props.index]] =
                  filteredData;
            }
            this.setState({
              modelExistingInfo: newData
            });
        }.bind(this));
    },
    handlePostEvent: function() {
        var dataToPost = {};
        var dataToPostKey = this.props.model + this.props.model_suffix;
        dataToPost[dataToPostKey] = [];
        var DataToBuild = {};
        for(var key in this.state.modelExistingInfo) {
            DataToBuild[key] = {};
            for (var field in this.state.modelExistingInfo[key]) {
                DataToBuild[key][field] =
                  this.convertToRequiredType
                  (this.state.modelExistingInfo[key][field],
                  typeof(this.state.modelExistingInfo[key][field]),
                  this.props.field_types[field])
            }
        }
        for(var key in this.state.modelCreatedInfo) {
            DataToBuild[key] = {};
            for (var field in this.state.modelCreatedInfo[key]) {
                DataToBuild[key][field] =
                  this.convertToRequiredType
                  (this.state.modelCreatedInfo[key][field],
                  typeof(this.state.modelCreatedInfo[key][field]),
                  this.props.field_types[field])
            }
            this.handleRemoveEvent(key);
        }
        for(var key in this.state.modelUpdatedInfo) {
            DataToBuild[key] = {};
            for (var field in this.state.modelUpdatedInfo[key]) {
                DataToBuild[key][field] =
                  this.convertToRequiredType
                  (this.state.modelUpdatedInfo[key][field],
                  typeof(this.state.modelUpdatedInfo[key][field]),
                  this.props.field_types[field])
            }
        }
        for (var key in DataToBuild) {
            dataToPost[dataToPostKey].push(DataToBuild[key]);
        }
        $.ajax({
            type: 'POST',
            url: this.props.url+'?clear=true',
            dataType: 'json',
            data: JSON.stringify(dataToPost),
            contentType: 'application/json'
        });
    },
    handleNewEvent: function() {
        var newKey = 'New'.concat(this.state.nextCreateKey.toString());
        var newModelCreatedInfo = this.state.modelCreatedInfo;
        newModelCreatedInfo[newKey] = {};
        for (var field in this.props.fields) {
            newModelCreatedInfo[newKey][this.props.fields[field]] = null;
        }
        this.setState({
            modelCreatedInfo: newModelCreatedInfo,
            nextCreateKey: this.state.nextCreateKey+1
        });
    },
    handleRemoveEvent: function(key) {
        var newModelExistingInfo = this.state.modelExistingInfo;
        var newModelCreatedInfo = this.state.modelCreatedInfo;
        var newModelUpdatedInfo = this.state.modelUpdatedInfo;
        delete newModelExistingInfo[key];
        delete newModelCreatedInfo[key];
        delete newModelUpdatedInfo[key];
        this.setState({
            modelExistingInfo: newModelExistingInfo,
            modelCreatedInfo: newModelCreatedInfo,
            modelUpdatedInfo: newModelUpdatedInfo
        });
    },
    handleUpdateEvent: function(key, data) {
        var newModelUpdatedInfo = this.state.modelUpdatedInfo;
        newModelUpdatedInfo[key] = data;
        this.setState({
            modelUpdatedInfo: newModelUpdatedInfo
        });
    },
    render: function() {
        var modelExistingInfo = [];
        var modelCreatedInfo = [];
        var buttons = {};
        for (var key in this.state.modelExistingInfo) {
            modelExistingInfo = modelExistingInfo.concat(<Element
              key={key}
              type={"existing"}
              name={this.props.name}
              model={this.props.model}
              model_suffix={this.props.model_suffix}
              index={key}
              data={this.state.modelExistingInfo[key]}
              field_types={this.props.field_types}
              head_url={this.props.url}
              url={this.props.url+'/'+key}
              onRemove={this.handleRemoveEvent}
              onUpdate={this.handleUpdateEvent}
              typeConverter={this.convertToRequiredType} />);
        }
        for (var key in this.state.modelCreatedInfo) {
            modelCreatedInfo = modelCreatedInfo.concat(<Element
              key={key}
              type={"created"}
              name={this.props.name}
              model={this.props.model}
              model_suffix={this.props.model_suffix}
              index={key}
              data={this.state.modelCreatedInfo[key]}
              field_types={this.props.field_types}
              head_url={this.props.url}
              url={this.props.url+'/'+key}
              onRemove={this.handleRemoveEvent}
              onUpdate={this.handleUpdateEvent}
              typeConverter={this.convertToRequiredType} />);
        }
        buttons['post'] = {};
        buttons['post']['name'] = 'post';
        buttons['post']['onClickEvent'] = this.handlePostEvent;
        buttons['new'] = {};
        buttons['new']['name'] = 'new';
        buttons['new']['onClickEvent'] = this.handleNewEvent;
        return (
            <div id={this.props.name+'head'}>
                <a data-toggle="collapse" href={'#Collapse'+this.props.name
                  +'Data'}>
                    <div className="panel panel-default col-md-9"
                      id={this.props.name}
                      style={{"clear":"both"}}>
                        {this.props.name}
                    </div>
                </a>
                <Buttons buttons={buttons}/>
                <div id={'Collapse'+this.props.name+'Data'}
                  className="panel-collapse collapse indent-right"
                  style={{"clear":"both"}}>
                    <span> {modelExistingInfo} </span>
                    <span> {modelCreatedInfo} </span>
                </div>
            </div>
        );
    }
});

/*This class holds information of all the database tables on the server side
  relevant to the app, alongwith their respective relevant fields and
  corresponding field data types*/
var Models = React.createClass({
    render: function() {
        var ppsInfoFields = ['pps_id', 'location', 'status', 'queue_barcodes',
          'pick_position', 'pick_direction', 'pps_url', 'paused'];
        var ppsInfoFieldTypes = {'pps_id': 'number', 'location': 'string',
          'status': 'string', 'queue_barcodes': 'object',
          'pick_position': 'string', 'pick_direction': 'number',
          'pps_url': 'string', 'paused': 'boolean'};
        var ppsBinTypeFields = ['type_id', 'length', 'breadth', 'height',
          'tag'];
        var ppsBinTypeFieldTypes = {'type_id': 'string', 'length': 'number',
          'breadth': 'number', 'height': 'number', 'tag': 'object'};
        var ppsBinRecFields = ['bin_info', 'status', 'position', 'type_id',
          'allowed_tags'];
        var ppsBinRecFieldTypes = {'bin_info': 'string', 'status': 'string',
          'position': 'object', 'type_id': 'string', 'allowed_tags': 'object'};
        var binGroupRecFields = ['bin_group_id', 'bin_list', 'group_enabled'];
        var binGroupRecFieldTypes = {'bin_group_id': 'string',
          'bin_list': 'object', 'group_enabled': 'boolean'};
        return (
            <div className="models">
                <Model url={this.props.baseURL+'/ppsinfo'}
                  name='PpsInfo'
                  model='ppsinfo'
                  model_suffix={this.props.model_suffix}
                  index='pps_id'
                  fields={ppsInfoFields}
                  field_types={ppsInfoFieldTypes}
                  pollInterval={this.props.pollInterval} />
                <Model url={this.props.baseURL+'/ppsbin_type'}
                  name='PpsBinType'
                  model='ppsbin_type'
                  model_suffix={this.props.model_suffix}
                  index='type_id'
                  fields={ppsBinTypeFields}
                  field_types={ppsBinTypeFieldTypes}
                  pollInterval={this.props.pollInterval} />
                <Model url={this.props.baseURL+'/ppsbinrec'}
                  name='PpsBinRec'
                  model='ppsbinrec'
                  model_suffix={this.props.model_suffix}
                  index='bin_info'
                  fields={ppsBinRecFields}
                  field_types={ppsBinRecFieldTypes}
                  pollInterval={this.props.pollInterval} />
                <Model url={this.props.baseURL+'/bingrouprec'}
                  name='BinGroupRec'
                  model='bingrouprec'
                  model_suffix={this.props.model_suffix}
                  index='bin_group_id'
                  fields={binGroupRecFields}
                  field_types={binGroupRecFieldTypes}
                  pollInterval={this.props.pollInterval} />
            </div>
        );
    }
});

//This class renders the entire UI
var SystemConfiguratorBox = React.createClass({
    render: function() {
        return (
            <div className="systemConfigurator">
                <Models baseURL={this.props.baseURL}
                  pollInterval={this.props.pollInterval}
                  model_suffix='_list'/>
            </div>
        );
    }
});

/*Render the UI, alongwith passing down the base server endpoint and refresh
  interval*/
ReactDOM.render(
    <SystemConfiguratorBox baseURL='/api/v2' pollInterval={5000}
      model_suffix='_list'/>,
      document.getElementById('container')
);
