<template>
  <div class="container">
    <button
      type="button"
      class="btn btn-primary"
    >
      {{ msg }}
    </button>
  </div>
</template>

<script>
import axios from 'axios';
import { baseUrl } from '../constants/constants.js';

export default {
  name: 'PingVue',
    
  data() {
    return {
      msg: 'Hello!'
    };
  },
  created() {
    this.getMessage();
  },
  methods: {
    getMessage() {
      const path = baseUrl + 'ping';

      axios.get(path)
        .then((res) => {
          this.msg = res.data.status;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    }
  }
};
</script>
