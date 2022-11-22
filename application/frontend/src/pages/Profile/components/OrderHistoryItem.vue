<template>
  <main class="item">
    <div class="item__main-block main">
      <div class="item__first-row first">
        <div class="first__column">
          <p class="first__subtitle">Дата</p>
          <p class="first__text">12.12.2022</p>
        </div>
        <div class="first__column">
          <p class="first__subtitle">Номер заказа</p>
          <p class="first__text">14349-0332</p>
        </div>
        <div class="first__column">
          <p class="first__subtitle">Кол-во товаров</p>
          <p class="first__text">4 шт.</p>
        </div>
        <div class="first__column">
          <p class="first__subtitle">Сумма</p>
          <p class="first__text">17 590 ₽</p>
        </div>
        <div class="first__column">
          <p class="first__subtitle">Статус</p>
          <p class="first__text">Доставлено</p>
        </div>
        <div class="first__column">
          <button v-if="show === false" class="first__button" @click="showData(show)"></button>
          <button v-else class="first__button rotated" @click="showData(show)"></button>
        </div>
      </div>
      <transition name="fade">
        <order-history-data v-if="show === true"/>
      </transition>
    </div>
  </main>
</template>

<script>
import OrderHistoryData from "@/pages/Profile/components/OrderHistoryData";

export default {
  name: "OrderHistoryItem",
  components: {OrderHistoryData},
  data: () => ({
    show: false,
  }),
  methods:
      {
        showData(show) {
          if (show) {
            this.show = false;
          } else {
            this.show = true;
          }
        }
      }
}
</script>

<style scoped>

.item {
  margin-bottom: 5%;
  border: 1.3px solid #BCBCBC;
  border-radius: 28px;
}

.item__first-row {
  display: flex;
  flex-direction: row;
  column-gap: 3%;
}

.first__column {
  display: flex;
  flex-direction: column;
  justify-content: center;
  margin-right: 1%;
  margin-left: 3%;
  align-items: flex-start;
  padding-top: 2%;
  padding-bottom: 1%;
}

.first__subtitle {
  font-style: normal;
  font-weight: 400;
  font-size: 16px;
  line-height: 19px;
  color: #797979;
  margin: 1% 0 1% 0;
}

.first__button {
  background-image: url("../../../assets/icon/iconBtnDown.svg");
  background-color: transparent;
  height: 8px;
  width: 16px;
  border: none;
  transition: 500ms;
}

.rotated {
  transform: rotate(180deg);
  transition: 500ms;
}

.fade-enter-active, .fade-leave-active {
  transition: opacity .5s;
}
.fade-enter, .fade-leave-to /* .fade-leave-active до версии 2.1.8 */ {
  opacity: 0;
}

</style>