<template>
  <main class="data">
    <p class="data__title">Данные о заказе</p>
    <div class="data__first-row">
      <p class="data__subtitle name">Наименование</p>
      <p class="data__subtitle count">Количество</p>
      <p class="data__subtitle final">Итого</p>
    </div>
    <order-history-card />
    <order-history-card />
    <order-history-card />
  </main>
</template>

<script>
import OrderHistoryCard from "@/pages/Profile/components/OrderHistoryCard";
export default {
  name: "OrderHistoryData",
  components: {OrderHistoryCard}
}
</script>

<style scoped>

.data {
  margin-right: 30px;
  margin-left: 30px;
}

.data__title {
  font-weight: 500;
  font-size: 24px;
  line-height: 29px;
  color: #1D1D1D;
}

.data__first-row {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;

}

.data__subtitle {
  font-weight: 400;
  font-size: 16px;
  line-height: 19px;
  color: #797979;
}

.count {
  text-align: center;
}

.final {
  text-align: end;
  margin-right: 15px;
}

</style>