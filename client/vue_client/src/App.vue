<template>
  <v-app>
    <v-app-bar app>
      <v-app-bar-title>Offline eLearning Resource Management System (OeRMS)</v-app-bar-title>
      <v-spacer />
      <div
        class="p-2"
      >
        <v-btn
          v-if="role === 'admin' && authUser.isLoggedIn"
          class="text-white"
          color="blue"
          @click="gotoStaff"
        >
          Manage Staff
        </v-btn>
      </div>
     
      <div
        class="p-4"
      >
        <v-btn
          class="text-white"
          color="blue"
          @click="gotoHome"
        >
          Home
        </v-btn>
      </div>

      <v-btn
        v-if="role != 'student' && authUser.isLoggedIn"
        class="text-white"
        color="red"
        @click="logout"
      >
        Logout
      </v-btn>
    </v-app-bar>
   
    <v-main>
      <v-container fluid />
      <router-view />
      <!-- 
        TODO: Add manage staff
        <v-footer
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
    },
    authUser() {
      return this.$store.state.authUser;
    }
  },
  methods: {
    logout() {
      this.$store.commit('LOGOUT');
      this.$store.commit('UPDATE_USER_ROLE', 'student');
      this.$router.replace('/');
    },
    gotoHome() {
      this.$router.replace('/');
    },
    gotoStaff() {
      if(this.role === 'admin') {
        this.$router.replace('/admin-staff');
      }
    }
  }
};

</script>

<style>
#app {
  margin-top: 60px
}
</style>
