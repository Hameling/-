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
      //name: 'workspace',
      component: Workspace,
      children: [
        {
          path: '',
          name: 'Cal_Monthly',
          component: Cal_Monthly
        },
        //캘린더 두개 더 추가
      ],
      //다른 path추가 login, project
      //create project는 어떤식으로 할것인가?
    },
    {
      path: '/title',
      name: 'title',
      component: Title,
      props:true
    },
  ],
  mode: 'history'
})
