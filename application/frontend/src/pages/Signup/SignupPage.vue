<template>
<div class="signup">
  <div class="signup__path-wrapper">
    <span class="signup__path" v-for="(path, index) in paths" :key="index"> {{path}} /</span>
    <span class="signup__path-last"> Регистрация </span>
  </div>

  <form
  action="http://127.0.0.1:8000/api/users/sign_up/"
  @submit="sendForm"
  >
    <input type="text" v-model="form.name" name="name" placeholder="Name">
    <input type="text" v-model="form.surname" name="surname" placeholder="Surname">
    <input type="text" v-model="form.password" name="password" placeholder="Password">
    <input type="text" v-model="form.email" name="email" placeholder="Email">

    <input type="submit" name="submit" value="Send">
  </form>
</div>
</template>

<script>
import axios from "axios";

export default {
  name: "SignupPage",
  data(){
    return{
      paths: ['Главная'],
      form: {}
    }
  },
  methods:{
    sendForm(e){
      e.preventDefault()
      console.log('Отправка JSON данных', this.form)

      axios(e.target.action, {
            method: 'POST', // *GET, POST, PUT, DELETE
            cache: 'no-cache', // *default, no-cache, reload, force-cache, only-if-cached
            credentials: 'same-origin', // include, *same-origin, omit
            headers: {
              'Content-Type': 'application/json'
            },
            body: JSON.stringify(this.form) // тип данных, должен соответствовать "Content-Type"
          }
      ).then(
          function(response) {
            // успешно получен ответ сервера на запрос
            console.log('Ответ сервера', response);
          },
          function(error) {
            // Ошибка при осуществлении запроса
            console.error(error);
          }
      );
    }
  }
}
</script>

<style scoped>
.signup{
  margin: 2% 7% 2% 7%;
}
.signup__path{
  color: rgba(184, 184, 184, 1);
  font-size: 17px;
}

.signup__path-last{
  font-size: 17px;
  color: rgba(29, 29, 29, 1);
}

</style>