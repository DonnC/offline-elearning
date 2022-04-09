<template>
  <v-container>
    <v-rol
      class="mb-6"
      align-content="space-between"
      no-gutters
    >
      <v-col
        md="4"
        sm="4"
      >
        <v-container>
          <v-list>
            <v-list-group
              v-for="content in contents"
              :key="content.id"
              no-action
            >
              <template #activator>
                <v-list-item-content>
                  <v-list-item-title v-text="content.topic" />
                </v-list-item-content>
              </template>

              <v-list-item
                v-for="section in content.sections"
                :key="section.id"
                v-model="section.id"
                link="true"
              >
                <v-list-item-content>
                  <v-list-item-title v-text="section.title" />
                </v-list-item-content>
              </v-list-item>
            </v-list-group>
          </v-list>
        </v-container>
      </v-col>

      <v-col
        md="4"
        offset-md="5"
      >
        <v-container>
          <p>
            Hie data
          </p>
        </v-container>
      </v-col>
    </v-rol>
  </v-container>
</template>
<script>

export default {
  data() {
    return {
      contents: [
        {
          topic: 'Introduction',
          description: '',
          id: 0,
          sections: [
            {
              title: 'Who is this for?',
              id: 0,
              data: ''
            },
            {
              title: 'What are we building?',
              id: 1,
              data: ''
            }
          ]
        },
        {
          topic: 'Prerequisites',
          description: '',
          id: 1,
          sections: [
            {
              title: 'Python',
              id: 2,
              data: ''
            },
            {
              title: 'MariaDB/Postgres',
              id: 3,
              data: ''
            },
            {
              title: 'Git/Github',
              id: 4,
              data: ''
            }
          ]
        },
        {
          topic: 'Install and Setup Bench',
          description: '',
          id: 2,
          sections: [
            {
              title: 'Installation',
              id: 5,
              data: ''
            },
            {
              title: 'Directory Structure',
              id: 6,
              data: ''
            }
          ]
        },
        {
          topic: 'Create an App',
          description: '',
          id: 3,
          sections: [
            {
              title: 'Create an app',
              id: 7,
              data: ''
            },
            {
              title: 'App structure',
              id: 8,
              data: ''
            }
          ]
        },
        {
          topic: 'Create a site',
          description: '',
          id: 4,
          sections: [
            {
              title: 'Create a new site',
              id: 9,
              data: ''
            },
            {
              title: 'Login to desk',
              id: 10,
              data: ''
            }
          ]
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
