function processstats() {
    eel.processstats()(displayResponse);
}
function displayResponse(response,leetid) {
    document.getElementById("response").innerText = response;
    document.getElementById("leetid").innerText = leetid;
}