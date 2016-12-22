$(document).ready(function() {

    console.log("jQuery Loaded");

    initial_value = $("#searchbar").val();

    IntervalID = setInterval(function() {

            teacher = window.location.href.split("/")[5]

    		current_value = $("#searchbar").val();

	    	if (current_value != initial_value) {
                //alert("NOT EQUAL: FIRING");
	            initial_value = current_value;
	            get_students_by_period(teacher, current_value);
	        }
    }, 100);

    function get_students_by_period(teacher, current_value) {
		
    	$.ajax({
    		url: "http://127.0.0.1:8000/ajax/class_list/" + teacher + "/" + current_value,
    		//crossDomain: true,
            //xhrFields: {
            //    withCredentials: true
            //},
    		success: function(data){
    			$("#results").replaceWith(data);
                make_sortable();
    		},
            failure: function(){
                alert("Failure to receive data");
            },
    	});

	};

});