import { createRouter, createWebHistory } from 'vue-router'
//import HomeView from '../views/HomeView.vue'
import App from '../App.vue'
import Editor from '../components/Editor.vue'
import Home from '../components/Home.vue'
import Settings from '../components/Settings.vue'
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
     {
      path: '/',
      name: 'Home',
      component: Home
    },
    {
      path: '/Editor/',
      name: 'Editor',
      component: Editor
    },
    {
      path: '/Settings/',
      name: 'Settings',
      component: Settings
    },
  ]
})

export default router
