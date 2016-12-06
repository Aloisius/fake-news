/*
 * Upload css to stylebot.me
 *
 */

var fs = require('fs');
var system = require('system');

var env = system.env;
var css = fs.read('tweaks.css');

var username = env['STYLEBOT_USERNAME'];
var password = env['STYLEBOT_PASSWORD'];

var casper = require('casper').create({
    pageSettings: {
        userAgent: "GitHub Script Updator 1.0",
        loadImages: false,        // The WebPage instance used by Casper will
        loadPlugins: false         // use these settings
    },
    logLevel: "info",              // Only "info" level messages will be logged
    verbose: true                  // log messages will be printed out to the console
});


casper.start('http://stylebot.me/login');

casper.waitForSelector('form[action="http://stylebot.me/login"]', function() {
  this.echo('login form exists');

  //this.debugHTML();

  this.fillSelectors('form[action="http://stylebot.me/login"]', {
    'input[name="login"]': username,
    'input[name="password"]': password
  }, true);
});

casper.waitForUrl(/stylebot\.me\/$/, function() {
    this.echo('redirected back to main page');
});

casper.thenOpen('http://stylebot.me/style/edit/15677');

casper.waitForSelector('form[action="http://stylebot.me/style/update"]', function() {
  this.echo('edit form exists');

  //this.debugHTML();
  this.fillSelectors('form[action="http://stylebot.me/style/update"]', {
    'textarea[name="css"]': css
  }, true);
});

casper.waitForUrl(/stylebot\.me\/$/, function() {
    this.echo('redirected back to main page');
});

casper.then(function() {
  //this.debugPage();

  this.evaluateOrDie(function() {
    return /was successfully updated/.test(document.body.innerText);
  }, 'submit to stylebot.me failed');
});

casper.run();
