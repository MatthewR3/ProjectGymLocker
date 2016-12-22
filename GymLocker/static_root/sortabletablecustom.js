$(document).ready(function() {

	console.log("jQuery Loaded");

	make_sortable();

});

function make_sortable() {

	// sortList: [attribute index, 0 (ascending) or 1 (descending)]
	if (window.location.pathname.indexOf("student") >= 0 || window.location.pathname.indexOf("class") >= 0) {
		$("#resultstable").tablesorter({sortList: [[3, 0], [2, 0], [0, 0]]});
	}
	else if (window.location.pathname.indexOf("lock") >= 0) {
		$("#resultstable").tablesorter({sortList: [[0, 0]]});
	}

	console.log("Table Sortable");

	$("#resultstable thead th").css("font-weight", "normal");

	// Reattaches event handler to newly generated table
	$("#resultstable").on("sortEnd", function(event) {
		// Prints the current sort order to the console
		console.log(event.target.config.sortList);
		redraw_arrows(event);
	});
}

function redraw_arrows(event) {

	// Clears existing arrows
	$("#resultstable thead th").each(function() {
		text_only = $(this).html().split("<img")[0];
		$(this).html(text_only);
	});

	// Note: first index starts from 0, while sorter starts from 1
	for (i = 0; i < event.target.config.sortList.length; i++) {

		// Only record colors for first three selections
		if (i > 2) {
			break;
		}

		index = event.target.config.sortList[i][0] + 1;
		order = event.target.config.sortList[i][1] + 1
		//console.log("First Index: " + index);
		//console.log("First Order: " + order);

		old_content = $("#resultstable thead th:nth-child(" + index + ")").html();

		if (i == 0) color = "green";
		else if (i == 1) color = "yellow";
		else color = "red";

		if (order == 1) image = '<img class="image" src="/static/' + color + '_down_arrow.png">';
		else image = '<img class="image" src="/static/' + color + '_up_arrow.png">';

		$("#resultstable thead th:nth-child(" + index + ")").html(old_content + image);
	}
}