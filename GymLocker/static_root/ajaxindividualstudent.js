$(document).ready(function() {

    console.log("jQuery Loaded");

    $("#addstudenttext").keypress(function(key) {
        key_code = key.which;
        if (key_code == 13) {
            student_id = $("#addstudenttext").val();
            if ($("#studentblock" + student_id).length) {
                $('#addstudenterror').fadeOut("fast", function() {
                    $('#addstudenterror').html("Student Already Displayed");
                    $('#addstudenterror').fadeIn("fast");
                });
            }
            else {
            get_student(student_id);
            };
        };
    });

    function get_student(student_id) {
		
    	$.ajax({
    		url: "http://127.0.0.1:8000/ajax/get_student/get/" + student_id,
    		//crossDomain: true,
            //xhrFields: {
            //    withCredentials: true
            //},
    		success: function(data){
                // Hack that returns true if "ERROR: STUDENT NOT FOUND" is in data
                if (~data.indexOf("ERROR: STUDENT NOT FOUND")) {
                    console.log("ERROR: STUDENT NOT FOUND");
                    $('#addstudenterror').fadeOut("fast", function() {
                        $('#addstudenterror').html("Student Not Found");
                        $('#addstudenterror').fadeIn("fast");
                    });
                }
                else {
                    $("#addstudentblock").before(data);
                    $("#addstudenterror").html("");
                    $("#addstudenttext").val("");
                };
    		},
            failure: function(){
                alert("Failure to receive data");
            },
    	});

	};

});

function remove_student(student_id) {
    console.log("Firing Remove");
    console.log(student_id);
    $("#studentblock" + student_id).remove();
};