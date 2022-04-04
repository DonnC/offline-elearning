<template>
  <div class="container">
    <div
      v-if="url"
    >
      <iframe
        :src="url"
        width="100%"
        height="100"
        frameborder="0"
      />
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
  name: 'PdfResourceVue',
  computed: {
    url() {
      return this.$store.getters.getResourceUrl;
    }
  }
};

</script>
