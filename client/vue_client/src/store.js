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
    content_id: 1,
    resource_url: null,
    resource_for: null,   // signal to fetch resource for course | section
    current_source_resource: {
      name: '',     // section | course
      id: -1        // source id
    }, 
    courses: [],
    contents: [],
    sections: [],
    resources: [],
    teachers: [],
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
    },
    error_response: {
      is_error: false,
      error_message: ''
    }
  },
  getters: {
    getCourses: (state) => state.courses,
    getResourceFor: (state) => state.resource_for,
    getCourseContents: (state) => state.contents,
    getLoaderStatus: (state) => state.loading,
    getResourceTabs: (state) => state.resource_tabs,
    getResourceUrl: (state) => state.resource_url,
    getResources: (state) => state.resources,
    getTeachers: (state) => state.teachers.filter(staff => staff.is_admin === false),
    getErrorResponse: (state) => state.error_response,
    getResourcesByType: (state) => {
      return state.resources.filter(resource => resource.type === state.resource_type.type);
    },
    getResourceById: (state) => (id) => {
      return state.resources.find(resource => resource.id === id);
    },
    getCurrentResourceSource: (state) => state.current_source_resource
  },
  mutations: {
    LOGOUT(state) {
      state.authUser = {
        token: '',
        isLoggedIn: false,
        userId: -1
      };
      state.role = 'student';
    },
    UPDATE_RESOURCE_FOR(state, type) {
      state.resource_for = type;
    },
    UPDATE_TEACHERS(state, staff) {
      state.teachers = staff;
    },
    UPDATE_CURRENT_SOURCE_RESOURCE(state, res) {
      state.current_source_resource = res;
    },
    UPDATE_CONTENT_ID(state, cont_id) {
      state.content_id = cont_id;
    },
    UPDATE_FORM(state, form) {
      state.form = form;
    },
    UPDATE_RESOURCE_URL(state, url) {
      state.resource_url = url;
    },
    UPDATE_ERROR_OBJ(state, error_obj) {
      state.error_response = error_obj;
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
      const path = baseUrl + 'contents/?course_id=' + state.course.id + '&skip=' + skip + '&limit=' + fetchLimit;

      commit('UPDATE_LOADING_STATUS', true);

      axios.get(path)
        .then((res) => {
          commit('SET_CONTENTS', res.data);
        })
        .catch((error) => {
          if(error.response) {
            // eslint-disable-next-line
            console.error(error.response.data);
            alert(error.response.data.detail);
          }

          else {
            console.log(error.message);
            console.error(error);
            alert(error.message);
          }

          commit('SET_CONTENTS', []);
        });
      
      commit('UPDATE_LOADING_STATUS', false);
    },
    async uploadResource({ commit, state, file, type, is_section }) {
      const section_path =  baseUrl + 'resources/section/?section_id=' + state.section.id + '&type=' + type;
      const course_path =  baseUrl + 'resources/course/?course_id=' + state.course.id + '&type=' + type;

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
    async fetchResources({ commit, state }) {
      var is_for = state.resource_for;

      var resource_path;

      console.log(state.resource_url);
      console.log('getting resources..');

      if(is_for) {
        if(is_for === 'course') {
          var type_id  = state.course.id; 
          resource_path = baseUrl + 'resources/course/' + type_id;
        }

        else {
          var sec_id  = state.section.id; 
          resource_path = baseUrl + 'resources/section/' + sec_id;
        }
      }

      else {
        return;
      }

      commit('UPDATE_LOADING_STATUS', true);

      console.log('fetching resources');

      axios.get(resource_path)
        .then((res) => {
          console.log('result');
          console.log(res.data);
          commit('SET_RESOURCES', res.data);
       
        })
        .catch((error) => {
          if(error.response) {
            // eslint-disable-next-line
            console.error(error.response.data);
            alert(error.response.data.detail);
          }

          else {
            console.log(error.message);
            console.error(error);
            alert(error.message);
          }
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
    async loginUser({ commit }, pp) {
      const path = baseUrl + 'users/login';
      
      commit('UPDATE_LOADING_STATUS', true);

      commit('UPDATE_ERROR_OBJ', {
        is_error: false,
        error_message: ''
      });

      console.log(pp);

      axios.post(path, pp)
        .then((res) => {

          console.log(res.data);
          
          var _role = 'student';

          var isAdmin = res.data.is_admin;

          if(isAdmin) {
            _role = 'admin';
          }

          else {
            _role = 'teacher';
          }

          var pl = {
            token: '82sshuds9sd9sdhd9dsy',
            isLoggedIn: true,
            userId: res.data.id
          };

          commit('UPDATE_AUTH_USER', pl);

          commit('UPDATE_USER_ROLE', _role);
        })
        .catch((error) => {
          if(error.response) {
            // eslint-disable-next-line
            commit('UPDATE_ERROR_OBJ', {
              is_error: true,
              error_message: error.response.data.detail
            });

            //alert(error.response.data.detail);
          }

          else {
            commit('UPDATE_ERROR_OBJ', {
              is_error: true,
              error_message: error.message
            });

            //alert(error.message);
          }
        });

      commit('UPDATE_LOADING_STATUS', false);

    },
    async addCourse({ commit, state }, pp) {
      // .. /courses/?form=form1
      const path = baseUrl + 'courses/?form=' + state.form;
      
      commit('UPDATE_LOADING_STATUS', true);

      console.log(pp);

      axios.post(path, pp)
        .then((res) => {
          console.log(res.data);
          
        })
        .catch((error) => {
          if(error.response) {
            // eslint-disable-next-line
            console.error(error.response.data);
            alert(error.response.data.detail);
          }

          else {
            console.log(error.message);
            console.error(error);
            alert(error.message);
          }
        });

      commit('UPDATE_LOADING_STATUS', false);

    },
    async addCourseContent({ commit, state }, pp) {
      // .. /courses/?form=form1
      const path = baseUrl + 'contents/' + state.course.id;
      
      commit('UPDATE_LOADING_STATUS', true);

      console.log(pp);

      axios.post(path, pp)
        .then((res) => {
          console.log(res.data);
          
        })
        .catch((error) => {
          if(error.response) {
            // eslint-disable-next-line
            console.error(error.response.data);
            alert(error.response.data.detail);
          }

          else {
            console.log(error.message);
            console.error(error);
            alert(error.message);
          }
        });

      commit('UPDATE_LOADING_STATUS', false);

    },
    async addContentSection({ commit }, pp) {
      const path = baseUrl + 'sections/' + pp.content + '/';
      
      commit('UPDATE_LOADING_STATUS', true);

      console.log(pp);

      axios.post(path, {
        'title': pp.title,
        'data': ''
      })
        .then((res) => {
          console.log(res.data);
          
        })
        .catch((error) => {
          if(error.response) {
            // eslint-disable-next-line
            console.error(error.response.data);
            alert(error.response.data.detail);
          }

          else {
            console.log(error.message);
            console.error(error);
            alert(error.message);
          }
        });

      commit('UPDATE_LOADING_STATUS', false);

    },
    async deleteCourse({ commit }, pp) {
      // .. /courses/?form=form1
      const path = baseUrl + 'courses/' + pp.id;
      
      commit('UPDATE_LOADING_STATUS', true);

      console.log(pp);

      axios.delete(path)
        .then((res) => {
          console.log(res.data);
          
        })
        .catch((error) => {
          if(error.response) {
            // eslint-disable-next-line
            console.error(error.response.data);
            alert(error.response.data.detail);
          }

          else {
            console.log(error.message);
            console.error(error);
            alert(error.message);
          }
        });

      commit('UPDATE_LOADING_STATUS', false);

    },
    async deleteResource({ commit }, pp) {
      const path = baseUrl + 'resources/' + pp.id;
      
      commit('UPDATE_LOADING_STATUS', true);

      console.log(pp);

      axios.delete(path)
        .then((res) => {
          console.log(res.data);
          
        })
        .catch((error) => {
          if(error.response) {
            // eslint-disable-next-line
            console.error(error.response.data);
            alert(error.response.data.detail);
          }

          else {
            console.log(error.message);
            console.error(error);
            alert(error.message);
          }
        });

      commit('UPDATE_LOADING_STATUS', false);

    },
    async fetchTeachers({ commit }) {
      const path = baseUrl + 'users/';
      
      commit('UPDATE_LOADING_STATUS', true);

      axios.get(path)
        .then((res) => {
          console.log(res.data);
          
          commit('UPDATE_TEACHERS', res.data);
        })
        .catch((error) => {
          if(error.response) {
            // eslint-disable-next-line
            console.error(error.response.data);
            alert(error.response.data.detail);
          }

          else {
            console.log(error.message);
            console.error(error);
            alert(error.message);
          }
        });

      commit('UPDATE_LOADING_STATUS', false);

    },
    async deleteTeacher({ commit }, pp) {
      const path = baseUrl + 'users/' + pp.id;
      
      commit('UPDATE_LOADING_STATUS', true);

      console.log(pp);

      axios.delete(path)
        .then((res) => {
          console.log(res.data);
          
        })
        .catch((error) => {
          if(error.response) {
            // eslint-disable-next-line
            console.error(error.response.data);
            alert(error.response.data.detail);
          }

          else {
            console.log(error.message);
            console.error(error);
            alert(error.message);
          }
        });

      commit('UPDATE_LOADING_STATUS', false);

    }
  }
});
