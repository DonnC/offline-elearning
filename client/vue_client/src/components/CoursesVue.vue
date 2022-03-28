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
    class="overlay"
  >
    Loading...
  </div>
</template>


<script>

export default {
  data() {
    return {
      loading: false
    };
  },
  computed: {
    courses() {
      return this.$store.getters.getCourses;
    }
  },
  mounted() {
    this.loading = true;
    this.$store.dispatch('fetchFormCourses');
    this.loading = false;
  }

};
</script>


<style scoped>
    .overlay {
      display: flex;
      align-items: center;
      justify-content: center;
      z-index: 10;
      color: #dc6868;
    }
</style>
