<template>
  <div>
    <NavBar></NavBar>
    <b-container id="contenedor">
    <Form></Form>
    <NoteList></NoteList>
  </b-container>
  </div>
</template>

<script>
  import Form from '../components/Form'
  import NoteList from '../components/NoteList'
  import NavBar from '../components/NavBar'


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
    width: 40%;
  }

  @media (max-width: 768px) {
    #contenedor {
      width: 100%;
    }
  }

</style>
