//expandir o menu
var btnExp = document.querySelector('#btn-exp')
var menuSide = document.querySelector('.menu-lateral')
var footer = document.querySelector('#footer')
var principal = document.querySelector('#principal');

btnExp.addEventListener('click', function(){
    menuSide.classList.toggle('expandir') //sempre q clicar no menu expandir, se existir a classe expandir, quero q remova, senão, quero q adiona

if (menuSide.classList.contains('expandir')) {
    footer.style.left = '300px';
    footer.style.width = 'calc(100% - 300px)';
} else {
    footer.style.left = '80px';
    footer.style.width = 'calc(100% - 80px)';
}
});

