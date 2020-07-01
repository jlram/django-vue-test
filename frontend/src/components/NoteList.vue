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
    data() {
      return {
        items: []
      }
    },
    methods: {
       loadTable() {
         const vm = this; // Declaracion auxiliar del this para poder usarlo en then

         this.$axios.get('http://127.0.0.1:8000/api/notes/')
          .then(function (response) {
            vm.items = response.data

            vm.items.forEach(item => {
              if(item.note.length > 10) {
                item.note = item.note.substring(1, 10) + '...';
              }
            });
          })
          .catch(function (error) {
            console.log(error);
          });
         }
    },

    created() {
      this.loadTable()

      this.$root.$on('refresh', data => {
          this.loadTable()
      });
    }
  }
</script>

<style scoped>

</style>
