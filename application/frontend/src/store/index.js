import Vue from 'vue'
import Vuex from 'vuex'


Vue.use(Vuex)
import auth from "@/store/auth";
import main from "@/store/main"
import favs from "@/store/favs";
export default new Vuex.Store({
 modules: {
   auth, main, favs
 },
})
