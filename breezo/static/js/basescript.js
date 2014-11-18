//    $(window).load(function(){
//        confirm("is it login window");
//        $('#myModal-login').modal('show');
//    });
//
//    $(window).load(function(){
//        $('#myModal-register').modal('show');
//    });
    $(document).ready(function(){
        $("#bucket").click(function() {
            $('div#dialog-form').hide();
        });
    });

//$(function() {
//  $( "#accordion" ).accordion({
//    event: "click hoverintent"
//});
//});
///*
//* hoverIntent | Copyright 2011 Brian Cherne
//* http://cherne.net/brian/resources/jquery.hoverIntent.html
//* modified by the jQuery UI team
//*/
//$.event.special.hoverintent = {
//  setup: function() {
//    $( this ).bind( "mouseover", jQuery.event.special.hoverintent.handler );
//},
//  teardown: function() {
//    $( this ).unbind( "mouseover", jQuery.event.special.hoverintent.handler );
//},
//  handler: function( event ) {
//    var currentX, currentY, timeout,
//    args = arguments,
//    target = $( event.target ),
//    previousX = event.pageX,
//    previousY = event.pageY;
//    function track( event ) {
//    currentX = event.pageX;
//    currentY = event.pageY;
//};
//  function clear() {
//    target
//      .unbind( "mousemove", track )
//      .unbind( "mouseout", clear );
//       clearTimeout( timeout );
//}
//
//function handler() {
//  var prop,
//  orig = event;
//  if ( ( Math.abs( previousX - currentX ) +
//    Math.abs( previousY - currentY ) ) < 7 ) {
//  clear();
//  event = $.Event( "hoverintent" );
//  for ( prop in orig ) {
//  if ( !( prop in event ) ) {
//  event[ prop ] = orig[ prop ];
//}
//}
//// Prevent accessing the original event since the new event
//// is fired asynchronously and the old event is no longer
//// usable (#6028)
//  delete event.originalEvent;
//  target.trigger( event );
//} else {
//  previousX = currentX;
//  previousY = currentY;
//  timeout = setTimeout( handler, 100 );
//}
//}
//  timeout = setTimeout( handler, 100 );
//  target.bind({
//  mousemove: track,
//  mouseout: clear
//});
//}
//};
//
//
////Login script
//
//$(function() {
//var dialog, form,
//// From http://www.whatwg.org/specs/web-apps/current-work/multipage/states-of-the-type-attribute.html#e-mail-state-%28type=email%29
//emailRegex = /^[a-zA-Z0-9.!#$%&'*+\/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$/,
//name = $( "#name" ),
//password = $( "#password" ),
//allFields = $( [] ).add( name ).add( password ),
//tips = $( ".validateTips" );
//function updateTips( t ) {
//tips
//.text( t )
//.addClass( "ui-state-highlight" );
//setTimeout(function() {
//tips.removeClass( "ui-state-highlight", 1500 );
//}, 500 );
//}
//function checkLength( o, n, min, max ) {
//if ( o.val().length > max || o.val().length < min ) {
//o.addClass( "ui-state-error" );
//updateTips( "Length of " + n + " must be between " +
//min + " and " + max + "." );
//return false;
//} else {
//return true;
//}
//}
//
//dialog = $( "#dialog-form" ).dialog({
//autoOpen: false,
//height: 300,
//width: 350,
//modal: true,
//buttons: {
//"Create an account": addUser,
//Cancel: function() {
//dialog.dialog( "close" );
//}
//},
//close: function() {
//form[ 0 ].reset();
//allFields.removeClass( "ui-state-error" );
//}
//});
//form = dialog.find( "form" ).on( "submit", function( event ) {
//event.preventDefault();
//addUser();
//});
//$( "#create-user" ).button().on( "click", function() {
//dialog.dialog( "open" );
//});
//});
//
