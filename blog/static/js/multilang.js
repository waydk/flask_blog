const maxImg = document.querySelector('.right-panel img');
const select = document.querySelector('select');
const allLang = ['ru', 'en'];

document.querySelectorAll('.left-panel img').forEach(item => item.onmouseenter = (event) => maxImg.src = event.target.src);

select.addEventListener('change', changeURLLanguage);

// redirect to the url indicating the language
function changeURLLanguage() {
    let lang = select.value;
    location.href = window.location.pathname + '#' + lang;
    location.reload();
}

function changeLanguage() {
    let hash = window.location.hash;
    hash = hash.substr(1);
    if (!allLang.includes(hash)) {
        location.href = window.location.pathname + '#ru';
        location.reload();
    }
    select.value = hash;

    for (let key in langArr) {
        let elem = document.querySelector('.lng-' + key);
        let img = document.querySelector('.lng-img-' + key);
        
        // Change text
        if (elem) {
            elem.innerHTML = langArr[key][hash];
            console.log(langArr[key][hash]);
        }

        // Change image
        if (img) {
            let pathImg = 'static/img/' + langArr[key][hash];
            document.getElementById("img-about").src=pathImg;
            console.log(img);
        }

    }
}

changeLanguage();