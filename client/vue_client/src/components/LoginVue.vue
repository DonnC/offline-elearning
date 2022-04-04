<template>
  <v-card
    class="mx-auto my-12"
    max-width="500"
    max-height="900"
  >
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
      </v-form>
    </div>
  </v-card>
</template>


<script>
export default {
  data: () => ({
    valid: true,
    name: '',
    show1: false,
    loading: false,
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
    },
    resetValidation () {
      this.$refs.form.resetValidation();
    },
    login() {
      var payload = {
        'name': this.name,
        'password': this.password
      };

      this.$store.dispatch('loginUser', payload);
    }
  }
};
</script>
