// let task_2_form = document.getElementById("task_2_form")
// task_2_form.addEventListener("submit",()=>{
//     let input_email = document.getElementById("input_email").value

//     alert(`Вам отправлено письмо на почту ${input_email}`)
// })
let res = document.getElementById("res")

document.getElementById("task_3_form").addEventListener("submit",(e)=>{
    let res = document.getElementById("res")
    let firstname_val = document.getElementById("firstmane").value
    let lastname_val = document.getElementById("lastname").value
    let b_day_val = document.getElementById("b_day").value
    let country = document.getElementById("country").value
    let city = document.getElementById("city").value
    let gender_val = ""
    for(let elem of document.getElementsByName("gender")){
        if(elem.checked){
            gender_val = elem.value
        }
    }
    let all_skills =""
    let all_skills_list = document.getElementsByClassName("skill_input")
    for(let elem of all_skills_list){
        if(elem.checked){
            all_skills += elem.name + ";"
        }
    }
    res.innerHTML = `
    <table>
        <tr>
            <td>Firstname</td>
            <td>${firstname_val}</td>
        </tr>
        <tr>
            <td>Lastname</td>
            <td>${lastname_val}</td>
        </tr>
        <tr>
            <td>Birthday</td>
            <td>${b_day_val}</td>
        </tr>
        <tr>
            <td>Country</td>
            <td>${country}</td>
        </tr>
        <tr>
            <td>City</td>
            <td>${city}</td>
        </tr>
        <tr>
            <td>Skills</td>
            <td>${all_skills}</td>
        </tr>

        <tr>
            <td>Gender</td>
            <td>${gender_val}</td>
        </tr>
    </table>
    `
    e.preventDefault()
})

