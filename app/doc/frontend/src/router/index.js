import {createRouter, createWebHashHistory} from 'vue-router'

const router = createRouter({
    history: createWebHashHistory(import.meta.env.BASE_URL), //createWebHashHistory  createWebHistory
    routes: [
        {
            path: '/',
            name: 'home',
            component: () => import('@/views/home/index/IndexView.vue')
        },
        {
            path: '/example/case.windows',
            name: 'case.windows',
            component: () => import('@/views/home/example/CaseWindows.vue')
        },
          {
            path: '/example/case.other',
            name: 'case.other',
            component: () => import('@/views/home/example/CaseOther.vue')
        }
    ]
})

export default router
