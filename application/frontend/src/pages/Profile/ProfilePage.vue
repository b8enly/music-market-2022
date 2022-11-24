<template>
  <main class="profile container">
    <h4 class="profile__title">Личный кабинет</h4>
    <div class="profile__block">
      <div class="profile__first-column">
        <section class="profile__menu">
          <button class="menu__btn" :class="{'activeBtn': this.value === '1'}" id="info" @click="onInfo">Мои данные</button>
          <button class="menu__btn" :class="{'activeBtn': this.value === '2'}" id="favs" @click="onFavs">Избранное</button>
          <button class="menu__btn" :class="{'activeBtn': this.value === '3'}"  id="orders" @click="onOrder">Мои заказы</button>
          <button class="menu__btn" id="exit" @click="logout">Выйти</button>
        </section>
      </div>
      <div class="profile__second-column">
        <personal-data-item v-if="this.value === '1'" v-bind:user="this.user"/>
        <address-data-item v-if="this.value === '1'"/>
        <favourites-page-item v-else-if="this.value === '2'"/>
        <order-history v-else-if="this.value === '3'"/>
      </div>
    </div>
  </main>
</template>

<script>

import PersonalDataItem from "@/pages/Profile/components/PersonalDataItem";
import AddressDataItem from "@/pages/Profile/components/AddressDataItem";
import FavouritesPageItem from "@/pages/Profile/components/FavouritesPageItem";
import OrderHistory from "@/pages/Profile/components/OrderHistory";
import {mapActions, mapGetters} from "vuex";




export default {
  name: "ProfilePage",
  components: {OrderHistory, FavouritesPageItem, AddressDataItem, PersonalDataItem},
  data: () => ({
    value: '1',
    user: null
  }),
  methods:
      {
        ...mapActions (['VISIBLE_UPDATE']),
        onInfo() {
          this.$router.push({query: {value: '1'}})
        },
        onFavs() {
          this.$router.push({query: {value: '2'}})
        },
        onOrder() {
          this.$router.push({query: {value: '3'}})
        },
        ...mapActions (['REQUEST_USER', 'LOGOUT_USER']),
        async logout(){
            await this.VISIBLE_UPDATE(false)
            await this.LOGOUT_USER()
            await this.$router.push({name: 'home'})
        },
      },

  mounted() {
  },
  computed: {
    ...mapGetters([
      'USER',
    ]),
  },
  watch: {
    '$route' (to) {
      this.value = to.query.value
    }
  },
  created() {
    this.value = this.$route.query.value ? this.$route.query.value : this.value
    this.REQUEST_USER().then(()=>{
      return this.user = this.USER
    })
  },
}
</script>

<style scoped>

.container {
  margin: 2% 7% 2% 7%;
}

.profile__block {
  display: flex;
  flex-direction: row;
}

.profile__first-column {
  display: flex;
  flex-direction: column;
  flex-grow: 0.2;
}

.profile__second-column {
  display: flex;
  flex-direction: column;
  flex-grow: 0.8;
  flex-wrap: wrap;
  width: 550px;
}

.profile__menu {
  background: #FFFFFF;
  border-radius: 26px;
  padding: 10%;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  margin-right: 15%;
  width: 150px;
}

.menu__btn {
  font-weight: 400;
  font-size: 20px;
  color: #797979;
  border: none;
  background: none;
  margin: 3%;
  padding: 2%;
}

.menu__btn:hover {
  color: #1D1D1D;
}

.menu__btn:active {
  color: #1D1D1D;
}
.activeBtn{
  color: #DFB259;
}
</style>