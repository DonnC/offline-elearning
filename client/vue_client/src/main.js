import BootstrapVue from 'bootstrap-vue';
import Vue from 'vue';
import App from './App.vue';
import router from './router';
import vuetify from './plugins/vuetify';
import 'bootstrap/dist/css/bootstrap.css';
import VueCoreVideoPlayer from 'vue-core-video-player';
import VueResizeText from 'vue-resize-text';



import { store } from './store.js';

Vue.use(VueResizeText);

Vue.use(VueCoreVideoPlayer);

Vue.use(BootstrapVue);

Vue.config.productionTip = false;

new Vue({
  router,
  vuetify,
  store,
  render: (h) => h(App)
}).$mount('#app');
