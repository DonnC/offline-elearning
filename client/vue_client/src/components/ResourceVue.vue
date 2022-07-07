<template>
  <v-container
    id="create"
  >
    <v-alert
      v-model="alert"
      shaped
      dismissible
      :type="alertType"
    >
      {{ alertMsg }}
    </v-alert>
    <v-tabs
      centered
      stacked
    >
      <v-tab
        v-for="(ctab, index) in tabs"
        :key="index"
        value="index"
        @click="updateType(ctab)"
      >
        <v-icon>
          {{ ctab.icon }}
        </v-icon>
        {{ ctab.name }}
      </v-tab>
    </v-tabs>

    <div
      v-if="!loading"
      class="main"
    > 
      <v-container
        v-if="resources.length > 0"
      >
        <v-row
          style="height: 150px;"
        >
          <v-col
            v-for="resource in resources"
            :key="resource.id"
            cols="12"
            md="6"
            lg="4"
            xl="4"
          >
            <div class="p-1">
              <v-card
                height="180px"
                width="200px"
                elevation="3"
                rounded
              >
                <div class="p-2">
                  <center>
                    <v-icon
                      size="550%"
                      @click="onResTap(resource)"
                    >
                      {{ tab.icon }}
                    </v-icon>
                  </center>
                  <div v-resize-text="{ratio:0.7, minFontSize: '10px', maxFontSize: '13px'}">
                    {{ resource.filename }}
                  </div>
                </div>
                <v-card-actions
                  v-if="role != 'student'"
                >
                  <v-spacer />
                  <v-btn
                    color="red darken-1"
                    text
                    @click="deleteFile(resource.id)"
                  >
                    Delete
                  </v-btn>
                </v-card-actions>
              </v-card>
            </div>
          </v-col>
        </v-row>
      </v-container>

      <v-container
        v-else
      >
        <center>
          <div class="p-2">
            <v-icon
              size="400%"
            >
              {{ tab.icon }}
            </v-icon>
            No resources found!
          </div>
        </center>
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
    <div
      class="p-4"
    >
      <v-dialog
        v-model="dialog"
        persistent
        max-width="400px"
      >
        <v-card>
          <v-card-title>
            <span class="text-h5">Add {{ selectedTab.name }} File </span>
          </v-card-title>
          <v-card-text>
            <v-container>
              <v-row>
                <v-col
                  cols="12"
                >
                  <v-file-input
                    v-model="resourceFile"
                    show-size
                    placeholder="upload file"
                    truncate-length="15"
                  />
                </v-col>
              </v-row>
            </v-container>
          </v-card-text>
          <v-card-actions>
            <v-spacer />
            <v-btn
              color="blue darken-1"
              text
              @click="dialog = false"
            >
              Close
            </v-btn>
            <v-btn
              color="blue darken-1"
              text
              @click="uploadResourceFile"
            >
              Upload
            </v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>
      <v-speed-dial
        v-if="role != 'student'"
        v-model="fab"
        :bottom="true"
        :left="true"
        :direction="bottom"
        :fixed="true"
        :transition="slide-y-reverse-transition"
      >
        <template #activator>
          <v-btn
            v-model="fab"
            color="blue darken-2"
            dark
            fab
          >
            <v-icon v-if="fab">
              mdi-close
            </v-icon>
            <v-icon v-else>
              mdi-note-plus-outline 
            </v-icon>
          </v-btn>
        </template>

        <v-btn
          v-for="(ctab, index) in tabs"
          :key="index"
          value="index"
          fab
          dark
          small
          color="blue"
          @click="showDialog(ctab)"
        >
          <v-icon>{{ ctab.icon }}</v-icon>
        </v-btn>
      </v-speed-dial>
    </div>
  </v-container>
</template>

<script>
import axios from 'axios';
import { baseUrl } from '../constants/constants.js';

export default {
  name: 'ResourceVue',
  data() {
    return {
      fab: false,
      dialog: false,
      resources: [],
      resourceFile: null,
      alertType: 'success',
      alertMsg: '',
      alert: false,
      selectedTab: {
        name: 'Books',
        icon: 'mdi-book-open-page-variant-outline',
        type: 'book'
      }
    };
  },

  computed: {
    role() {
      return this.$store.state.role;
    },
    tabs() {
      return this.$store.getters.getResourceTabs;
    },
    tab() {
      return this.$store.state.resource_type;
    },
    loading() {
      return this.$store.getters.getLoaderStatus;
    }
  },
  mounted() {
    this.$store.dispatch('fetchResources');
    this.resources = this.$store.getters.getResourcesByType;
  },
  
  methods: {
    deleteFile(file_id) {
      this.$store.dispatch('deleteResource', {'id': file_id});
      this.$store.dispatch('fetchResources');
      this.resources = this.$store.getters.getResourcesByType;
    },
    showDialog(tab) {
      this.dialog = true;
      this.selectedTab = tab;
    },
    updateType(tab) {
      console.log(tab);
      this.$store.commit('UPDATE_RESOURCE_TYPE', tab);
      this.resources = this.$store.getters.getResourcesByType;
    },
    onResTap(res) {
      this.$store.commit('UPDATE_RESOURCE_URL', res.url);

      if(res.type == 'video') {
        // go to resource viewer
        this.$router.push('/player');
      }
      
      else {
        // go to resource viewer
        this.$router.push('/pdf');
      }
     
    },
    async uploadResourceFile() {
      this.dialog = false;
      console.log(this.resourceFile);

      if(this.resourceFile === undefined) {
        return;
      }

      try {
        var source = this.$store.getters.getCurrentResourceSource;

        var _s = source.name;
        var _id = source.id;

        if (_id === -1) {
          return;
        }

        //determine if uploading course | section resource
        const path = baseUrl + 'resources/' + _s + '/?' + _s + '_id=' + _id + '&type=' + this.selectedTab.type;

        console.log(path);

        var formData = new FormData();

        formData.append('file', this.resourceFile);

        var res = await axios.post(path, formData);

        console.log(res);

        this.$store.dispatch('fetchResources');
        this.resources = this.$store.getters.getResourcesByType;

        this.alert = true;
        this.alertType = 'success';
        this.alertMsg = 'Resource file uploaded successfully!';

        this.resourceFile = null;
      }

      catch(error) {
        this.alert = true;
        this.alertType = 'warning';
        this.alertMsg = error.response.data.detail;
      }
    }
  }
};
</script>

<style>
  #create .v-speed-dial {
    position: absolute;
  }

  #create .v-btn--floating {
    position: relative;
  }
</style>
