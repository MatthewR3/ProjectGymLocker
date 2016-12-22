$(document).ready(function() {

    console.log("jQuery Loaded");

});

function get_confirmation() {
    first_select_bar = document.getElementById("firstselectbar");
    second_select_bar = document.getElementById("secondselectbar");
    first_select_value = first_select_bar.options[first_select_bar.selectedIndex].value;
	second_select_value = second_select_bar.options[second_select_bar.selectedIndex].value;
	first_text_value = document.getElementById("firsttextbar").value
	second_text_value = document.getElementById("secondtextbar").value
	console.log(first_select_value);
	console.log(second_select_value);
	console.log(first_text_value);
	console.log(second_text_value);
	if (first_text_value == "" || second_text_value == "") {
		$('#error').fadeOut("fast", function() {
            $('#error').html("Please Fill In All Fields");
            $('#error').fadeIn("fast");
        });
	}
	else {
		location.href = "/edit/mass/confirm/" + first_select_value + "/" + first_text_value + "/" + second_select_value + "/" + second_text_value;
	};
}