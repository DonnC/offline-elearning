<template>
  <v-card
    class="mx-auto my-12"
    max-width="800"
    max-height="900"
  >
    <v-alert
      v-model="alert"
      type="alertType"
      dismissible
    >
      {{ alertMsg }}
    </v-alert>
    
    <v-card-text>
      <div> Add New {{ form }} {{ course.name }} Content Section </div>
    </v-card-text>

    <div class="p-3">
      <v-form
        ref="form"
        v-model="valid"
        lazy-validation
      >
        <v-select
          v-model="content"
          label="Content Section"
          :items="contents"
        />
        
        <v-text-field
          v-model="name"
          label="Section Title"
          required
        />

        <div class="p-4">
          <v-btn
            :disabled="!valid"
            color="success"
            class="mr-4"
            @click="validate"
          >
            Save
          </v-btn>

          <v-btn
            color="error"
            class="mr-4"
            @click="reset"
          >
            Cancel
          </v-btn>
        </div>
      </v-form>
    </div>
  </v-card>
</template>


<script>
export default {
  data: () => ({
    valid: true,
    name: '',
    content: null,
    loading: false,
    alert: false,
    alertType: 'success',
    alertMsg: ''
  }),
  computed: {
    form() {
      return this.$store.state.form;
    },
    course() {
      return this.$store.state.course;
    },
    contents() {
      return  this.$store.getters.getCourseContents.map(
        function(elem) {
          return elem.topic;
        }
      );
    }
  },
  mounted() {
    this.$store.dispatch('fetchCourseContents');
  },
  methods: {
    validate () {
      this.$refs.form.validate();

      this.saveCourse();
    },
    reset () {
      this.$refs.form.reset();
    },
    resetValidation () {
      this.$refs.form.resetValidation();
    },
    saveCourse() {
      if(this.name.length === 0 || this.content  === null) {
        return;
      }

      var content_p = this.$store.getters.getCourseContents.find(cont => cont.topic === this.content);

      this.$store.dispatch('addContentSection',  {
        'title': this.name,
        'data': '',
        'content': content_p.id
      });

      this.reset();
      this.alert = true;
      this.alertMsg = 'Content section added successfully';
      this.alertType = 'success';
    }
  }
};
</script>
