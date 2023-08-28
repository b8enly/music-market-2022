<template>
  <main class="error">
    <div class="error__row-first">
      <h1 class="error__title">Ошибка 404!</h1>
      <p class="error__subtitle">К сожалению, страница не найдена. <br /> Пожалуйста, вернитесь на главную
        страницу <br /> или воспользуйтесь меню сайта.</p>
      <button class="error__button btn">Перейти на главную</button>
    </div>
    <div class="error__row-second">
      <img class="error__image"
           :src="ErrorImage"
           alt="ErrorImage"
      />
    </div>
  </main>
</template>

<script>
import ErrorImage from '@/assets/img/error.png';

export default {
  name: "ErrorPage",
  data: () => ({
    ErrorImage: ErrorImage,
  }),
}
</script>

<style scoped>

.error {
  display: flex;
  margin: 2% 2% 0 7%;
  position: relative;
  overflow: hidden;
  height: 720px;
}

.error__subtitle {
  font-style: normal;
  font-weight: 400;
  font-size: 25px;
  line-height: 140%;
  color: #1D1D1D;
}

.error__row-first {
  display: flex;
  flex-direction: column;
  margin-top: 10%;
}

.error__row-second {
  position: absolute;
  bottom: -165px;
  right: 0px;
}

.error__button {
  width: 292px;
  height: 50px;
  background: radial-gradient(106.43% 423.1% at 72.36% 34.29%, rgba(255, 226, 153, 0.5) 0%, rgba(255, 234, 182, 0) 100%) /* warning: gradient uses a rotation that is not supported by CSS and may not behave as expected */, linear-gradient(98.73deg, #DFB259 28.23%, #EDB442 85.02%);
  box-shadow: 0px 0px 21px rgba(255, 217, 142, 0.5);
  border-radius: 23px;
  border: none;
  font-size: 16px;
  color: #FFFFFF;
}


.error__image {
  /*top: -812px;*/
  /*z-index: -1;*/

  /*top: 50px;*/
  /*right: 20px;*/
}
</style>