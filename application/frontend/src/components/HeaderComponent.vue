<template>
<div class="header">
  <div class="top_header">
  <div class="top_header_main main">
    <div class="top_header_contacts">

      <div class="contacts_phone">
        <img class="top_header_icon" :src="require('../assets/icon/iconPhone.svg')" height="30" width="30" alt="phone"/>
        <span class="contacts_text"> +7 999 999-99-99 </span>
      </div>


      <div class="contacts_email">
        <img :src="require('../assets/icon/iconMail.svg')" class="top_header_icon" height="30" width="30" alt="mail"/>
        <span class="contacts_text">BuyGuitars@mail.com</span>
      </div>

    </div>

    <div class="top_header_logotype">
      <img class="logotype" :src="require('../assets/icon/iconLogo.svg')" height="50" width="167" alt="logo"/>
    </div>

    <div class="top_header_nav">
      <ul class="nav_list">
        <li class="nav_element"><a href="#" class="nav_element_link">Акции</a></li>
        <li class="nav_element"><a href="#" class="nav_element_link">О нас</a></li>
        <li class="nav_element"><a href="#" class="nav_element_link">Помощь</a></li>
        <li class="nav_element"><a href="#" class="nav_element_link">Контакты</a></li>
      </ul>
    </div>
  </div>

  <div class="contacts_social">
      <a href="https://vk.com/" class="social_networks">Вконтакте</a>
      <a href="https://www.whatsapp.com/" class="social_networks social_networks_margin">WhatsApp</a>
      <a href="https://web.telegram.org/" class="social_networks">Telegram</a>
  </div>

</div>
<div class="bottom_header">
  <div class="bottom_header_main main">

    <div class="bottom_header_wrapper">
    <div class="bottom_header_catalog">
      <span class="catalog_title">Каталог</span>
      <img class="bottom_header_icon" :src="require('../assets/icon/iconMenu.svg')" height="30" width="30" alt="menu"/>
    </div>
    <div class="bottom_header_search">
      <img :src="require('../assets/icon/iconSearch.svg')" height="15" width="15" alt="search"/>
      <input class="search_input" placeholder="Поиск..."/>
      <button class="search_button"> <img :src="require('../assets/icon/iconArrowWhite.svg')" alt="arrow" width="24" height="14"> </button>
    </div>
    </div>

    <div class="bottom_header_functional">
      <div class="functional_bag">
        <span class="functional_bag_price" :class="{'hidden': this.price === 0 }"> {{this.price}} ₽</span>
        <img class="top_header_icon" :src="require('../assets/icon/iconBag.svg')" height="30" width="30" alt="bag"/>
      </div>
      <img class="top_header_icon" :src="require('../assets/icon/iconHeart.svg')" height="30" width="30" alt="heart"/>
      <img class="top_header_icon" :src="require('../assets/icon/iconUser.svg')" height="30" width="30" alt="user"/>
    </div>
<!--    <img class="top_header_icon top_header_menu" :src="require('../assets/icon/iconMenu.svg')" height="30px" width="30px" alt="menu"/>-->
  </div>
</div>
</div>
</template>

<script>
export default {
  name: "HeaderComponent",
  data() {
    return {
      price: 15550,
      a: null, b: null
    }
  },
  methods: {
    Sticky: function () {
      this.b = document.querySelector('.top_header');
      this.a = document.querySelector('.bottom_header');
      if(this.b.getBoundingClientRect().top >= -70)
      {
        this.a.classList.remove('sticky');
      }
      else if (this.a.getBoundingClientRect().top <= 0) { // elem.getBoundingClientRect() возвращает в px координаты элемента относительно верхнего левого угла области просмотра окна браузера
        this.a.classList.add('sticky');
      }
    },
  },
  created: function (){
    window.addEventListener('scroll', this.Sticky, false);
    document.body.addEventListener('scroll', this.Sticky, false);  // если у html и body высота равна 100%
  },
  destroyed: function () {
    window.addEventListener('scroll', this.Sticky, false);
    document.body.addEventListener('scroll', this.Sticky, false);  // если у html и body высота равна 100%
  }
}
</script>

<style scoped>

.header{
  padding: 1.7% 0 0;
  background-color: rgba(29, 29, 29, 1);
  color: rgba(248, 248, 248, 1);
}
/*Верхняя часть хедера*/
.top_header {
  min-height: 67px;
  display: flex;
  border-bottom: 1px solid rgba(248, 248, 248, 1);
  flex-direction: column;
  margin: 0 7%;
}
.top_header_main {
  height: 50%;
}
.top_header_icon, .bottom_header_icon {
  cursor: pointer;
  margin: 5px;
}
.main {
  display: flex;
  justify-content: space-between;
  /*height: 50%;*/
  align-items: center;
  width: 100%;
}
.contacts_social {
  display: flex;
  flex-grow: 1;
  align-items: center;
}
.top_header_contacts {
  display: flex;
  flex-direction: row;
  width: 33%;
  justify-content: space-between;
}

.contacts_phone {
  display: flex;
  align-items: center;
}
.contacts_text {
  font-size: 14px;
  font-weight: 500;
  margin-left: 5px;
  white-space: nowrap;
}
.social_networks {
  font-size: 12px;
  font-weight: 400;
  color: rgba(248, 248, 248, 1);
  text-decoration: none;
}
.social_networks:hover {
  color: #2b669a;
}

.social_networks_margin {
  margin: 0 10px;
}

.contacts_email {
  display: flex;
  align-items: center;
  margin-left: 10px
}

.bottom_header_functional {
  display: flex;
  align-items: center;
  width: 24%;
  justify-content: space-between;

}
.functional_bag {
  display: flex;
  align-items: center;
}
.functional_bag_price {
  font-weight: 500;
  margin-right: 5px;
  white-space: nowrap;
  min-width: 60px;
  max-width: 100px;
}
.top_header_logotype  {
  position: absolute;
  margin-top: -11px;
  left: 45%;
  display: flex;
  align-items: center;
}

.hidden{
  visibility: hidden;
}
/*Нижняя часть хедера*/

.bottom_header {
  padding: 0 7%;
  min-height: 73px;
  display: flex;
  align-items: center;
  align-content: center;
  z-index: 101;
  width: 86%;
  background-color: rgba(29, 29, 29, 1);;
  /*top: 93.5px;*/
}

.sticky{
  top: 0;
  position: fixed;
  z-index: 101;
}

.bottom_header_catalog {
  display: flex;
  align-items: center;
}
.top_header_nav {
  display: flex;
  width: 33%;
}
.nav_list {
  margin: 0;
  padding: 0;
  display: flex;
  justify-content: space-between;
  width: 100%;
}
.nav_element {
  list-style-type: none;
  display: flex;
  align-items: center;
}

.bottom_header_search {
  display: flex;
  border: none;
  align-items: center;
  width: 60%;
  border-radius: 11px;
  min-height: 29px;
  max-height: 35px;
  padding-left: 10px;
  margin-left: 10px;
  background-color: rgba(55, 55, 55, 1);
  /*box-sizing: border-box;*/
}
.search_input {
  border: none;
  width: 100%;
  margin: 0 5px;
  outline:none;
  background-color: rgba(55, 55, 55, 1);
  color: rgba(248, 248, 248, 1);
}
.search_button{
  background: #DFB259;
  border-radius: 11px;
  border: none;
  width: 55px; /*Исправить потом*/
  height: 29px;
  cursor: pointer;
}
/*noinspection CssNoGenericFontName*/
.catalog_title{
  font-family: Inter semiBold;
  margin-right: 10px;
  font-size: 23px;
  font-weight: 500;
}
/*noinspection CssNoGenericFontName*/
.nav_element_link{
  text-decoration: none;
  font-size: 15px;
  font-weight: 500;
  color: rgba(248, 248, 248, 1);
  font-family: Inter semiBold;
}
.nav_element_link:hover{
  color: #2b669a;
}
.bottom_header_wrapper{
  display: flex;
  justify-content: space-between;
  align-items: center;
  width: 50%;
}


/*Медиа запросы*/
/*@media screen and (max-width: 850px) {*/
/*  .contacts_email {*/
/*    display: none;*/
/*  }*/
/*  .bottom_header_functional {*/
/*    display: none;*/
/*  }*/
/*  .top_header_nav{*/
/*    display: none;*/
/*  }*/
/*  .top_header_menu {*/
/*    display: flex;*/
/*  }*/
/*  .contacts_phone {*/
/*    display: flex;*/
/*  }*/
/*  .bottom_header_wrapper{*/
/*    width: 100%;*/
/*  }*/
/*}*/
/*@media screen and (max-width: 400px) {*/
/*  .top_header_contacts {*/
/*    display: none;*/
/*  }*/
/*  .top_header_main {*/
/*    justify-content: flex-end;*/
/*  }*/
/*  .top_header_logotype {*/
/*    left: 7%;*/
/*  }*/
/*}*/

/*@media screen and (min-width: 850px) {*/
/*  .contacts_email {*/
/*    display: flex;*/
/*  }*/
/*  .bottom_header_functional {*/
/*    display: flex;*/
/*  }*/
/*  .top_header_menu {*/
/*    display: none;*/
/*  }*/
/*  .contacts_phone {*/
/*    display: flex;*/
/*  }*/

/*}*/

</style>