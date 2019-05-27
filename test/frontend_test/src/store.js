import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    uid: '',
    accessToken: null,
    enrollList : [],
    assignList : []
  },
  mutations: {
    LOGIN(state, { id, accessToken }) {
      state.uid = id
      state.accessToken = accessToken
      localStorage.uid = id
      localStorage.accessToken = accessToken
    },
    LOGOUT(state) {
      state.uid = ""
      state.accessToken = null

      delete localStorage.uid
      delete localStorage.accessToken
    },
    SETBASE_DATA(state, {enrollList, assignList}){
      state.enrollList = enrollList
      state.assignList = assignList
    }
  },
  actions: {
    LOGIN({ commit }, { id, pwd }) {
      return new Promise((resolve, reject) => {
        axios.post('http://211.109.53.216:20000/member/login/', {
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
            commit('SETBASE_DATA', {
              enrollList : res.data[0].enrollTitle,
              assignList : res.data[0].assignContent
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
