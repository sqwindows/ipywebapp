import 'core-js'
import router from '@/router/index';
import fn from '@/utils/common/function.js'
import http from '@/utils/common/http'
import element from '@/utils/common/element'

export default {
    install(app) {
        app.use(http)//挂载http
        app.use(router) //挂载路由
        app.use(element)//挂载elementPlus
        //挂载公共方法
        Object.defineProperties(app.config.globalProperties, {
            fn: {
                get() {
                    return fn
                }
            }
        })
    }

}
