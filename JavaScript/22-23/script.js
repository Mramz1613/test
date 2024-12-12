// let btn_scroll_top = document.getElementById("btn_scroll_top")
// btn_scroll_top.addEventListener("click",()=>{
//     window.scrollTo({"left":0,"top":0,"behavior":"smooth"})
// })

// btn_scroll_top.addEventListener("scrollend",check_scroll_val())
// function check_scroll_val(){
//     console.log(window.scrollY)
//     if(window.scrollY > 100){
//         btn_scroll_top.style.display = "block"
//     }else{
//         btn_scroll_top.style.display = "none"
//     }}

// document.querySelectorAll(".buttons_row button").forEach((button)=>{
//     button.addEventListener("click",calc_btn_click)
// })
// let res_div = document.getElementById("res_div")
// let first_num = ""
// let sec_num = ""
// let action = ""
// let cur_number = "first"

// function calc_btn_click(e){
//     let char = e.target.innerHTML
//     if("0123456789".includes(char)){
//         if(cur_number === "first"){
//             first_num += char
//             console.log(first_num)
//             res_div.innerHTML = first_num
//         }else if(cur_number === "second"){
//             sec_num += char
//             res_div.innerHTML = `${first_num} ${action} ${sec_num}`
//         }
//     }
//     if("+-*/".includes(char)){
//         action = char
//         cur_number = "second"
//         res_div.innerHTML = `${first_num} ${action}`
//     }
//     if(char === "="){
//         switch (action){
//             case "+": res_div.innerHTML = `${first_num} ${action} ${sec_num} = ${Number(first_num)+ Number(sec_num)}`
//             break
//             case "-":res_div.innerHTML = `${first_num} ${action} ${sec_num} = ${Number(first_num)- Number(sec_num)}`
//             break
//             case "*":res_div.innerHTML = `${first_num} ${action} ${sec_num} = ${Number(first_num)* Number(sec_num)}`
//             break
//             case "/":res_div.innerHTML = `${first_num} ${action} ${sec_num} = ${Number(first_num)/ Number(sec_num)}`
//         }
//     }
//     if(char === "C"){
//         res_div.innerHTML = ""
//         first_num = ""
//         sec_num = ""
//         action = ""
//         cur_number = "first"
//     }
// }
let rem_btn = document.getElementById("rem_btn")
let id_form_task = document.getElementById("id_form_task")
id_form_task.addEventListener("submit",(e)=>{
    if(rem_btn.checked){
        alert(document.getElementById("name").value)
    }else alert(document.getElementById("pass").value)
})

