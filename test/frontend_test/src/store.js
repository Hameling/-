import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    acessToken : null,
    uid : ''
  },
  mutations: {
    LOGIN (state, {accessToken}) {
      state.accessToken = accessToken
      localStorage.accessToken = accessToken
    },
    LOGOUT (state) {
      state.accessToken = null;
      delete localStorage.accessToken
    }
  },
  actions: {
    LOGIN({commit}, {id, pwd}) {
      return this.$http.post("211.109.53.216/member", {id, pwd})
      .then(({data}) => {
          commit('LOGIN',data)
          $http.defaults.headers.common['Authorization'] = data.accessToken
      }
  )},
    LOGOUT({commit}){
      $http.defaults.headers.common['Authorization'] = undefined
      commit('LOGOUT')
  }
  }
})
