<template>
  <div class="player-container p-3">
    <div
      v-if="url"
    >
      <v-card>
        <vue-core-video-player
          :src="url"
        />
      </v-card>
    </div>

    <div
      v-else
    >
      <center>
        Failed to get resource 
      </center>
    </div>
  </div>
</template>

<script>

export default {

  computed: {
    url() {
      return this.$store.getters.getResourceUrl;
    }
  }
};
</script>

