<template>
  <div v-if="show" class="background" >
    <div class="hystmodal_wrap">
      <div class="modal">
        <form
            class="modalBodyWrapper"
            @submit="sendForm"
        >
          <slot name="title">
            <div class="modal-block-title">
              <h3 class="modal-title">Редактирование</h3>
              <div class="modal-close" @click="closeModal">&#10006;</div>
            </div>
          </slot>
          <slot name="body">
            <div class="modal-content">
              <!--              <div class="signup__form-wrongs" v-if="this.error !== null">-->
              <!--                <div class="signup__form-wrong" :key="index" v-for="(wrong, index) in Object.values(this.error).flat()">{{wrong}}</div>-->
              <!--              </div>-->
              <div class="modal__form-row">
                <div class="modal__form-block">
                  <label class="modal__form-label" for="firstName">Фамилия</label>
                  <input class="modal__form-input" type="text" v-model="fullName.firstName"
                         name="firstName" placeholder="Фамилия"
                         id="firstName">
                </div>
                <div class="modal__form-block">
                  <label class="modal__form-label" for="lastName">Имя</label>
                  <input class="modal__form-input" type="text" v-model="fullName.lastName"
                         name="lastName" placeholder="Имя"
                         id="lastName">
                </div>
              </div>

              <div class="modal__form-row">
                <div class="modal__form-block">
                  <label class="modal__form-label" for="patronymic">Отчество</label>
                  <input class="modal__form-input" type="text" v-model="fullName.patronymic"
                         name="patronymic" placeholder="Отчество"
                         id="patronymic">
                </div>
                <div class="modal__form-block">
                  <label class="modal__form-label" for="phone">Телефон</label>
                  <input class="modal__form-input" type="text" v-model="phone"
                         name="phone" placeholder="Телефон"
                         id="phone">
                </div>
              </div>

              <div class="modal__form-row">
                <div class="modal__form-block">
                  <label class="modal__form-label" for="email">Email</label>
                  <input class="modal__form-input" type="email" v-model="email"
                         name="email" placeholder="Город"
                         id="email">
                </div>
                <div class="modal__form-block">
                  <label class="modal__form-label" for="birthday">Дата рождения</label>
                  <input class="modal__form-input" type="text" v-model="birthday"
                         name="birthday" placeholder="Дата рождения"
                         id="birthday">
                </div>
              </div>
            </div>
          </slot>
          <slot name="footer">
            <div class="modal-footer">
              <button class="modal-footer_button" @click="closeModal">
                Назад
              </button>
              <button class="modal-footer_button">
                Сохранить
              </button>
            </div>
          </slot>
        </form>

      </div>
    </div>
  </div>

</template>

<script>

export default {
  name: "AddressDataUpdate",
  props:{
    user: {
      type: Object,
      default() {
        return {}
      }
    },
  },
  data: function () {
    return {
      show: false,
      fullName: {
        firstName: this.user.name,
        lastName: this.user.surname,
        patronymic: this.user.patronymic ? this.user.patronymic: ''
      },
      phone: '',
      birthday: '',
      email: this.user.email
    }
  },
  computed: {},
  methods: {
    closeModal(){
      this.show = false;
    },
    async sendForm(e) {
      e.preventDefault()
    }
  },
  mounted(){
  },
  created() {

  }
}
</script>

<style scoped>
.background {
  z-index: 10;
  position: fixed;
  overflow: auto;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.85);
}

.modal{
  border-radius: 8px;
  padding: 15px;
  min-width: 260px;
  max-width: 480px;
  width: 50%;
  margin: auto;
  z-index: 11;
  background-color: black;
  box-shadow: 0 0 20px rgba(0, 0, 0, 0.9);
}
.hystmodal_wrap {
  height: 100%;
  display: flex;
  justify-content: center;
  align-content: center;
}
.modalBodyWrapper {
  display: flex;
  flex-direction: column;
  width: 100%;
  height: 100%;
  overflow: hidden auto;
}
.modal-block-title{
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  margin-bottom: 40px;
  margin-top: 10px;
}
.modal-close {
  border-radius: 50%;
  color: #fff;
  background: #DFB259;
  display: flex;
  align-items: center;
  justify-content: center;
  width: 30px;
  height: 30px;
  cursor: pointer;
}

.modal-title {
  font-weight: 600;
  font-size: 24px;
  color: #DFB259;
}

.modal-content {
  display: flex;
  flex-direction: column;
  margin-bottom: 20px
}
.modal-footer{
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  justify-content: space-between;
}

.modal-footer_button {

  min-height: 42px;
  background: radial-gradient(rgba(255, 226, 153, 0.5) 0%, rgba(255, 234, 182, 0) 100%), linear-gradient(98.73deg, #DFB259 28.23%, #EDB442 85.02%);
  /* блюр_кнопка */
  width: 40%;
  box-shadow: 0 0 21px rgba(255, 217, 142, 0.5);
  border-radius: 23px;
  font-weight: 600;
  font-size: 20px;
  color: #FFFFFF;
  border: none;
  box-sizing: border-box;
  cursor: pointer;
  margin: 10px 0;
}
.modal__form-row{
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  justify-content: space-between;
  align-items: center;

}
.modal__form-label{
  color: #FFFFFF;
  font-size: 16px;
  margin: 10px 0;
}
.modal__form-block{
  display: flex;
  flex-wrap: nowrap;
  flex-direction: column;
  width: 47%;
  margin: 10px 0;
}
.modal__form-input{
  border: 1.3px solid #BCBCBC;
  border-radius: 14px;
  box-sizing: border-box;
  min-height: 40px;
  padding: 10px 20px;
}
</style>

