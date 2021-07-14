window.addEventListener("scroll", function(){
    var header = document.querySelector("nav");
    header.classList.toggle("sticky", window.scrollY > 650 );
})



// const currentLocation = location.href;
// const menuItem = document.querySelectorAll('.menuItem');
// const menuLength = menuItem.length;
// for(let i=0; i<menuLength; i++){
//     if(menuItem[i].href === currentLocation){
//         menuItem[i].className = "active";
//     }
// }

const animationItems = document.querySelectorAll('.menuItem');
const sectionItems = document.querySelectorAll('.navItem');
const animationOnScroll = () => {
    if (animationItems.length > 0) {
        for (let i = 0; i < animationItems.length; i++) {
            const animationStart = 4;
            let windowsHeight = window.scrollY;
            let sectionHeight = sectionItems[i].scrollY;
            if  (windowsHeight>sectionHeight){
                animationItems[i].classList.add('active');
            }
            }
        }
    }

window.addEventListener('scroll', animationOnScroll);
// Sehife acilanda il section animasiyanin aktivlesmesi
animationOnScroll();
