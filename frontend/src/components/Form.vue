<template>
  <div>
    <b-row>
      <b-col cols="12" class="mt-5">
        <h1 class="display-4">Introduce una nueva Nota</h1>
      </b-col>
    </b-row>

    <b-row class="mt-5">
      <b-col cols="12" lg="6" class="">
        <label for="end-date">Choose a date</label>
        <b-form-datepicker id="end-date" v-model="fechavalue" class="mb-2"></b-form-datepicker>

        <label for="tags" class="mt-3">Añade etiquetas libremente</label>
        <b-form-input id="tags" v-model="text" placeholder="Etiquetas..."></b-form-input>

        <b-form-file
          id="file"
          class="mt-4"
          v-model="file"
          placeholder="Choose a file..."
          drop-placeholder="Drop file here..."></b-form-file>

      </b-col>

      <b-col cols="12" lg="6" class="">
          <label for="tags" id="label-user">Elige un usuario al que asignarle la Nota</label>
          <b-form-select v-model="selected" :options="options"></b-form-select>

          <label for="tags" class="mt-4">Elige un tipo de Nota</label>
          <b-form-select v-model="selected" :options="options"></b-form-select>

          <b-form-checkbox
            id="is-task"
            class="mt-4"
            v-model="status"
            name="is-task"
            value="task"
            unchecked-value="not_task">
            ¿Es una task?
          </b-form-checkbox>
      </b-col>
    </b-row>

    <b-row>
      <b-form-textarea
        id="textarea"
        class="mt-4 ml-3"
        v-model="text"
        placeholder="Introduce el texto de tu nota..."
        rows="3"
        max-rows="6">
      </b-form-textarea>

      <b-col cols="12">
         <b-button @click="submitForm" variant="outline-primary" class="ml-2 mt-3" style="width: 100%">Añadir nota</b-button>
      </b-col>
    </b-row>
  </div>
</template>

<script>

  import axios from 'axios';

    export default {
      name: "Form",
      data() {
        return({
          selected: true,
          options: [],
          text: '',
          fechavalue: new Date().toISOString().slice(0,10),
          file: [],
          status: 'task'
          })
      },
        methods: {
          submitForm(){
            console.log(this.fechavalue)
          }
        },
      created() {
        axios.get('http://127.0.0.1:8000/api/users/')
          .then(function (response) {
            console.log(response);
          })
          .catch(function (error) {
            console.log(error);
          });



      }
    }
</script>

<style scoped>
  .display-4 {
    font-size: 36px !important;
  }

  @media (max-width: 992px) {
    #label-user {
      margin-top: 1rem;
    }
  }


</style>
