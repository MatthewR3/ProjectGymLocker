$(document).ready(function() {

    console.log("jQuery Loaded");

    $("#addlocktext").keypress(function(key) {
        key_code = key.which;
        if (key_code == 13) {
            serial = $("#addlocktext").val();
            if ($("#lockblock" + serial).length) {
                $('#addlockerror').fadeOut("fast", function() {
                    $('#addlockerror').html("Lock Already Displayed");
                    $('#addlockerror').fadeIn("fast");
                });
            }
            else {
            get_lock(serial);
            };
        };
    });

    function get_lock(serial) {
		
    	$.ajax({
    		url: "http://127.0.0.1:8000/ajax/get_lock/get/" + serial,
    		//crossDomain: true,
            //xhrFields: {
            //    withCredentials: true
            //},
    		success: function(data){
                // Hack that returns true if "ERROR: LOCK NOT FOUND" is in data
                if (~data.indexOf("ERROR: LOCK NOT FOUND")) {
                    console.log("ERROR: LOCK NOT FOUND");
                    $('#addlockerror').fadeOut("fast", function() {
                        $('#addlockerror').html("Lock Not Found");
                        $('#addlockerror').fadeIn("fast");
                    });
                }
                else {
                    $("#addlockblock").before(data);
                    $("#addlockerror").html("");
                    $("#addlocktext").val("");
                };
    		},
            failure: function(){
                alert("Failure to receive data");
            },
    	});

	};

});

function remove_lock(serial) {
    $("#lockblock" + serial).remove();
};