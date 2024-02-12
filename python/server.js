//create a node server
var express = require('express');
var app = express();
var path = require('path');
var bodyParser = require('body-parser');
var mongoose = require('mongoose');
var port = process.env.PORT || 8080;
var router = express.Router();
var appRoutes = require('./app/routes/api')(router);
var passport = require('passport');
var social = require('./app/passport/passport')(app, passport);
var port = process.env.PORT || 8080;

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));
app.use(express.static(__dirname + '/public'));
app.use('/api', appRoutes);
app.listen(port, function() {
    console.log('Running the server on port ' + port);
});