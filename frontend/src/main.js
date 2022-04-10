import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import axios from "axios";
// import VueHighlightJS from "vue-highlightjs";

const app = createApp(App);
axios.defaults.baseURL = "/api"; // Do this so we don't need to write in xx.vue everytime
// app.use(VueHighlightJS); // Tell Vue.js to use vue-highlightjs
app.use(store).use(router).mount("#app");
