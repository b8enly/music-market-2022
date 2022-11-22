<template>
  <div class="signup">
    <div class="signup__path-wrapper">
      <span class="signup__path" v-for="(path, index) in paths" :key="index"> {{ path }} /</span>
      <span class="signup__path-last"> Регистрация </span>
    </div>

    <div class="signup__title">Регистрация</div>
    <div class="signup__main">
    <form
        class="signup__form"
        action="http://127.0.0.1:8000/api/users/sign_up"
        @submit="sendForm"
    >

      <div class="signup__form-wrongs" v-if="this.error !== null">
        <div class="signup__form-wrong" :key="index" v-for="(wrong, index) in Object.values(this.error).flat()">{{wrong}}</div>
      </div>


      <div class="signup__form-title">Создание аккаунта</div>

      <label class="signup__form-label" for="firstName">Имя</label>
      <input class="signup__form-input" type="text" v-model="firstName" name="name" placeholder="Имя" id="firstName">
      <label class="signup__form-label" for="surname">Фамилия</label>
      <input class="signup__form-input" type="text" v-model="surname" name="surname" placeholder="Фамилия" id="surname">
      <label class="signup__form-label" for="patronymic">Отчество</label>
      <input class="signup__form-input" type="text" v-model="patronymic" name="patronymic" placeholder="Отчество" id="patronymic">
      <label class="signup__form-label" for="email">Email</label>
      <input class="signup__form-input" type="email" v-model="email" name="email" placeholder="Email" id="email" required>
      <label class="signup__form-label" for="phone">Телефон</label>
      <input class="signup__form-input" type="text" name="phone" placeholder="Телефон" id="phone">

      <label class="signup__form-label" for="password">Пароль</label>
      <input class="signup__form-input" type="password" v-model="password" name="password" placeholder="Пароль" id="password" required>
      <label class="signup__form-label" for="password2">Повторите пароль</label>
      <input class="signup__form-input" type="password" v-model="password2" name="password2" placeholder="Повторите пароль" id="password2" required>


      <div class="signup__form-agreements">

        <label class="signup__form-label-checkbox" for="notification">
          Хочу получать уведомления о новых предложениях по электронной почте
          <input class="signup__form-checkbox" type="checkbox" name="notification" id="notification">
          <span class="signup__form-checkmark"></span>
        </label>
     </div>

      <div class="signup__form-agreements">

      <label class="signup__form-label-checkbox" for="accept">
        Я принимаю условия
        <a href="#" style="color: rgba(223, 178, 89, 1); text-decoration:  underline rgba(223, 178, 89, 1);">
        Пользовательского соглашения
        </a>
        *
        <input class="signup__form-checkbox" v-model="accept" type="checkbox" name="accept" id="accept">
        <span class="signup__form-checkmark"></span>
      </label>
      </div>

      <input class="signup__form-btn" type="submit" name="submit" value="Зарегистрироваться">

    </form>

      <div class="signup__advance">
        <div class="signup__advance-title"> Преимущества сервиса BuyGuitar </div>
        <div class="signup__advance-block">
        <div class="signup__advance-col">
          <ul class="signup__advance-list">
            <li class="signup__advance-elem"><div class="signup__advance-circle"></div> Зарегистрировавшись, вы сможете добавлять товары в избранное</li>
            <li class="signup__advance-elem"><div class="signup__advance-circle"></div> Вы первыми узнаете о новинках и акциях</li>
          </ul>
        </div>
        <div class="signup__advance-col">
          <ul class="signup__advance-list">
            <li class="signup__advance-elem"><div class="signup__advance-circle"></div> История заказов всегда под рукой</li>
            <li class="signup__advance-elem"><div class="signup__advance-circle"></div> Оформление заказов станет удобнее и быстрее</li>
          </ul>
        </div>
        </div>
      </div>

    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "SignupPage",
  data() {
    return {
      paths: ['Главная'],
      email: '',
      password: '',
      surname: '',
      firstName: '',
      patronymic: '',
      password2: '',
      accept: false,
      error: null,

    }
  },
  methods: {
    sendForm(e) {
      e.preventDefault()
      console.log(this.accept)
      if (this.password === this.password2) {
        if(this.accept) {
          axios({
                method: 'post', // *GET, POST, PUT, DELETE
                data: {
                  email: this.email,
                  password: this.password,
                  surname: this.surname,
                  name: this.firstName,
                  patronymic: this.patronymic
                },
                headers: {
                  'Content-Type': 'application/json'
                },
                url: e.target.action,
              }
          ).then((response) => {
                // успешно получен ответ сервера на запрос
                console.log('Ответ сервера', response);
                this.$router.push({name: 'home'});
              },
              (error) => {
                // Ошибка при осуществлении запроса
                console.error(error);
                this.error = error.response.data.details[0]
              }
          );
        }else{
          this.error = {"accept": ["Accept the terms of the user agreement"]}
        }
      } else {
        this.error = {"password": ["password1 is not equal to password2"]}
      }
    }
  }
}
</script>

<style scoped>
.signup {
  margin: 2% 7% 2% 7%;
}

.signup__path {
  color: rgba(184, 184, 184, 1);
  font-size: 17px;
}

.signup__path-last {
  font-size: 17px;
  color: rgba(29, 29, 29, 1);
}
.signup__title{
  font-weight: 600;
  font-size: 38px;
  color: #DFB259;
  margin-top: 30px;
  margin-bottom: 46px;

}
.signup__main{
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  justify-content: space-between;
}

.signup__form{
  display: flex;
  flex-direction: column;
  background-color: #FFFFFF;
  border-radius: 20px;
  max-width: 380px;
  padding: 30px 46px 46px 46px;
  margin-bottom: 100px;
}
.signup__form-title{
  font-weight: 500;
  font-size: 24px;
  color: #1D1D1D;
}
.signup__form-label{
  font-weight: 400;
  font-size: 16px;
  color: #1D1D1D;
  margin-top: 30px;
  margin-bottom: 10px;
}
.signup__form-input{
  border: 1.3px solid #BCBCBC;
  border-radius: 14px;
  box-sizing: border-box;
  min-height: 40px;
  padding: 10px 20px;
;
}
.signup__form-agreements{
  display: flex;
  flex-direction: row;
  flex-wrap: nowrap;
  margin-top: 30px;
}

.signup__form-label-checkbox {
  display: block;
  position: relative;
  padding-left: 30px;
  cursor: pointer;
  font-size: 14px;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}

/* Hide the browser's default checkbox */
.signup__form-checkbox {
  position: absolute;
  opacity: 0;
  cursor: pointer;
  height: 0;
  width: 0;
}

/* Create a custom checkbox */
.signup__form-checkmark {
  position: absolute;
  top: 0;
  left: 0;
  height: 14px;
  width: 14px;
  margin-top: 3px;
  border: 2px solid #DFB259;
  border-radius: 3px;
}

/* When the checkbox is checked, add a blue background */
.signup__form-checkbox:checked ~ .signup__form-checkmark {
  background-color: #DFB259;
}

/* Create the checkmark/indicator (hidden when not checked) */
.signup__form-checkmark:after {
  content: "";
  position: absolute;
  display: none;
}

/* Show the checkmark when checked */
.signup__form-checkbox:checked ~ .signup__form-checkmark:after {
  display: block;
}

/* Style the checkmark/indicator */
.signup__form-label-checkbox .signup__form-checkmark:after {
  left: 4.5px;
  top: 0;
  width: 4px;
  height: 9px;
  border: solid white;
  border-width: 0 2px 2px 0;
  transform: rotate(45deg);
  -webkit-transform: rotate(45deg);
  -ms-transform: rotate(45deg);
}
.signup__form-wrongs{
  padding: 20px 5px;
  background-color: #FF7777;
  margin-bottom: 30px;
}
.signup__form-wrong{
  margin: 5px 0;
}
.signup__form-btn{
  width: 100%;
  min-height: 42px;
  background: radial-gradient(rgba(255, 226, 153, 0.5) 0%, rgba(255, 234, 182, 0) 100%), linear-gradient(98.73deg, #DFB259 28.23%, #EDB442 85.02%);
  /* блюр_кнопка */
  margin-top: 40px;
  box-shadow: 0 0 21px rgba(255, 217, 142, 0.5);
  border-radius: 14px;
  font-weight: 600;
  font-size: 16px;
  color: #FFFFFF;
  border: none;
  box-sizing: border-box;
  cursor: pointer;
}

.signup__advance{
  padding: 30px 40px;
  background: #FFFFFF;
  border-radius: 26px;
  max-height: 200px;
  max-width: 760px;
  box-sizing: border-box;
}
.signup__advance-title{
  font-weight: 600;
  font-size: 22px;
  color: #1D1D1D;
}
.signup__advance-col{
  display: flex;
  flex-direction: column;
  width: 50%;
}
.signup__advance-block{
  display: flex;
  flex-direction: row;
}
.signup__advance-list{
  padding: 0;
}
.signup__advance-elem{
  list-style-type: none;
  margin: 15px 0;
  font-size: 14px;
  display: flex;
  align-items: center;
}
.signup__advance-circle{
  min-width: 8px;
  min-height: 8px;
  background-color: #DFB259;
  margin-right:10px;
  border-radius: 50%;
}
</style>