import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import { plugin, defaultConfig } from '@formkit/vue'
import config from '@/../formkit.config';


const app = createApp(App);
app.use(plugin, defaultConfig(config));
app.use(router).mount('#app')