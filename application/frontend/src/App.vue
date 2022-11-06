<template>
  <div id="app">
    <!--    <nav>-->
    <!--      <router-link to="/">Home</router-link> |-->
    <!--      <router-link to="/about">About</router-link>-->
    <!--    </nav>-->
    <HeaderComponent/>
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
  /*text-align: center;*/
  color: black;
}

body {
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

h1 {
  background: radial-gradient(106.43% 423.1% at 72.36% 34.29%, rgba(255, 226, 153, 0.5) 0%, rgba(255, 234, 182, 0) 100%) /* warning: gradient uses a rotation that is not supported by CSS and may not behave as expected */, linear-gradient(98.73deg, #DFB259 28.23%, #EDB442 85.02%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  text-fill-color: transparent;
  font-size: 70px;
  margin: 0 0 0 0;
}

h2 {
  color: #1D1D1D;
  font-weight: 500;
  font-size: 60px;
  margin: 0 0 0 0;
}

h3 {
  font-weight: 500;
  font-size: 25px;
  color: #1D1D1D;
  margin: 0 0 0 0;
}

h5 {
  color: #DFB259;
  font-style: normal;
  font-weight: 700;
  font-size: 45px;
  line-height: 54px;
  margin: 0 0 0 0;
}

</style>

<script>
import HeaderComponent from "@/components/HeaderComponent";

export default {
  components: {HeaderComponent}
}
</script>