$(document).ready(function() {

    console.log("jQuery Loaded");

    initial_limit = 0;

    initial_attributes = [];
    initial_values = [];

    function check_changes() {

        IntervalID = setInterval(function() {

            change = false;

            limit = $("#limit").val();

            current_attributes = [];
            current_values = [];

            // Checks attributes
            $(".searchattribute").each(function(index) {

                // Checks if a search parameter was added
                if (index > (initial_attributes.length - 1)) {
                    change = true;
                }

                // Checks if attribute was changed
                if ($(this).val() != initial_attributes[index]) {
                    change = true;
                }

                current_attributes.push($(this).val());
            });

            // Checks values
            $(".searchvalue").each(function(index) {

                //Checks if a search parameter was added
                if (index > (initial_values.length - 1)) {
                    change = true;
                }

                //Checks if value was changed
                if ($(this).val() != initial_values[index]) {
                    change = true;
                }

                current_values.push($(this).val());
            });

            //console.log(current_attributes);
            //console.log(current_values);

            if (change) {
                //alert("NOT EQUAL: FIRING");
                //console.log("CHANGES");
                initial_attributes = current_attributes;
                initial_values = current_values;
                search_students(current_attributes, current_values, limit);
            }
        }, 100);
    };

    check_changes();

});

function search_students(search_parameters, search_values, limit) {

    if (limit.toUpperCase() == "ALL") {
        limit = Number.MAX_SAFE_INTEGER;
    }

    //console.log(current_attributes);
    //console.log(current_values);
        
    $.ajax({
        url: "http://127.0.0.1:8000/ajax/search_locks/" + limit + "/",
        data: {search_parameters: search_parameters, search_values: search_values},
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

function force_search() {
    search_parameters = current_attributes;
    search_values = current_values;
    limit = $("#limit").val();
    search_students(search_parameters, search_values, limit);
}