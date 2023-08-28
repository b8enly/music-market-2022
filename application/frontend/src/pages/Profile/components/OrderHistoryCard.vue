<template>
  <div class="card">
    <div class="card__block">
      <div class="card__image">
        <img class="card__picture" :src="require('@/assets/img/guitarexample.jpg')" alt="guitarExample">
      </div>
      <div class="card__named named">
        <p class="first__title">Акустическая гитара BEST 21F</p>
        <p class="first__subtitle">Артикул A097575</p>
      </div>
    </div>
    <p class="card__value">1 шт.</p>
    <p class="card__price">19 700 ₽</p>
  </div>
</template>

<script>
export default {
  name: "OrderHistoryCard"
}
</script>

<style scoped>

.card {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
  margin-bottom: 20px;
  align-items: center;
}

.card__block {
  display: flex;
  align-items: center;
  justify-content: center;
}

.card__image {
  width: 80px;
  height: 85px;
  background: #FFFFFF;
  border-radius: 23px;
  display: flex;
  align-items: center;
  justify-content: center;
  margin-right: 3%;
}

.card__picture {
  width: 22px;
  height: 65px;
}

.first__subtitle {
  font-weight: 400;
  font-size: 14px;
  line-height: 17px;
  color: #797979;
}

.card__value {
  text-align: center;
}

.card__price {
  text-align: end;
  margin-right: 15px;
}

</style>