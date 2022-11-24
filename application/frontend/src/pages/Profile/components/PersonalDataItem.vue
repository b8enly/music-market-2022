<template>
  <main class="data">
    <div class="data__first-row">
      <h3 class="data__title">Личные данные</h3>
      <button class="data__button btn-edit">Редактировать</button>
    </div>
    <div class="data__block" v-if="user">
      <div class="data__row">
        <p class="data__subtitle-first">
          ФИО:
        </p>
        <p class="data__first-value">
          {{ `${user.name ? user.name: '' } ${user.surname ? user.surname: '' } ${user.patronymic ? user.patronymic: ''}` }}
        </p>
        <p class="data__subtitle-second">
          Телефон:
        </p>
        <p class="data__second-value">
          {{ '-' }} <!--телефон отстуствует в бд, пока прочерк-->
        </p>
      </div>
      <div class="data__row">
        <p class="data__subtitle-first">
          Email:
        </p>
        <p class="data__first-value">
<!--          petr************@gmail.com-->
          {{user.email}}
        </p>
        <p class="data__subtitle-second">
          День рождения:
        </p>
        <p class="data__second-value">
          {{ '-' }} <!--Дата рождения? этого нет в бд, пока прочерк-->
        </p>
      </div>
    </div>
  </main>
</template>

<script>
export default {
  props:{
    user: {
      type: Object,
      default() {
        return {}
      }
    },
  },


  name: "PersonalDataItem"
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