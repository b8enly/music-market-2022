<template>
  <div id="app">
<!--    <nav>-->
<!--      <router-link to="/">Home</router-link> |-->
<!--      <router-link to="/about">About</router-link>-->
<!--    </nav>-->
    <HeaderComponent />
    <router-view/>
  </div>
</template>

<style>
@font-face {
  font-family: Inter regular; /* Гарнитура шрифта */
  src: url(assets/fonts/Inter-Regular.otf); /* Путь к файлу со шрифтом */
}
@font-face {
  font-family: Inter semiBold; /* Гарнитура шрифта */
  src: url(assets/fonts/Inter-SemiBold.otf); /* Путь к файлу со шрифтом */
}
/*noinspection CssNoGenericFontName*/
#app {
  font-family: Inter regular;
  font-style: normal;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: black;
}
body{
  margin: 0;
}
nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>

<script>
import HeaderComponent from "@/components/HeaderComponent";
export default {
  components: {HeaderComponent}
}
</script>