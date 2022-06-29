<template>
  <v-container>
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
            cols="2"
          >
            <div class="p-1">
              <v-card
                height="180px"
                width="200px"
                elevation="3"
                rounded
                @click="onResTap(resource)"
              >
                <div class="p-2">
                  <center>
                    <v-icon
                      size="550%"
                    >
                      {{ tab.icon }}
                    </v-icon>
                  </center>
                  <div v-resize-text="{ratio:0.7, minFontSize: '10px', maxFontSize: '13px'}">
                    {{ resource.filename }}
                  </div>
                </div>
              </v-card>
            </div>
          </v-col>
        </v-row>
      </v-container>

      <v-container
        v-else
      >
        <center>
          <div class="p-5">
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
  </v-container>
</template>

<script>
export default {
  name: 'ResourceVue',
  data() {
    return {
      resources: []
    };
  },

  computed: {
    
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
     
    }
  }
};
</script>
