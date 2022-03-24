<template>
  <v-container class="grey lighten-5">
    <v-row
      style="height: 150px;"
      :class="mb-6"
    >
      <v-col
        v-for="(course, index) in courses"
        :key="index"
        cols="4"
      >
        <div class="p-4">
          <v-card
            height="400px"
            elevation="10"
            rounded
            outlined
            tile
          >
            <v-img
              src="http://127.0.0.1:8000/static/form4/biology/introduction/customeff.png"
              height="250px"
              cover
            />
            <v-card-subtitle>
              7 lessons
            </v-card-subtitle>
            <v-card-title>
              Biology
            </v-card-title>
            <v-spacer />
          </v-card>
        </div>
      </v-col>
      <v-responsive
        v-if="index === 2"
        :key="`width-${index}`"
        width="100%"
      />
    </v-row>
  </v-container>
</template>


<script>

export default {
  data() {
    return {
      courses: [
        'bio',
        'bio',
        'bio',
        'bio',
        'bio',
        'bio',
        'bio',
        'bio',
        'bio',
        'bio',
        'bio'
      ]
    };
  }

};
</script>
