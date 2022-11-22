<template>
  <main class="checkout container">
    <h5 class="checkout__title">Оформление заказа</h5>
    <div class="checkout__block">
      <div class="checkout__first-column">
        <section class="checkout__information information">
          <h3 class="information__title">1. Информация о получателе</h3>
          <form class="information__forms form" id="form">
            <div class="form__name">
              <label class="form__label" for="name">Имя</label>
              <input
                  class="form__input name"
                  type="text"
                  id="name"
                  name="name"
                  placeholder="Имя"
              />
            </div>
            <div class="form__phone">
              <label class="form__label" for="phone">Телефон</label>
              <input
                  class="form__input phone"
                  type="text"
                  id="phone"
                  name="phone"
                  placeholder="Телефон"
              />
            </div>
            <div class="form__email">
              <label class="form__label" for="email">Почтовый адрес</label>
              <input
                  class="form__input email"
                  type="text"
                  id="email"
                  name="email"
                  placeholder="Почтовый адрес"
              />
            </div>
          </form>
        </section>
        <section class="checkout__address address">
          <h3 class="address__title">2. Адрес получателя</h3>
          <form class="address__forms form" id="addform">
            <div class="form__first-row">
              <div class="form__region">
                <label class="form__label" for="region">Регион</label>
                <input
                    class="form__input region"
                    type="text"
                    id="region"
                    name="region"
                    placeholder="Регион"
                />
              </div>
              <div class="form__city">
                <label class="form__city" for="city">Город</label>
                <input
                    class="form__input city"
                    type="text"
                    id="city"
                    name="city"
                    placeholder="Город"
                />
              </div>
            </div>
            <div class="form__second-row">
              <div class="form__street">
                <label class="form__label" for="street">Улица, дом</label>
                <input
                    class="form__input-two street"
                    type="text"
                    id="street"
                    name="street"
                    placeholder="Улица, дом"
                />
              </div>
              <div class="form__apart">
                <label class="form__label" for="apart">Квартира</label>
                <input
                    class="form__input-two apart"
                    type="text"
                    id="apart"
                    name="apart"
                    placeholder="Квартира"
                />
              </div>
              <div class="form__intercom">
                <label class="form__label" for="intercom">Домофон</label>
                <input
                    class="form__input-two intercom"
                    type="text"
                    id="intercom"
                    name="intercom"
                    placeholder="Домофон"
                />
              </div>
            </div>
          </form>
        </section>
        <section class="checkout__confirmation confirmation">
          <h3 class="confirmation__title">3. Подтверждение заказа</h3>
          <div class="confirmation__row">
            <div class="confirmation__pos">
              <input type="radio" name="option_conf" value="positive" id="positive" checked/>
              <label for="positive">Звонок менеджера</label>
            </div>
            <div class="confirmation__neg">
              <input type="radio" name="option_conf" value="negative" id="negative"/>
              <label for="negative">Подтверждение не требуется</label>
            </div>
          </div>
        </section>
        <section class="checkout__payment payment">
          <h3 class="payment__title">4. Способ оплаты</h3>
          <div class="payment__first_row">
            <fieldset class="payment__field">
              <input type="radio" name="option_payment" value="first" id="first" checked/>
              <label for="first">Банковской картой при получении</label>
            </fieldset>
            <fieldset class="payment__field">
              <input type="radio" name="option_payment" value="second" id="second"/>
              <label for="second">Наличными при получении</label>
            </fieldset>
          </div>
          <!--          <div class="payment__second-row">-->
          <!--            <fieldset class="payment__field">-->
          <!--              <input type="radio" name="option_payment" value="third" id="third"/>-->
          <!--              <label for="third">Система быстрых платежей</label>-->
          <!--            </fieldset>-->
          <!--            <fieldset class="payment__field">-->
          <!--              <input type="radio" name="option_payment" value="fourth" id="fourth"/>-->
          <!--              <label for="fourth">Наличными при получении</label>-->
          <!--            </fieldset>-->
          <!--          </div>-->
        </section>
        <section class="checkout__promo promo">
          <h3 class="promo__title">5. Промокод</h3>
          <p class="promo__subtitle">При наличии секретного кода, введите его ниже</p>
          <div class="promo__row">
            <form class="promo__form" id="promo">
              <input
                  class="promo__input"
                  type="text"
                  id="promo"
                  name="promo"
              />
            </form>
            <button class="promo__button">Применить</button>
          </div>
        </section>
        <section class="checkout__final final">
          <h3 class="final__title">6. Итого</h3>
          <p class="final__subtitle">Пожалуйста, проверьте свои данные перед отправкой</p>
          <div class="final__block">
            <div class="final__first-row">
              <p class="final__promo">Промокод</p>
              <p class="final__sale">- 1 500₽</p>
            </div>
            <div class="final__second-row">
              <p class="final__sum">Сумма заказа</p>
              <p class="final__cost">38 200 ₽</p>
            </div>
          </div>
          <button class="final__button">Оформить заказ</button>
        </section>
      </div>
      <div class="checkout__second-column">
        <div class="checkout__second-container">
          <section class="checkout__summary">
            <h4 class="summary__title">4 позиции <span class="color">в заказе</span></h4>
            <checkout-item-component/>
            <checkout-item-component/>
            <checkout-item-component/>
            <button class="summary__go-back">Вернуться в корзину &#8594;</button>
          </section>
        </div>
      </div>
    </div>
  </main>
</template>

<script>
import CheckoutItemComponent from "@/components/CheckoutItemComponent";

export default {
  name: "CheckoutPage",
  components: {CheckoutItemComponent}
}
</script>

<style scoped>
.container {
  margin: 3% 7% 0 7%;
}

.checkout__title {
  margin-bottom: 3%;
}

.checkout__block {
  display: flex;
  flex-direction: row;
  column-gap: 3%;
}

.checkout__first-column {
  display: flex;
  flex-direction: column;
  /*margin-right: 3%;*/
  flex-grow: 0.6;
}

.checkout__second-column {
  display: flex;
  flex-direction: column;
  flex-grow: 0.4;
}

.checkout__second-container {
  background: #FFFFFF;
  border-radius: 26px;
}

.checkout__information {
  background: #FFFFFF;
  border-radius: 26px;
  padding: 2% 0 2% 5%;
}

.form__input {
  display: block;
  width: 345px;
  background-color: #fff;
  padding: 3%;
  margin: 3% 0 5% 0;
  border: 1.3px solid #BCBCBC;
  border-radius: 14px;
  height: 20px;
}

.form__input-two {
  display: block;
  width: 213px;
  background-color: #fff;
  padding: 5%;
  margin: 3% 0 5% 0;
  border: 1.3px solid #BCBCBC;
  border-radius: 14px;
  height: 20px;
}

.form__input::placeholder {
  color: #212529;
  opacity: 0.4;
}

.form__input:focus {
  color: #212529;
  background-color: #fff;
  border-color: #bdbdbd;
  outline: 0;
  box-shadow: 0 0 0 0.2rem rgba(158, 158, 158, 0.25);
}

.form__input-two::placeholder {
  color: #212529;
  opacity: 0.4;
}

.form__input-two:focus {
  color: #212529;
  background-color: #fff;
  border-color: #bdbdbd;
  outline: 0;
  box-shadow: 0 0 0 0.2rem rgba(158, 158, 158, 0.25);
}

.information__forms {
  display: grid;
  grid-template-areas: "name email"
                        "phone .";
}

.form__name {
  grid-area: name;
}

.form__email {
  grid-area: email;
}

.form__phone {
  grid-area: phone;
}

.form__first-row {
  display: flex;
  flex-direction: row;
  /*gap: 90px;*/
  gap: 10%;

}

.form__second-row {
  display: flex;
  flex-direction: row;
  /*gap: 70px;*/
  gap: 8%;
}

.checkout__address {
  padding: 2% 0 2% 5%;
  background: #FFFFFF;
  border-radius: 26px;
  margin-top: 30px;
  display: flex;
  flex-direction: column;
  flex-wrap: wrap;
}

.checkout__confirmation {
  padding: 2% 0 5% 5%;
  background: #FFFFFF;
  border-radius: 26px;
  margin-top: 30px;
}

.confirmation__row {
  display: flex;
  flex-direction: row;
}

.confirmation__pos {
  margin-right: 10%;
}

.checkout__payment {
  padding: 2% 0 2% 5%;
  background: #FFFFFF;
  border-radius: 26px;
  margin-top: 30px;
  display: flex;
  flex-direction: column;
}

.payment__first_row {
  display: flex;
  flex-direction: row;
  gap: 5%;
  margin-bottom: 3%;
}

/*.payment__second-row {*/
/*  display: flex;*/
/*  flex-direction: row;*/
/*  gap: 5%;*/
/*}*/

.payment__field {
  border: 1.3px solid #BCBCBC;
  border-radius: 18px;
  padding: 3%;
  width: 300px;
}

.payment__field:active {
  border: 1.3px solid #DFB259;
  border-radius: 18px;
}

.checkout__promo {
  padding: 2% 0 2% 5%;
  background: #FFFFFF;
  border-radius: 26px;
  margin-top: 30px;
}

.promo__row {
  display: flex;
  flex-direction: row;
}

.promo__input {
  width: 527px;
  border: 1.3px solid #BCBCBC;
  border-radius: 14px;
  height: 37px;
  position: relative;
}

.promo__input::placeholder {
  color: #212529;
  opacity: 0.4;
}

.promo__input:focus {
  color: #212529;
  background-color: #fff;
  border-color: #bdbdbd;
  outline: 0;
  box-shadow: 0 0 0 0.2rem rgba(158, 158, 158, 0.25);
}

.promo__button {
  background: radial-gradient(106.43% 423.1% at 72.36% 34.29%, rgba(255, 226, 153, 0.5) 0%, rgba(255, 234, 182, 0) 100%) /* warning: gradient uses a rotation that is not supported by CSS and may not behave as expected */, linear-gradient(98.73deg, #DFB259 28.23%, #EDB442 85.02%);
  border-radius: 14px;
  border: none;
  width: 150px;
  height: 42px;
  color: #FFFFFF;
  position: absolute;
  left: 530.5px;
  font-weight: 600;
  font-size: 16px;
}

.checkout__final {
  padding: 2% 0 2% 5%;
  background: #FFFFFF;
  border-radius: 26px;
  margin-top: 30px;
  margin-bottom: 13%;
}

.final__block {
  display: flex;
  flex-direction: column;
  max-width: 350px;
}

.final__first-row {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: center;
}

.final__second-row {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: center;
}

.final__sum {
  font-weight: 500;
  font-size: 24px;
  color: #1D1D1D;
}

.final__cost {
  font-weight: 700;
  font-size: 28px;
  color: #DFB259;
}

.final__button {
  width: 292px;
  height: 50px;
  background: radial-gradient(106.43% 423.1% at 72.36% 34.29%, rgba(255, 226, 153, 0.5) 0%, rgba(255, 234, 182, 0) 100%) /* warning: gradient uses a rotation that is not supported by CSS and may not behave as expected */, linear-gradient(98.73deg, #DFB259 28.23%, #EDB442 85.02%);
  box-shadow: 0px 0px 21px rgba(255, 217, 142, 0.5);
  border-radius: 23px;
  border: none;
  font-size: 16px;
  color: #FFFFFF;
}

.checkout__summary {
  padding: 7% 0 10% 7%;
}

.summary__title {
  font-weight: 500;
  font-size: 24px;
  color: #DFB259;
  margin: 0 0 3% 0;
}

.color {
  color: #1D1D1D;
}

.summary__go-back {
  font-weight: 500;
  font-size: 20px;
  line-height: 24px;
  color: #1D1D1D;
  border: none;
  background: none;
  margin-top: 5%;
}

.summary__go-back:hover {
  color: #DFB259;
}

.information__title {
  margin-bottom: 3%;
  margin-top: 2%;
}

.final__title {
  margin-bottom: 3%;
  margin-top: 2%;
}

.confirmation__title {
  margin-bottom: 3%;
  margin-top: 2%;
}

.address__title {
  margin-bottom: 3%;
  margin-top: 2%;
}

.information__title {
  margin-bottom: 3%;
  margin-top: 2%;
}

.promo__title {
  margin-bottom: 3%;
  margin-top: 2%;
}

.payment__title {
  margin-bottom: 3%;
  margin-top: 2%;
}


</style>