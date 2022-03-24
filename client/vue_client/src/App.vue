<template>
  <v-app>
    <center>
      Offline eLearning Resource Management System (OeRMS)
    </center>
   
    <v-main>
      <v-container fluid />
      <router-view />
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
      </v-footer>
    </v-main>
  </v-app>
</template>

<script>

export default {
  name: 'App',

  data: () => ({
  })
};
</script>

<style>
#app {
  margin-top: 60px
}
</style>
