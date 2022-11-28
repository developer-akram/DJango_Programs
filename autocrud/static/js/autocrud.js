function valid() {
    let name = document.getElementById("name").value;
    let a2z = /^[a-zA-Z ]+$/;
    let email = document.getElementById("email").value;
    let atpos = email.indexOf('@');
    let dotpos = email.lastIndexOf('.');
    let svalue = '';
    let state = document.getElementById('state');
    for (let i =0; i < state.options.length; i++)
    {
        if(state.options[i].selected)
        {
            svalue += state.options[i].value;
        }
    }
    let country = document.getElementById('country').value;
    let gender = document.querySelector('input[name="gender"]:checked');
    let city = document.getElementById('city').value;
    let mob = document.getElementById('mob').value;
    mob = String(Number(mob));
    let tech = document.querySelectorAll('input[name="tech"]:checked');
    let qua = document.getElementById('qualification').value;
    let message = document.getElementById('mytextarea').value;
    // console.log(tech.length);
    if (name.length == 0) {
        alert("First Name cannot Empty");
        return false;
    } else if (!a2z.test(name)) {
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
    else if (isNaN(mob))
    {
        alert("Only Numbers can be Acceptable");
        return false;
    }
    else if (mob.length != 10) {
        alert("Number Should be 10 digits");
        return false;
    }
    else if (country === '') {
        alert("Select Country");
        return false;
    }
    else if (svalue === '')
    {
        alert("Select State");
        return false;
    }
    else if (city === '') {
        alert("Select City");
        return false;
    }
    else if (qua === '') {
        alert("Select Qualification");
        return false;
    }
    else if (tech.length == 0) {
        alert("Select At least one Technology");
        return false;
    }
    else if (message.length == 0) {
        alert("Message box cannot be empty");
        return false;
    }
    else {
        alert("Success!");
        return true;
    }
}
