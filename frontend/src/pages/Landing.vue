<template>
  <div>
    <NavBar></NavBar>
    <b-container id="contenedor">
      <Form></Form>
      <NoteList :key=this.$store.state.count></NoteList>
    </b-container>
  </div>
</template>

<script>
  import Form from '../components/Form'
  import NoteList from '../components/NoteList'
  import NavBar from '../components/NavBar'

  // Componente que va a cargar tanto el NavBar, como el formulario y la lista de Notes
  export default {
    name: "Landing",
    components: {
        Form,
        NoteList,
        NavBar
    }
  }
</script>

<style scoped>
  #contenedor {
    width: 50%;
  }

  @media (max-width: 768px) {
    #contenedor {
      width: 100%;
    }
  }

</style>
