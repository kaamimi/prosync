window.onload = () => {
    var stats=eel.retrieve_data();
    console.log(stats);
    document.getElementById("stats").innerText = stats;
    processstats();
}

function processstats() {
    eel.processstats()(displayResponse);
}
function displayResponse(response,leetid) {
    document.getElementById("response").innerText = response;
    document.getElementById("leetid").innerText = leetid;
}