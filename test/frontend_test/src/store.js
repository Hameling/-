import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    uid: '',
    accessToken: null,
  },
  getters:{
    getUID: state => state.uid,
    getToken : state => state.accessToken,
  },
  mutations: {
    LOGIN(state, { id, accessToken }) {
      state.uid = id
      state.accessToken = accessToken
      sessionStorage.uid = id
      sessionStorage.accessToken = accessToken
    },
    LOGOUT(state) {
      state.uid = ""
      state.accessToken = null

      delete sessionStorage.uid
      delete sessionStorage.accessToken
    },
  },
  actions: {
    LOGIN({ commit }, { id, pwd }) {
      return new Promise((resolve, reject) => {
        axios.post('http://211.109.53.216:20000/session/create-session/', {
          memberid: id, memberpwd: pwd
        }).then(res => {
          if (res.data[0].token == "Not Matched") {
            reject("Not Matched")
          }
          else {
            commit('LOGIN', {
              id: id,
              accessToken: res.data[0].token
            })
            resolve()
          }
        })
      })

    },
    LOGOUT({ commit }) {
      commit('LOGOUT')
    }
  }
})
