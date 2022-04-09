import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";

import axios from "axios";

const app = createApp(App);
axios.defaults.baseURL = "/api"; // Do this so we don't need to write in xx.vue everytime
app.use(store).use(router).mount("#app");
