<template>
  <v-card
    class="mx-auto my-12"
    max-width="500"
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
      <div>Welcome {{ role }} - Login to proceed</div>
    </v-card-text>

    <div class="p-3">
      <v-form
        ref="form"
        v-model="valid"
        lazy-validation
      >
        <v-text-field
          v-model="name"
          label="Username"
          :rules="[rules.required]"
          required
        />

        <v-text-field
          v-model="password"
          :append-icon="show1 ? 'mdi-eye' : 'mdi-eye-off'"
          :rules="[rules.required]"
          :type="show1 ? 'text' : 'password'"
          label="Password"
          @click:append="show1 = !show1"
        />
        <div class="p-4">
          <v-btn
            :disabled="!valid"
            color="success"
            class="mr-4"
            @click="validate"
          >
            Login
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
      this.$router.push('/');
    }

  },
  methods: {
    validate () {
      if(this.role === 'student') {
        this.$router.push('/forms');
      }
    
      this.$refs.form.validate();

      this.login();
    },
    reset () {
      this.$refs.form.reset();
      this.alert = false;
      this.$store.commit('UPDATE_ERROR_OBJ', {
        is_error: false,
        error_message: ''
      });
    },
    resetValidation () {
      this.$refs.form.resetValidation();
    },
    async login() {
      if(this.name.length === 0 || this.password.length  === 0) {
        return;
      }

      if(this.role === 'student') {
        this.$router.push('/forms');
      }

      try {
        const path = baseUrl + 'users/login';

        var res = await axios.post(path, {
          'name': this.name,
          'password': this.password
        });

       
        console.log(res.data);
          
        var _role = 'student';

        var isAdmin = res.data.is_admin;

        if(isAdmin) {
          _role = 'admin';
        }

        else {
          _role = 'teacher';
        }

        var pl = {
          token: '82sshuds9sd9sdhd9dsy',
          isLoggedIn: true,
          userId: res.data.id
        };

        this.$store.commit('UPDATE_AUTH_USER', pl);

        this.$store.commit('UPDATE_USER_ROLE', _role);
        
        this.$router.push('/forms');

      }

      catch (error) {
        this.alert = true;
        this.alertType = 'danger';
        this.alertMsg = error.response.data.detail;
      }
    }
  }
};
</script>
