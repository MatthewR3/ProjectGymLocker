$(document).ready(function() {

    console.log("jQuery Loaded");

});

function get_confirmation() {
    select_bar = document.getElementById("selectbar");
    select_value = select_bar.options[select_bar.selectedIndex].value;
	text_value = document.getElementById("textbar").value
	console.log(select_value);
	console.log(text_value);
	location.href = "/delete/mass/confirm/" + select_value + "/" + text_value + "/";
}