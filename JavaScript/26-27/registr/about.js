let user_email = ""
let all_cookies = document.cookie.split(";")
for(cur_cookie of all_cookies){
    let key_val = cur_cookie.trim().split("=")
    if(key_val[0] === "email"){
        user_email = key_val[1]
    }
}
if(user_email === ""){
    window.location.href = "reg.html"
}else{
    document.getElementById("user_info_txt").innerHTML = `Привет,${user_email}`
}
