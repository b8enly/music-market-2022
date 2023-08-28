import Vue from 'vue'
import VueRouter from 'vue-router'
import MainPage from "@/pages/Main/MainPage";
import CheckoutPage from "@/pages/Checkout/CheckoutPage";
import ShoppingCart from "@/pages/Cart/ShoppingCart";
import CatalogPage from "@/pages/Catalog/CatalogPage";
import ProductPage from "@/pages/Product/ProductPage";
import ProfilePage from "@/pages/Profile/ProfilePage";
import SignupPage from "@/pages/Signup/SignupPage";
import ErrorPage from "@/pages/Error/ErrorPage";
import SigninPage from "@/pages/Signin/SigninPage";
import Cookies from "js-cookie";


Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: MainPage,
    meta: {
      public: true
    }
  },
  {
    path: '/checkout', // только для зарегестрированных
    name: 'checkout',
    component: CheckoutPage,
    meta: {
      public: false
    }
  },
  {
    path: '/cart',
    name: 'cart',
    component:  ShoppingCart,
    meta: {
      public: true
    }
  },
  {
    path: '/catalog/:category', // категория товара например акустические гитары
    name: 'catalog',
    component: CatalogPage,
    props: true,
    meta: {
      public: true
    }
  },
  {
    path: '/catalog/:category/:id', // категория товара например акустические гитары и id товара
    name: 'product',
    component: ProductPage,
    props: true,
    meta: {
      public: true
    }
  },
  {
    path: '/profile', // только для зарегестрированных
    name: 'profile',
    component: ProfilePage,
    meta: {
      public: false
    }
  },
  {
    path: '/users/sign_up',
    name: 'sign_up',
    component: SignupPage,
    props: true,
    meta: {
      public: true
    }
  },
  {
    path: '/error',
    name: 'error',
    component: ErrorPage,
    props: true,
    meta: {
      public: true
    }
  },
  {
    path: '/users/sign_in',
    name: 'sign_in',
    component: SigninPage,
    props: true,
    meta: {
      public: true
    }
  }
]

const router = new VueRouter({
  mode: 'history',
  scrollBehavior: (to)  => {
    if (to.hash) {
      return {selector: to.hash}
    } else {
      return {x: 0, y: 0}
    }
  },
  routes
})


// для перенаправления пользователей на вход пытавшихся зайти на страницы доступные только авторизированным пользователям
router.beforeEach( (to, from, next)=>{
  const isAuthentication = !!(Cookies.get('token'))
  if(!to.meta?.public &&  !isAuthentication){
    return next("/users/sign_in")
  }
  next();
})
// чтобы авторизированному пользователю нельзя было попасть на вход или регистрацию
router.beforeEach( (to, from, next)=>{
  const isAuthentication = !!(Cookies.get('token'))
  if(to.name === 'sign_in' || to.name === 'sign_up') {
    if(isAuthentication){
      return next("/")
    }
  }
  next();
})
export default router
