<template>
<div class="card">
  <div class="card__header">
    <img class="card__img" :src="require('../assets/img/imgReview.png')" alt="profile" height="70px" width="70px">
    <div class="card__wrapper">
      <div class="card__date">
        25 сентября 2022
      </div>
      <div class="card__name">
        Александр Лобанин
      </div>
    </div>
  </div>
  <div class="card__main">
    <p class="card__description">
      Каждая из этих моделей имеет уникальную форму корпуса и свой индивидуальный тон.
      Важность этих моделей состоит еще и в том, что они настолько повлияли на рок-музыку в целом, что их названия стали...
      <a class="card__link-vk" href="https://vk.com/groups">Читать полностью</a>
    </p>

  </div>
  <div class="description">

  </div>

</div>
</template>

<script>
export default {
  name: "ReviewItemComponent"
}
</script>

<style scoped>
  .card{
    display: flex;
    flex-wrap: nowrap;
    flex-direction: column;
    max-width: 410px;
    max-height: 347px;
    background-color: #FFFFFF;
    border-radius: 30px;
    padding: 40px;
    box-sizing: border-box;
    margin: 5px;
  }
  .card__header{
    display: flex;
    flex-direction: row;
    flex-wrap: wrap;
    justify-content: space-between;
  }
  .card__wrapper{
    display: flex;
    flex-direction: column;
    justify-content: space-around;
  }
  .card__date{
    font-size: 16px;
    color: rgba(81, 81, 81, 1);
  }
  .card__name{
    font-size: 24px;
    font-weight: 600;
  }
  .card__description{
    font-size: 17px;
  }
  .card__link-vk{
    color: rgba(223, 178, 89, 1);
  }
</style>