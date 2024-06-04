class pageWork {
    constructor(app, pageVm, options = {}) {
        this.app = app;
        this.pageVm = pageVm || {};
        this.options = options;
    }

    /**
     * 调用接口：请求之前处理
     * @return {object} this
     */
    startRequest() {
        this.pageVm.loading = true
        return this;
    }

    /**
     * 调用接口结束请求
     * @return {object} this
     */
    endRequest() {
        this.pageVm.loading = false
        return this;
    }

    /**
     * 调用接口：解析异常信息
     * @param {Any} res
     * @return {string}
     */
    parseCatchData(res) {
         console.info(res)
        let err = ''
        if (res.response && res.response.status) {
            err = this._parseHttpStatusCode(res.response.status)
        } else {
            err = this._parseAxiosErrorKey(res.message)
        }

        return err
    }

    /**
     * 解析Uni.request错误KEY 部分KEY
     * @param {Object} key
     */
    _parseAxiosErrorKey(message) {

        let msgs = {
            'Network Error': '网络异常',
            'timeout of': '请求已超时',
            //...其他KEY在此完善
        };
        let msg = ''
        for (let key in msgs) {
            if (message.includes(key)) {
                msg = msgs[key]
                break
            }
        }
        return msg || message;
    }

    /**
     * 解析HTTP状态码
     * @param {int} status
     * @return {string}
     */
    _parseHttpStatusCode(status = 0, msg = '') {
        let statusCodes = {
            401: msg || '无权访问或登录失效',
            404: msg || '页面不存在',
            500: msg || '服务端异常',
            502: msg || '服务端连接超时',
            //...其他状态码在此完善
        };
        return statusCodes[status] || '服务端响应发生异常';
    }


}

export default pageWork;