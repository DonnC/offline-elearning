<template>
  <v-container fluid>
    <v-row>
      <v-col
        cols="12"
        sm="6"
        md="3"
        lg="3"
        xl="3"
      >
        <div class="p-2">
          <v-card
            class="max-auto"
            height="200px"
            max-width="340px"
            elevation="4"
            color="blue"
            @click="studentLogic('student')"
          >
            <center>
              <v-col
                align-self="center"
                cols="auto"
              >
                <account-details
                  fill-color="white"
                  :size="80"
                />
                <v-container />
                <h5>
                  Student
                </h5>
              </v-col>
            </center>
          </v-card>
        </div>
      </v-col>
      <v-col
        cols="12"
        sm="6"
        md="3"
        lg="3"
        xl="3"
      >
        <div class="p-2">
          <v-card
            class="max-auto"
            height="200px"
            max-width="340px"
            elevation="4"
            color="blue"
            @click="staffLogic('teacher')"
          >
            <center>
              <v-col
                align-self="center"
                cols="auto"
              >
                <account-tie
                  fill-color="white"
                  :size="80"
                />
                <v-container />
                <h5>
                  Teacher
                </h5>
              </v-col>
            </center>
          </v-card>
        </div>
      </v-col>
      <v-col
        cols="12"
        sm="6"
        md="3"
        lg="3"
        xl="3"
      >
        <div class="p-2">
          <v-card
            class="max-auto"
            height="200px"
            max-width="340px"
            elevation="4"
            color="blue"
            @click="staffLogic('admin')"
          >
            <center>
              <v-col
                align-self="center"
                cols="auto"
              >
                <shield-account
                  fill-color="white"
                  :size="80"
                />
                <v-container />
                <h5>
                  Admin
                </h5>
              </v-col>
            </center>
          </v-card>
        </div>
      </v-col>
      <!-- <v-col
        cols="6"
      >
        <div class="p-2">
          <v-card
            class="max-auto"
            height="200px"
            max-width="340px"
            elevation="4"
            color="blue"
            @click="studentLogic('student')"
          >
            <center>
              <v-col
                align-self="center"
                cols="auto"
              >
                <account-details
                  fill-color="white"
                  :size="80"
                />
                <v-container />
                <h5>
                  Student
                </h5>
              </v-col>
            </center>
          </v-card>
        </div>
      </v-col>

      <v-col
        cols="6"
      >
        <div class="p-2">
          <v-card
            class="max-auto"
            height="200px"
            max-width="340px"
            elevation="4"
            color="blue"
            @click="staffLogic('teacher')"
          >
            <center>
              <v-col
                align-self="center"
                cols="auto"
              >
                <account-tie
                  fill-color="white"
                  :size="80"
                />
                <v-container />
                <h5>
                  Teacher
                </h5>
              </v-col>
            </center>
          </v-card>
        </div>
      </v-col>

      <v-col
        cols="6"
      >
        <div class="p-2">
          <v-card
            class="max-auto"
            height="200px"
            max-width="340px"
            elevation="4"
            color="blue"
            @click="staffLogic('admin')"
          >
            <center>
              <v-col
                align-self="center"
                cols="auto"
              >
                <shield-account
                  fill-color="white"
                  :size="80"
                />
                <v-container />
                <h5>
                  Admin
                </h5>
              </v-col>
            </center>
          </v-card>
        </div>
      </v-col> -->
    </v-row>
  </v-container>
</template>

<script>
import AccountDetails from 'vue-material-design-icons/AccountDetails.vue';
import AccountTie from 'vue-material-design-icons/AccountTie.vue';
import ShieldAccount from 'vue-material-design-icons/ShieldAccount.vue';

export default {
  components: {
    AccountDetails,
    AccountTie,
    ShieldAccount
  },
  computed: {
    role() {
      return this.$store.state.role;
    },
    authUser() {
      return this.$store.state.authUser;
    }
  },
  methods: {
    updateRole(user) {
      this.$store.commit('UPDATE_USER_ROLE', user);
    },
    staffLogic(user) {
      // if(this.role === 'student') {
      //   return;
      // }

      console.log(user);
      console.log(this.authUser);
      console.log(this.role);

      var status = this.authUser;

      console.log(status.isLoggedIn);

      // if(this.role === 'student' && user != 'student') {

      // }

      if(this.role === user) {
        if(status.isLoggedIn === true) {
          this.$router.replace('/forms');
        }

        else {
          this.$store.commit('LOGOUT');
          this.$store.commit('UPDATE_USER_ROLE', user);
          this.$router.replace('/login');
        }
      }

      else {
        if(this.role === 'admin' && user === 'teacher') {
          if(status.isLoggedIn === true) {
            this.$router.replace('/forms');
          }

          else {
            this.$store.commit('LOGOUT');
            this.$store.commit('UPDATE_USER_ROLE', user);
            this.$router.replace('/login');
          }
        }

        else {
          this.$store.commit('LOGOUT');
          this.$store.commit('UPDATE_USER_ROLE', user);
          this.$router.replace('/login');
        }
      }

    },
    studentLogic(user) {
      if(this.role === user) {
        this.$store.commit('LOGOUT');
        this.$store.commit('UPDATE_USER_ROLE', user);
        this.$router.replace('/forms');
      }

      else {
        this.$store.commit('UPDATE_USER_ROLE', user);
        this.$router.replace('/forms');
      }
    }
  }
};
</script>

