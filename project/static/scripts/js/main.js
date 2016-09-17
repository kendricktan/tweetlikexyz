(function e(t,n,r){function s(o,u){if(!n[o]){if(!t[o]){var a=typeof require=="function"&&require;if(!u&&a)return a(o,!0);if(i)return i(o,!0);var f=new Error("Cannot find module '"+o+"'");throw f.code="MODULE_NOT_FOUND",f}var l=n[o]={exports:{}};t[o][0].call(l.exports,function(e){var n=t[o][1][e];return s(n?n:e)},l,l.exports,e,t,n,r)}return n[o].exports}var i=typeof require=="function"&&require;for(var o=0;o<r.length;o++)s(r[o]);return s})({1:[function(require,module,exports){
var DynamicSearch = React.createClass({displayName: "DynamicSearch",

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
      React.createElement("div", null, 
        React.createElement("input", {type: "text", value: this.state.searchString, onChange: this.handleChange, placeholder: "@twitter handle"}), 
        React.createElement("ul", null, 
           peoples.map(function(people){ return React.createElement("li", null, React.createElement("a", {href: "#", onClick: () => this.handleClick(people.thandle)}, people.thandle)) }.bind(this)) 
        )
      )
    )
  }

});

// list of peoples, defined with JavaScript object literals
var peoples = [
  {"thandle": "@realDonaldTrump"}, {"thandle": "@BarackObama"}
];

ReactDOM.render(
  React.createElement(DynamicSearch, {items:  peoples }),
  document.getElementById('twitter_handler_search')
);

},{}]},{},[1]);
