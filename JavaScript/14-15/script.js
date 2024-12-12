// vasya = {
//     "name": "Vasya",
//     "phone": "89907981111",
//     "address":{
//         "city":"Kaliningrad",
//         "street":"Pushkina"
//     }
// }

// console.log(vasya["phone"])
// console.log(vasya.name)


// let rectangle = {
//     "x1":10,
//     "y1":20,
//     "x2":30,
//     "y2":5,
// }

// function rectangle_info(rect){
//     console.log(`A) x: ${rect.x1}; y:${rect.y1}`)
//     console.log(`B) x: ${rect.x1}; y:${rect.y2}`)
//     console.log(`C) x: ${rect.x2}; y:${rect.y1}`)
//     console.log(`D) x: ${rect.x2}; y:${rect.y2}`)
// }
// rectangle_info(rectangle)
// function moove_x(rect,change){
//     rect.x1+=change
//     rect.x2+=change
// }
// function moove_y(rect,change){
//     rect.y1+=change
//     rect.y2+=change
// }
// moove_x(rectangle,10)
// moove_y(rectangle,20)
// console.log(rectangle)

// class User{
//     firstname = "test"
//     lastname = "some test"

//     constructor(login,password){
//         this.login = login
//         this.password = password
//     }
//     get_info(){
//         console.log(`login: ${this.login}, pass: ${this.password}}`)
//     }
//     static hello(){
//         console.log("Я статичная функция")
//     }
// }

// vasya  = new User("admin","133228")

// petya = new User("NeAdmin","noPass")

// petya.get_info()
// User.hello()
// class PrintMashin{
//     constructor (size,color,family){
//         this.size = size
//         this.color = color
//         this.family = family
//     }
//     print(text){
//         document.write(`<p style ="font-size: ${this.size}px; color: ${this.color} ; font-family: ${this.family}">${text}</p>`)
//     }
// }
// style_font = new PrintMashin(50,"blue","Arial")
// style_font.print("Ваааааау")

class News{
    constructor(title,content,all_tags,publish_data){
        this.title = title
        this.content = content
        this.all_tags = all_tags
        this.publish_data = new Date(publish_data)

    }
    print(){
        document.write(`<div class="news_div"><h2 class="news_title">${this.title}</h2>`)
        let cur_day = new Date()
        let date_dif = Math.floor((cur_day - this.publish_data)/1000/60/60/24)
        console.log(date_dif)
        if( date_dif == 0){
            document.write(`<p>Сегодня</p>`)
        }else if( date_dif <= 7 ){document.write(`<p>${date_dif} Дней(Дня) назад</p>`)
        }else{document.write(`<p>${this.publish_data.toLocaleDateString()}</p>`)}
            
        document.write(`<p class="news_content">${this.content}</p>`)
        
        for(let tag of this.all_tags){
            document.write(`<a href="#" class="news_tag" style="margin-right: 10px">#${tag}</a>`)
        }
        document.write("</div>")
    }
}


class NewsThread{
    constructor (all_news = []){
        this.all_news = all_news
    }

    get_news_amount(){
        return this.all_news.length

    }

    get_all_news(){
        for( let cur_news of this.all_news){
            cur_news.print()
        }
    }
    add_news(news){
        this.all_news.push(news) 
    }
    delete_news(){
        
    }
    sort_by_date(){
        this.all_news.sort((a,b) => (a.publish_data - b.publish_data))
    }
    search_by_tag(){
        
    }
}
let news_1 = new News("Привет","Что-то тут было",["best","useful"],"2024-9-11")
let news_2 = new News("Бу испугался?","Не бойся я друг",["friend","scary"],"2022-1-14")
let news_3 = new News("Привет","Что-то тут было",["best","useful"],"2023-10-4")
let my_news_thread = new NewsThread()


my_news_thread.add_news(news_1)
my_news_thread.add_news(news_2)
my_news_thread.add_news(news_3)
my_news_thread.sort_by_date()
my_news_thread.get_all_news()
console.log(my_news_thread.get_news_amount())