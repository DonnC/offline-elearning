import Vue from 'vue';
import VueRouter from 'vue-router';
import PingVue from '../components/PingVue.vue';
import LoginVue from '../components/LoginVue.vue';
import BooksVue from '../components/BooksVue.vue';
import EditorVue from '../components/EditorVue.vue';
import CoursesVue from '../components/CoursesVue.vue';
import HomePageVue from '../components/HomePageVue.vue';
import VideoPlayerVue from '../components/VideoPlayerVue.vue';
import FormsVue from '../components/FormsVue.vue';
import ResourceVue from '../components/ResourceVue.vue';
import PdfResourceVue from '../components/PdfResourceVue.vue';

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
    path: '/resource',
    name: 'ResourceVue',
    component: ResourceVue
  },
  {
    path: '/login',
    name: 'LoginVue',
    component: LoginVue
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
    path: '/pdf',
    name: 'PdfResourceVue',
    component: PdfResourceVue
  },
  {
    path: '/courses',
    name: 'CoursesVue',
    component: CoursesVue
  },
  {
    path: '/forms',
    name: 'FormsVue',
    component: FormsVue
  }
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
});

export default router;
