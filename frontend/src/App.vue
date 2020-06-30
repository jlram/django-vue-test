<template>
  <div id="app">
    <Landing/>
  </div>
</template>

<script>

  import Landing from './pages/Landing'


  export default {
    name: 'App',
    components: {
      Landing
    }
  }
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
