<template>
  <v-container fluid>
    <v-row
      style="height: 100px;"
    >
      <v-col
        cols="4"
      >
        <div class="p-2">
          <v-card
            class="max-auto"
            height="200px"
            max-width="340px"
            elevation="4"
            color="blue"
            to="/forms"
            @click="updateRole('student')"
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
        cols="4"
      >
        <div class="p-2">
          <v-card
            class="max-auto"
            height="200px"
            max-width="340px"
            elevation="4"
            color="blue"
            to="/login"
            @click="updateRole('teacher')"
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
        cols="4"
      >
        <div class="p-2">
          <v-card
            class="max-auto"
            height="200px"
            max-width="340px"
            elevation="4"
            color="blue"
            to="/login"
            @click="updateRole('admin')"
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
  methods: {
    updateRole(user) {
      this.$store.commit('UPDATE_USER_ROLE', user);
    }
  }
};
</script>

