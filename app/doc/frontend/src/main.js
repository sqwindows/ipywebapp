import './assets/main.css'
import { createApp } from 'vue'
import App from './App.vue'
import initialization from './utils/common/initialization';

const app = createApp(App)

app.use(initialization)
app.mount('#app')
