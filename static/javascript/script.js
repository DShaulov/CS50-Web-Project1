function checkUser(){
    if (document.getElementById("username").value == "") {
        document.getElementById("userError").hidden = false;
        return false;
    }

    if (document.getElementById("password").value == "") {
        document.getElementById("passwordError").hidden = false;
        return false;
    }

    if (document.getElementById("confirmation").value == "") {
        document.getElementById("confirmationError").hidden = false;
        return false;
    }

    if(document.getElementById("password").value != document.getElementById("confirmation").value) {
        document.getElementById("matchError").hidden = false;
        return false;
    }
}

function checkSearch() {
    if (document.getElementById('search').value == "") {
        document.getElementById('searchError').hidden = false;
        return false;
    }
}

function reviewCheck() {
    if (document.getElementById('review').value == "" ){
        document.getElementById('reviewError').hidden = false;
        return false;
    }
}
