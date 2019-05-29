import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import BootstrapVue from 'bootstrap-vue'
import axios from 'axios'

import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

import VueCtkDateTimePicker from 'vue-ctk-date-time-picker';
import 'vue-ctk-date-time-picker/dist/vue-ctk-date-time-picker.css';

import moment from 'moment-timezone'



Vue.use(BootstrapVue)
Vue.config.productionTip = false
Vue.prototype.$http = axios

Vue.component('VueCtkDateTimePicker', VueCtkDateTimePicker);

moment.tz.setDefault('Asia/Seoul')

// axios.defaults.withCredentials = false
// axios.defaults.proxy = {
//   host: 'http://localhost',
//   port: 5000,
// };

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
