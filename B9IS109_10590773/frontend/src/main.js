import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import "bootstrap/dist/css/bootstrap.css";
import Axios from "axios";

const app = createApp(App);
// global axios  setup
app.config.globalProperties.$axios = Axios;
// base url for server configuration
app.config.globalProperties.$base_url = "https://back-end-blood-donation-app.herokuapp.com";
app.use(router);

app.mount("#app");
