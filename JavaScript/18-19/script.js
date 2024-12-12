// function testclick(){
//     alert("Молодец")
// }

// let sombtn = document.getElementById("some_button")
// sombtn.addEventListener("click",testclick)

// let my_div = document.getElementById("my_div")
// my_div.addEventListener('mousemove',() =>{
//     my_div.innerHTML += "A"
// })
// my_div.addEventListener('mousemove',() =>{
//     my_div.innerHTML += "A"
// })
// my_div.addEventListener('click',() =>{
//     my_div.innerHTML = ""
// })
// function div_click(e){
//     console.log(e.target)
//     let colors = ["red","green","aqua"]
//     e.target.style.backgroundColor = colors[Math.round((Math.random()*10))% 3]
// }
// my_div.addEventListener("mousemove",div_click)
document.getElementById("get_random").addEventListener("click",()=>{
    let random_number = Math.floor(Math.random()*100)
    document.getElementById("random_number_place").innerHTML = random_number
})
function get_cord(e){
    document.getElementById("holdplace").innerHTML = `X = ${e.clientX} : Y = ${e.clientY}`
}
document.getElementById("task_2").addEventListener("mousemove",get_cord)
document.getElementById("task_3_btn").addEventListener("click",()=>{
    let task_3_text = document.getElementById("task_3_text")
    if (task_3_text.style.display !== "none"){
        task_3_text.style.display = "none"
    }else{
        task_3_text.style.display = "block"
    }
})
// let all_buttons = document.querySelectorAll(".task_4_btn")
// all_buttons.forEach((elem)=>{
//     elem.addEventListener("click",()=>{

//     })
// })

let html_btn = document.getElementById("html")
let css_btn = document.getElementById("css")
let js_btn = document.getElementById("js")
function change_task_4_content(e){
    if(e.target.innerHTML === "HTML"){
        e.target.style.backgroundColor = "blue"
        css_btn.style.backgroundColor = "darkcyan"
        js_btn.style.backgroundColor = "darkcyan"
        document.getElementById("task_4_text").innerHTML = "Кто то сказал"
    }else if(e.target.innerHTML === "CSS") {
        e.target.style.backgroundColor = "blue"
        html_btn.style.backgroundColor = "darkcyan"
        js_btn.style.backgroundColor = "darkcyan"
        document.getElementById("task_4_text").innerHTML = "что у тебя не получится,я ответил хорошо"
    }else if(e.target.innerHTML === "JS") {
        e.target.style.backgroundColor = "blue"
        html_btn.style.backgroundColor = "darkcyan"
        css_btn.style.backgroundColor = "darkcyan"
        document.getElementById("task_4_text").innerHTML = "И у меня получилось"
    }
}
html_btn.addEventListener("click",change_task_4_content)
css_btn.addEventListener("click",change_task_4_content)
js_btn.addEventListener("click",change_task_4_content)
let progress_bar_val = 50
document.getElementById("task_6_btn").addEventListener("click",()=>{
    progress_bar_val += 10
    if(progress_bar_val > 200) progress_bar_val = 200
    document.getElementById("cur_progress").style.width = progress_bar_val +"px"
})

let all_cells = document.querySelectorAll("#task_7_table td")
for(let cur_cell of all_cells){
    cur_cell.addEventListener("mouseenter",cell_on)
    cur_cell.addEventListener("mouseleave",cell_off)
}
function cell_on(e){
    e.target.style.backgroundColor = "blue"
}
function cell_off(e){
    e.target.style.backgroundColor = "bisque"
}