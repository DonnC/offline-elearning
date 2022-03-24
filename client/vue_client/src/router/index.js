import Vue from 'vue';
import VueRouter from 'vue-router';
import PingVue from '../components/PingVue.vue';
import BooksVue from '../components/BooksVue.vue';
import EditorVue from '../components/EditorVue.vue';
import CoursesVue from '../components/CoursesVue.vue';
import HomePageVue from '../components/HomePageVue.vue';
import VideoPlayerVue from '../components/VideoPlayerVue.vue';

Vue.use(VueRouter);

const routes = [
  {
    path: '/ping',
    name: 'PingVue',
    component: PingVue
  },
  {
    path: '/',
    name: 'HomePageVue',
    component: HomePageVue
  },
  {
    path: '/books',
    name: 'BooksVue',
    component: BooksVue
  },
  {
    path: '/editor',
    name: 'EditorVue',
    component: EditorVue
  },
  {
    path: '/player',
    name: 'VideoPlayerVue',
    component: VideoPlayerVue
  },
  {
    path: '/courses',
    name: 'CoursesVue',
    component: CoursesVue
  }
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
});

export default router;
