/**
 * Created by anx on 19/02/15.
 */
$( document ).ready(function() {
    showSpinner();
    $('#dtContainer').load('ajax/getStudent',function(){$('#dataTable').dataTable();}).removeClass('hide');
});

function showSpinner(){
    var html = "<div class=\"loader\">Loading...</div>";
    $('#dtContainer').html(html);
}

$('#showStudentTable').click(function () {
    showSpinner();
    $('#dtContainer').load('ajax/getStudent',function(){
        $('#dataTable').dataTable().on( 'init.dt', function () {
        console.log( 'Table initialisation complete: '+new Date().getTime() );
    } );
    }).removeClass('hide');
});

$('#showCompanyTable').click(function () {
    showSpinner();
    $('#dtContainer').load('ajax/getCompany',function(){$('#dataTable').dataTable();}).removeClass('hide');
});

$('#showContactTable').click(function () {
    showSpinner();
    $('#dtContainer').load('ajax/getContact',function(){$('#dataTable').dataTable();}).removeClass('hide');
});

$('#showPlacementTable').click(function () {
    showSpinner();
    $('#dtContainer').load('ajax/getPlacement',function(){$('#dataTable').dataTable();}).removeClass('hide');
});
