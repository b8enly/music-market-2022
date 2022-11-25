<template>
  <main class="main">
    <section class="main__block">
      <div class="main__block container">
        <h1 class="main__title title">
          Гитары, которые<br>
          будут играть долго
        </h1>
        <p class="main__subtitle first-subtitle">
          Мы собрали для вас гитары разного класса, которые объединяет лишь одно — неизменно высокое качество.
        </p>
        <a class="main__catalog-btn" href="#catalog">
          <div class="main__background-btn"></div>
          В каталог
        </a>
        <div class="main__background-block"></div>
      </div>
    </section>
    <section class="main__items items">
      <div class="items__buttons">
        <button class="items__button sale">Скидки</button>
        <button class="items__button popular">Популярное</button>
        <button class="items__button news">Новые товары</button>
        <button class="items__button professional">Профессионалам</button>
      </div>
      <div class="items__products">
        <!--      Здесь должна быть карточка -->
        <CatalogItemComponent />
        <CatalogItemComponent />
        <CatalogItemComponent />
        <CatalogItemComponent />
      </div>
      <button class="items__show-more">Показать еще</button>
    </section>
    <section class="main__catalog catalog">
      <h2 class="catalog__title" id="catalog">Каталог</h2>
      <!--      Здесь должен быть каталог с картинками-->
      <div class="catalog__container">
        <div class="catalog__first-row">
          <div class="catalog__acoustic-card">
            <h4 class="catalog__acoustic-title">Акустические гитары</h4>
            <p class="catalog__acoustic-text">140 товаров</p>
          </div>
          <div class="catalog__electric-card">
            <h4 class="catalog__electric-title">Электрогитары</h4>
            <p class="catalog__electric-text">95 товаров</p>
          </div>
        </div>
        <div class="catalog__bass-card">
          <h4 class="catalog__bass-title">Бас-гитары</h4>
          <p class="catalog__bass-text">55 товаров</p>
        </div>
        <div class="catalog__acs-card">
          <h4 class="catalog__acs-title">Аксессуары <br>и комплектующие</h4>
          <p class="catalog__acs-text">210 товаров</p>
        </div>
        <div class="catalog__proc-card">
          <h4 class="catalog__proc-title">Процессоры <br>и педали эффектов</h4>
          <p class="catalog__proc-text">30 товаров</p>
        </div>
      </div>
    </section>
    <section class="main__actions actions">
      <!--      Это блок акций, но я случайно в запаре записала его как actions-->
      <div class="actions__container">
        <div class="actions__first">
          <h3 class="actions__first-title">Невероятное уникальное рекламное предложение</h3>
          <button class="actions__first-button">
            <div class="actions__background-btn"></div>
            Повестись на акцию
          </button>
          <div class="actions__background-block actions__background-block--first"></div>
        </div>
        <div class="actions__down-block">
          <div class="actions__second">
            <h3 class="actions__second-title">Оплати 2, получи 3!</h3>
            <p class="actions__second-sub">При покупке трех позиций из категории “Аксессуары” можно оплатить только
              две.</p>
            <button class="actions__down-button">
              К акссесуарам &#8594;
            </button>
            <div class="actions__background-block actions__background-block--second"></div>
          </div>
          <div class="actions__third">
            <h3 class="actions__third-title">Бесплатная доставка</h3>
            <p class="actions__third-sub">При заказе на сумму от 1500 рублей мы осуществляем доставку за наш счет.</p>
            <button class="actions__down-button">
              В каталог &#8594;
            </button>
            <div class="actions__background-block actions__background-block--third"></div>
          </div>
        </div>
      </div>
    </section>
    <section class="main__brands brands">
      <!--      Это блок с брэндами-->
      <div class="brands__container">
        <div class="brands__first-row">
          <h2 class="brands__title">Бренды</h2>
          <button class="brands__btn">Смотреть все &#8594;</button>
        </div>
        <div class="brands__second-row">
          <img class="brands__image"
               :src="Ibanez"
               alt="Ibanez"
          />
          <img class="brands__image"
               :src="Fender"
               alt="Fender"
          />
          <img class="brands__image"
               :src="Marshall"
               alt="Marshall"
          />
          <img class="brands__image"
               :src="Gibson"
               alt="Gibson"
          />
        </div>
        <div class="brands__third-row">
          <img class="brands__image"
               :src="Framus"
               alt="Framus"
          />
          <img class="brands__image"
               :src="Ovation"
               alt="Ovation"
          />
          <img class="brands__image"
               :src="Sharvel"
               alt="Sharvel"
          />
          <img class="brands__image"
               :src="Sigma"
               alt="Sigma"
          />
        </div>
      </div>
    </section>
    <section class="main__description description">
      <img class="description__image"
           :src="BackgroundImage"
           alt="BackgroundImage"
      />
      <div class="description__block">
        <h5 class="description__title">BuyGuitar <span id="color">
          — это любовь к гитарам и своему делу!</span>
        </h5>
        <p class="description__subtitle">Каждая из этих моделей имеет уникальную форму корпуса и свой индивидуальный
          тон.
          Важность этих моделей состоит еще и в том, что они настолько повлияли на рок-музыку в целом, что их названия
          стали именами нарицательными. Например, в музыкальном магазине вам может попасться гитара, произведенная
          компанией Yamaha, форма которой точно соответствует форме Stratocaster, или гитара компании Ibanez с
          дизайном Gibson ES-355.
        </p>
        <button class="description__button">
          <div class="description__background-btn"></div>
          Узнать больше
        </button>
      </div>
      <div class="description__background-light"></div>
    </section>
    <section class="main__feedback feedback">
      <div class="feedback__first-row">
      <h2 class="feedback__title">О нас пишут...</h2>
      <button class="feedback__btn">Смотреть все &#8594;</button>
      <!--      Здесь должна быть карточка -->
      </div>
      <div  class="feedback__second-row">
      <ReviewItemComponent />
      <ReviewItemComponent />
      <ReviewItemComponent />
      </div>
    </section>
  </main>
</template>

<script>

import AcousticGuitar from "../../assets/img/acguitar.jpg"
import ElectricGuitar from "../../assets/img/elguitar.jpg"
import BassGuitar from "../../assets/img/bass.jpg"
import Accessories from "../../assets/img/acs.jpg"
import Processors from "../../assets/img/proc.jpg"
import Fender from "../../assets/img/fender.png"
import Framus from "../../assets/img/framus.png"
import Gibson from "../../assets/img/gibson.png"
import Marshall from "../../assets/img/marshall.png"
import Ovation from "../../assets/img/ovation.png"
import Sharvel from "../../assets/img/sharvel.png"
import Sigma from "../../assets/img/sigma.png"
import Ibanez from "../../assets/img/ibanez.png"
import BackgroundImage from "../../assets/img/backgroundmain.png"
import CatalogItemComponent from "@/components/CatalogItemComponent";
import ReviewItemComponent from "@/components/ReviewItemComponent";

export default {
  name: "MainPage",
  components: {ReviewItemComponent, CatalogItemComponent},
  data: () => ({
    AcousticGuitar: AcousticGuitar,
    ElectricGuitar: ElectricGuitar,
    BassGuitar: BassGuitar,
    Accessories: Accessories,
    Processors: Processors,
    Fender: Fender,
    Framus: Framus,
    Gibson: Gibson,
    Marshall: Marshall,
    Ovation: Ovation,
    Sharvel: Sharvel,
    Sigma: Sigma,
    Ibanez: Ibanez,
    BackgroundImage: BackgroundImage,
  }),
};
</script>

<style scoped>
/*в целом, зачем нужен здесь scoped? мы не используем ни БЭМ, ни scss*/


.main__block {
  position: relative;
  background: #1D1D1D;
  overflow: hidden;
  width: auto;
  height: 650px;
  /*height: auto;*/
}

.main__background-block {
  width: 165px;
  height: 165px;
  position: absolute;
  right: 21%;
  bottom: 35%;
  background: rgba(255, 217, 142, 0.5);
  filter: blur(120px);
}

.container {
  margin: 0 0 0 5%;
}

.title {
  padding: 4% 0 2.5% 2%;
  text-align: left;
  justify-content: left;
}

.main__catalog-btn {
  position: relative;
  margin-left: 2%;
  background: linear-gradient(98.73deg, #DFB259 28.23%, #EDB442 85.02%), radial-gradient(106.43% 423.1% at 72.36% 34.29%, rgba(255, 226, 153, 0.5) 0%, rgba(255, 234, 182, 0) 100%);
  border-radius: 23px;
  /*width: 270px;*/
  /*height: 65px;*/
  color: #FFFFFF;
  font-size: 25px;
  font-weight: 600;
  z-index: 0;
  padding: 18px 75px;
  text-decoration: none;
}

.main__background-btn {
  border-radius: 23px;
  border-color: rgba(255, 217, 142, 0.5);
  position: absolute;
  width: 270px;
  height: 65px;
  bottom: 0;
  left: 0;
  background: rgba(255, 217, 142, 0.5);
  overflow: hidden;
  filter: blur(10px);
  z-index: -1;
}

.first-subtitle {
  width: 712px;
  height: 60px;
  color: #F8F8F8;
  font-size: 25px;
  margin: 0 0 0 0;
  padding: 0 0 5.5% 2%;
}

.items {
  margin: 5%;
}

.main__items {
  width: auto;
  height: auto;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.items__buttons {
  /*надо будет здесь поменять на % вместо px*/
  display: flex;
  flex-direction: row;
  justify-content: space-between;
}

.items__button {
  border: none;
  background: #F5F5F5;
  font-weight: 500;
  font-size: 25px;
  padding: 0 30px 5% 30px;
  /*нужно поправить, тут какая-то хуйня с расположением кнопок, то ли align-items неверный, то ли что*/
  color: #1D1D1D;
}

.items__button:hover {
  color: #DFB259;
  text-decoration-line: underline;
}

.items__button:active {
  color: #DFB259;
  text-decoration-line: underline;
}
.items__products{
  display: flex;
  justify-content: space-between;
  flex-wrap: wrap;
  flex-direction: row;
  width: 100%;
  margin: 0 -5px 55px -5px;
}
.items__show-more {
  width: 300px;
  height: 65px;
  background: #1D1D1D;
  border-radius: 23px;
  color: #FFFFFF;
  font-size: 25px;
  font-weight: 600;
}

.catalog {
  margin: 0 0 0 6%;
}

.actions__container {
  align-items: center;
  justify-content: center;
  margin: 5%;

}

.actions__first {
  background: #1D1D1D;
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
  padding: 3%;
  border-radius: 25px;
  /*z-index: -1;*/
  overflow: hidden;
  position: relative;
}

.actions__first-title {
  color: #DFB259;
  font-weight: 700;
  font-size: 32px;
  line-height: 39px;
}

.actions__first-button {
  position: relative;
  margin-left: 2%;
  background: linear-gradient(98.73deg, #DFB259 28.23%, #EDB442 85.02%), radial-gradient(106.43% 423.1% at 72.36% 34.29%, rgba(255, 226, 153, 0.5) 0%, rgba(255, 234, 182, 0) 100%);
  border-radius: 23px;
  width: 350px;
  height: 65px;
  font-weight: 600;
  font-size: 25px;
  line-height: 30px;
  color: #FFFFFF;
  z-index: 0;
}

.actions__background-btn {
  border-radius: 23px;
  border-color: rgba(255, 217, 142, 0.5);
  position: absolute;
  width: 350px;
  height: 65px;
  bottom: 0;
  left: 0;
  background: rgba(255, 217, 142, 0.5);
  overflow: hidden;
  filter: blur(10px);
  z-index: -1;
}

.actions__down-block {
  display: flex;
  gap: 10px;
  margin: 5% 0 5% 0;
}

.actions__second {
  grid-area: s;
  background: #1D1D1D;
  border-radius: 25px;
  padding: 5%;
  overflow: hidden;
  position: relative;
}

.actions__third {
  grid-area: t;
  background: #1D1D1D;
  border-radius: 25px;
  padding: 5%;
  overflow: hidden;
  position: relative;
}

.actions__second-title {
  color: #DFB259;
  font-weight: 700;
  font-size: 32px;
  line-height: 39px;
}

.actions__second-sub {
  font-weight: 400;
  font-size: 20px;
  line-height: 24px;
  color: #FFFFFF;
}

.actions__third-title {
  color: #DFB259;
  font-weight: 700;
  font-size: 32px;
  line-height: 39px;
}

.actions__third-sub {
  font-weight: 400;
  font-size: 20px;
  line-height: 24px;
  color: #FFFFFF;
}

.actions__down-button {
  font-weight: 500;
  font-size: 20px;
  line-height: 24px;
  color: #DFB259;
  background: none;
  border: none;
}

.actions__down-button:hover {
  text-decoration-line: underline;
}

.actions__background-block {
  width: 50px;
  height: 150%;
  /* background: none; */
  position: absolute;
  background: rgba(255, 217, 142, 0.5);
  filter: blur(80px);
  /*transform: rotate(45deg);*/
  /* top: 13%; */
  /* right: 42.1%; */
  /*z-index: 10*/
}

.actions__background-block--first {
  transform: rotate(-45deg);
}

.actions__background-block--second {
  transform: rotate(-45deg);
  top: -40%;
  right: 30%;
  /*height: 400px;*/
}

.actions__background-block--third {
  transform: rotate(45deg);
  top: -40%;
  right: 45%;
  /*height: 400px;*/
}

.catalog__title {
  margin-bottom: 3%;
}

.catalog__container {
  display: grid;
  grid-gap: 20px;
  margin-right: 5%;
  grid-template-rows: 415px 415px;
  grid-template-areas:
      "row row row"
      "b acs pr";
}

.catalog__first-row {
  grid-area: row;
  width: 100%;
  display: flex;
  align-items: center;
  height: 100%;
  gap: 20px;
}

.catalog__acoustic-card {
  border-radius: 30px;
  background: #FFFFFF url("../../assets/img/acguitar.jpg") 0 0 / cover no-repeat;
  height: 100%;
  flex-basis: 55%;
}

.catalog__acoustic-title {
  margin-left: 40px;
  margin-top: 40px;
  margin-bottom: 0;
  font-weight: 500;
  font-size: 30px;
  color: #1D1D1D;
}

.catalog__acoustic-text {
  margin-left: 40px;
  margin-top: 15px;
  font-weight: 500;
  font-size: 20px;
  color: #5C5C5C;
}

/*.catalog__acoustic-img {*/
/*  max-width: 650px;*/
/*  border-radius: 30px;*/
/*}*/

.catalog__electric-card {
  border-radius: 30px;
  background: #FFFFFF url("../../assets/img/elguitar.jpg") 0 0 / cover no-repeat;
  height: 100%;
  flex-basis: 45%;

}

.catalog__electric-title {
  margin-left: 40px;
  margin-top: 40px;
  margin-bottom: 0;
  font-weight: 500;
  font-size: 30px;
  color: #1D1D1D;
}

.catalog__electric-text {

  margin-left: 40px;
  margin-top: 15px;
  font-weight: 500;
  font-size: 20px;
  color: #5C5C5C;
}

/*.catalog__electric-img {*/
/*  max-width: 420px;*/
/*  border-radius: 30px;*/
/*}*/

.catalog__bass-card {
  border-radius: 30px;
  background: #FFFFFF url("../../assets/img/bass.jpg") 0 0 / cover no-repeat;
  width: 100%;
  grid-area: b;
}

.catalog__bass-title {
  margin-left: 40px;
  margin-top: 40px;
  margin-bottom: 0;
  font-weight: 500;
  font-size: 30px;
  color: #1D1D1D;
}

.catalog__bass-text {
  margin-left: 40px;
  margin-top: 15px;
  font-weight: 500;
  font-size: 20px;
  color: #5C5C5C;
}


.catalog__acs-card {
  background: #FFFFFF url("../../assets/img/acs.jpg") center 90% / 50% no-repeat;
  border-radius: 30px;
  grid-area: acs;
  width: 100%;
}

.catalog__acs-title {
  margin-left: 40px;
  margin-top: 40px;
  margin-bottom: 0;
  font-weight: 500;
  font-size: 30px;
  color: #1D1D1D;
}

.catalog__acs-text {
  margin-left: 40px;
  margin-top: 15px;
  font-weight: 500;
  font-size: 20px;
  color: #5C5C5C;
}

.catalog__proc-card {
  border-radius: 30px;
  background: #FFFFFF url("../../assets/img/proc.jpg") center 95% / 70% no-repeat;
  width: 100%;
  grid-area: pr;
}

.catalog__proc-title {
  margin-left: 40px;
  margin-top: 40px;
  margin-bottom: 0;
  font-weight: 500;
  font-size: 30px;
  color: #1D1D1D;
}

.catalog__proc-text {
  margin-top: 15px;
  margin-left: 40px;
  font-weight: 500;
  font-size: 20px;
  color: #5C5C5C;
}

.brands__container {
  margin: 5%;
}

.brands__first-row {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
}

.brands__title {
  margin-bottom: 40px;
}

.brands__btn {
  background: none;
  border: none;
  font-weight: 500;
  font-size: 25px;
  color: #1D1D1D;
  align-content: flex-end;
}

.brands__btn:hover {
  text-decoration-line: underline;
}

.brands__image {
  margin: 0 25px 30px 0;
  max-width: 300px;
}

.description {
  background: #1D1D1D;
  display: flex;
  flex-direction: row;
  position: relative;
  overflow: hidden;
}

.description__background-light {
  width: 165px;
  height: 165px;
  position: absolute;
  right: 20%;
  bottom: 65%;
  background: rgba(255, 217, 142, 0.5);
  filter: blur(120px);
}

.description__image {
  width: 45%;
}

.description__title {
  margin: 5% 29% 5% 5%;
  font-family: "Inter regular";
}

.description__subtitle {
  margin: 0 20% 8% 5%;
  font-family: "Inter regular";
  font-style: normal;
  font-weight: 300;
  font-size: 22px;
  line-height: 27px;
  color: #F8F8F8;
}

#color {
  color: #FFFFFF !important;
  background: none;
  -webkit-text-fill-color: unset;
  background-clip: border-box;
}

.description__button {
  margin-bottom: 6%;
  margin-left: 5%;
  border: none;
  position: relative;
  background: linear-gradient(98.73deg, #DFB259 28.23%, #EDB442 85.02%), radial-gradient(106.43% 423.1% at 72.36% 34.29%, rgba(255, 226, 153, 0.5) 0%, rgba(255, 234, 182, 0) 100%);
  border-radius: 23px;
  width: 350px;
  height: 65px;
  font-weight: 600;
  font-size: 25px;
  line-height: 30px;
  color: #FFFFFF;
  z-index: 0;
}

.description__background-btn {
  border-radius: 23px;
  border-color: rgba(255, 217, 142, 0.5);
  position: absolute;
  width: 350px;
  height: 65px;
  bottom: 0;
  left: 0;
  background: rgba(255, 217, 142, 0.5);
  overflow: hidden;
  filter: blur(10px);
  z-index: -1;
}

.feedback {
  margin: 5%;
}


.feedback__btn {
  background: none;
  border: none;
  font-weight: 500;
  font-size: 25px;
  color: #1D1D1D;
  align-content: flex-end;
}

.feedback__btn:hover {
  text-decoration-line: underline;
}
.feedback__first-row{
  display: flex;
  flex-direction: row;
  justify-content: space-between;
}
.feedback__second-row{
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  padding: 50px 0 20px 0;
  margin: 0 -5px 0 -5px;
  flex-wrap: wrap;
}
</style>