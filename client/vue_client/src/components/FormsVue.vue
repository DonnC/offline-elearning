<template>
  <v-container class="grey lighten-5">
    <v-btn
      v-if="role === 'admin'"
      width="200"
      color="blue"
      class="white--text"
      @click="gotoAddCourse"
    >
      Add Teacher
      <v-icon
        right
      >
        mdi-user
      </v-icon>
    </v-btn>
    
    <v-row
      style="height: 150px;"
    >
      <v-col
        v-for="form in forms"
        :key="form.grade"
        cols="4"
      >
        <div class="p-4">
          <v-card
            height="200px"
            elevation="6"
            color="#5695E8"
            rounded
            outlined
            tile
            @click="updateForm(form.grade)"
          >
            <div
              class="text-center"
              align="center"
            >
              {{ form.name }}
            </div>
          </v-card>
        </div>
      </v-col>
    </v-row>
  </v-container>
</template>


<script>

export default {
  data() {
    return {
      forms: [
        {
          name: 'Form 1',
          grade: 'form1'    // corresponds to available server grades
        },
        {
          name: 'Form 2',
          grade: 'form2'
        },
        {
          name: 'Form 3',
          grade: 'form3'
        },
        {
          name: 'Form 4',
          grade: 'form4'
        },
        {
          name: 'Form 5',
          grade: 'form5'
        },
        {
          name: 'Form 6',
          grade: 'form6'
        }
      ]
    };
  },
  methods: {
    updateForm(form) {
      this.$store.commit('UPDATE_FORM', form);

      this.$router.push('/courses');
    }
  }

};
</script>
