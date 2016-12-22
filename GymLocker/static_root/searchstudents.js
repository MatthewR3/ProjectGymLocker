$(document).ready(function() {

    console.log("jQuery Loaded");

    $("#addsearch").hover(function() {
        $(this).animate({backgroundColor: "#7DABFF"}, {duration: 300, queue: false});
        $(this).animate({color: "#333"}, {duration: 300, queue: false});
    }, function() {
        $(this).animate({backgroundColor: "FCFCFC"}, {duration: 300, queue: false});
        $(this).animate({color: "#969696"}, {duration: 300, queue: false});
    });

    $("#addsearch").click(function() {
        $(this).before('<select class="searchbar searchattribute" id="attributesearch"><option value="student_id">ID</option><option value="first_name">First Name</option><option value="last_name">Last Name</option><option value="yis">YIS</option><option value="teacher">Teacher</option><option value="locker_number">Locker Number</option><option value="period">Period</option><option value="gender">Gender</option><option value="tardies">Tardies</option><option value="rentals">Rentals</option></select><h1>is</h1><input class="searchbar searchvalue" id="valuesearch" type="text" placeholder="Value"></br>');
    });

    $("#limitbar div").hover(function() {
        $(this).animate({backgroundColor: "#7DABFF"}, {duration: 300, queue: false});
    }, function() {
        if ($("#limit").val() != $(this).text()) {
            $(this).animate({backgroundColor: "FCFCFC"}, {duration: 300, queue: false});
        }
    });

    $("#limitbar div").click(function() {
        $("#limitbar div").not(this).animate({backgroundColor: "FCFCFC"}, {duration: 300, queue: false});
        $(this).css("background-color", "#7DABFF");
        $("#limit").val($(this).text());
        force_search();
    });

});