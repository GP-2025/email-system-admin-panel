function setLang(lang) {
    sessionStorage.setItem('lang', lang);
    document.cookie = `lang=${lang}; max-age=31536000; path=/`;
    window.location.reload();
}