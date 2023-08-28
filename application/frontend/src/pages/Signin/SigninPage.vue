<template>
  <div class="signin">
    <div class="signin__path-wrapper">
      <span class="signin__path" v-for="(path, index) in paths" :key="index"> {{ path }} /</span>
      <span class="signin__path-last"> Вход </span>
    </div>

    <div class="signin__title">Вход</div>
    <div class="signin__main">
      <form
          class="signin__form"
          @submit="sendForm"
      >


        <div class="signin__form-wrongs" v-if="this.error !== null">
          <div class="signin__form-wrong" :key="index" v-for="(wrong, index) in Object.values(this.error).flat()">{{wrong}}</div>
        </div>

        <div class="signin__form-title">Авторизация</div>


        <label class="signin__form-label" for="email">Email</label>
        <input class="signin__form-input" type="email" v-model="email" name="email" placeholder="Email" id="email" required>


        <label class="signin__form-label" for="password">Пароль</label>
        <input class="signin__form-input" type="password" v-model="password" name="password" placeholder="Пароль" id="password"
               autocomplete="off"
               required>

        <input class="signin__form-btn" type="submit" name="submit" value="Войти">

      </form>

      <div class="signin__signup">
        <div class="signin__signup-block">
          <div class="signin__signup-col col-text">
            <div class="signin__signup-title"> Еще не зарегистрированы на BuyGuitar? </div>
            <p>Главное достоинство нашего товара не дизайн, а качество, поэтому
              предпочтение отдадим маркам, пользующимся популярностью уже много лет.</p>
            <p>Если вы давно мечтале о гитаре, которая будет играть долго — найдите ее здесь.</p>
            <input class="signin__form-btn" type="submit" value="Зарегистрироваться" @click="()=>{
              return this.$router.push({name: 'sign_up'})}">
          </div>
          <div class="signin__signup-col col-img">
              <img class="signin__signup-img" :src="require('../../assets/img/groupGuitar.png')" alt="img"/>
          </div>
        </div>
      </div>

    </div>
  </div>
</template>

<script>
import {mapActions, mapGetters} from "vuex";

export default {
  name: "SignupPage",
  data() {
    return {
      paths: ['Главная'],
      email: '',
      password: '',
      error: null
    }
  },
  methods: {
    ...mapActions (['REQUEST_TOKEN']),
    async sendForm(e) {
      e.preventDefault()
      let user = {
        email: this.email,
        password: this.password
      }
      await this.REQUEST_TOKEN(user)
      if(this.TOKEN){
        await this.$router.push({name: 'profile', query: {value: '1'}})
      }else {
        this.error = this.ERROR
      }
    }
  },
  computed: {
    ...mapGetters([
      'ERROR',
      'TOKEN'
    ]),
  },

}
</script>

<style scoped>
.signin {
  margin: 2% 7% 2% 7%;
}

.signin__path {
  color: rgba(184, 184, 184, 1);
  font-size: 17px;
}

.signin__path-last {
  font-size: 17px;
  color: rgba(29, 29, 29, 1);
}
.signin__title{
  font-weight: 600;
  font-size: 38px;
  color: #DFB259;
  margin-top: 30px;
  margin-bottom: 46px;

}
.signin__main{
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  justify-content: space-between;
}

.signin__form{
  display: flex;
  flex-direction: column;
  background-color: #FFFFFF;
  border-radius: 20px;
  max-width: 410px;
  min-width: 380px;
  padding: 30px 46px 46px 46px;
  margin-bottom: 100px;
  box-sizing: border-box;
}
.signin__form-title{
  font-weight: 500;
  font-size: 24px;
  color: #1D1D1D;
}
.signin__form-label{
  font-weight: 400;
  font-size: 16px;
  color: #1D1D1D;
  margin-top: 30px;
  margin-bottom: 10px;
}
.signin__form-input{
  border: 1.3px solid #BCBCBC;
  border-radius: 14px;
  box-sizing: border-box;
  min-height: 40px;
  padding: 10px 20px;
}

.signin__form-wrongs{
  padding: 20px 5px;
  background-color: #FF7777;
  margin-bottom: 30px;
}
.signin__form-wrong{
  margin: 5px 0;
}
.signin__form-btn{
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

.signin__signup{
  /*padding: 30px 40px;*/
  background: #FFFFFF;
  border-radius: 26px;
  max-height: 390px;
  max-width: 760px;
  box-sizing: border-box;
}
.signin__signup-title{
  font-weight: 600;
  font-size: 22px;
  color: #1D1D1D;
}
.signin__signup-col{
  display: flex;
  flex-direction: column;
  width: 50%;
}
.signin__signup-block{
  display: flex;
  flex-direction: row;
}
.signin__signup-img{
  width: 100%;
  height: 100%;
}
.col-text{
  padding: 40px 0 35px 30px;
}
.col-img{
  justify-content: flex-end;
  align-items: flex-end;
}
</style>