import Vue from 'vue';
import Vuex from 'vuex';
import axios from 'axios';
import { baseUrl, skip, fetchLimit } from './constants/constants.js';

Vue.use(Vuex);

export const store = new Vuex.Store({
  state: {
    loading: false,
    form: 'form1',
    course: {
      id: 1
    },
    section: {
      id: 1
    },
    resource_url: null,
    courses: [],
    contents: [],
    sections: [],
    resources: [],
    resource_type: {
      name: 'Books',
      icon: 'mdi-book-open-page-variant-outline',
      type: 'book'
    },
    resource_tabs: [
      {
        name: 'Books',
        icon: 'mdi-book-open-page-variant-outline',
        type: 'book'
      },
      {
        name: 'Exam Papers',
        icon: 'mdi-file-document-edit',
        type: 'exam'
      },
      {
        name: 'Tests',
        icon: 'mdi-file-percent',
        type: 'test'
      },
      {
        name: 'Exercises',
        icon: 'mdi-file-cog',
        type: 'exercise'
      },
      {
        name: 'Assignments',
        icon: 'mdi-text-box-check',
        type: 'assignment'
      },
      {
        name: 'Videos',
        icon: 'mdi-youtube',
        type: 'video'
      },
      {
        name: 'Others',
        icon: 'mdi-dots-horizontal-circle',
        type: 'other'
      }
    ],
    editor: '',
    role: 'student', // student | teacher | admin
    // authenticated user teacher | admin
    authUser: {
      token: '',
      isLoggedIn: false,
      userId: -1
    }
  },
  getters: {
    getCourses: (state) => state.courses,
    getCourseContents: (state) => state.contents,
    getLoaderStatus: (state) => state.loading,
    getResourceTabs: (state) => state.resource_tabs,
    getResourceUrl: (state) => state.resource_url,
    getResourcesByType: (state) => {
      return state.resources.filter(resource => resource.type === state.resource_type.type);
    },
    getResourceById: (state) => (id) => {
      return state.resources.find(resource => resource.id === id);
    }
  },
  mutations: {
    UPDATE_FORM(state, form) {
      state.form = form;
    },
    UPDATE_RESOURCE_URL(state, url) {
      state.resource_url = url;
    },
    UPDATE_RESOURCE_TYPE(state, type) {
      state.resource_type = type;
    },
    UPDATE_LOADING_STATUS(state, status) {
      state.loading = status;
    },
    UPDATE_AUTH_USER(state, authU) {
      state.authUser = authU;
    },
    UPDATE_USER_ROLE(state, role) {
      state.role = role;
    },
    UPDATE_EDITOR(state, data) {
      state.editor = data;
    },
    SET_COURSES(state, courses) {
      state.courses = courses;
    },
    SET_CONTENTS(state, contents) {
      state.contents = contents;
    },
    SET_COURSE(state, course) {
      state.course = course;
    },
    SET_SECTION(state, section) {
      state.section = section;
    },
    SET_SECTION_DATA(state, data) {
      var current =  state.section;

      current['data'] = data;

      state.section = current;
    },
    SET_RESOURCES(state, resources) {
      state.resources = resources;
    }
  },
  actions: {
    async fetchFormCourses({ commit, state }) {
      // /courses/?form=form3&skip=0&limit=500
      const path = baseUrl + 'courses/?form=' + state.form + '&skip=' + skip + '&limit=' + fetchLimit;

      commit('UPDATE_LOADING_STATUS', true);

      axios.get(path)
        .then((res) => {
          commit('SET_COURSES', res.data);
        })
        .catch((error) => {
          // eslint-disable-next-line
          alert(error);
          console.error(error);
        });
      
      commit('UPDATE_LOADING_STATUS', false);
    },
    async fetchCourseContents({ commit, state }) {
      const path = baseUrl + 'contents/?course_id' + state.course.id + '&skip=' + skip + '&limit=' + fetchLimit;

      commit('UPDATE_LOADING_STATUS', true);

      axios.get(path)
        .then((res) => {
          commit('SET_CONTENTS', res.data);
        })
        .catch((error) => {
          // eslint-disable-next-line
          alert(error);
          console.error(error);
        });
      
      commit('UPDATE_LOADING_STATUS', false);
    },
    async uploadResource({ commit, state, file, type, is_section }) {
      const section_path =  baseUrl + 'resources/section/?section_id' + state.section.id + '&type=' + type;
      const course_path =  baseUrl + 'resources/course/?course_id' + state.course.id + '&type=' + type;

      const path = is_section ? section_path : course_path;
      
      commit('UPDATE_LOADING_STATUS', true);

      var formData = new FormData();

      formData.append('file', file);

      axios.post({
        url: path, 
        data: formData
      })
        .then((res) => {
          // TODO fetch latest
          res;

        })
        .catch((error) => {
          // eslint-disable-next-line
          alert(error);
          console.error(error);
        });
      
      commit('UPDATE_LOADING_STATUS', false);
    },
    async fetchCourseResources({ commit, state }) {
      var courseId = state.course.id; 
      const path = baseUrl + 'resources/course/' + courseId;

      commit('UPDATE_LOADING_STATUS', true);

      axios.get(path)
        .then((res) => {
          commit('SET_RESOURCES', res.data);
       
        })
        .catch((error) => {
          // eslint-disable-next-line
          alert(error);
          console.error(error);
        });

      commit('UPDATE_LOADING_STATUS', false);
    },
    async updateSection({ commit, state }) {
      var data = state.section;
      const path = baseUrl + 'sections/';

      console.log(data);

      commit('UPDATE_LOADING_STATUS', true);

      axios.patch(path, data)
        .then((res) => {
          commit('SET_SECTION', res.data);
       
        })
        .catch((error) => {
          // eslint-disable-next-line
          alert(error);
          console.error(error);
        });

      commit('UPDATE_LOADING_STATUS', false);
    },
    async fetchSectionResources({ commit, state }) {
      var sectionId = state.section.id;
      const path = baseUrl + 'resources/section/' + sectionId;

      commit('UPDATE_LOADING_STATUS', true);

      axios.get(path)
        .then((res) => {
          commit('SET_RESOURCES', res.data);
        })
        .catch((error) => {
          // eslint-disable-next-line
          alert(error);
          console.error(error);
        });

      commit('UPDATE_LOADING_STATUS', false);
    },
    async loginUser({ commit, payload }) {
      const path = baseUrl + 'users/login';
      
      commit('UPDATE_LOADING_STATUS', true);

      axios.post(path, payload)
        .then((res) => {
          // ! token needed TODO Add proper token
          // localStorage.setItem('todo_items', JSON.stringify(this.todo_items));
          // if (localStorage.getItem('todo_items'))
          // this.todo_items = JSON.parse(localStorage.getItem('todo_items'));
          var pl = {
            token: '82sshuds9sd9sdhd9dsy',
            isLoggedIn: true,
            userId: res.id
          };

          commit('UPDATE_AUTH_USER', pl);
        })
        .catch((error) => {
          // eslint-disable-next-line
          alert(error);
          console.error(error);
        });

      commit('UPDATE_LOADING_STATUS', false);

    } 
  }
});
