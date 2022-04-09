<template>
  <v-container>
    <LayoutColumns
      column-count="2"
      flow-direction="row"
      vertical-align="stretch"
      gap-x="10"
      gap-y="10"
    >
      <v-col
        sm="7"
      >
        <v-container>
          <v-list>
            <v-list-group
              v-for="content in contents"
              :key="content.id"
              no-action
            >
              <template #activator>
                <v-list-item-content>
                  <v-list-item-title v-text="content.topic" />
                </v-list-item-content>
              </template>

              <v-list-item
                v-for="sec in content.sections"
                :key="sec.id"
               
                @click="updateSelected(sec)"
              >
                <v-list-item-content>
                  <div :style="{color: sec.id === selectedSection ? 'dodgerblue' : 'slategrey'}">
                    <v-list-item-title v-text="sec.title" />
                  </div>
                </v-list-item-content>
              </v-list-item>
            </v-list-group>
          </v-list>
        </v-container>
      </v-col>


      <!-- section data -->
      <v-container>
        <v-btn
          color="blue"
          class="ma-2 white--text"
          @click="gotoEditor"
        >
          Edit
          <v-icon
            right
          >
            mdi-pencil
          </v-icon>
        </v-btn>
        <br>
        <div
          v-html="section.data"
        />
      </v-container>
    </LayoutColumns>
  </v-container>
</template>


<script>
import vueLayoutComponents from 'vue-layout-system';
import 'vue-layout-system/dist/vue-layout-system.css';


export default {
  components: {
    ...vueLayoutComponents
  },
  data() {
    return {
      selectedSection: 0
      // contents: [
      //   {
      //     topic: 'Introduction',
      //     description: '',
      //     id: 0,
      //     sections: [
      //       {
      //         title: 'Who is this for?',
      //         id: 0,
      //         data: ''
      //       },
      //       {
      //         title: 'What are we building?',
      //         id: 1,
      //         data: ''
      //       }
      //     ]
      //   },
      //   {
      //     topic: 'Prerequisites',
      //     description: '',
      //     id: 1,
      //     sections: [
      //       {
      //         title: 'Python',
      //         id: 2,
      //         data: ''
      //       },
      //       {
      //         title: 'MariaDB/Postgres',
      //         id: 3,
      //         data: ''
      //       },
      //       {
      //         title: 'Git/Github',
      //         id: 4,
      //         data: ''
      //       }
      //     ]
      //   },
      //   {
      //     topic: 'Install and Setup Bench',
      //     description: '',
      //     id: 2,
      //     sections: [
      //       {
      //         title: 'Installation',
      //         id: 5,
      //         data: ''
      //       },
      //       {
      //         title: 'Directory Structure',
      //         id: 6,
      //         data: ''
      //       }
      //     ]
      //   },
      //   {
      //     topic: 'Create an App',
      //     description: '',
      //     id: 3,
      //     sections: [
      //       {
      //         title: 'Create an app',
      //         id: 7,
      //         data: ''
      //       },
      //       {
      //         title: 'App structure',
      //         id: 8,
      //         data: ''
      //       }
      //     ]
      //   },
      //   {
      //     topic: 'Create a site',
      //     description: '',
      //     id: 4,
      //     sections: [
      //       {
      //         title: 'Create a new site',
      //         id: 9,
      //         data: ''
      //       },
      //       {
      //         title: 'Login to desk',
      //         id: 10,
      //         data: ''
      //       }
      //     ]
      //   }
      // ]
    };
  },
  computed: {
    contents() {
      return this.$store.getters.getCourseContents;
    },
    section() {
      return this.$store.state.section;
    }
  },
  mounted() {
    // fetch course contents
    this.$store.dispatch('fetchCourseContents');
  },
  
  methods: {
    gotoEditor() {
      this.$router.push('/editor');
    },
    updateSelected(sec) {
      this.$store.commit('SET_SECTION', sec);

      this.selectedSection = sec.id;
    }
  }

};
</script>
