<template>
  <v-card
    class="mx-auto my-12"
    max-width="500"
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
      <div> Add New Staff Member </div>
    </v-card-text>

    <div class="p-3">
      <v-form
        ref="form"
        v-model="valid"
        lazy-validation
      >
        <v-text-field
          v-model="name"
          label="Teacher Username"
          :rules="[rules.required]"
          required
        />

        <v-text-field
          v-model="password"
          :append-icon="show1 ? 'mdi-eye' : 'mdi-eye-off'"
          :rules="[rules.required]"
          :type="show1 ? 'text' : 'password'"
          label="Teacher Password"
          @click:append="show1 = !show1"
        />
        <div class="p-4">
          <v-btn
            :disabled="!valid"
            color="success"
            class="mr-4"
            @click="validate"
          >
            Submit
          </v-btn>

          <v-btn
            color="error"
            class="mr-4"
            @click="reset"
          >
            Cancel
          </v-btn>
        </div>

        <div v-if="error_obj['is_error']"> 
          {{ error_obj['error_message'] }}
        </div>
      </v-form>
    </div>
  </v-card>
</template>


<script>
import axios from 'axios';
import { baseUrl } from '../constants/constants.js';

export default {
  data: () => ({
    valid: true,
    name: '',
    show1: false,
    loading: false,
    alertType: 'success',
    alertMsg: '',
    alert: false,
    password: '',
    rules: {
      required: value => !!value || 'Required.',
      min: v => v.length >= 8 || 'Min 8 characters',
      emailMatch: () => ('The email and password you entered don\'t match')
    }
   
  }),
  computed: {
    role() {
      return this.$store.state.role;
    },
    error_obj() {
      return this.$store.state.error_response;
    }
  },
  mounted() {
    if(this.$store.state.role === 'student') {
      this.$router.replace('/');
    }
  },
  methods: {
    validate () {
      if(this.role === 'student') {
        this.$router.replace('/forms');
      }
    
      this.$refs.form.validate();

      this.login();
    },
    reset () {
      this.$refs.form.reset();
      this.$store.commit('UPDATE_ERROR_OBJ', {
        is_error: false,
        error_message: ''
      });
    },
    resetValidation () {
      this.$refs.form.resetValidation();
    },
    // register
    async login() {
      if(this.name.length === 0 || this.password.length  === 0) {
        return;
      }

      if(this.role === 'student') {
        this.$router.replace('/forms');
      }

      try {
        const path = baseUrl + 'users/register';


        var res = await axios.post(path, {
          'name': this.name,
          'password': this.password,
          'is_admin': false,
          'is_teacher': true,
          'is_student': false
        });

        console.log(res.data);
          
        this.alert = true;
        this.alertType = 'success';
        this.alertMsg = 'New Teacher added successfully';

        this.reset();
      }

      catch (error) {
        this.alert = true;
        this.alertType = 'warning';
        this.alertMsg = error.response.data.detail;
      }
    }
  }
};
</script>
