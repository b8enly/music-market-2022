<template>
  <main class="cart">
    <h4 class="cart__title">Корзина</h4>
    <div class="card__first-row">
      <div class="card__first-block">
        <ShoppingCartComponent/>
        <ShoppingCartComponent/>
        <ShoppingCartComponent/>
        <ShoppingCartComponent/>
      </div>
      <section class="cart__order order">
        <p class="order__title">Ваш заказ</p>
        <div class="order__line line">
          <p class="line__text">Количество единиц товара</p>
          <p class="line__text">4</p>
        </div>
        <div class="order__line line">
          <p class="line__text">Общая скидка</p>
          <p class="line__text">- 4 500₽</p>
        </div>
        <div class="order__line line">
          <p class="line__text">Доставка</p>
          <p class="line__text">бесплатно</p>
        </div>
        <div class="order__line forth">
          <p class="forth__finals">Итого</p>
          <p class="forth__cost">39 700 ₽</p>
        </div>
        <button class="order__processing">Перейти к оформлению</button>
      </section>
      <section class="card__additional additional">
        <p class="additional__title">Дополнительные сведения</p>
        <p class="additional__subtitle">Обращаем Ваше внимание, что окончательная стоимость и состав заказа,
          если в нем присутствуют товары и/или услуги, участвующие в акции,
          будет подтверждена после обработки заказа.</p>
      </section>
    </div>
    <section class="card__something-else else">
      <h6 class="else__title">Может, что-то еще?</h6>
      <div class="else__row">
      <CatalogItemComponent/>
      <CatalogItemComponent/>
      <CatalogItemComponent/>
      <CatalogItemComponent/>
      </div>
    </section>
  </main>
</template>

<script>
import ShoppingCartComponent from "@/components/ShoppingCartComponent";
import CatalogItemComponent from "@/components/CatalogItemComponent";

export default {
  name: "ShoppingCart",
  components: {CatalogItemComponent, ShoppingCartComponent},
}
</script>

<style>

.cart {
  margin: 0 1% 0 7%;
}

.card__first-row {
  display: grid;
  grid-template-areas: "fblock fblock sblock"
                        "fblock fblock add"
                        "fblock fblock .";
}

.card__first-block {
  grid-area: fblock;
  margin-right: 5%;
}

.cart__order {
  grid-area: sblock;
  background: #FFFFFF;
  border-radius: 26px;
  padding: 3%;
  max-width: 429px;
  max-height: 351px;
  justify-content: center;
  display: flex;
  flex-direction: column;
  margin-bottom: 30px;
  /*  очередной хреновый код тут и в блоке ниже, вот это все max что-то там хорошо бы убрать*/
}

.card__additional {
  grid-area: add;
  background: #FFFFFF;
  border-radius: 26px;
  max-width: 429px;
  display: flex;
  justify-content: center;
  flex-direction: column;
  height: fit-content;
  padding: 3%;
}

.card__something-else {
  margin: 1% 0 1% 0;
}

.else__row {
  display: flex;
  flex-direction: row;
  margin-bottom: 5%;
}

.order__title {
  margin: 1% 0 1% 5%;
  font-size: 24px;
  color: #1D1D1D;
}

.order__line {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  margin: 0 5% 0 5%;
}

.line__text {
  font-size: 16px;
  color: #1D1D1D;
}

.forth {
  margin-bottom: 0;
}

.forth__finals {
  font-size: 24px;
  color: #1D1D1D;
}

.forth__cost {
  font-size: 28px;
  line-height: 34px;
  color: #DFB259;
}

.order__processing {
  width: 345px;
  height: 59px;
  background: radial-gradient(106.43% 423.1% at 72.36% 34.29%, rgba(255, 226, 153, 0.5) 0%, rgba(255, 234, 182, 0) 100%) /* warning: gradient uses a rotation that is not supported by CSS and may not behave as expected */, linear-gradient(98.73deg, #DFB259 28.23%, #EDB442 85.02%);
  box-shadow: 0px 0px 21px rgba(255, 217, 142, 0.5);
  border-radius: 21px;
  margin-left: 10%;
  border: none;
  color: #FFFFFF;
  padding: 3%;
  font-size: 16px;
  /*  тоже не очень с margin-left*/
}

.additional__title {
  font-size: 24px;
  color: #1D1D1D;
  font-weight: 500;
  margin: 0;
  padding: 5%;
}

.additional__subtitle {
  font-weight: 400;
  font-size: 16px;
  color: #1D1D1D;
  margin: 0;
  padding: 5%;
}

</style>