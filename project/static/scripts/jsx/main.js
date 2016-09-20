var React = require('react');
var ReactDOM = require('react-dom');
var MultiSelect = require('react-bootstrap-multiselect');
var request = require('request');

// Our column things
var TweetPage = React.createClass({
  getQuote: function(){
    console.log('yay');
  },

  render: function() {
    return (
      <div className="row">
        <div className="col-md-6 border-right">
          <h3>tweet like:</h3>
          <DynamicSearch ref="dynamicsearch" /> <br/>
          <h3>phrase to mimic:</h3>
          <DataFeeder red="datafeeder" /><br/>
          <button type="button" onClick={(event) => this.getQuote()} className="btn btn-default">xyz-fy</button>
        </div>

        <div className="col-md-6">
          <span className="fancyMcFancy"><GetNewExpression /></span>
        </div>
      </div>
    );
  }
})

// Get phrase
var GetNewExpression = React.createClass({
  getInitialState: function(){
    return {quote: ""};
  },

  componentDidMount: function() {
    request({url: 'http://127.0.0.1:5000/random'}, function(error, response, body){
      result = JSON.parse(body);
      this.setState({
        'quote': result['text']
      });
    }.bind(this));
  },

  componentWillUnmount: function() {
    this.serverRequest.abort();
  },

  render: function(){
    return (<p>"{this.state.quote}"</p>)
  }
})

// Out input text box
var DataFeeder = React.createClass({
  render: function () {
    return (
      <textarea className="form-control" rows="15" id="data_feeder" maxLength="140"/>
    );
  }
})

var DynamicSearch = React.createClass({
    render: function(){
        var self = this, 
            options = ["shakespeare" ,"@BarackObama", "@realDonaldTrump"].map(function(name){
                return {label: name, value: name}
            });
        return <MultiSelect 
            data = {options} 
            placeholder = "Select names"
        />
    }
});

ReactDOM.render(
  <TweetPage />,
  document.getElementById("content")
);