function list_view() {
    document.getElementById("listresults").style.display = "block";
    document.getElementById("tileresults").style.display = "none";
    // Forces border colors
    document.getElementById("listview").style.border = "2px solid #969696";
    document.getElementById("tileview").style.border = "2px solid #7DABFF";
}

function tile_view() {
    document.getElementById("listresults").style.display = "none";
    document.getElementById("tileresults").style.display = "block";
    // Forces border colors
    document.getElementById("listview").style.border = "2px solid #7DABFF";
    document.getElementById("tileview").style.border = "2px solid #969696";
}