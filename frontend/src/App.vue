<template>
  <div id="app">

    <form @submit.prevent="submitForm">
      <div class="form-group row">
        <input type="text" class="form-control col-3 mx-2" placeholder="Nome" v-model="autor.nome">
        <input type="text" class="form-control col-3 mx-2" placeholder="Tema" v-model="autor.tema">
        <input type="text" class="form-control col-3 mx-2" placeholder="Texto" v-model="autor.texto">
        <button class="btn btn-success">Submit</button>
      </div>
    </form>

    <table class="table">
      <thead>
        <th>Nome</th>
        <th>Tema</th>
        <th>Texto</th>
      </thead>
      <tbody>
        <tr v-for="autor in autores" :key="autor.id" @dblclick="$data.autor = autor">
          <td>{{ autor.nome }}</td>
          <td>{{ autor.tema }}</td>
          <td>{{ autor.texto }}</td>
          <td>
            <button class="btn btn-outline-danger btn-sm mx-1" @click = "deleteAutor(autor)">X</button>

          </td> 
        </tr>
      </tbody>
    </table>

  </div>
</template>

<script>


export default {
  name: 'App',
  data(){
    return{
      autor:{},
      autores: []
    }
  },
  async created(){
    await this.getAutores();
  },
  methods:{
    submitForm(){
      if (this.autor.id === undefined){
        this.createAutor();
      }else{
        this.editAutor();
      }
    },

    async getAutores(){
      var response = await fetch('http://localhost:8000/api/autores/');
      this.autores = await response.json();
    },
    async createAutor(){
      await this.getAutores(); 

      await fetch('http://localhost:8000/api/autores/', {
        method: 'post',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(this.autor)
      });
      await this.getAutores();
    },
    async editAutor(){
      await this.getAutores(); 

      await fetch(`http://localhost:8000/api/autores/${this.autor.id}/`, {
        method: 'put',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(this.autor)
      });
      await this.getAutores();
      this.autor = {};
    },
    async deleteAutor(autor){
      await this.getAutores(); 

      await fetch(`http://localhost:8000/api/autores/${autor.id}/`, {
        method: 'delete',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(this.autor)
      });
      await this.getAutores();

    }
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
