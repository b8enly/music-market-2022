<template>
  <main class="history">
    <p class="history__title">История заказов</p>
    <order-history-item />
    <order-history-item />
    <order-history-item />
  </main>
</template>

<script>
import OrderHistoryItem from "@/pages/Profile/components/OrderHistoryItem";
export default {
  name: "OrderHistory",
  components: {OrderHistoryItem}
}
</script>

<style scoped>
.history {
  background: #FFFFFF;
  border-radius: 26px;
  padding: 1% 3% 1% 3%;
  margin-bottom: 50px;
}

.history__title {
  font-weight: 500;
  font-size: 24px;
  line-height: 29px;
  color: #1D1D1D;
}

</style>