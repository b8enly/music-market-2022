<template>
  <main class="item">
    <p class="item__name">Акустическая гитара BEST 21F</p>
    <p class="item__cost">17 850 ₽ — 1 шт.</p>
  </main>
</template>

<script>
export default {
  name: "CheckoutItemComponent"
}
</script>

<style scoped>

.item {
  margin: 0;
}

.item__cost {
  font-weight: 400;
  font-size: 14px;
  line-height: 17px;
  color: #797979;
}

</style>