<template>
  <b-row>
    <b-col cols="12" class="mt-5">
        <b-table striped hover :items="items" responsive class="mt-5"></b-table>
    </b-col>
  </b-row>
</template>

<script>
  export default {
    name: "NoteList",
    // Items de la tabla
    data() {
      return {
        items: []
      }
    },
    methods: {
        // Metodo con el cual refrescamos la tabla haciendo una consulta a la BBDD y metiendo
        // el resultado en la variable items de data
       loadTable() {
         const vm = this; // Declaracion auxiliar del this para poder usarlo en then

         this.$axios.get('http://127.0.0.1:8000/notes/')
          .then(function (response) {
            vm.items = response.data

            vm.items.forEach(item => {
              // Para mejor lectura de la tabla, he puesto que el maximo que se pueda ver
              // del mensaje son 10 caracteres
              if(item.note.length > 10) {
                item.note = item.note.substring(1, 10) + '...';
              }
            });
          })
          .catch(function (error) {
            console.log(error);

            // Notificacion que muestra al darse un error recogiendo datos de la API
            vm.$notify({
              group: 'foo',
              type: 'warn',
              title: 'Ha habido un error',
              text: 'Ha habido un error recogiendo los datos de la tabla, vuelve a intentarlo.'
            });
          });
         }
    },

    mounted() { // Metodo del ciclo de vida que se activa al montar el componente
      this.loadTable()
    }
  }
</script>

<style scoped>

</style>
