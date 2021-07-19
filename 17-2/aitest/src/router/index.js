import Vue from 'vue'
import VueRouter from 'vue-router'
// import Home from '../views/Home.vue'
import SignIn from '../components/SignIn.vue'
import SignUp from '../components/Signup.vue'
import Case from '../components/Case.vue'
import Jenkins from '../components/Jenkins.vue'
import Task from '../components/Task.vue'
import Report from '../components/Report.vue'


// 解决tab页面自我跳转报错
const originalPush = VueRouter.prototype.push

VueRouter.prototype.push = function push(location){
  return originalPush.call(this,location).catch(err => err)
}


Vue.use(VueRouter)

const routes = [
  // {
  //   path: '/',
  //   name: 'Home',
  //   component: Home
  // },
  // {
  //   path: '/about',
  //   name: 'About',
  //   // route level code-splitting
  //   // this generates a separate chunk (about.[hash].js) for this route
  //   // which is lazy-loaded when the route is visited.
  //   component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  // }
  {
    path: '/',
    name: 'SignIn',
    component: SignIn
  },
  {
    path: '/sign-up',
    name: 'SignUp',
    component: SignUp
  },
  {
    path: '/case',
    name: 'Case',
    component: Case
  },
  {
    path: '/jenkins',
    name: 'Jenkins',
    component: Jenkins
  },
  {
    path: '/task',
    name: 'Task',
    component: Task
  },
  {
    path: '/report',
    name: 'Report',
    component: Report
  },
]

const router = new VueRouter({
  routes
})

export default router
