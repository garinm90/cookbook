<template>
  <div id="app">
    <div id="secret_message">
      <span v-bind:title="message">
    Hover your mouse over me for a few seconds
    to see my dynamically bound title!
      </span>
    </div>

  </div>
</template>

<script>

export default {
  name: 'App',
  message: message
}
 
 var message = 'You loaded this page on ' + new Date().toLocaleString()
  

</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
