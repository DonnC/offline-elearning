<template>
  <v-card
    class="mx-auto my-12"
    max-width="800"
    max-height="900"
  >
    <v-alert
      v-model="alert"
      shaped
      dismissible
      :type="alertType"
    >
      {{ alertMsg }}
    </v-alert>
    
    <v-card-text>
      <div> Add New {{ form }} {{ course.name }} Content </div>
    </v-card-text>

    <div class="p-3">
      <v-form
        ref="form"
        v-model="valid"
        lazy-validation
      >
        <v-text-field
          v-model="name"
          label="Topic Name"
          required
        />

        <v-textarea
          v-model="description"
          label="Description"
          placeholder="a short description about this content topic"
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
    description: '',
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
    }
  },
  mounted() {
    this.$store.dispatch('fetchFormCourses');
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
      if(this.name.length === 0 || this.description.length  === 0) {
        this.alert = true;
        this.alertMsg = 'name and description is required';
        this.alertType = 'warning';
        return;
      }

      this.$store.dispatch('addCourseContent',  {
        'topic': this.name,
        'description': this.description
        // 'course_id': this.course.id
      });

      
      this.alert = true;
      this.alertMsg = 'Course content added successfully';
      this.alertType = 'success';
      this.reset();
    }
  }
};
</script>
