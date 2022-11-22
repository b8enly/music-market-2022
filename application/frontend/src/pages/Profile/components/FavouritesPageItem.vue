<template>
  <main class="favourites">
    <div class="favourites__first-row">
      <div class="favourites__sort sort">
        <p class="sort__text">Сортировка</p>
        <div class="sort__dropdown dropdown" @click="showSort(show)">
          <p class="sort__dropdown-title">
            {{ chosenSort }}
          </p>
          <img class="dropdown__image" :src="require('@/assets/icon/iconBtnDown2.svg')"/>
          <ul v-if="show == true" class="dropdown__list is-show">
            <li v-for="(item, index) in sort" :key="index" class="dropdown__item" @click="chooseSort(index)">
              {{ item }}
            </li>
          </ul>
          <ul v-else class="dropdown__list">
            <li v-for="(item, index) in sort" :key="index" class="dropdown__item">
              {{ item }}
            </li>
          </ul>
        </div>
      </div>
      <div class="favourites__available available">
        <p class="available__text">Только в наличии</p>
        <label class="available__switch switch">
          <input type="checkbox">
          <span class="available__slider slider"></span>
        </label>
      </div>
    </div>
    <div class="favourites__second-row">
      <catalog-item-component/>
      <catalog-item-component/>
      <catalog-item-component/>
      <catalog-item-component/>
      <catalog-item-component/>
    </div>
  </main>
</template>

<script>

import CatalogItemComponent from "@/components/CatalogItemComponent";

export default {
  name: "FavouritesPageItem",
  components: {CatalogItemComponent},
  data: () => ({
    show: false,
    sort: [
      "Первая сортировка",
      "Вторая сортировка",
      "Третья сортировка",
      "Четвертая сортировка",
    ],
    chosenSort: "Выберите сортировку",
  }),
  methods: {
    showSort(show) {
      if (show) {
        this.show = false;
      } else {
        this.show = true;
      }
    },
    chooseSort(index) {
      this.chosenSort = this.sort[index];
    }
  }
}
</script>

<style scoped>

.favourites {
  margin: 0;
}

.favourites__first-row {
  display: flex;
  flex-direction: row;
  margin-bottom: 20px;
}

.favourites__second-row {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
  grid-gap: 5px;
}

.favourites__sort {
  display: flex;
  flex-direction: row;
}

.favourites__available {
  display: flex;
  flex-direction: row;
}

.available__switch {
  align-self: center;
  margin-left: 20px;
}

.switch {
  position: relative;
  display: inline-block;
  width: 60px;
  height: 30px;
  border-radius: 6px;
}


.switch input {
  opacity: 0;
  width: 0;
  height: 0;
}


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
  height: 22px;
  width: 22px;
  left: 4px;
  bottom: 4px;
  background-color: white;
  -webkit-transition: .4s;
  transition: .4s;
  border-radius: 6px;
}

input:checked + .slider {
  background-color: #DFB259;
}

input:focus + .slider {
  box-shadow: 0 0 1px #DFB259;
}

input:checked + .slider:before {
  -webkit-transform: translateX(26px);
  -ms-transform: translateX(26px);
  transform: translateX(26px);
}

.favourites__sort {
  align-items: center;
}

.dropdown__list {
  display: none;
  position: absolute;
  top: 40px;
  left: 0;
  width: 100%;
  background: #FFFFFF;
  list-style: none;
  padding: 0;
}

.dropdown {
  display: flex;
  align-items: center;
  border: 1.3px solid #919191;
  border-radius: 10px;
  background: #FFFFFF;
  cursor: pointer;
  position: relative;
  width: 240px;
  justify-content: space-between;
  padding: 0 10px;
}

.dropdown__item {
  padding: 8px 15px;
}

.dropdown__item:hover {
  background: #919191;
}

.dropdown__image {
  margin: 0 0 0 5px;
}

.is-show {
  display: block;
}

.favourites__sort {
  margin-right: 5%;
}

.sort__text {
  margin-right: 20px;
}


</style>