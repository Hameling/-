import Vue from 'vue'
import Router from 'vue-router'
import Workspace from './views/workspace'
import Title from './views/Title'
import Cal_Monthly from './components/calendar/Cal_Monthly'

import Main_Page from './components/Main_Page'


Vue.use(Router)

export default new Router({
  routes: [
    {
      path : '',
      component : Main_Page
    },
    {
      path: '/workspace',
      name: 'workspace',
      component: Workspace,
    },
    {
      path: '/title/:titleid',  //path: '/title/:titleid' 고려중
      name: 'title',
      component: Title,
      props:true
    },
  ],
  //mode: 'history'
})
