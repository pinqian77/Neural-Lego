import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import axios from "axios";

const app = createApp(App);

// Set global axios
app.config.globalProperties.$http = axios;

// App start
app.use(store).use(router).mount("#app");

// createApp(App).use(store).use(router).mount("#app");
