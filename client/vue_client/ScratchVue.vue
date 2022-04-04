<template>
  <v-container>
    <v-tabs
      centered
      stacked
    >
      <v-tab
        v-for="(tab, index) in tabs"
        :key="index"
        value="index"
        @click="updateType(tab)"
      >
        <v-icon>
          {{ tab.icon }}
        </v-icon>
        {{ tab.name }}
      </v-tab>
    </v-tabs>

    <div
      v-if="!loading"
      class="main"
    > 
      <v-container>
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
                height="150px"
                width="150px"
                elevation="3"
                rounded
              >
                <div class="p-3">
                  <center>
                    <v-icon
                      size="550%"
                    >
                      {{ tab.icon }}
                    </v-icon>
                  </center>
                  <div v-resize-text="{ratio:1.0, minFontSize: '15px', maxFontSize: '25px'}">
                    {{ resource.filename }}
                  </div>
                  <v-card-subtitle>
                    {{ resource.created_on }}
                  </v-card-subtitle>
                </div>
              </v-card>
            </div>
          </v-col>
        </v-row>
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
    this.$store.dispatch('fetchCourseResources');
  },
  
  methods: {
    updateType(tab) {
      console.log(tab);
      this.$store.commit('UPDATE_RESOURCE_TYPE', tab);
      this.resources = this.$store.getters.getResourcesByType;
    }
  }
};
</script>
