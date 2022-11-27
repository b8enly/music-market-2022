import axios from "../config/updateAxios";

export default {
    state: {
        count: 1,
        products: [],
        currentProduct: {},
        characteristicsLength: 0,
    },
    getters: {
        CATEGORY_PRODUCTS(state) {
            return state.products;
        },
        CURRENT_PRODUCT(state) {
            return state.currentProduct;
        },
        CHARACTERISTICS_LENGTH(state) {
            return state.characteristicsLength;
        }
    },
    mutations: {
         SET_CATEGORY_PRODUCTS(state, products) {
             state.products = products;
            console.log(state.products);
        },
        SET_CURRENT_PRODUCT(state, product) {
            state.currentProduct = product;
            state.characteristicsLength = product.characteristics.length;
        },
    },
    actions: {
         LOAD_PRODUCTS_BY_CATEGORY(ctx, {categoryId, page, pageSize}) {
              axios
                .get('http://127.0.0.1:8000/api/products/categories/' +categoryId +'/products?page='+page+'&page_size='+pageSize)
                .then(async (data) => {
                    console.log(data.data);
                    await ctx.commit('SET_CATEGORY_PRODUCTS', data.data)
                });
        },
        LOAD_PRODUCT_BY_ID(ctx, productId) {
            axios
                .get('http://127.0.0.1:8000/api/products/' +productId)
                .then(data => {
                    this.data = data;
                    // console.log(this.data.data);
                    ctx.commit('SET_CURRENT_PRODUCT', this.data.data)
                });
        },
    },
    modules: {}
}