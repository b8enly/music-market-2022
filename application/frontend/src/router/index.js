import Vue from 'vue'
import VueRouter from 'vue-router'
import MainPage from "@/pages/Main/MainPage";
import CheckoutPage from "@/pages/Checkout/CheckoutPage";
import ShoppingCart from "@/pages/Cart/ShoppingCart";
import CatalogPage from "@/pages/Catalog/CatalogPage";
import ProductPage from "@/pages/Product/ProductPage";
import ProfilePage from "@/pages/Profile/ProfilePage";

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: MainPage
  },
  {
    path: '/checkout',
    name: 'checkout',
    component: CheckoutPage
  },
  {
    path: '/cart',
    name: 'cart',
    component:  ShoppingCart
  },
  {
    path: '/catalog/:category', // категория товара например акустические гитары
    name: 'catalog',
    component: CatalogPage,
    props: true
  },
  {
    path: '/catalog/:category/:id', // категория товара например акустические гитары и id товара
    name: 'product',
    component: ProductPage,
    props: true

  },
  {
    path: '/profile',
    name: 'profile',
    component: ProfilePage,
  }
]

const router = new VueRouter({
  mode: 'history',
  routes
})

export default router
