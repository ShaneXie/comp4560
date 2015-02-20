/**
 * Created by anx on 19/02/15.
 */

$('#showStudentTable').click(function () {
    $('#dtContainer').load('ajax/getStudent',function(){$('#dataTable').dataTable();}).removeClass('hide');
});