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
      <div> Add New {{ form }} Course </div>
    </v-card-text>

    <div class="p-3">
      <v-form
        ref="form"
        v-model="valid"
        lazy-validation
      >
        <v-text-field
          v-model="name"
          label="Course Name"
          placeholder="e.g Mathematics"
          required
        />

        <v-text-field
          v-model="synopsis"
          label="Synopsis"
          placeholder="short course description"
          required
        />

        <v-textarea
          v-model="description"
          label="Description"
          placeholder="detailed course description"
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
import { kColor } from '@/constants/constants';
export default {
  data: () => ({
    valid: true,
    name: null,
    color: '#5695E8FF',
    alertType: 'success',
    alertMsg: '',
    synopsis: null,
    description: null,
    alert: false
    
  }),
  computed: {
    form() {
      return this.$store.state.form;
    },
    loading() {
      return this.$store.state.loading;
    }
  },
  mounted() {
    if(this.$store.state.role === 'student') {
      this.$router.push('/');
    }

  },
  methods: {
    validate () {
      if(this.$refs.form.validate()) 
      {
        if(!! this.name && !!this.synopsis && this.description) {
          this.saveCourse();
        }

        else {
          this.alert = true;
          this.alertType = 'danger';
          this.alertMsg = 'All fields are required';
        }
      }
    },
    reset () {
      this.$refs.form.reset();
    },
    resetValidation () {
      this.$refs.form.resetValidation();
    },
    saveCourse() {

      this.$store.dispatch('addCourse',  {
        'form': this.form,
        'name': this.name,
        'synopsis': this.synopsis,
        'description': this.description,
        'color': kColor
      });

      this.reset();
      this.alert = true;
      this.alertMsg = 'New course added successfully';
      this.alertType = 'success';
    }
  }
};
</script>
