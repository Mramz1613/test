// class Circle{
//     constructor(radius){
//         this.radius = radius
//     }

//     getRad(){
//         return this.radius
//     }
//     setRad(newRad){
//         this.radius = newRad
//     }
//     getDiam(){
//         return (this.radius*2)
//     }
//     getSq(){
//         let res = (Math.PI*(this.radius)**2)
//         return res
//     }
//     getDlina(){
//         let res = 2*Math.PI*this.radius
//         return res
//     }
        
// }

// new_cir = new Circle(10)
// console.log(new_cir.getRad())
// new_cir.setRad(15)
// console.log(new_cir.getRad())
// console.log(new_cir.getDiam())
// console.log(new_cir.getSq())
// console.log(new_cir.getDlina())

// class CssClass{
//     constructor(name,styles = []){
//         this.name = name
//         this.styles = styles
//     }

// }
// class Human{
//     constructor(firstname = "",lastname = ""){
//         this.firstname = firstname
//         this.lastname = lastname
//     }
//     getInfo(){
//         return this.firstname + " " + this.lastname
//     }


// }

// class Student extends Human{
//     constructor(firstname = "",lastname = "",speciality){
//         super(firstname,lastname);
//         this.speciality = speciality
//     }

//     getInfo(){
//         return this.firstname + " " + this.lastname + " " + this.speciality
//     }
// }

// vasya = new Human("Vasya","Vasin")
// petya = new Student("Petya","Petrov","cook")
// console.log(vasya.getInfo())
// console.log(petya.getInfo())


// class Button{
//     constructor(width = 10, hight = 10,text = "lol"){
//         this.width = width
//         this.hight = hight
//         this.text = text
//     }
//     showBtn(){
//         document.write(`<button style ="width:${this.width} px; hight:${this.hight} px;">${this.text}</button>`)
//     }
// }

// class BootstrapButton extends Button{
//     constructor(width,hight,text,color= "red",bgColor = "black"){
//         super(width,hight,text)
//         this.color = color
//         this.bgColor = bgColor
//     }
//     showBtn(){
//         document.write(`<button style ="width:${this.width} px; hight:${this.hight} px; color:${this.color}; background-color: ${this.bgColor} ;>${this.text}</button>`)
//     }
// }
    
// new_but = new Button()
// for(let i = 0 ;i < 10;i++){
//     new_but.width += i
//     new_but.text += i
//     new_but.showBtn()

// }
// new_but2 = new BootstrapButton()
// for(let i = 0 ;i < 10;i++){
//     new_but2.width += i
//     new_but2.hight += i
//     new_but2.showBtn()

// }


// class Figure{
//     constructor(name = ""){
//         this.name = name
//     }
//     get_name(){
//         return this.name
//     }
//     get_info(){}

//     get_area(){}

//     get_per(){}
// }

// class Square extends Figure{
//     constructor(size = 1){
//         super("square")
//         this.size = size
//     }
//     get_info(){
//         return this.name + " "+ this.size
//     }

//     get_area(){
//         return this.size**2
//     }

//     get_per(){
//         return this.size*4
//     }
// }

// class Rectangle extends Figure{
//     constructor(side_one = 1 ,side_two = 1
//     ){
//         super("rectangle")
//         this.side_one = side_one
//         this.side_two = side_two
//     }
//     get_info(){
//         let res = "Первая сторона:" + this.side_one +" Вторая сторона: "+ this.side_two + " " + this.name
        
//         return res
//     }

//     get_area(){
//         return this.side_one * this.side_two
//     }

//     get_per(){
//         return (this.side_one*2)+(this.side_two*2)
//     }
// }

// rec = new Rectangle(10,10)
// console.log(rec.get_area())
// console.log(rec.get_per())
// console.log(rec.get_info())

// class ExtendetArray extends Array{
//     getString(separator){
//         return this.join(separator)
//     }
//     getHTML(tagName){
//         let res_string = ""
//         if(tagName === "li"){
//             res_string += "<ol>"
//             for ( let elem of this){
//                 res_string +=`<${tagName}>${elem}</${tagName}>`
//             }
//             res_string += "</ol>"
//             document.write(res_string)
//         }
//         else{for ( let elem of this){
//             res_string +=`<${tagName}>${elem}</${tagName}>`
//         }
//         document.write(res_string)}
        
//     }
// }

// let my_arr = new ExtendetArray("От","топота","копыт","пыль","по","полю","летит")
// let res = my_arr.getString("/")
// console.log(res)
// my_arr.getHTML("li")

// class HtmlElement{
//     constructor(tag_name,is_self_closed = false,text = "",all_atr = {},all_styles = {},children = []){
//         this.tag_name = tag_name
//         this.is_self_closed = is_self_closed
//         this.text = text
//         this.all_atr = all_atr
//         this.all_styles = all_styles
//         this.children = children
//     }
//     set_atr(atr,val){
//         this.all_atr[atr] = val

//     }
//     set_style(atr,val){
//         this.all_styles[atr] = val
//     }
//     add_child_to_end(html_element){

//     }
//     add_child_to_start(html_element){

//     }
//     getHtml(){
//         let res_html_str = ""
//         if (this.is_self_closed){
//             res_html_str+= `<${this.tag_name}`
            
//         }
//         else {
//             res_html_str+= `<${this.tag_name}`
//             for (let atr in this.all_atr){
//                 res_html_str += ` ${atr}="${this.all_atr[atr]}"`
//             }
//             res_html_str += " style='"
//             for (let atr in this.all_styles){
//                 res_html_str += `${atr}:${this.all_styles[atr]}; `
//             }
//             res_html_str +="'"
//             res_html_str+= `>`
//             res_html_str += this.text
//             res_html_str+= `</${this.tag_name}`
//         }
//         document.write(res_html_str)
//     }
// }

// let some_element = new HtmlElement("div",false,"lorem lorem lorem",{"id": "first","class":"my_divs"},{"color":"red"})
// some_element.set_atr("id","new_id")
// some_element.set_style("background-color","blue")
// some_element.getHtml()

class Employee{
    constructor(firstname = "", lastname = "", vacancy = "", salary = 0){
        this.firstname = firstname
        this.lastname = lastname
        this.vacancy = vacancy
        this.salary = salary
    }
}

class EmployeeTable{
    constructor(all_workers=[]){
      this.all_workers = all_workers  
    }
    get_html(){
        let res_tbl = "<table>"
        for (let i = 0 ;i < this.all_workers.length;i++){
            res_tbl += "<tr>"
                for(let probrty of this.all_workers[i])
            res_tbl += "</tr>"
        }
        res_tbl += "</table>"
   }
}

let vasya = new Employee("Vasya","Vasin","manager",2345)
let petya = new Employee("Petya","Petrov","CEO",46456)
let vanya = new Employee("Vanya","Vanin","manager",435646)
let my_table = new EmployeeTable([vanya,petya,vanya])