import Vue from 'vue'
import Router from 'vue-router'
import Workspace from './views/workspace'
import Title from './views/Title'
import Cal_Monthly from './components/calendar/Cal_Monthly'

import Empty_Page from './components/Empty_Page'


Vue.use(Router)

export default new Router({
  routes: [
    {
      path : '',
      component : Empty_Page
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
