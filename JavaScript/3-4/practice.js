document.querySelector(".add").onclick = function() {
    let num1 = Number(document.querySelector(".num1").value)
    let num2 = Number(document.querySelector(".num2").value)
    let res = num1 + num2
    document.querySelector("span").innerHTML = res
    document.querySelector(".num1").value = ""
    document.querySelector(".num2").value = ""
}
document.querySelector(".sub").onclick = function() {
    let num1 = Number(document.querySelector(".num1").value)
    let num2 = Number(document.querySelector(".num2").value)
    let res = num1 - num2
    document.querySelector("span").innerHTML = res
    document.querySelector(".num1").value = ""
    document.querySelector(".num2").value = ""
}
document.querySelector(".mul").onclick = function() {
    let num1 = Number(document.querySelector(".num1").value)
    let num2 = Number(document.querySelector(".num2").value)
    let res = num1 * num2
    document.querySelector("span").innerHTML = res
    document.querySelector(".num1").value = ""
    document.querySelector(".num2").value = ""
}
document.querySelector(".div").onclick = function() {
    let num1 = Number(document.querySelector(".num1").value)
    let num2 = Number(document.querySelector(".num2").value)
    if (num2 == 0){
        alert("На ноль делить нельзя")
        document.querySelector(".num2").value = ""
    }
    else{
        let res = Math.round (num1 / num2)
    document.querySelector("span").innerHTML = res
    document.querySelector(".num1").value = ""
    document.querySelector(".num2").value = ""
    }
        
}