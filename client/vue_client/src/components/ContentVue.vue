<template>
  <v-container>
    <h4>Table of Contents</h4>
    <LayoutColumns
      column-count="1"
    >
      <v-col>
        <v-container
          v-if="contents.length > 0"
        >
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
               
                @click="updateSelected(content, sec)"
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

        <v-container
          v-else
        >
          <center>
            <div class="p-5">
              No course content found!
            </div>
          </center>
        </v-container>
      </v-col>

      <v-divider />
      
      <h4>Notes</h4>

    
      <!-- section data -->
      <v-container>
        <v-col>
          <LayoutFlexRow>
            <template #left>
              <v-btn
                v-if="role != 'student'"
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
            </template>
            <template #right>
              <v-btn
                color="blue"
                class="ma-2 white--text"
                @click="gotoSectionResource"
              >
                Resources
                <v-icon
                  right
                >
                  mdi-file-multiple
                </v-icon>
              </v-btn>
            </template>
          </LayoutFlexRow>
       
          <br>
          <div
            v-if="section.data"
            v-html="section.data"
          />

          <div 
            v-else
          >
            <center>
              No Notes available!
            </center>
          </div>
        </v-col>
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
    };
  },
  computed: {
    role() {
      return this.$store.state.role;
    },
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
    updateSelected(cont, sec) {
      console.log('received cont');
      console.log(cont);
      console.log('updating section');
      console.log(sec);
      this.$store.commit('UPDATE_EDITOR_CONTENT', cont.topic);
      this.$store.commit('SET_SECTION', sec);

      this.selectedSection = sec.id;
    },
    gotoSectionResource() {
      this.$store.commit('UPDATE_RESOURCE_FOR', 'section');
      this.$store.commit('UPDATE_CURRENT_SOURCE_RESOURCE', {
        name: 'section',    
        id: this.section.id      
      });
      this.$router.push('/resource');
    }
  }

};
</script>
