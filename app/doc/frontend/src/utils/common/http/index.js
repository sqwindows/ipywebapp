import interceptor from '@/utils/common/http/interceptor'
import pageWork from '@/utils/common/http/pageWork'

class Http {
    constructor(app, pageVm) {
        this.app = app;
        this.pageVm = pageVm
    }

    /**
     * 请求之前处理
     */
    _start(options = {}) {
        this.options = typeof options == 'object' ? options : {};
        this.pageWork = new pageWork(this.vm, this.pageVm, this.options).startRequest();
        return this;
    }

    /**
     * 请求结束处理
     * @param {Object} requestData
     */
    _then(requestData) {
        this.requestData = requestData;
        this.pageWork.endRequest();
        return this.requestData;
    }

    /**
     * 请求异常处理
     * @param {Object} catchError
     */
    _catch(catchError) {
        this.pageWork.endRequest();
        this.errorMsg = this.pageWork.parseCatchData(catchError);
        return this.errorMsg;
    }

    get(options = {}) {
        this._start(options);
        return new Promise((resolve, reject) => {
            interceptor({
                url: options.url,
                method: 'get',
                params: options.data || {}
            }).then(requestData => {
                resolve(this._then(requestData));
            }).catch(catchError => {
                reject(this._catch(catchError));
            })
        })
    }

    post(options = {}) {
        this._start(options);
        return new Promise((resolve, reject) => {
            interceptor({
                url: options.url || '',
                method: 'post',
                params: options.data || {}
            }).then(requestData => {
                resolve(this._then(requestData));
            }).catch(catchError => {
                reject(this._catch(catchError));
            })
        })
    }
}

Http.install = (app) => {
    app.config.globalProperties.interceptor = interceptor;
    app.config.globalProperties.http = (pageVm) => {
        return new Http(app, pageVm)
    };
}
export default Http