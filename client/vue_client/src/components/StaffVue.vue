<template>
  <v-container class="grey lighten-5">
    <v-btn
      v-if="role === 'admin'"
      width="200"
      color="blue"
      class="white--text"
      @click="gotoAddStaff"
    >
      Add Teacher
      <v-icon
        right
      >
        mdi-user
      </v-icon>
    </v-btn>
    
    <v-row
      v-if="teachers.length > 0"
      style="height: 150px;"
    >
      <v-col
        v-for="teacher in teachers"
        :key="teacher.id"
        cols="4"
      >
        <div class="p-4">
          <v-card
            height="200px"
            elevation="6"
            rounded
            outlined
            tile
          >
            <div
              class="text-center p-5"
            >
              {{ teacher.name }}
            </div>
            <v-spacer />
            <v-card-actions>
              <v-spacer />
              <v-btn
                text
                color="blue"
                :href="editStaffUrl"
                :target="_blank"
              >
                Edit
              </v-btn>
              <v-dialog
                v-if="role === 'admin'"
                v-model="dialog"
                persistent
                max-width="290"
              >
                <template #activator="{ on, attrs }">
                  <v-btn
                    color="red"
                    dark
                    v-bind="attrs"
                    v-on="on"
                  >
                    Delete
                  </v-btn>
                </template>
                <v-card>
                  <v-card-title class="text-h5">
                    Confirm delete?
                  </v-card-title>
                  <v-card-text>
                    Please note that deleting a teacher is permanent.
                    After deleting, teacher will be removed from system.
                  </v-card-text>
                  <v-card-actions>
                    <v-spacer />
                    <v-btn
                      color="green darken-1"
                      text
                      @click="dialog = false"
                    >
                      Abort
                    </v-btn>
                    <v-btn
                      color="red darken-1"
                      text
                      @click="deleteStaff(teacher.id)"
                    >
                      Confirm
                    </v-btn>
                  </v-card-actions>
                </v-card>
              </v-dialog>
            </v-card-actions>
          </v-card>
        </div>
      </v-col>
    </v-row>

    <center
      v-else
    >
      No Staff Members currently available!
    </center>
  </v-container>
</template>


<script>
import { baseUrl } from '../constants/constants.js';

export default {
  data() {
    return {
      dialog: false,
      editStaffUrl: baseUrl + 'docs#/users/update_user_users__patch'
    };
  },
  computed: {
    role() {
      return this.$store.state.role;
    },
    teachers() {
      return this.$store.getters.getTeachers;
    }
  },
  mounted() {
    if(this.$store.state.role === 'student') {
      this.$router.replace('/');
    }

    this.$store.dispatch('fetchTeachers');

  },
  methods: {
    gotoAddStaff() {
      this.$router.push('/add-staff');
    },
    deleteStaff(staff_id) {
      this.dialog = false;
      
      this.$store.dispatch('deleteTeacher', {'id': staff_id});

      this.$store.dispatch('fetchTeachers');
    }
  }
};
</script>
