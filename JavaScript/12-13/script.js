// let some_string = "vasya"
// some_string = 'vasya'
// some_string =`vasya`

// console.log(`Май нейм из ${some_string}`)
// console.log(some_string.at(-1))
// console.log(some_string.length)
// some_string = "\n    лол &&&& asdasd \n"
// console.log(some_string.trim())
// for ( let i = 0; i < 5000;i++){
//     document.write(String.(i))
// }
// let some_string = "vasya"
// console.log(some_string.startsWith("VA".toLowerCase()))
// console.log(some_string.endsWith("a"))
// console.log(some_string.indexOf('u'))
// console.log(some_string.includes("u"))
// document.write("spam ".repeat(10))
// let str = "Вася пришел к Маше"
// console.log(str.replaceAll("а","*"))
// console.log(str.split(" "))
// console.log("як"> "собака")
// console.log("кот"> "котенок")
// console.log("ё".charCodeAt())
// for ( let i = 1030;i < 1150;i++){
//     document.write(String.fromCharCode(i))
// }
// console.log("КОТИК".toLowerCase())
// console.log("котик".toUpperCase())
// function comparison(first,second){
//     if(first.lenght > second.lenght) return 1
//     if(first.lenght < second.lenght) return -1
//     return 0
// }
// console.log(comparison("Кот","Котики"))


// function capital(some_string){
//     return some_string[0].toUpperCase + some_string.slice(1)
// }
// console.log("fsdfsdfs")

// function isGlasn(str){
//     let glasni = "ауоиэыяюеёАУОИЭЫЮЕЁ"
//     let count = 0
//     for (let i of str){
//         if(glasni.includes(i)){
//             count++
//         }
//     }
//     return count

// }
// console.log(isGlasn("Бляяяяя"))

// function antispam(str){
//     str = str.toLowerCase()
//     let spam = ["бесплатно","только сегодня","не удаляйте"]
//     for (let i of spam){
//         if(str.includes(i)) return true   
//     }
//     return false
// }
// function antispam2(str){
//     str = str.toLowerCase()
//     let spam = ["бесплатно","только сегодня","не удаляйте"]
//     for (let i of spam){
//         if(str.includes(i)){
//             str =  str.replaceAll(i,"*".repeat(i.length))
//         }   
//     }
//     return str
// }
// console.log(antispam2("Бесплатно испугался не бойся б не удаляйте  Бесплатно я друг Бесплатно" ))
// console.log(antispam("бу испугался не бойся я друг" ))
// function truncate(str,num){
//     let len = str.length
//     if (len > num){
//         return str.slice(0,num - len) + ".".repeat(len - num)
//     }

// }
// console.log(truncate("Привет сук",10))

// function count_words(str){
//     let count = 0
//     let words = str.split(" ")
//     for(let i of words){
//         count++
//     }
//     return count
// }
// console.log(count_words("Как так"))

// function biggest_word(str){
//     let cur_biggest_word = ""
//     let words = str.split(" ")
//     for (let word of words){
//         if (word.lenght > cur_biggest_word.lenght){
//             cur_biggest_word = words
//         }
//     }
//     return cur_biggest_word
// }
// console.log(biggest_word("Ты что делаешь"))
function avg(str){
    let count_letters = 0
    let all_words = str.split(" ")
    let len = all_words.length
    for(word of all_words){
        count_letters += word.length
    }
    let res = count_letters/len
    return res
}
console.log(avg("Я Я Я Я"))