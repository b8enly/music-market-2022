<template>
  <!-- по id что передается через пропс router найти информацию о товаре-->
  <div class="product">
    <div class="product__path-wrapper">
      <span class="product__path" v-for="(path, index) in paths" :key="index"> {{ path }} /</span>
      <span class="product__path-last"> {{ product.name }} </span>
    </div>

    <section class="product__main">
      <!--    <p>{{$route.params.id}}</p>-->
      <div class="main__block container">
        <div class="main__first-column">
          <!-- через  colorArrow менять цвет стрелки в зависимости от есть ли еще картинки-->
          <button class="main__additional-btn">
            <img class="main__img-arrow"
                 :src="require(`../../assets/icon/${this.colorArrow}`)"
                 style="transform: rotate(-90deg);"
                 height="14"
                 width="25"
                 alt="guitar"/>
          </button>

          <div class="main__additional-block" @click="()=>{return this.currentImg = 'guitarAdditional1.png'}">
            <img class="main__additional-img" :src="require('../../assets/img/guitarAdditional1.png')" alt="guitar"/>
          </div>
          <div class="main__additional-block" @click="()=>{return this.currentImg = 'guitarAdditional2.png'}">
            <img class="main__additional-img" :src="require('../../assets/img/guitarAdditional2.png')" alt="guitar"/>
          </div>
          <div class="main__additional-block" @click="()=>{return this.currentImg = 'guitarAdditional3.png'}">
            <img class="main__additional-img" :src="require('../../assets/img/guitarAdditional3.png')" alt="guitar"/>
          </div>

          <button class="main__additional-btn">
            <img class="main__img-arrow"
                 :src="require(`../../assets/icon/${this.colorArrow}`)"
                 style="transform: rotate(90deg);"
                 height="14"
                 width="25"
                 alt="guitar"/>
          </button>
        </div>

        <div class="main__second-column">
          <div class="main__img-block">
            <img class="main__img" :src="require(`../../assets/img/${this.currentImg}`)" alt="img"/>
          </div>
        </div>

        <div class="main__third-column">
          <div class="main__header">
            <div class="main__tag">
              популярное
            </div>
            <span v-if="product.amount > 0" class="main__status">
              есть в наличии
            </span>
            <span v-else class="main__status main__status--none">
              нет в наличии
            </span>
          </div>

          <div class="main__title">{{ product.name }}</div>
          <div class="main__price">
            <span class="main__price-current"> {{ product.price }}&#8381;</span>
            <!--          <span class="main__price-old"> 22500 ₽ </span>-->
          </div>
          <!--          {{ chars }}-->
          <ul class="main__list" v-if="len > 9">
            <li v-for="(characteristic, index) in product.characteristics.slice(0, 8)"
                :key="index" class="main__list-elem">
              <span class="main__list-title">{{ characteristic.name }}</span>
              <span class="main__line-dotted"></span>
              <span class="main__list-info">{{ characteristic.info }}</span>
            </li>
          </ul>
          <ul class="main__list" v-else>
            <li v-for="(characteristic, index) in product.characteristics" :key="index" class="main__list-elem">
              <span class="main__list-title">{{ characteristic.name }}</span>
              <span class="main__line-dotted"></span>
              <span class="main__list-info">{{ characteristic.info }}</span>
            </li>
          </ul>
          <div class="main__link">
            <a href="#characteristic"
               class="main__link-feature"
               @click="()=>{return this.currentLink = 'Характеристики'}"
            >
              Все характеристики
              <img class="main__link-arrow" :src="require('../../assets/icon/iconArrowGold.svg')" alt="arrow"/>
            </a>
          </div>

          <div class="main__cart">
            <button class="main__cart-btn">
              В корзину
            </button>
          </div>
        </div>

      </div>
    </section>

    <section class="product__nav">
      <div class="nav__block container">
        <ul class="nav__list">
          <li class="nav__list-elem">
            <button class="nav__list-btn"
                    :class="{'active-btn': this.currentLink ==='Описание'}"
                    @click="()=>{return this.currentLink = 'Описание'}"
            >Описание
            </button>
          </li>
          <li class="nav__list-elem">
            <button class="nav__list-btn"
                    :class="{'active-btn': this.currentLink ==='Характеристики'}"
                    @click="()=>{return this.currentLink = 'Характеристики'}"
                    id="characteristic"
            >Характеристики
            </button>
          </li>
          <li class="nav__list-elem">
            <button class="nav__list-btn"
                    :class="{'active-btn': this.currentLink ==='Аксессуары'}"
                    @click="()=>{return this.currentLink = 'Аксессуары'}"
            >Аксессуары
            </button>
          </li>
          <li class="nav__list-elem">
            <button class="nav__list-btn"
                    :class="{'active-btn': this.currentLink ==='Инструкции'}"
                    @click="()=>{return this.currentLink = 'Инструкции'}"
            >Инструкции и документация
            </button>
          </li>
        </ul>


        <div class="nav__description wrapper" v-if="this.currentLink ==='Описание'">
          <div class="nav__first-column column">
            <span class="nav__description-title nav-title">О товаре</span>
          </div>
          <div class="nav__second-column column">
            <p class="nav__description-info">{{product.description}}</p>
          </div>
        </div>


        <div class="nav__characteristic wrapper" v-if="this.currentLink ==='Характеристики'">
          <div class="nav__first-column column">
            <span class="nav__characteristic-title nav-title">Характеристики</span>
          </div>
          <div class="nav__second-column column">
            <ul class="main__list">
              <li class="main__list-elem">
                <span class="main__list-title">бренд</span>
                <span class="main__line-dotted"></span>
                <span class="main__list-info">{{ product.brand.name }}</span>
              </li>

              <li class="main__list-elem">
                <span class="main__list-title">категория</span>
                <span class="main__line-dotted"></span>
                <span class="main__list-info">{{ product.category.name }}</span>
              </li>
              <li v-for="(characteristic, index) in product.characteristics" :key="index" class="main__list-elem">
                <span class="main__list-title">{{ characteristic.name }}</span>
                <span class="main__line-dotted"></span>
                <span class="main__list-info">{{ characteristic.info }}</span>
              </li>
              <!--          <li class="main__list-elem">-->
              <!--            <span class="main__list-title">конфигурация звукоснимателей</span>-->
              <!--            <span class="main__line-dotted"></span>-->
              <!--            <span class="main__list-info">Информация</span>-->
              <!--          </li>-->
              <!--          <li class="main__list-elem">-->
              <!--            <span class="main__list-title">форма</span>-->
              <!--            <span class="main__line-dotted"></span>-->
              <!--            <span class="main__list-info">Информация</span>-->
              <!--          </li>-->
              <!--          <li class="main__list-elem">-->
              <!--            <span class="main__list-title">тип корпуса</span>-->
              <!--            <span class="main__line-dotted"></span>-->
              <!--            <span class="main__list-info">Информация</span>-->
              <!--          </li>-->
              <!--          <li class="main__list-elem">-->
              <!--            <span class="main__list-title">количество струн</span>-->
              <!--            <span class="main__line-dotted"></span>-->
              <!--            <span class="main__list-info">Информация</span>-->
              <!--          </li>-->
              <!--          <li class="main__list-elem">-->
              <!--            <span class="main__list-title">верхняя дека </span>-->
              <!--            <span class="main__line-dotted"></span>-->
              <!--            <span class="main__list-info">Информация</span>-->
              <!--          </li>-->
              <!--          <li class="main__list-elem">-->
              <!--            <span class="main__list-title">задняя дека и обечайки </span>-->
              <!--            <span class="main__line-dotted"></span>-->
              <!--            <span class="main__list-info">Информация</span>-->
              <!--          </li>-->
              <!--          <li class="main__list-elem">-->
              <!--            <span class="main__list-title">материал грифа </span>-->
              <!--            <span class="main__line-dotted"></span>-->
              <!--            <span class="main__list-info">Информация</span>-->
              <!--          </li>-->
              <!--          <li class="main__list-elem">-->
              <!--            <span class="main__list-title">накладка</span>-->
              <!--            <span class="main__line-dotted"></span>-->
              <!--            <span class="main__list-info">Информация</span>-->
              <!--          </li>-->
              <!--          <li class="main__list-elem">-->
              <!--            <span class="main__list-title">сборка (страна) </span>-->
              <!--            <span class="main__line-dotted"></span>-->
              <!--            <span class="main__list-info">Информация</span>-->
              <!--          </li>-->
              <!--          <li class="main__list-elem">-->
              <!--            <span class="main__list-title">ширина грифа </span>-->
              <!--            <span class="main__line-dotted"></span>-->
              <!--            <span class="main__list-info">Информация</span>-->
              <!--          </li>-->
              <!--          <li class="main__list-elem">-->
              <!--            <span class="main__list-title">особенности </span>-->
              <!--            <span class="main__line-dotted"></span>-->
              <!--            <span class="main__list-info">Информация</span>-->
              <!--          </li>-->
              <!--          <li class="main__list-elem">-->
              <!--            <span class="main__list-title">крепление грифа </span>-->
              <!--            <span class="main__line-dotted"></span>-->
              <!--            <span class="main__list-info">Информация</span>-->
              <!--          </li>-->
              <!--          <li class="main__list-elem">-->
              <!--            <span class="main__list-title">мензура</span>-->
              <!--            <span class="main__line-dotted"></span>-->
              <!--            <span class="main__list-info">Информация</span>-->
              <!--          </li>-->
              <!--          <li class="main__list-elem">-->
              <!--            <span class="main__list-title">струнодержатель</span>-->
              <!--            <span class="main__line-dotted"></span>-->
              <!--            <span class="main__list-info">Информация</span>-->
              <!--          </li>-->
              <!--          <li class="main__list-elem">-->
              <!--            <span class="main__list-title">артикул</span>-->
              <!--            <span class="main__line-dotted"></span>-->
              <!--            <span class="main__list-info">Информация</span>-->
              <!--          </li>-->
            </ul>
          </div>

        </div>
        <div class="nav__instruction-block" v-if="this.currentLink ==='Инструкции'">
          <div class="nav__instruction wrapper">
            <div class="nav__first-column column">
              <span class="nav__instruction-title nav-title">Документация</span>
            </div>
            <div class="nav__second-column column">
              <ul class="nav__instruction-list">
                <li class="nav__instruction-elem">
                  <a href="#" class="nav__instruction-link">
                    <img :src="require('../../assets/icon/iconLoad.svg')" alt="load"
                         class="nav__instruction-icon"
                         height="20" width="20"/>
                    Название файла по документации.pdf
                  </a>
                </li>

                <li class="nav__instruction-elem">
                  <a href="#" class="nav__instruction-link">
                    <img :src="require('../../assets/icon/iconLoad.svg')" alt="load"
                         class="nav__instruction-icon"
                         height="20" width="20"/>
                    Название файла по документации.pdf
                  </a>
                </li>
                <li class="nav__instruction-elem">
                  <a href="#" class="nav__instruction-link">
                    <img :src="require('../../assets/icon/iconLoad.svg')" alt="load"
                         class="nav__instruction-icon"
                         height="20" width="20"/>
                    Название файла по документации.pdf
                  </a>
                </li>
              </ul>
            </div>
          </div>

          <div class="nav__instruction wrapper">
            <div class="nav__first-column column">
              <span class="nav__instruction-title nav-title">Сертификация</span>
            </div>
            <div class="nav__second-column column">
              <ul class="nav__instruction-list">
                <li class="nav__instruction-elem">
                  <a href="#" class="nav__instruction-link">
                    <img :src="require('../../assets/icon/iconLoad.svg')" alt="load"
                         class="nav__instruction-icon"
                         height="20" width="20"/>
                    Название файла по документации.pdf
                  </a>
                </li>
                <li class="nav__instruction-elem">
                  <a href="#" class="nav__instruction-link">
                    <img :src="require('../../assets/icon/iconLoad.svg')" alt="load"
                         class="nav__instruction-icon"
                         height="20" width="20"/>
                    Название файла по документации.pdf
                  </a>
                </li>
                <li class="nav__instruction-elem">
                  <a href="#" class="nav__instruction-link">
                    <img :src="require('../../assets/icon/iconLoad.svg')" alt="load"
                         class="nav__instruction-icon"
                         height="20" width="20"/>
                    Название файла по документации.pdf
                  </a>
                </li>
              </ul>
            </div>
          </div>
        </div>


        <!--        <div class="nav__accessory wrapper" v-if="this.currentLink ==='Аксессуары'">-->
        <!--          <div class="nav__first-column column">-->
        <!--            <span class="nav__accessory-title recommendation__title">Подборка аксессуаров</span>-->
        <!--          </div>-->

        <!--          <div class="nav__second-column column">-->
        <!--            <CatalogItemComponent />-->
        <!--            <CatalogItemComponent />-->
        <!--            <CatalogItemComponent />-->
        <!--             <CatalogItemComponent />-->
        <!--          </div>-->
        <!--        </div>-->

      </div>
    </section>

    <!--  <div class="product__recommendation wrapper">-->
    <!--    <div class="recommendation__first-column column">-->
    <!--      <span class="recommendation__title">Рекомендуем также</span>-->
    <!--    </div>-->

    <!--    <div class="recommendation__second-column column">-->
    <!--      <CatalogItemComponent />-->
    <!--      <CatalogItemComponent />-->
    <!--      <CatalogItemComponent />-->
    <!--      <CatalogItemComponent />-->
    <!--    </div>-->
    <!--  </div>-->

    <!--  <div class="product__recommendation product-wrapper">-->
    <!--    <div class="recommendation__first-column column">-->
    <!--      <span class="recommendation__title">Похожие товары</span>-->
    <!--    </div>-->

    <!--    <div class="recommendation__second-column column">-->
    <!--      <CatalogItemComponent />-->
    <!--      <CatalogItemComponent />-->
    <!--      <CatalogItemComponent />-->
    <!--      <CatalogItemComponent />-->
    <!--    </div>-->
    <!--  </div>-->


  </div>
</template>

<script>
// import CatalogItemComponent from "@/components/CatalogItemComponent";
import {mapActions, mapGetters} from "vuex";

export default {
  name: "ProductPage",
  data() {
    return {
      paths: ['Главная', 'Каталог', 'Акустические гитары'],
      colorArrow: 'iconArrowGrey.svg',
      currentImg: 'imgGuitar.png',
      currentLink: 'Описание',
      // chars: this.product.characteristics,
    }
  },
  methods: {
    ...mapActions(['LOAD_PRODUCT_BY_ID'])
  },
  mounted() {
    this.LOAD_PRODUCT_BY_ID(this.$route.params.id)
  },
  computed: {
    ...mapGetters({
      product: "CURRENT_PRODUCT",
      len: "CHARACTERISTICS_LENGTH"
    })
  },
  // components:{CatalogItemComponent}

}
</script>

<style scoped>
.product {
  margin: 2% 7% 2% 7%;
}

.product__path {
  color: rgba(184, 184, 184, 1);
  font-size: 17px;
}

.product__path-last {
  font-size: 17px;
  color: rgba(29, 29, 29, 1);
}

.container {
  display: flex;
  flex-wrap: wrap;
}

.main__block {
  margin: 80px 0;
  flex-direction: row;
}

.main__first-column {
  flex-direction: column;
  display: flex;
  align-items: center;
  margin: -10px 0;
}

.main__additional-img {
  margin: 10px 0;
}

.main__additional-img {
  min-height: 144px;
  min-width: 55px;
}

.main__additional-block {
  min-width: 170px;
  min-height: 182px;
  background: #FFFFFF;
  border-radius: 18px;
  display: flex;
  justify-content: center;
  align-items: center;
  margin: 10px 0;
  cursor: pointer;
}

.main__additional-btn {
  background: transparent;
  border: none;
  cursor: pointer;
  margin: 10px 0;
}

.main__img-block {
  min-width: 426px;
  min-height: 670px;
  background: #FFFFFF;
  border-radius: 21px;
  box-sizing: border-box;
  display: flex;
  justify-content: center;
  align-items: center;
  margin: 0 60px;
}

.main__additional-img {
  width: 55px;
  height: 144px;
}

.main__img {
  min-width: 220px;
  min-height: 578px;
}

.main__third-column {
  display: flex;
  flex-direction: column;
  flex: 1;
}

.main__header, .main__price {
  display: flex;
  flex-direction: row;
  flex-wrap: nowrap;
  align-items: center;
}

.main__list {
  margin: -5px 0 40px 0;
  padding: 0;
  width: 100%;
}

.main__list-elem {
  display: flex;
  justify-content: space-between;
  margin: 5px 0;
}

.main__line-dotted {
  flex: 1 0;
  border-bottom: 2px dotted rgba(167, 167, 167, 1);
  height: 1em;
  margin: 0 .4em;
}

.main__tag {
  border: 1px solid rgba(223, 178, 89, 1);
  color: rgba(223, 178, 89, 1);
  box-sizing: border-box;
  border-radius: 7px;
  font-weight: 500;
  font-size: 14px;
  padding: 6px 16px;
  margin-right: 25px;
}

.main__status {
  font-size: 14px;
  color: rgba(4, 200, 0, 1);

}

.main__title {
  font-weight: 600;
  font-size: 36px;
  margin: 20px 0 30px 0;
}

.main__price {
  display: flex;
  flex-direction: row;
  flex-wrap: nowrap;
  align-items: center;
  margin-bottom: 40px;
}

.main__price-current {
  font-weight: 700;
  font-size: 36px;
  color: rgba(223, 178, 89, 1);
}

.main__price-old {
  font-weight: 500;
  font-size: 24px;
  text-decoration-line: line-through;
  color: #B8B8B8;
  margin: 0 30px;
}

.main__list-title {
  font-weight: 600;
  font-size: 22px;
  color: #373737;
}

.main__list-info {
  font-weight: 400;
  font-size: 22px;
  color: #373737;
}

.main__link {
  display: flex;
  flex-direction: row;
  flex-wrap: nowrap;
  align-items: center;
  margin-bottom: 20px;
}

.main__link-feature {
  font-weight: 500;
  font-size: 25px;
  text-decoration: none;
  color: #DFB259;
}

.main__link-arrow {
  margin: 0 5px;
}

.main__cart-btn {
  min-width: 285px;
  min-height: 62px;
  background: radial-gradient(rgba(255, 226, 153, 0.5) 0%, rgba(255, 234, 182, 0) 100%), linear-gradient(98.73deg, #DFB259 28.23%, #EDB442 85.02%);
  /* блюр_кнопка */

  box-shadow: 0 0 21px rgba(255, 217, 142, 0.5);
  border-radius: 23px;
  font-weight: 600;
  font-size: 25px;
  color: #FFFFFF;
  border: none;
  box-sizing: border-box;
  cursor: pointer;
}

.main__cart {
  display: flex;
  align-items: flex-end;
  flex: 1 0;
}

.nav__block {
  flex-direction: column;
  margin: 80px 0;
}

.nav__list {
  display: flex;
  flex-direction: row;
  margin: 0 -50px 40px -50px;
  padding: 0;
  flex-wrap: wrap;
}

.nav__list-elem {
  list-style-type: none;
  margin: 10px 50px;
}

.nav__list-btn {
  padding: 6px 0;
  box-sizing: border-box;
  background: transparent;
  border: none;
  font-weight: 600;
  font-size: 25px;
  cursor: pointer;
}

.active-btn {
  color: #DFB259;
  border-bottom: 2px solid #DFB259;
}

.wrapper {
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  margin: 5px 0;
}

.column {
  display: flex;
  flex-direction: row;
  flex-wrap: nowrap;
  align-items: flex-start;
}

.nav__second-column {
  max-width: 86%;
  min-width: 80%;
}

.nav-title {
  white-space: nowrap;
  font-weight: 600;
  font-size: 22px;
  color: #1D1D1D;
  margin-right: 84px;
}

.recommendation__title {
  white-space: nowrap;
  font-weight: 600;
  font-size: 22px;
  color: #1D1D1D;
  margin-bottom: 15px;
}

.nav__description-info {
  margin: 0;
  font-weight: 400;
  font-size: 20px;
}

.nav__instruction-list {
  margin: -10px 0;
  padding: 0;
}

.nav__instruction-block {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}

.nav__instruction-link {
  text-decoration: none;
  color: black;
  font-weight: 400;
  font-size: 20px;
  align-items: center;
  display: flex;
}

.nav__instruction-elem {
  list-style-type: none;
  margin: 10px 0;
  align-items: center;
  display: flex;
  flex-direction: row;
}

.nav__instruction-icon {
  margin-right: 15px;
}

.product__recommendation {
  margin-bottom: 60px;
}

.main__status--none {
  color: red;
}
</style>