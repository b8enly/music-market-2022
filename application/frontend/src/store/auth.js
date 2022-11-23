import axios from "../config/updateAxios";


export default {
    state:()=>({
        token: null,
        error: null,
        user: null
    }),

    actions:{
        REQUEST_TOKEN({commit}, user) {
            return axios.post("http://127.0.0.1:8000/api/users/sign_in", {
                email: user.email,
                password: user.password
            })
                .then((response) => {
                    // console.log(response.data, response.status)
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
        }
    }
}