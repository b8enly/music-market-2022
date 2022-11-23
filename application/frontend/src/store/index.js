import Vue from 'vue'
import Vuex from 'vuex'


Vue.use(Vuex)
import auth from "@/store/auth";
import main from "@/store/main"
import createPersistedState from "vuex-persistedstate"
import Cookies from 'js-cookie';
export default new Vuex.Store({
 modules: {
   auth, main
 },
    plugins: [
        createPersistedState({
            paths: ["auth"],
            storage: {
                getItem: (key) => {
                    return Cookies.get(key);
                },
                setItem: (key, value) =>
                    Cookies.set(key, value, { expires: 365, secure: false }),
                removeItem: key => Cookies.remove(key)
                },
        })
    ]
})
