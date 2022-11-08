function valid() {
    let fname = document.getElementById("fname").value;
    let lname = document.getElementById("lname").value;
    let a2z = /^[a-zA-Z]+$/;
    let email = document.getElementById("email").value;
    let atpos = email.indexOf('@');
    let dotpos = email.lastIndexOf('.');
    let country = document.getElementBy.value;
    console.log(country);
    let gender = document.querySelector('input[name="gender"]:checked');
    let mob = document.getElementById('mob').value;
    mob = String(Number(mob));
    let course = document.querySelectorAll('input[name="course"]:checked');
    // let state = document.frm.state.value;
    // let msg = document.getElementById('message').value;
    if (fname.length == 0) {
        alert("First Name cannot Empty");
        return false;
    } else if (!a2z.test(fname) && !a2z.test(lname)) {
        alert("Name Should be in Alphabets only");
        return false;
    }
    else if (lname.length == 0) {
        alert(" Last Name cannot Empty");
        return false;
    } else if (!a2z.test(lname)) {
        alert("Name Should be in Alphabets only");
        return false;
    }
    else if (gender == null) {
        alert("Select Your Gender");
        return false;
    }
    else if (
        email.length == 0 ||
        !a2z.test(email[0]) ||
        !a2z.test(email[email.length - 1]) ||
        (email.match(/@/g) || []).length != 1 ||
        dotpos - atpos < 3
    ) {
        alert("Invalid format Email");
        return false;
    }
    else if (isNaN(mob)) {
        alert("Only Numbers can be Acceptable");
        return false;
    }
    else if (mob.length != 10) {
        alert("Number Should be 10 digits");
        return false;
    }
    else if (course.length == 0) {
        alert('Select at least one Course');
        return false;
    }
    // else if (country == 'none') {
    //     alert("Select Country");
    //     return false;
    // }
    // else if (state == 'none') {
    //     alert("Select City");
    //     return false;
    // }
    // else if (msg.length <= 50) {
    //     alert("Message contains at least 50 alphabets");
    //     return false;
    // }
    else {
        alert("Success!");
        return true;
    }
}
