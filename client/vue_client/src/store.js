import Vue from 'vue';
import Vuex from 'vuex';
import axios from 'axios';
import { baseUrl, skip, fetchLimit } from './constants/constants.js';

Vue.use(Vuex);

export const store = new Vuex.Store({
  state: {
    form: 'form1',
    course: {},
    section: {},
    courses: [],
    contents: [],
    sections: [],
    resources: [],
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
    getResourcesByType: (state) => (type) => {
      return state.resources.filter(resource => resource.type === type);
    },
    getResourceById: (state) => (id) => {
      return state.resources.find(resource => resource.id === id);
    }
  },
  mutations: {
    UPDATE_FORM(state, form) {
      state.form = form;
    },
    UPDATE_USER_ROLE(state, role) {
      state.role = role;
    },
    UPDATE_EDITOR(state, data) {
      state.editor = data;
    },
    SET_COURSES(state, courses) {
      state.courses = courses;
    }
  },
  actions: {
    async fetchFormCourses({ commit, state }) {

      // /courses/?form=form3&skip=0&limit=500
      const path = baseUrl + 'courses/?form=' + state.form + '&skip=' + skip + '&limit=' + fetchLimit;

      axios.get(path)
        .then((res) => {
          commit('SET_COURSES', res.data);
        })
        .catch((error) => {
          // eslint-disable-next-line
          alert(error);
          console.error(error);
        });

    } 
  }
});
