<template>
  <div id="app">
    {{info }}
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'App',

  data(){
    return{
      info: null
    }
  },
  mounted(){
    axios.get('http://127.0.0.1:8000/recipes/')
    .then(response => (this.info = response.data))
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
