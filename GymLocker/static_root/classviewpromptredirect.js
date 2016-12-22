$(document).ready(function() {

    console.log("jQuery Loaded");

});

function get_class() {
    select_bar = document.getElementById("selectbar");
    value = select_bar.options[select_bar.selectedIndex].value;
    location.href = "/view/class/" + value
}