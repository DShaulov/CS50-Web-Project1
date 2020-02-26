function checkUser(){
    console.log("The value is: " + document.getElementById("username").value)
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