document.getElementById("reg_form").addEventListener("submit",(e)=>{
    let user_emal = document.getElementById("email_input").value
    let pass_1_input = document.getElementById("pass_1_input").value
    let pass_2_input = document.getElementById("pass_2_input").value
    let temp_emal = /(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])/
    let temp_pass = /[a-zA-Z]/
    let has_error = false
    if(temp_emal.test(user_emal) === false){
        document.getElementById("email_error").style.display = "inline"
        has_error = true
    }
    else{
        document.getElementById("email_error").style.display = "none"
    }

    let password_err = ""
    if(pass_1_input.length < 6){
        password_err += "need more than 6 chars;"
    }
    if(/[a-z]/.test(pass_1_input) === false){
        password_err += "need small chars; "
    }
    if(/[A-Z]/.test(pass_1_input)=== false){
        password_err += "need capital chars; "
    }if(/[0-9]/.test(pass_1_input)=== false){
        password_err += "need at least one didgit; "
    }

    if (password_err){
        document.getElementById("pass_1_error").style.display = "inline"
        document.getElementById("pass_1_error").innerHTML = password_err
        has_error = true
    }
    else{
        document.getElementById("pass_1_error").style.display = "none"
    }

    if(pass_1_input !== pass_2_input){
        document.getElementById("pass_2_error").style.display = "inline"
        has_error = true
    }
    else{
        document.getElementById("pass_2_error").style.display = "none"
    }

    if(has_error){
        e.preventDefault()
    }
    else{
        document.cookie = `email = ${user_emal};path=/;max-age=60`
    }
})