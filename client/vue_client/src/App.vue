<template>
  <v-app>
    <v-app-bar app>
      <v-app-bar-title>Offline eLearning Resource Management System (OeRMS)</v-app-bar-title>
      <v-spacer />
      <v-btn
        v-if="role != 'student'"
        color="red"
        @click="logout"
      >
        Logout
      </v-btn>
    </v-app-bar>
   
    <v-main>
      <v-container fluid />
      <router-view />
      <!-- <v-footer
        class="text-blue text-center d-flex flex-column"
        max-height="110"
        app
      >
        <div>
          Offline eLearning Resource Management System - an elegant eLearning system to learn on the go offline <br>
          <b>Student Number:</b> N0173320W <br>
        </div>
        <br>
        <div class="text-black">
          {{ new Date().getFullYear() }} — <strong>Nust Final Year Project</strong>
        </div>
      </v-footer> -->
    </v-main>
  </v-app>
</template>

<script>

export default {
  name: 'App',

  data: () => ({
  }),
  computed: {
    role() {
      return this.$store.state.role;
    }
  },
  methods: {
    logout() {
      this.$router.replace('/');
    }
  }
};

</script>

<style>
#app {
  margin-top: 60px
}
</style>
