<template>
  <v-container>
    <v-col>
      <h4> {{ course.name }} </h4> 
      {{ course.synopsis }}
      <br>
      {{ course.description }}
    </v-col>

    <v-container>
      <v-btn
        color="blue"
        class="ma-2 white--text"
        @click="gotoEditor"
      >
        Course Resources
        <v-icon
          right
        >
          mdi-pencil
        </v-icon>
      </v-btn>
      <br>
    </v-container>
    
    <br>
    <br>
    <h5>  Course Outline </h5>
    <LayoutColumns
      column-count="2"
      flow-direction="row"
      vertical-align="stretch"
      gap-x="10"
      gap-y="5"
    >
      <v-col>
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
                @click="gotoContent()"
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
    course() {
      return this.$store.state.course;
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
    gotoContent() {
      this.$router.push('/content');
    }
  }

};
</script>
