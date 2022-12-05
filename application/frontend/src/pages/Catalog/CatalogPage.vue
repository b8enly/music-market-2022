<template>
  <div class="catalog">

    <!--    верх каталога и фильтрация-->
    <div class="catalog__path-wrapper">
      <span class="catalog__path" v-for="(path, index) in paths" :key="index"> {{ path }} /</span>
      <span class="catalog__path-last"> {{ products.category.name }} </span>
    </div>

    <div class="catalog__title" @click="onTest()"> {{ products.category.name }} </div>
    <!--    {{$route.params.category}}-->

    <div class="catalog__tags"> <!-- теги потом будет вывод через цикл-->
      <button class="catalog__tags-btn">Классика</button>
      <button class="catalog__tags-btn">Эстрада</button>
      <button class="catalog__tags-btn">Для новичков</button>
    </div>

    <div class="catalog__filter">

      <div class="catalog__sort wrapper">
        <label class="catalog__label" for="sort">Сортировка</label>
        <select class="catalog__select" id="sort">
          <option class="catalog__select-item" value="Popular" selected>Популярное</option>
          <option class="catalog__select-item" value="Discounts">Скидки</option>
          <option class="catalog__select-item" value="New">Новое</option>
          <option class="catalog__select-item" value="Professional">Профи</option>
        </select>
      </div>

      <div class="catalog__price wrapper">
        <label class="catalog__label" for="price">Цена</label>
        <div class="catalog__price" id="price">
          <input class="catalog__price-item" type="text" placeholder="от"/>
          <input class="catalog__price-item" type="text" placeholder="до"/>
        </div>
      </div>

      <div class="catalog__brand wrapper">
        <label class="catalog__label" for="brand">
          Бренд
        </label>
        <div>
          <select class="catalog__select" id="brand">
            <option class="catalog__select-item" value="Fender" selected>Fender</option>
            <option class="catalog__select-item" value="Ibanez">Ibanez</option>
            <option class="catalog__select-item" value="Gibson">Gibson</option>
            <option class="catalog__select-item" value="Ovation">Ovation</option>
          </select>
        </div>
      </div>

      <div class="catalog__checkbox wrapper">

        <label class="catalog__label" for="checkbox"> Только в наличии</label>
        <label class="switch">
          <input type="checkbox" id="checkbox">
          <span class="slider"></span>
        </label>
      </div>
    </div>


    <!--      карточки-->

    <div class="catalog__card-wrapper">

            <CatalogItemComponent
                v-for="(product, index) in products.results"
                :key="index" :category="products.category" :product="product"
            />
<!--                v-bind:product_data="product"-->
    </div>


    <!--    пагинация-->

    <div class="catalog__page">
      <div class="catalog__page-prev" v-if="this.currentPage > 1">
        <span class="catalog__prev-btn" @click="()=>{return this.currentPage-=1}"><img class="catalog__page-img"
                                                                                       style="transform:rotateY(180deg)"
                                                                                       :src="require('../../assets/icon/iconArrowBlack.svg')"
                                                                                       alt="arrow"> Предыдущая страница </span>
        <span class="catalog__page-add"> ... </span>
      </div>

      <div class="catalog__page-wrapper">
        <input class="catalog__page-btn"
               type="button"
               :class="{'active': page===currentPage}"
               v-for="(page, index) in pages"
               :key="index"
               @click="nextPage(page)"
               :value="page"
        >
      </div>

      <div class="catalog__page-next" v-if="this.currentPage < this.pages">
        <span class="catalog__page-add"> ... </span>
        <span class="catalog__next-btn" @click="()=>{return this.currentPage+=1}"> Следующая страница <img
            class="catalog__page-img"
            :src="require('../../assets/icon/iconArrowBlack.svg')" alt="arrow"></span>
        <!-- переделать span на button?-->
      </div>
    </div>

  </div>

</template>

<script>

import CatalogItemComponent from "@/components/CatalogItemComponent";
import {mapActions, mapGetters} from "vuex";

export default {
  name: "CatalogPage",
  components: {CatalogItemComponent},

  data() {
    return {
      paths: ['Главная', 'Каталог'],
      pages: 3,
      currentPage: 1,
    }
  },
  mounted() {
    this.LOAD_CATEGORY(),
        this.LOAD_PRODUCTS_BY_CATEGORY({
          categoryId: this.$route.params.category,
          page: '1',
          pageSize: '20',
        }).then(() => {
        })
    // this.LOAD_PRODUCTS_BY_CATEGORY_NAME(this.$route.params.category
  },
  computed: {
    ...mapGetters({products: 'CATEGORY_PRODUCTS', category: 'CATEGORY'}
    ),
  },
  methods: {
    ...mapActions(['LOAD_PRODUCTS_BY_CATEGORY_NAME', 'LOAD_CATEGORY', 'LOAD_PRODUCTS_BY_CATEGORY']),
    nextPage: function (page) {
      return this.currentPage = page
    },
    onTest: function () {
      console.log(this.products.category.name);
    }
  }
}
</script>

<style scoped>
.catalog {
  margin: 2% 7% 2% 7%;
}

.catalog__path {
  color: rgba(184, 184, 184, 1);
  font-size: 17px;
}

.catalog__path-last {
  font-size: 17px;
  color: rgba(29, 29, 29, 1);
}

.catalog__title {
  color: rgba(223, 178, 89, 1);
  font-size: 38px;
  font-weight: 600;
  margin: 30px 0;
}

.catalog__tags {
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  margin: 0 -11px;
}

.catalog__tags-btn {
  background-color: rgba(228, 228, 228, 1);
  padding: 11px 64px;
  font-size: 18px;
  box-sizing: border-box;
  border: none;
  border-radius: 14px;
  margin: 3px 11px;
  cursor: pointer;
}

.catalog__filter {
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  margin: 40px -30px;
}

.catalog__select {
  font-size: 16px;
  font-weight: 600;
  min-width: 173px;
  min-height: 42px;
  box-sizing: border-box;
  border: 2px solid rgba(144, 144, 144, 1);
  border-radius: 10px;
  padding: 0 10px;
}

.catalog__price-item {
  max-width: 90px;
  min-height: 42px;
  box-sizing: border-box;
  border: 2px solid rgba(144, 144, 144, 1);
  border-radius: 10px;
  padding: 0 10px;
  margin: 0 5px;
}

.catalog__label {
  color: rgba(29, 29, 29, 1);
  font-size: 18px;
  margin: 0 10px;
}

.wrapper {
  display: flex;
  flex-direction: row;
  flex-wrap: nowrap;
  margin: 3px 30px;
  align-items: center;
}

.switch {
  position: relative;
  display: inline-block;
  width: 60px;
  height: 34px;
}

/* Hide default HTML checkbox */
.switch input {
  opacity: 0;
  width: 0;
  height: 0;
}

/* The slider */
.slider {
  position: absolute;
  cursor: pointer;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: #ccc;
  -webkit-transition: .4s;
  transition: .4s;
  border-radius: 6px;
}

.slider:before {
  position: absolute;
  content: "";
  height: 23px;
  width: 23px;
  left: 5px;
  bottom: 5px;
  background-color: white;
  -webkit-transition: .4s;
  transition: .4s;
  border-radius: 6px;
}

input:checked + .slider {
  background-color: rgba(223, 178, 89, 1);
}

input:focus + .slider {
  box-shadow: 0 0 1px #2196F3;
}

input:checked + .slider:before {
  -webkit-transform: translateX(26px);
  -ms-transform: translateX(26px);
  transform: translateX(26px);
}

/* Rounded sliders */
.slider.round {
  border-radius: 34px;
}

.slider.round:before {
  border-radius: 50%;
}

.catalog__card-wrapper {
  display: flex;
  flex-wrap: wrap;
  flex-direction: row;
  margin: 0 -5px;
}

.catalog__page {
  flex-wrap: wrap;
  display: flex;
  flex-direction: row;
  align-items: center;
  margin: 60px -5px;
}

.catalog__page-next, .catalog__page-wrapper, .catalog__page-prev {
  flex-wrap: nowrap;
  display: flex;
  flex-direction: row;
}


.catalog__page-btn {
  min-width: 41px;
  min-height: 38px;
  border: none;
  box-sizing: border-box;
  background-color: transparent;
  margin: 5px;
  font-size: 20px;
  cursor: pointer;
  text-align: center;
  outline: none
}

.active {
  background: #DFB259;
  color: #FFFFFF;
  border-radius: 6px;
  font-weight: 600;
}

.catalog__page-add {
  margin: 0 20px;
}

.catalog__page-img {
  margin: 0 5px;
}

.catalog__next-btn, .catalog__prev-btn {
  cursor: pointer;
}

</style>