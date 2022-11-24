import axios from "../config/updateAxios";
import Cookies from 'js-cookie';

export default {
    state:()=>({
        token: null,
        error: null,
        user: null,
        visible: null
    }),

    actions:{
        REQUEST_TOKEN({commit}, user) {
            return axios.post("http://127.0.0.1:8000/api/users/sign_in", {
                email: user.email,
                password: user.password
            })
                .then((response) => {
                    // console.log(response.data, response.status)
                    Cookies.set('token', response.data.token)
                    commit('SET_TOKEN', response.data.token)

                })
                .catch((error) => {
                    console.error(error);
                    commit('SET_ERROR', error.response.data.detail[0])
                });
    },
        REQUEST_USER({commit}){
            return axios.get("http://127.0.0.1:8000/api/users/me", {})
                .then((response) => {
                    commit('SET_USER', response.data)
                })
                .catch((error) => {
                    console.error(error);
                });
        },
        LOGOUT_USER({commit}){
            return axios.get("http://127.0.0.1:8000/api/users/sign_out", {})
                .then((response) => {
                    commit('RESET_STATE', response.data)
                })
                .catch((error) => {
                    console.error(error);
                });
        },
        TOKEN_UPDATE({commit}){
            commit('SET_TOKEN',  Cookies.get('token') ?  Cookies.get('token') : null)
        },
        VISIBLE_UPDATE({commit}, boolean){
            commit('SET_VISIBLE', boolean)
        }
    },
    mutations: {
        SET_TOKEN: (state, token)=>{
            state.token = token;
        },
        SET_ERROR: (state, error)=>{
            state.error = error;
        },
        SET_USER: (state, user)=>{
            state.user = user
        },
        RESET_STATE: (state)=>{
            Cookies.remove('token')
            state.user = null;
            state.token = null;
        },
        SET_VISIBLE: (state, visible)=>{
            state.visible = visible
        }
    },
    getters: {
        TOKEN(state) {
            return state.token
        },
        ERROR(state){
            return state.error
        },
        USER(state){
            return state.user
        },
        isAuthentication(state){
            return state.token !== null
        },
        VISIBLE(state){
            return state.visible
        }
    }

}