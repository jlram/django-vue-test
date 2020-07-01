<template>
  <b-navbar type="dark" variant="info" id="topBar">
    <b-navbar-brand href="#">Vue-Notes</b-navbar-brand>
      <b-navbar-nav class="ml-auto">
        <b-nav-item>
            <em>jlram</em>
        </b-nav-item>
      </b-navbar-nav>
  </b-navbar>
</template>

<script>
    // Componente situado en la parte superior de la app
    export default {
        name: "NavBar"
    }
</script>

<style scoped>
  #topBar {
    position: fixed;
    top: 0;
    width: 100%;
    z-index: 99;
  }
</style>
