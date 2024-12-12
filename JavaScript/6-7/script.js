let day_of_weak = 1
switch (day_of_weak){
    case 1:
        console.log("Понедельник")
        break
    case 2:
        console.log("Вторник")
        break
    case 3:
        console.log("Среда")
        break
    case 4:
        console.log("Четверг")
        break
    case 5:
        console.log("Пятница")
        break
    case 6:
        console.log("Суббота")
        break
    case 7:
        console.log("Воскресенье")
        break
}

// let a = 6
// let b = 10
// console.log(a % 5 == 0 ? "Кратно":"Не кратно")
// let num = Number(prompt("введите число"))
// let n = 0
// while(n <= num){
//     console.log(n)
//     n++
// }
// for (let i = 0; i <= num; i++){
//     console.log(i)
// }
// let user = Number(prompt("Введите число"))
// let n = user
// while (n <= 100){
//     console.log()
// }
// for (let i = user; i <= 100; i+=user){
//     console.log(i)
// do {
//     answer = Number(prompt("2 + 2 * 2"))
// }
// while(answer != 6)

// let count  = 0
// let res1 = 1500
// let res = res1
// do {
//     res = res1 / 2
//     count++
// }

// while(res > 50)
// console.log(`Число: ${res},Делений: ${count}`)

// function f(a = 0,b = 0){
//     return(a<b ? a:b)
// }

// concsole.log(f(1,2))

// function table (a=1){
//     for (let i = 1;i <= 10;i++)
//     console.log(`${i} * ${a} = ${a*i}`)
// }

// console.log(table(Number(prompt("введите число"))))
// function sum_of_5 (a = 0,b = 0,c = 0,d = 0,e = 0,){
//     return a + b + c + d + e

// }
    
// console.log(sum_of_5(12,2,1))

// function sum_5(){
//     let res = -Infinity
//     for (let elem of arguments){
//         if (elem > res){
//             res = elem
//         }
//     }
//     return res

// }

// console.log(sum_5(-20,0.00001,0))

// function get_even_or_odd(start = 0,finish = 0,is_od_or_ev = true){
//     if (is_od_or_ev){
//         for(let i = start; i <= finish;i++){
//             if ( i % 2 == 0){
//                 console.log(i)
//             }
            
//         }
//     }
//     else{
//         for(let i = start; i <= finish;i++){
//             if ( i % 2 != 0){
//                 console.log(i)
//             }
//     }
// }
// }
// get_even_or_odd(1,10,false)


// let arr = [12,32,43,123,44]
// console.log(arr)
// arr.push(22)
// console.log(arr)
let arr = []
for (let i = 0; i <=99;i++){
    b = (Math.floor(Math.random()*10))
    arr.push(b)
}
console.log(arr)