// Создание функции
function calc(){
    let ans = confirm("Вы не робот");
    return ans
}
let answer = calc()
if (answer == true){
    alert("Привет,Человек")
}
else{
    alert("01001001000000111011100001010110")
}
const arr = ["Я","имею","валюту","на","зубах","руда"]
let color = document.querySelector(".color")
console.log(color.className)
document.querySelector(".party").onclick = function(){
    color.className = "stop_color"
}
document.querySelector(".stop").onclick = function(){
    color.className = "color"
}
var count = 0
document.getElementById("song").onclick = function(){
        let word = document.getElementById("test")
        word.innerHTML = arr[count]
        count += 1
        if (arr.length <= count){
            count = 0
        }
}