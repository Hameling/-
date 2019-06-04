import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import BootstrapVue from 'bootstrap-vue'
import axios from 'axios'

import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

//ContentForm의 데이피커
import VueCtkDateTimePicker from 'vue-ctk-date-time-picker';
import 'vue-ctk-date-time-picker/dist/vue-ctk-date-time-picker.css';

//현재 시간을 얻기 위한 패키지
import moment from 'moment-timezone'

Vue.use(BootstrapVue)
Vue.config.productionTip = false
Vue.prototype.$http = axios

Vue.component('VueCtkDateTimePicker', VueCtkDateTimePicker);

moment.tz.setDefault('Asia/Seoul')


Vue.mixin({
  methods: {
    async checkToken(data){
      if(data.token === "expire"){
        //modal
        alert("세션이 만료되었습니다.")
        await this.$store.dispatch("LOGOUT")
        this.$router.push("/");
        location.reload()
      }
    }
  },
})

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
