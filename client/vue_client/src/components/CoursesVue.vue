<template>
  <div
    v-if="!loading"
    class="main"
  >
    <v-container
      v-if="courses.length > 0"
    >
      <h4>
        {{ form }} Courses
      </h4>
      <br>
    
      <v-container class="grey lighten-5">
        <v-row
          style="height: 150px;"
        >
          <v-col
            v-for="course in courses"
            :key="course.id"
            cols="4"
          >
            <div class="p-4">
              <v-card
                height="330px"
                elevation="3"
                rounded
                @click="onCourseTap(course)"
              >
                <v-responsive :aspect-ratio="4/2.3">
                  <v-icon
                    size="200px"
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

export default {
  computed: {
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
    onCourseTap(course) {
      this.$store.commit('SET_COURSE', course);

      // go to course view page
      this.$router.push('/content');
    }
  }

};
</script>

