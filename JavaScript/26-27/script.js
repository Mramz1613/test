// let template = /2/
// console.log(template.test("vasya"))
// console.log(template.test("vasya2"))
// console.log(template.test("va1sya"))
// console.log(template.test("va2sya22"))
// console.log(template.test("Вася"))

// let template = /1234/
// console.log(template.test("1234vasya"))
// console.log(template.test("vasya2"))
// console.log(template.test("va1sya"))
// console.log(template.test("va2sya22"))
// console.log(template.test("Вася"))

// let template = /vasya/
// console.log(template.test("vas1234ya"))
// console.log(template.test("vasya2"))
// console.log(template.test("va1sya"))
// console.log(template.test("va2sya22"))
// console.log(template.test("Вася"))

// let template = /vasya/i
// console.log(template.test("vas1234ya"))
// console.log(template.test("vasya2"))
// console.log(template.test("va1sya"))
// console.log(template.test("va2sya22"))
// console.log(template.test("Vasya"))

// let template = /vasya|123/i
// console.log(template.test("vasya123"))
// console.log(template.test("vasya2"))
// console.log(template.test("va1sya"))
// console.log(template.test("va2sya22"))
// console.log(template.test("Vasya"))

// let template = /\d/ digit
// console.log(template.test("vasya123"))
// console.log(template.test("vasya2"))
// console.log(template.test("va1sya"))
// console.log(template.test("va2sya22"))
// console.log(template.test("Vasya"))

// let template = /\D/           not digit
// console.log(template.test("vasya123"))
// console.log(template.test("vasya2"))
// console.log(template.test("va1sya"))
// console.log(template.test("va2sya22"))
// console.log(template.test("Vasya"))

// let template = /\d\d/
// console.log(template.test("vasya123"))
// console.log(template.test("vasya2"))
// console.log(template.test("Vasya"))
// console.log(template.test("va1sya"))
// console.log(template.test("va2sya22"))

// let template = /\d{4}/
// console.log(template.test("vasya1234"))
// console.log(template.test("vasya2"))
// console.log(template.test("Vasya"))
// console.log(template.test("va1sya"))
// console.log(template.test("va2sya22"))

// let template = /\w/
// console.log(template.test("vasya1234"))
// console.log(template.test("vasya22"))
// console.log(template.test("Vasya"))
// console.log(template.test("va1sya"))
// console.log(template.test("va2sya22"))

// let template = /^\d/
// console.log(template.test("1vasya1234"))
// console.log(template.test("vasya22"))
// console.log(template.test("1Vasya"))
// console.log(template.test("va1sya"))
// console.log(template.test("va2sya22"))

// let template = /\d\d$/
// console.log(template.test("1vasya1234"))
// console.log(template.test("vasya22"))
// console.log(template.test("1Vasya"))
// console.log(template.test("va1sya"))
// console.log(template.test("va2sya22"))

// let template = /^\d\d$/
// console.log(template.test("1vasya1234"))
// console.log(template.test("vasya22"))
// console.log(template.test("1Vasya"))
// console.log(template.test("va1sya"))
// console.log(template.test("va2sya22"))

// let template = /^\d{2,4}:$/
// console.log(template.test("1vasya1234"))
// console.log(template.test("vasya22"))
// console.log(template.test("122:"))
// console.log(template.test("va1sya"))
// console.log(template.test("va2sya22"))

// let template = /[a-z]/
// console.log(template.test("1vasya1234"))
// console.log(template.test("vasya22"))
// console.log(template.test("122:"))
// console.log(template.test("va1sya"))
// console.log(template.test("va2sya22"))

// let template = /[a-zа-я]/i
// console.log(template.test("1vasya1234"))
// console.log(template.test("vasya22"))
// console.log(template.test("122:"))
// console.log(template.test("va1sya"))
// console.log(template.test("123"))

// let template = /^[1-5]/i
// console.log(template.test("123"))
// console.log(template.test("12345"))
// console.log(template.test("122:"))
// console.log(template.test("12345va1sya"))
// console.log(template.test("v3"))

// let template = /^\d{2}:\d{2}$/
// console.log(template.test("12:99"))
// console.log(template.test("122:245"))
// console.log(template.test("22:11"))
// console.log(template.test("12345va1sya"))
// console.log(template.test("v3"))

let email_temp = /^[a-zA-Z0-9_.]{3,100}@[a-zA-Z]{1,100}\.[a-zA-Z]{2,10}/
console.log(email_temp.test("lol12.3@gmail.co"))


let password_temp = /^[0-9a-zA-Zа-яА-Я!?]{8,20}$/
console.log(password_temp.test("987sdfk123!"))