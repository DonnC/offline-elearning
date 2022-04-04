<template>
  <div
    v-if="!loading"
    class="main"
  > 
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
              height="400px"
              elevation="10"
              rounded
              outlined
              tile
              @click="onCourseTap(course)"
            >
              <v-card-subtitle>
                {{ course.content.length }} lessons
              </v-card-subtitle>
              <v-card-title>
                {{ course.name }}
              </v-card-title>
            </v-card>
          </div>
        </v-col>
      </v-row>
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

      // TODO go to course view page
    }
  }

};
</script>

