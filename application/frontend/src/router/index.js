import Vue from 'vue'
import VueRouter from 'vue-router'
import MainPage from "@/pages/Main/MainPage";
import CheckoutPage from "@/pages/Checkout/CheckoutPage";

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: MainPage
  },
  // {
  //   path: '/home',
  //   name: 'main page',
  //   component: MainPage
  // },
  {
    path: '/checkout',
    name: 'checkout',
    component: CheckoutPage
  },
]

const router = new VueRouter({
  mode: 'history',
  routes
})

export default router
