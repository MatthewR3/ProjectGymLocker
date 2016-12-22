$(document).ready(function() {

    console.log("jQuery Loaded");

    // Cannot use $(".selectbar") because of event delegation; it will not fire in dynamically added student blocks
    $(document.body).on("change", "select", function() {
        console.log((this).id);
        student_id = this.id.split("_")[0];
        console.log(student_id);
        serial = $(this).val();
        console.log(serial);
        $(".lock").each(function(index) {
            if ($(this).val().split("_")[0] == serial) {
                combination = $(this).val().split("_")[1]
            }
        });
        $("#" + student_id + "_combination").text(combination);
    });

});