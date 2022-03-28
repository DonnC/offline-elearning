<template>
  <v-container class="grey lighten-5">
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
            rounded
            outlined
            tile
            @click="updateForm(form.grade)"
          >
            <center>
              <v-card-title>
                {{ form.name }}
              </v-card-title>
            </center>
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

      // go to router
      this.$router.push('/courses');
    }
  }

};
</script>
