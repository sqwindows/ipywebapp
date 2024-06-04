import axios from 'axios';

// 创建axios实例
const interceptor = axios.create({
    baseURL: 'https://saas.maoren.la/app/idouyiner/home/',
    timeout: 5000 // 请求超时时间
});

// 请求拦截器
interceptor.interceptors.request.use(
    config => {

        return config;
    },
    error => {
        Promise.reject(error);
    }
);

// 响应拦截器
interceptor.interceptors.response.use(
    response => {
        return response.data;
    },
    error => {
        return Promise.reject(error);
    }
);

interceptor.install = (app) => {
    app.config.globalProperties.interceptor = interceptor;

}
export default interceptor;