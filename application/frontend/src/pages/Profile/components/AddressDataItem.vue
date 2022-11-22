<template>
  <main class="data">
    <div class="data__first-row">
      <h3 class="data__title">Адрес доставки</h3>
      <button class="data__button btn-edit">Редактировать</button>
    </div>
    <div class="data__block">
      <div class="data__row">
        <p class="data__subtitle-first">
          Регион:
        </p>
        <p class="data__first-value">
          Московская область
        </p>
        <p class="data__subtitle-second">
          Улица, дом
        </p>
        <p class="data__second-value">
          ул. Ленина, 45
        </p>
      </div>
      <div class="data__row">
        <p class="data__subtitle-first">
          Город:
        </p>
        <p class="data__first-value">
          Москва
        </p>
        <p class="data__subtitle-second">
          Квартира:
        </p>
        <p class="data__second-value">
          45 кв.
        </p>
      </div>
    </div>
  </main>
</template>

<script>
export default {
  name: "AddressDataItem"
}
</script>

<style scoped>

.data {
  background: #FFFFFF;
  border-radius: 26px;
  padding: 5% 5% 2% 5%;
  margin-top: 0;
  margin-bottom: 3%;
}

.data__first-row {
  display: flex;
  flex-direction: row;
}

.data__title {
  margin: 0 3% 3% 0;
}

.data__row {
  display: flex;
}

.data__subtitle-first {
  flex-basis: 20%;
}

.data__first-value {
  flex-basis: 40%;
}

.data__subtitle-second {
  flex-basis: 20%;
}

.data__second-value {
  flex-basis: 20%;
}

.btn-edit {
  font-weight: 500;
  font-size: 16px;
  line-height: 19px;
  color: #DFB259;
  background: none;
  margin: 0 3% 3% 0;
  border: 0;
  border-bottom: 2px solid #DFB259;
}

</style>