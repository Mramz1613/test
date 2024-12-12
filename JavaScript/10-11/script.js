// function rec(n){
//     if (n <=1)
//         {return 1}
//     else return n * rec(n-1)
// }
// function rec_brascet(n){
//     if (n <= 0) return ""
//     return "(" + rec_brascet + ")"
// }
// let recurcia = document.getElementById("rec1").innerHTML
// recurcia = rec_brascet(5)
// let my_arr = new Array
// my_arr = [123,-123,"ПРИВ",true,["lol",123],false]
// // for( let i in my_arr){
// //     console.log(i)
// // }
// console.log(my_arr[(my_arr.length-1)])
// my_arr.push(123)
// my_arr.unshift(true)
// console.log(my_arr)
// console.log(my_arr.slice(2,5))


// function randint(a,b){
//     return Math.floor((a + Math.random())*(b+1-a))
// }

// let new_arr = []
// for( let i = 0; i < 10;i ++){
//     new_arr.push(randint(0,10))
// }
// // alert(randint(1,10))
// // console.log(new_arr)
// // function only_even(arr){
// //     for(let elem of arr){
// //         if(elem%2==0){
// //             document.write(`<p>${elem}</p}`)
// //         }
// //     }
// // }
// function summ(arr){
//     res = 0
//     for (let i of arr){
//         res += i
//     }
//     return res
// }
// function max(arr){
//     res = -Infinity
//     for( let i of arr){
//         if(i>res){
//             res = i
//         }
//     }
//     return res
// }
// alert(new_arr)
// alert(summ(new_arr))
// alert(max(new_arr))
function slovar(){
    let short = []
    let long = []
    let arr = []
    for(let i = 0;i<10;i++){
        arr.push(prompt("Введите слово"))
    }
    let stat = ""
    let short_word = document.getElementById("short")
    let long_word = document.getElementById("long")
    short_word.style.color = "blue"
    for(let i of arr){
        if(i.length <=5){
            stat+=i+" :короткое\n"
            short.push(i)
            short_word.innerHTML += `<li>${i}</li>`
        }else{
            stat+=i+" :длинное\n"
            long.push(i)
            long_word.innerHTML += `<li>${i}</li>`
            
        }
    }
    return stat
}

alert(slovar())