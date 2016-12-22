$(document).ready(function() {

    console.log("jQuery Loaded");

});

function add_tardy(student_id) {

    console.log(student_id);
        
    $.ajax({
        url: "http://127.0.0.1:8000/ajax/add_tardy/" + student_id,
        //crossDomain: true,
        //xhrFields: {
        //    withCredentials: true
        //},
        success: function(data){
            $(".tardies" + student_id).text(data);
        },
        failure: function(){
            alert("Failure to receive data");
        },
    });

};

function add_rental(student_id) {

    console.log("Firing")
        
    $.ajax({
        url: "http://127.0.0.1:8000/ajax/add_rental/" + student_id,
        //crossDomain: true,
        //xhrFields: {
        //    withCredentials: true
        //},
        success: function(data){
            $(".rentals" + student_id).text(data);
        },
        failure: function(){
            alert("Failure to receive data");
        },
    });

};