import {fileURLToPath, URL} from 'node:url'
import {defineConfig} from 'vite'
import vue from '@vitejs/plugin-vue'
import legacy from '@vitejs/plugin-legacy'

// https://vitejs.dev/config/
export default defineConfig({
    base: './',
    plugins: [
        vue(),
        legacy()
    ],
    build: {
        outDir: '../resources'
    },
    server: {
        host: '0.0.0.0',
        port: '8090', // 指定启动端口
        open: false //启动后是否自动打开浏览器
    },
    resolve: {
        alias: {
            '@': fileURLToPath(new URL('./src', import.meta.url))
        }
    }
})
