<template>
<footer class="footer">
  <div class="footer__col col-3">
    <img class="footer__img" :src="require('../assets/icon/iconLogo.svg')" height="50" width="163" alt="logo"/>
    <span class="footer__label_logo">Ваши лучшие гитары</span>
  </div>
  <div class="footer__col col-3">
    <ul class="footer__list">
      <li class="footer__elem">
        <a class="footer__link" href="#">Каталог</a>
      </li>
      <li class="footer__elem">
        <a class="footer__link"  href="#">Акции</a>
      </li>
      <li class="footer__elem">
        <a class="footer__link"  href="#">Гарантии</a>
      </li>
    </ul>
    <span class="footer__label_guarantee">Политика конфиденциальности</span>
  </div>
  <div class="footer__col col-3">
    <ul class="footer__list">
      <li class="footer__elem">
        <a class="footer__link"  href="#">Доставка</a>
      </li>
      <li class="footer__elem">
        <a class="footer__link"  href="#">Способы оплаты</a>
      </li>
      <li class="footer__elem">
        <a class="footer__link"  href="#">Контакты</a>
      </li>
    </ul>
  </div>
  <div class="footer__col col-4">

    <label for="subscription" class="footer__label_input">Подпишитесь, чтобы получать уведомления
        о скидках, акциях и новых предложениях! </label>
    <div class="footer__subscription">
      <img :src="require('../assets/icon/iconSearch.svg')" height="15" width="15" alt="subscription"/>
      <input class="footer__input" placeholder="email..." id="subscription"/>
      <button class="footer__button"> <img :src="require('../assets/icon/iconArrow.svg')" alt="arrow" width="24" height="14"> </button>
    </div>
  </div>
</footer>
</template>

<script>
export default {
  name: "FooterComponent.vue"
}
</script>

<style scoped>
.footer{
  display: flex;
  flex-direction: row;
  padding: 4% 7% 0 7%;
  color: rgba(248, 248, 248, 1);
  max-height: 272px;
  min-height: 250px;
  background-color: rgba(29, 29, 29, 1);
  justify-content: space-between;
  box-sizing: border-box;
}
.footer__col{
  display: flex;
  flex-direction: column;
  align-items: flex-start;
}
.footer__elem{
  list-style-type: none;
  margin: 20px;
  font-size: 18px;
}
.footer__list{
  text-align: left;
  padding-left: 0;
  margin: -20px 0 0 0;
}
.footer__subscription{
  display: flex;
  border: none;
  align-items: center;
  border-radius: 11px;
  width: 100%;
  box-sizing: border-box;
  min-height: 29px;
  max-height: 30px;
  padding-left: 10px;
  background-color: rgba(55, 55, 55, 1);
}

.footer__input{
  border: none;
  width: 100%;
  margin: 0 5px;
  outline:none;
  background-color: rgba(55, 55, 55, 1);
  color: rgba(248, 248, 248, 1);
}
.footer__button{
  background: #DFB259;
  border-radius: 11px;
  border: none;
  width: 65px; /*Исправить потом*/
  height: 29px;
  cursor: pointer;

}
.footer__label_guarantee{
  margin-top: -10px;
  margin-left: 20px;
  font-size: 12px;
  color: rgba(181, 181, 181, 1);
}
.footer__label_logo{
  font-size: 15px;
}
.footer__label_input{
  text-align: left;
  margin: 10px 0 24px 0;
}
.footer__img{
  margin: 10px 0;
}
.footer__link{
  text-decoration: none;
  color: rgba(248, 248, 248, 1);
}
.col-3{
  max-width: 315px;
}
.col-4{
  max-width: 360px;
}

</style>