<template>
  <div
    v-if="!loading"
    class="main"
  >
    <div
      class="p-4"
    >
      <v-btn
        v-if="role != 'student'"
        width="200"
        color="blue"
        class="white--text"
        @click="gotoAddCourse"
      >
        Add Course
        <v-icon
          right
        >
          mdi-pencil
        </v-icon>
      </v-btn>
    </div>
   
   
    <v-container
      v-if="courses.length > 0"
    >
      <v-row>
        <h4>
          {{ form }} Courses
        </h4>
      </v-row>
      
      <br>
    
      <v-container class="grey lighten-5">
        <v-row>
          <v-col
            v-for="course in courses"
            :key="course.id"
            cols="12"
            md="6"
            lg="4"
            xl="4"
          >
            <div class="p-4">
              <v-card
                height="330px"
                elevation="3"
                rounded
                @click="onCourseTap(course)"
              >
                <v-responsive>
                  <v-icon
                    class="pl-12"
                    size="150px"
                  >
                    mdi-book-open-variant
                  </v-icon>
                </v-responsive>
               
                <v-spacer />
                <v-card-title>
                  {{ course.name }}
                </v-card-title>
                <v-card-subtitle>
                  {{ course.content.length }} lesson(s)
                </v-card-subtitle>
                <v-card-actions>
                  <v-dialog
                    v-if="role != 'student'"
                    v-model="dialog"
                    persistent
                    max-width="290"
                  >
                    <template #activator="{ on, attrs }">
                      <v-btn
                        color="red"
                        dark
                        v-bind="attrs"
                        v-on="on"
                      >
                        Delete
                      </v-btn>
                    </template>
                    <v-card>
                      <v-card-title class="text-h5">
                        Confirm delete?
                      </v-card-title>
                      <v-card-text>
                        Please note that deleting a course is permanent.
                        After deleting, this course will not be available to students.
                      </v-card-text>
                      <v-card-actions>
                        <v-spacer />
                        <v-btn
                          color="green darken-1"
                          text
                          @click="dialog = false"
                        >
                          Abort
                        </v-btn>
                        <v-btn
                          color="red darken-1"
                          text
                          @click="deleteCourse(course.id)"
                        >
                          Confirm
                        </v-btn>
                      </v-card-actions>
                    </v-card>
                  </v-dialog>
                </v-card-actions>
              </v-card>
            </div>
          </v-col>
        </v-row>
      </v-container>
    </v-container>
    
    
    <v-container
      v-else
    >
      <center>
        <div
          class="p-5"
          align="center"
        >
          <v-icon
            large
          >
            mdi-school
          </v-icon>
          <v-spacer />
          No {{ form }} courses found!
        </div>
      </center>
    </v-container>
  </div>

  <div
    v-else
  >
    <v-progress-circular
      :size="70"
      :width="7"
      color="blue"
      indeterminate
    />
  </div>
</template>


<script>

//  color="#5695E8" // card color
export default {
  data () {
    return {
      dialog: false
    };
  },
  computed: {
    role() {
      return this.$store.state.role;
    },
    courses() {
      return this.$store.getters.getCourses;
    },
    form() {
      return this.$store.state.form;
    },
    loading() {
      return this.$store.getters.getLoaderStatus;
    }
  },
  mounted() {
    this.$store.dispatch('fetchFormCourses');
  },
  methods: {
    gotoAddCourse() {
      this.$router.push('/add-course');
    },
    onCourseTap(course) {
      this.$store.commit('SET_COURSE', course);

      this.$store.commit('SET_CONTENTS', []);

      // go to course view page
      this.$router.push('/course-detail');
    },
    deleteCourse(course_id) {
      this.dialog = false;
      this.$store.dispatch('deleteCourse', {'id': course_id});

      this.$store.dispatch('fetchFormCourses');
    }
  }

};
</script>

