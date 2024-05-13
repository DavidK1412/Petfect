import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap-icons/font/bootstrap-icons.css';
import { createApp } from 'vue';
import App from './App.vue';
import router from './router';
import { plugin, defaultConfig } from "@formkit/vue";
import config from '../formkit.config.js';
import VueSweetalert2 from "vue-sweetalert2";
import "sweetalert2/dist/sweetalert2.min.css";
import '@formkit/addons/css/multistep';


const app = createApp(App).use(router);
app.use(plugin, defaultConfig(config));
app.use(VueSweetalert2);
app.mount('#app');

import 'bootstrap/dist/js/bootstrap.min.js';