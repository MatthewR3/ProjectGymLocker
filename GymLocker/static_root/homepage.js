$(document).ready(function() {

    console.log("jQuery Loaded");

    $("a div").hover(function() {
        $(this).animate({backgroundColor: "#7DABFF"}, 300);
    }, function() {
    	if ($(this).is("#wrapper > div:nth-child(2) div")) {
			$(this).animate({backgroundColor: "#E8F0FF"}, 300);
    	}
        else {
        	$(this).animate({backgroundColor: "FCFCFC"}, 300);
        }
    });

});