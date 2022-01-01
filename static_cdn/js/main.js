// console.log("Hello world")

const examBox = document.querySelector('#exam-box')
const CountdownBox = document.querySelector('#countdown-box')
// console.log(examBox)

const examDate = Date.parse(examBox.textContent)
// console.log(examBox)

const now = new Date().getTime()
// console.log(now)

const myCountdown = setInterval(()=>{
    const now =  new Date().getTime()
    // console.log(now)

    const diff = examDate - now
    // console.log(diff)

    const d = Math.floor(examDate  / ( 1000 * 60 * 60 * 24) - ( now /  ( 1000 * 60 * 60 * 24)))
    const h = Math.floor((examDate  / ( 1000 * 60 * 60 ) - ( now /  ( 1000 * 60 * 60 ))) % 24)  
    const m = Math.floor((examDate  / ( 1000 * 60 ) - ( now /  ( 1000 * 60  ))) % 60)  
    const s = Math.floor((examDate  / (1000) - ( now /  (1000))) % 60)  
    console.log(h)

    if (diff>0){
        CountdownBox.innerHTML = d + " days, " + h + " hours, " + m + " minutes, " + s + " seconds "
    } else {
        clearInterval(myCountdown)
        CountdownBox.innerHTML = 'Exam as Started'
    }
}, 1000)