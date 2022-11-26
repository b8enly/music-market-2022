import axios from "../config/updateAxios";

export default {
    state:()=>({
        favorites: [],
    }),

    actions:{
        REQUEST_FAVORITES({commit}, parameters){
            return axios.get(`http://127.0.0.1:8000/api/products/favorites?user_id=${parameters.userId}&page=${parameters.page}&page_size=${parameters.pageSize}`, {})
                .then((response) => {
                    console.log(response.data)
                    commit('SET_FAVORITES', response.data)
                })
                .catch((error) => {
                    console.error(error);
                });
        },
    },
    mutations: {
        SET_FAVORITES: (state, favorites)=>{
            state.favorites = favorites
        }
    },
    getters: {
        FAVORITES(state){
            return state.favorites
        }
    }

}