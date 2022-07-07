<template>
  <div
    class="p-4"
  >
    <h1> Notes</h1>
    <v-btn
      v-if="url != null"
      class="text-white"
      color="blue"
      @click.prevent="downloadItem()"
    >
      download pdf
    </v-btn>
   
    <vue-pdf-embed
      :source="url"
    />
  </div>
</template>

<script>
import axios from 'axios';
import VuePdfEmbed from 'vue-pdf-embed/dist/vue2-pdf-embed';

export default {
  components: {
    VuePdfEmbed
  },
  computed: {
    url() {
      return this.$store.getters.getResourceUrl;
    }
  },
  methods: {
    async downloadItem() {
      console.log(this.url);
      if(this.url != null) {
        const response = await axios.get(this.url, { responseType: 'blob' });
        const blob = new Blob([ response.data ]);
        const link = document.createElement('a');
        link.href = window.URL.createObjectURL(blob);
        var filename = this.url.substring(this.url.lastIndexOf('/')+1);
        link.setAttribute('download', filename);
        document.body.appendChild(link);
        link.click();
        window.URL.revokeObjectURL(link.href);
      }
    
    }
  }
};
</script>
