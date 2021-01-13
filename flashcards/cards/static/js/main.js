// debugger;
const front = document.querySelector('.card-front')
const back = document.querySelector('.card-back')
const card = document.querySelector('.flashcard')

card.addEventListener('click', function(event){
    // debugger;
    flipCard()
})
// style.display resets elements display property to default
function flipCard(){
    if (front.style.display == 'none'){
        front.style.display = 'block'
        back.style.display = 'none'
    } else {
        front.style.display = 'none'
        back.style.display = 'block'
    }
}