window.$ = window.jQuery = require('./js/jquery-1.11.3.js');
require('./js/bootstrap.min.js');

const remote = require('electron').remote;
const app = remote.app;
const BrowserWindow = remote.BrowserWindow;
const shell = require('electron').shell;

// var apikey = "zm9pzc89zw35c5asda890j3ad2";

$('form#main').on('submit', function(event) {

    event.preventDefault();
    $('#request-status').removeClass().addClass('alert').addClass('alert-info');
    $('#request-status').html('<img src="res/loading.gif"> &nbsp; Please wait...').show();
    var host     = $('#host').val();
    var username = $('#username').val();
    var password = $('#password').val();

    try {
        if(host.match(/^[0-9a-zA-Z-.]{1,40}$/)){
            var child_process = require('child_process');
            $('#request-status').removeClass('alert-info').addClass('alert-success');
            document.getElementById("request-status").innerHTML = '<h3>Lookup results for <b>'+host+'</b></h3><br>';

            var wmic = ['computersystem', 'processor', 'displayconfiguration', 'operatingsystem', 'nic', 'bios'];
            var i = 0;
            wmic.forEach(function(entry) {
                var result = child_process.execSync('cmd.exe /c "python ./resources/app/sys_win32_'+entry+'.py '+host+' '+username+' '+password+'"', {stdio:'pipe'}).toString();
                document.getElementById("request-status").innerHTML += `<pre>`+result+`</pre>`;
                i++;
            })

            // wmic.forEach(function(entry) {
            //     var result = child_process.execSync('cmd.exe /c "python ./resources/app/sys_win32_'+entry+'.py '+host+' '+username+' '+password+'"', {stdio:'pipe'}).toString();
            //     document.getElementById("request-status").innerHTML += `
            //      <div class="panel-group">
            //         <div class="panel panel-default">
            //             <a data-toggle="collapse" href="#collapse`+i+`">
            //                 <div class="panel-heading">
            //                     <h4 class="panel-title">`+entry+`</h4>
            //                 </div>
            //             </a>
            //             <div id="collapse`+i+`" class="panel-collapse collapse.in">
            //                 <div class="panel-body"><pre>`+result+`</pre></div>
            //             </div>
            //         </div>
            //     </div><br>`;
            //     i++;
            // })
        }
        else {
            throw new Error('Invalid host machine. Only use alphanumeric characters, "." and "-".');
        }
    }
    catch(e) {
        $('#request-status').removeClass('alert-info').addClass('alert-danger');
        document.getElementById("request-status").innerHTML = '<h3>Lookup results</h3><br>';
        var error_offline = e.message.indexOf("The RPC server is unavailable");
        var error_accessdenied = e.message.indexOf("Access is denied");
        if (error_offline > 0 && error_accessdenied == -1) {
            document.getElementById("request-status").innerHTML += 'Host machine is currently offline.';
        }
        else if (error_accessdenied > 0 && error_offline == -1) {
            document.getElementById("request-status").innerHTML += 'Access denied.';
        }
        else {
            document.getElementById("request-status").innerHTML += e.message;
        }
    }
    const dialog = remote.dialog;
});


$('#btn-about').on('click', function(event) {
    var AboutWindow = new BrowserWindow({ width:500, height:640, frame:false });
    AboutWindow.loadURL('file://' + __dirname + '/about.html');
});
$('#btn-changelog').on('click', function(event) {
    shell.openExternal('https://github.com/kek91');
});


/*
$.ajax({
    type: "GET",
    dataType: "json",
    url: "http://web2/computerinfo/api/pc/"+host+"/"+apikey,
    success: function(data){
        if(data.error) {
            $('#request-status').removeClass('alert-info').addClass('alert-danger');
        }
        else {
            $('#request-status').removeClass('alert-info').addClass('alert-success');
        }
        $('#request-status').html(data.result);
    },
    error: function(xhr, status) {
        $('#request-status').removeClass('alert-info').addClass('alert-danger');
        $('#request-status').html('Error: ' + status);
        $('#request-status').append('<br><br><b>Details:</b><br><pre>' + JSON.stringify(xhr, undefined, 4) + '</pre>');
    }
});
*/

// const dialog = electron.dialog;
// dialog.showMessageBox(BrowserWindow, {type:'info', buttons:['Sounds good', 'Wait a minute...'], defaultId:1, title:'Tittel', message:'message box!', detail:output.toString()});
