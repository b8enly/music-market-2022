<template>
  <main class="card">
    <div class="card__image">
      <img class="card__picture" :src="require('../assets/img/guitarexample.jpg')" alt="guitarExample">
    </div>
    <section class="card__first-block first">
      <p class="first__title">Акустическая гитара BEST 21F</p>
      <p class="first__subtitle">Артикул A097575</p>
      <button class="first__fav"><img class="first_favorite-icon" :src="require('../assets/icon/iconHeartBlack.svg')" alt="favorite" height="15" width="15"/> В избранное</button>
      <button class="first__delete"><img class="first__delete-icon" :src="require('../assets/icon/iconDelete.svg')" alt="delete" height="9.5" width="9.5"/> Удалить</button>
    </section>
    <section class="card__second-block second">
      <button class="second__button" id="minus" @click="minusItem" >-</button>
      <p class="second__amount" id="count"> {{ $store.state.main.count }}</p>
      <button class="second__button" id="plus" @click="plusItem">+</button>
    </section>
    <section class="card__third-block third">
      <p class="third__price-new">19 700 ₽</p>
      <p class="third__price-old">22 500 ₽</p>
    </section>
  </main>
</template>

<script>
export default {
  name: "ShoppingCartComponent",
  data() {
    return {

    }
  },
  methods: {
    minusItem() {
      if (this.$store.state.main.count > 1) {
        this.$store.state.main.count--;
      }
    },
    plusItem() {
      this.$store.state.main.count++;
    },
  },
}
</script>

<style scoped>

.card {
  display: flex;
  flex-direction: row;
  align-items: center;
  margin-bottom: 5%;
  /*width: 800px;*/
}

.card__image {
  width: 150px;
  height: 150px;
  background: #FFFFFF;
  border-radius: 23px;
  display: flex;
  align-items: center;
  justify-content: center;
  margin-right: 3%;
}

.card__picture {
  max-width: 42px;
  max-height: 113px;
}

.card__first-block {
  display: grid;
  grid-template-areas: "title title"
                        "subtitle ."
                        "fav del";
  margin-right: 5%;
  grid-column-gap: 1%;
}

.first__title {
  grid-area: title;
  font-size: 16px;
  line-height: 19px;
  color: #1D1D1D;
  margin-bottom: 5px;
}

.first__subtitle {
  grid-area: subtitle;
  font-size: 14px;
  line-height: 17px;
  color: #797979;
  margin-bottom: 50px;
}

.first__fav {
  grid-area: fav;
  display: flex;
  flex-direction: row;
  align-items: center;
  /*justify-content: center;*/
  padding-right: 5%;
  font-size: 14px;
  color: #1D1D1D;
  border: none;
  background: none;
  margin-bottom: 10px;
}

.first__fav:hover {
  color: #DFB259;
}

.first_favorite-icon{
  padding-right: 5%;
  padding-left: 0;
  margin: 0;
}

.first__delete {
  grid-area: del;
  font-size: 14px;
  color: #1D1D1D;
  border: none;
  background: none;
  margin-bottom: 10px;
}

.first__delete:hover {
  color: #DFB259;
}

.first__delete-icon {
  padding-right: 5%;
}

.card__second-block {
  display: flex;
  flex-direction: row;
  margin-right: 5%;
  align-items: center;
  justify-content: center;
}

.second__amount {
  margin: 0 25px 0 25px;
  font-size: 28px;
  color: #1D1D1D;
}

.second__button:enabled {
  background: none;
  border: 1.5px solid #DFB259;
  border-radius: 8.5px;
  width: 38px;
  height: 38px;
  font-size: 29px;
  color: #DFB259;
}

.second__button:disabled {
  border-radius: 8.5px;
  width: 38px;
  height: 38px;
  border: 1.5px solid #B8B8B8;
  font-size: 29px;
  color: #B8B8B8;
}

.card__third-block {
  display: flex;
  flex-direction: column;
  align-content: flex-start;
}

.third__price-new {
  font-size: 28px;
  color: #1D1D1D;
  margin: 0;
}

.third__price-old {
  font-size: 18px;
  text-decoration-line: line-through;
  color: #B8B8B8;
  align-self: flex-end;
}

</style>