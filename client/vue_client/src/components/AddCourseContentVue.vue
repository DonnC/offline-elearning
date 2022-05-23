<template>
  <v-card
    class="mx-auto my-12"
    max-width="800"
    max-height="900"
  >
    <v-card-text>
      <div> Add New {{ form }} Course Content </div>
    </v-card-text>

    <div class="p-3">
      <v-form
        ref="form"
        v-model="valid"
        lazy-validation
      >
        <v-select
          v-model="course"
          label="Course"
          :items="courses"
        />

        <v-text-field
          v-model="name"
          label="Topic Name"
          required
        />

        <v-text-field
          v-model="description"
          label="Description"
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
    course: null,
    name: '',
    description: '',
    loading: false
  }),
  computed: {
    form() {
      return this.$store.state.form;
    },
    courses() {
      return this.$store.getters.getCourses;
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
      var payload = {
        'topic': this.name,
        'description': this.description,
        'course_id': this.course.id
      };

      console.log(payload);

      // this.$store.dispatch('loginUser', payload);
    }
  }
};
</script>
