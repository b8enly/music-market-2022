<template>
  <div class="card">
    <div class="card_header">
   <div class="card_teg">  <!--   тег непонятно кликабедьная ли-->
        Популярное
      </div>
      <div class="wrapper_favorite">
      <img class="card_favorite" :src="require('../assets/icon/iconHeartBlack.svg')" alt="favorite" height="18" width="19"/> <!--  избранное -->
      </div>
    </div>
    <div class="card_guitar">
        <img :src="require('../assets/img/imgGuitar.png')" alt="img" height="238" width="88"/> <!--   картинка гитары -->
    </div>
    <div class="switch_img_guitar">
    <span class="switch_img switch_active"> </span> <!--   переключатели фоток -->
    <span class="switch_img"> </span> <!--   переключатели фоток -->
    <span class="switch_img"> </span> <!--   переключатели фоток -->
    <span class="switch_img"> </span> <!--   переключатели фоток -->
    </div>
    <div class="card_footer">
      <span class="title_guitar">Акустическая гитара Homage LF-3900</span> <!--   название -->
      <div class="card_price">
        <span class="new_price">14 000 ₽</span> <!--   новая цена -->
        <span class="old_price">12500 ₽ </span> <!--   старая цена -->
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "CatalogItemComponent"
}
</script>

<style scoped>
  .card{
    background-color: white;
    max-width: 314px;
    min-width: 300px;
    /*height: 384px;*/
    height: 450px;
    display: flex;
    flex-direction: column;
    flex-wrap: nowrap;
    border-radius: 30px;
    margin: 5px;
  }
  .card_header{
    display: flex;
    flex-direction: row;
    align-items: flex-start;
    padding: 20px;
  }
  .card_teg{
    border: 1px solid rgba(223, 178, 89, 1);
    color: rgba(223, 178, 89, 1);
    box-sizing: border-box;
    border-radius: 7px;
    font-weight: 500;
    font-size: 14px;
    padding: 6px 16px;
  }

  .wrapper_favorite{
    flex: 1;
    display: flex;
    justify-content: flex-end;
    align-items: center;
    height: 100%;
  }

  .card_favorite{
    cursor: pointer;
  }

  .switch_img{
    height: 8px;
    width: 8px;
    border:1px solid rgba(223, 178, 89, 1);
    background-color: white;
    border-radius: 50%;
    display: inline-block;
    margin: 0 4px;
    cursor: pointer;
  }
  .switch_active{
    background-color: rgba(223, 178, 89, 1);
  }
  .switch_img_guitar{
    display: flex;
    justify-content: center;
    margin: 12px 0;
  }
  .card_footer{
    padding: 0 20px;
  }
  /*noinspection CssNoGenericFontName*/
  .title_guitar{
    font-weight: 500;
    font-size: 16px;
    color: rgba(29, 29, 29, 1);
    width: 80%;
    text-align: left;
    font-family: 'Inter semiBold';
    margin-bottom: 20px;
  }
  .card_footer{
    display: flex;
    flex-direction: column;
    flex: 1;
  }
  .card_price{
    flex: 1;
    text-align: left;
  }
  .new_price{
    color: rgba(223, 178, 89, 1);
    font-size: 22px;
    font-weight: 700;
    margin-right: 27px;
  }
  .old_price{
    font-weight: 500;
    color: rgba(116, 116, 116, 1);
    font-size: 18px;
    text-decoration: line-through;
  }
  .card_guitar{
    display: flex;
    justify-content: center;
  }
</style>