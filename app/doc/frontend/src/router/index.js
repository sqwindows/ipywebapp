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
            path: '/example/windows',
            name: 'example_windows',
            component: () => import('@/views/home/example/WindowsView.vue')
        }
    ]
})

export default router
