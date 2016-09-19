var React = require('react');
var ReactDOM = require('react-dom');
var MultiSelect = require('react-bootstrap-multiselect');

// Our column things
var TweetPage = React.createClass({
  render: function() {
    return (
      <div className="row">
        <div className="col-md-6 border-right">
          <h3>tweet like:</h3>
          <DynamicSearch /> <br/>
          <h3>phrase to mimic:</h3>
          <DataFeeder /><br/>
          <button type="button" className="btn btn-default">xyz-fy</button>
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
  render: function(){
    return (<p>"one upon a time the quick brown fox jumped over a lazy dog and ate himself up, one upon a time the quick brown fox jumped over a lazy dog and ate himself up"</p>);
  }
})

// Out input text box
var DataFeeder = React.createClass({
  render: function () {
    return (
      <textarea className="form-control" rows="15" id="data_feeder" maxlength="140"/>
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