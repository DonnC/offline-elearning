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
    <div>
      <v-alert
        v-model="showAlert"
        class="p-3"
        :type="alertType"
        dismissible
        shaped
        dense
      >
        {{ alertMsg }}
      </v-alert>
    </div>


    <div class="p-3">
      <v-card v-if="preview">
        <div
          class="p-3"
          v-html="content"
        />
      </v-card>

      <v-card
        v-else
      >
        <vue-editor
        
          id="editor"
          v-model="content"
          placeholder="write or edit section notes for students here.."
          :editor-options="editorSettings"
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
//import  ImageResize  from 'quill-image-resize-vue';
import axios from 'axios';
import { baseUrl } from '../constants/constants.js';

// Quill.register('modules/imageResize', ImageResize);

export default {
  components: {
    VueEditor
  },
  data() {
    return {
      content: '',
      showAlert: false,
      // success, info, warning or error
      alertMsg: 'content saved',
      alertType: 'info',
      preview: false,   // show preview when selected, else show editor
      editorSettings: {
        modules: {
          imageResize: {}
        }
      }
      
    };
  },
  computed: {
    items()  {
      var course = this.$store.state.course;
      var section = this.$store.state.section;
      var content = this.$store.state.editor_content;

      return  [
        {
          text: course.name,
          disabled: true,
          href: '#'
        },
        {
          text: content,
          disabled: true,
          href: '#'
        },
        {
          text: section.title,
          disabled: true,
          href: '#'
        }
      ];
    }
  },

  mounted() {
    // fetch default section content data
    var sec_content = this.$store.state.section;

    var content = '';

    if(sec_content.data == null) {
      content = '';
    }

    else if (sec_content.data.length == 0) {
      content = '';
    }

    else {
      content =  this.$store.state.section.data;
    }

    this.content = content;
    
  },

  methods: {
    togglePreview: function() {
      let status = false;

      if(!this.preview) status = true;

      this.preview = status;
    },
    saveContent: function() {
      // You have the content to save
      // 
      if(this.content.length === 0) {
        this.showAlert = true;
        this.alertMsg = 'no section notes added';
        this.alertType = 'warning';

        return;
      }

      this.$store.commit('SET_SECTION_DATA', this.content);
      
      console.log(this.content);
      // setSection
      this.$store.dispatch('updateSection');
      // show alert
      console.log('section updated');

      this.showAlert = true;
      this.alertMsg = 'section notes added successfully';
      this.alertType = 'success';

      // go back 
      this.$router.back();

    },
    handleImageAdded: function(file, Editor, cursorLocation, resetUploader) {
      // resources/section/?section_id=1&type=other
      // images have type == other
      console.log('handle img..');
      const path = baseUrl + 'resources/section/?section_id=' + this.$store.state.section.id + '&type=other';

      console.log('handle img url: ' + path);

      var formData = new FormData();

      formData.append('file', file);

      console.log(formData);

      console.log('uploading img to server..');

      console.log(formData);

      axios.post(path, formData)
        .then((res) => {
          console.log(res.data);
          const url = res.data.url; // Get url from response
          Editor.insertEmbed(cursorLocation, 'image', url);
          resetUploader;
        })
        .catch((error) => {
          // eslint-disable-next-line
          alert(error);
          console.error(error);
        });
    }
  }
};
</script>
