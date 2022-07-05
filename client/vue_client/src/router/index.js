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
import ContentVue from '../components/ContentVue.vue';
import AddStaffVue from '../components/AddStaffVue.vue';
import StaffVue from '../components/StaffVue.vue';
import CourseDetailsVue from '../components/CourseDetailsVue.vue';
import ResourceVue from '../components/ResourceVue.vue';
import AddCourseVue from '../components/AddCourseVue.vue';
import AddCourseContentVue from '../components/AddCourseContentVue.vue';
import PdfResourceVue from '../components/PdfResourceVue.vue';
import AddContentSectionVue from '../components/AddContentSectionVue';

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
    path: '/add-course',
    name: 'AddCourseVue',
    component: AddCourseVue
  },
  {
    path: '/add-course-content',
    name: 'AddCourseContentVue',
    component: AddCourseContentVue
  },
  {
    path: '/add-content-section',
    name: 'AddContentSectionVue',
    component: AddContentSectionVue
  },
  {
    path: '/login',
    name: 'LoginVue',
    component: LoginVue
  },
  {
    path: '/content',
    name: 'ContentVue',
    component: ContentVue
  },
  {
    path: '/add-staff',
    name: 'AddStaffVue',
    component: AddStaffVue
  },
  {
    path: '/admin-staff',
    name: 'StaffVue',
    component: StaffVue
  },
  {
    path: '/course-detail',
    name: 'CourseDetailsVue',
    component: CourseDetailsVue
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
