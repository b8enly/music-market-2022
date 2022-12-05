import axios from "../config/updateAxios";

export default {
    state: {
        count: 1,
        products: [],
        currentProduct: {},
        characteristicsLength: 0,
        cart: [],
        category: [],
        productsByName: [],
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
        },
        CART(state) {
            return state.cart;
        },
        CATEGORY(state) {
            return state.category;
        }
    },
    mutations: {
         SET_CATEGORY_PRODUCTS(state, products) {
             state.products = products;
        },
        SET_CURRENT_PRODUCT(state, product) {
            state.currentProduct = product;
            state.characteristicsLength = product.characteristics.length;
        },
        SET_CATEGORY(state, category) {
             state.category = category;
        },
        SET_CATEGORY_BY_NAME(state, categoryName) {
             this.productsByName =  state.category.findIndex(function (cat){
                 return cat.name === categoryName;
             });
        }
    },
    actions: {
        LOAD_PRODUCTS_BY_CATEGORY(ctx, {categoryId, page, pageSize}) {
            return axios
                .get('http://127.0.0.1:8000/api/products/categories/' + categoryId + '/products?page=' + page + '&page_size=' + pageSize)
                .then(async (data) => {
                    await ctx.commit('SET_CATEGORY_PRODUCTS', data.data)
                });
        },
        LOAD_PRODUCT_BY_ID(ctx, productId) {
            axios
                .get('http://127.0.0.1:8000/api/products/' +productId)
                .then(data => {
                    this.data = data;
                    ctx.commit('SET_CURRENT_PRODUCT', this.data.data)
                });
        },
        LOAD_CATEGORY(ctx) {
            return axios
                .get('http://127.0.0.1:8000/api/products/categories?count=5')
                .then(async (data) => {
                    await ctx.commit('SET_CATEGORY', data.data)
                })
        },
        LOAD_PRODUCTS_BY_CATEGORY_NAME(ctx, {categoryName}) {
            ctx.commit('SET_CATEGORY_BY_NAME', categoryName);
        }
    },
    modules: {}
}