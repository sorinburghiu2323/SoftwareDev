<template>
  <div id="app">
    <HomePage 
    :homepagePotatos="potatos"/>
  </div>
</template>

<script>
import axios from 'axios';
import HomePage from './views/HomePage.vue'

export default {
  name: 'App',
  components: {
    HomePage,
  },
  created() {
    this.getPotatos();
  },
  mounted() {
    this.$root.$on('updatePotatos', () => {
        // your code goes here
        this.getPotatos();
    });
  },
  data() {
    return {
      potatos: null
    }
  },
  methods: {
    getPotatos() {
      axios.get('api/potato').then(response => 
        this.potatos = response.data.potatoes
      );
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
