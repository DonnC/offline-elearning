<template>
  <div>
    <center>
      <h4> Course Content Editor </h4>
      <br><br>
    </center>
    <v-breadcrumbs
      :items="items"
      large
    />
    
    <v-alert
      v-if="showAlert"
      :type="alertType"
      closable
    >
      {{ alertMsg }}
    </v-alert>

    <div class="p-3">
      <v-card v-if="preview">
        <div class="p-3" v-html="content" />
      </v-card>

      <v-card v-else>
        <vue-editor
          id="editor"
          v-model="content"
          use-custom-image-handler
          @imageAdded="handleImageAdded"
        />
      </v-card>
    </div>
  
    <center>
      <div
        class="btn-group"
        role="group"
      >
        <button
          type="button"
          class="btn btn-warning mr-10"
          @click="togglePreview"
        >
          {{ preview ? "Edit" : "Preview" }}
        </button>
        <button
          type="button"
          class="btn btn-primary"
          @click="saveContent"
        >
          Save Content
        </button>
      </div>
    </center>
  </div>
</template>

<script>
import { VueEditor } from 'vue2-editor';
import axios from 'axios';
import { baseUrl } from '../constants/constants.js';

export default {
  components: {
    VueEditor
  },

  data() {
    return {
      content: 'write course content here..',
      showAlert: false,
      // success, info, warning or error
      alertMsg: 'content saved',
      alertType: 'info',
      preview: false,   // show preview when selected, else show editor
      items: [
        {
          text: 'Biology',
          disabled: false,
          href: 'breadcrumbs_dashboard'
        },
        {
          text: 'Introduction',
          disabled: false,
          href: 'breadcrumbs_link_1'
        },
        {
          text: 'intro',
          disabled: true,
          href: 'breadcrumbs_link_2'
        }
      ]
    };
  },

  methods: {
    togglePreview: function() {
      let status = false;

      if(!this.preview) status = true;

      this.preview = status;
    },
    saveContent: function() {
      // You have the content to save
      // ! update database
      console.log(this.content);
    },
    handleImageAdded: function(file, Editor, cursorLocation, resetUploader) {
      // An example of using FormData
      // NOTE: Your key could be different such as:
      // formData.append('file', file)

      var formData = new FormData();

      const path = baseUrl;

      formData.append('image', file);

      axios({
        url: path,
        method: 'POST',
        data: formData
      })
        .then(result => {
          const url = result.data.url; // Get url from response
          Editor.insertEmbed(cursorLocation, 'image', url);
          resetUploader();
        })
        .catch(err => {
          // show error message popup
          console.log(err);
        });
    }
  }
};
</script>
