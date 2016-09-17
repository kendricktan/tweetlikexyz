var DynamicSearch = React.createClass({

  // sets initial state
  getInitialState: function(){
    return { searchString: '' };
  },

  // sets state, triggers render method
  handleChange: function(event){
    // grab value form input box
    this.setState({searchString:event.target.value});
  },

  handleClick: function(value){
    this.setState({searchString:value})
  },

  render: function() {

    var peoples = this.props.items;
    var searchString = this.state.searchString.trim().toLowerCase();

    // filter peoples list by value from input box
    if(searchString.length > 0){
      peoples = peoples.filter(function(people){
        return people.thandle.toLowerCase().match( searchString );
      });
    }

    return (
      <div>
        <input type="text" value={this.state.searchString} onChange={this.handleChange} placeholder="@twitter handle"/>
        <ul>
          { peoples.map(function(people){ return <li><a href="#" onClick={() => this.handleClick(people.thandle) }>{people.thandle}</a></li> }.bind(this)) }
        </ul>
      </div>
    )
  }

});

// list of peoples, defined with JavaScript object literals
var peoples = [
  {"thandle": "@realDonaldTrump"}, {"thandle": "@BarackObama"}
];

ReactDOM.render(
  <DynamicSearch items={ peoples } />,
  document.getElementById('twitter_handler_search')
);