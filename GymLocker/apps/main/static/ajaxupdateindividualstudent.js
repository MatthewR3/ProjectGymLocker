$(document).ready(function() {

	console.log("jQuery Loaded");

});

function update_student(input) {
	student_id = input.split("-")[0];
	attribute = input.split("-")[1];
	table_data = $("#" + student_id + attribute);
	current_value = table_data.html();
	if (input_active == true) {
		if (active_input == student_id + attribute + "update") {
			return;
		};
		$("#" + active_input).replaceWith(input_replacement);
	}
	if (attribute == "note") {
		current_value = current_value.replace("<p>", "").replace("</p>", "");
		table_data.replaceWith('<input class="updatenoteinput" id=' + student_id + "noteupdate" + ' type="text">');
		current_value = current_value.trim();
		$("#" + student_id + "noteupdate").val(current_value);
		input_replacement = '<div class="studentnote" id="' + student_id + 'note"><p>' + current_value + '</p></div>';
	}
	else {
		table_data.html('<input class="updateinput" id=' + student_id + attribute + 'update type="text" value=' + current_value + '>');
		input_replacement = current_value;
	}
	input_active = true;
	active_input = student_id + attribute + "update";

	$("#" + student_id + attribute + "update").keypress(function(key) {
        key_code = key.which;
        if (key_code == 13) {
        	new_value = $("#" + student_id + attribute + "update").val();
		    if (attribute == "firstname") {attribute = "firstname"}
			else if (attribute == "lastname") {attribute = "lastname"}
			else if (attribute == "lockernumber") {attribute = "lockernumber"};
            new_value = update_student_value(student_id, attribute, new_value);
        };
    });
};

function update_student_value(student_id, attribute, value) {
	
	//console.log("");
	//console.log("ID: " + student_id);
    //console.log("Attribute: " + attribute);
    //console.log("Value: " + value);
    //console.log("URL: " + "http://127.0.0.1:8000/ajax/update_student/" + student_id + "/" + attribute + "/" + value);

	$.ajax({
		url: "http://127.0.0.1:8000/ajax/update_student/" + student_id + "/" + attribute + "/" + value,
		//crossDomain: true,
		//xhrFields: {
		//	withCredentials: true
		//},
		success: function(data){
            // Hack that returns true if "ERROR" is in data
            if (~data.indexOf("ERROR")) {
                console.log("ERROR");
                $("#studentblock" + student_id).fadeOut("fast", function() {
                    $("#studentblock" + student_id).html("<h2>ERROR: Please Reload</h2></br><h2>If this error persists,</h2></br><h2>contact Tech Intern</h2>");
                    $("#studentblock" + student_id).fadeIn("fast");
                });
            }
            else {
            	//console.log("DATA: " + data);
            	if (attribute == "note") {
            		$("#" + student_id + "noteupdate").replaceWith('<div class="studentnote" id="' + student_id + 'note"><p>' + data + '</p></div>');
            	}
            	else {
            		$("#" + student_id + attribute).html(data);
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