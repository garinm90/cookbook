<template>
  <div id="app">
    <h1>Recipes</h1>
    <div
    v-for="recipe in info"
    :key="recipe.id"
    >
    {{ recipe.recipe_name }}

    </div>
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
    axios.get('/recipes')
    .then(response => (this.info = response.data))
    .catch(error => console.log(error))
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
