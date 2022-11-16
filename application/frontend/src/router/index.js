import Vue from 'vue'
import VueRouter from 'vue-router'
import MainPage from "@/pages/Main/MainPage";
import ShoppingCart from "@/pages/Cart/ShoppingCart";
import CatalogPage from "@/pages/Catalog/CatalogPage";


Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: MainPage
  },
  {
    path: '/cart',
    name: 'cart',
    component:  ShoppingCart
  },
  {
    path: '/catalog',
    name: 'catalog',
    component: CatalogPage
  }

]

const router = new VueRouter({
  mode: 'history',
  routes
})

export default router
