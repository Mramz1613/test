function num_up(){
    let num = document.getElementById("task_1_num")
    num.innerHTML = Number(num.innerHTML) + 1
}

function num_down(){
    let num = document.getElementById("task_1_num")
    num.innerHTML -= Number(1)
}

let all_pallet = document.getElementById("all_color_pallet")
let add_color_btn =  document.getElementById("add_color_btn")
add_color_btn.addEventListener("click",() =>{
    let new_color_block = document.createElement("div")
    new_color_block.setAttribute("class", "color_block")
    let red = Math.floor(Math.random()*255)
    let blue = Math.floor(Math.random()*255)
    let green = Math.floor(Math.random()*255)
    new_color_block.style.backgroundColor = `rgb(${red},${green},${blue})`
    new_color_block.addEventListener("click",(e)=>{
        all_pallet.removeChild(e.target)
    })
    all_pallet.append(new_color_block)
})

let all_blocks = document.getElementsByClassName("color_block")
let task_3_text = document.getElementById("task_3_text")
for(let cur_block of all_blocks){
    cur_block.addEventListener("click",(e) =>{
        task_3_text.style.color = e.target.getAttribute("data-color")
    })
}

let comment_form = document.getElementById("comment_form")
comment_form.addEventListener("submit",(e)=>{
    e.preventDefault()
    let user_name = document.getElementById("name").value
    let comment_content = document.getElementById("new_comment_text").value
    let comment_date = new Date().toLocaleDateString()

    let new_comment_div = document.createElement("div")
    new_comment_div.setAttribute("class","comment_div")
    new_comment_div.innerHTML = `
    <h4>${user_name}</h4>
    <p>${comment_date}</p>
    <p>${comment_content}</p>
    <hr>
    `
    document.getElementById("all_coments_div").append(new_comment_div)
    document.getElementById("name").value = ""
    document.getElementById("new_comment_text").value = ""
})

let all_contries = ["Russia","Latvia","Poland","Portugies","Spain","SPQR","Romania","Estonia","USA","UK"]
let task_5_input = document.getElementById("task_5_input")
let counytries_datalist = document.getElementById("counytries_datalist")
task_5_input.addEventListener("input",()=>{
    counytries_datalist.innerHTML = ""
    let cur_user_input = task_5_input.value.toLowerCase()
    for(let country of all_contries){
        if(country.toLowerCase().startsWith(cur_user_input)){
            let new_country_option = document.createElement("option")
            new_country_option.innerHTML = country
            counytries_datalist.append(new_country_option)
        }
    }
})
