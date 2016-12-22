$(document).ready(function() {

	console.log("jQuery Loaded");

});

function update_lock(input) {
	serial = input.split("-")[0];
	attribute = input.split("-")[1];
	table_data = $("#" + serial + attribute);
	current_value = table_data.html();
	if (input_active == true) {
		if (active_input == serial + attribute + "update") {
			return;
		};
		$("#" + active_input).replaceWith(input_replacement);
	}
    console.log("ATTRIBUTE: " + attribute);
    if (attribute == "student_id") {
        console.log($(serial + "student_id"));
        $("#" + serial + "student_id").css("display", "none");
        table_data.replaceWith('<input class="updateinput" id=' + serial + attribute + 'update type="text" value="' + current_value + '">');
    }
    else {
        table_data.html('<input class="updateinput" id=' + serial + attribute + 'update type="text" value="' + current_value + '">');
    }
	input_replacement = current_value;
	input_active = true;
	active_input = serial + attribute + "update";

	$("#" + serial + attribute + "update").keypress(function(key) {
        key_code = key.which;
        if (key_code == 13) {
        	new_value = $("#" + serial + attribute + "update").val();
        	if ((new_value == "" || $.isNumeric(new_value) != true) && attribute == "student_id") {
        		$("#" + serial + attribute).html(current_value);
        		input_active = false;
        	}
        	else {
            	new_value = update_lock_value(serial, attribute, new_value);
            };
        };
    });
};

function update_lock_value(serial, attribute, value) {
	
	//console.log("");
	//console.log("Serial: " + serial);
    //console.log("Attribute: " + attribute);
    //console.log("Value: " + value);
    //console.log("URL: " + "http://127.0.0.1:8000/ajax/update_lock/" + serial + "/" + attribute + "/" + value);

	$.ajax({
		url: "http://127.0.0.1:8000/ajax/update_lock/" + serial + "/" + attribute + "/" + value,
		//crossDomain: true,
        //xhrFields: {
        //    withCredentials: true
        //},
		success: function(data){
            console.log(data);
            // Hack that returns true if "ERROR" is in data
            if (~data.indexOf("ERROR")) {
                console.log("ERROR");
                $("#lockblock" + serial).fadeOut("fast", function() {
                    $("#lockblock" + serial).html("<h2>ERROR: Please Reload</h2></br><h2>If this error persists,</h2></br><h2>contact Tech Intern</h2>");
                    $("#lockblock" + serial).fadeIn("fast");
                });
            }
            else {
                if (attribute == "student_id") {
                    $("#" + serial + attribute + "update").replaceWith('<a id="' + serial + 'student_id" href="/view/individual/students/' + value + '">' + data + '</a>');
                }
                else {
                    $("#" + serial + attribute).html(data);
                }
            	input_active = false;
            };
		},
        failure: function(){
            alert("Failure to receive data");
        },
	});
};

input_active = false
active_input = ""
input_replacement = ""