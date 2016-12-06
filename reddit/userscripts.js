/*
 * Upload css to userscripts.org
 *
 */

var fs = require('fs');
var system = require('system');

var env = system.env;
var css = fs.read('stylish.css');

var username = env['USERSCRIPTS_USERNAME'];
var password = env['USERSCRIPTS_PASSWORD'];

var casper = require('casper').create({
    pageSettings: {
        userAgent: "GitHub Script Updator 1.0",
        loadImages: false,        // The WebPage instance used by Casper will
        loadPlugins: false         // use these settings
    },
    logLevel: "info",              // Only "info" level messages will be logged
    verbose: true                  // log messages will be printed out to the console
});


casper.start('https://userstyles.org/login?view=password');

casper.waitForSelector('form#password-login', function() {
  this.echo('login form exists');

  //this.debugHTML();

  this.fillSelectors('form#password-login', {
    'input[name="login"]': username,
    'input[name="password"]': password
  }, true);
});

casper.waitForUrl(/\/users\/378459$/, function() {
    this.echo('redirected to user page');
});


casper.thenOpen('https://userstyles.org/styles/136035/edit');

casper.waitForSelector('form[action="/styles/update"]', function() {
  this.echo('edit form exists');

  //this.debugHTML();
  this.fillSelectors('form[action="/styles/update"]', {
      'textarea[name="style[style_code_attributes][code]"]': css
    }, true);
});

casper.waitForUrl(/\/styles\/136035\/reddit-fake-news-tagger$/, function() {
    this.echo('redirected to tagger page');
});

casper.run();
