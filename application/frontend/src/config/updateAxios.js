import Cookies from 'js-cookie';
import axios from "axios";

const instance = axios.create({
    baseUrl: "/",
})

instance.interceptors.request.use(
    function (config) {
        const { url, headers } = config;
        const token  = Cookies.get('token');
        if(url.startsWith("http://127.0.0.1:8000/api/products/")){
            headers["Authorization"] = `Token ${token}`;
        }
        else if (url.startsWith("http://127.0.0.1:8000/api/users/")) {
            headers["Authorization"] = token;
        }

        return config;
    },
    function (error){
        return Promise.reject(error)
    }
)
export default instance;