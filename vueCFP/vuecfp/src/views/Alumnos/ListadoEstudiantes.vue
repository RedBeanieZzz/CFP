<template>
  <div>
    <NavBar/>
    <br>
  </div>
  <div>
  <h1>Listado de Alumnos</h1>
    <div>
      <table class="table table-hover ">
        <thead>
          <tr>
            <th scope="col">Documento</th>
            <th scope="col">ApellidoyNombre</th>
            <th scope="col">Direccion</th>
            <th scope="col">Localidad</th>
            <th scope="col">Telefono</th>
            <th scope="col">Estudios</th>
            <th scope="col">Nacimiento</th>
            <th scope="col">LugarDeNacimiento</th>
            <th scope="col">ProvinciaDeNacimiento</th>
            <th scope="col">IDNacionalidad</th>
            <th scope="col">Sexo</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="Estud in Alumnos" :key="Estud.Documento" >
            <th scope="row"><button type="button" class="btn btn-secondary btn-outline-info" style="background-color: #008080" v-on:click="editar(Estud.Documento)">{{Estud.Documento}}</button></th>
            <td>{{Estud.ApellidoyNombre}}</td>
            <td>{{Estud.Direccion}}</td>
            <td>{{Estud.Localidad}}</td>
            <td>{{Estud.Telefono}}</td>
            <td>{{Estud.Estudios}}</td>
            <td>{{Estud.Nacimiento}}</td>
            <td>{{Estud.LugarDeNacimiento}}</td>
            <td>{{Estud.ProvinciaDeNacimiento}}</td>
            <td>{{Estud.IDNacionalidad}}</td>
            <td>{{Estud.Sexo}}</td>
          </tr>       
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
  export default{
        name:"ListAlumnos",
        data(){
            return{
              Alumnos:[],
              pagina:1
            }
        },
      methods: {
          getAlumnos() {
             axios
               const baseURL = "http://localhost:8000";

    // obtengo token del localstorage
    let authTokens = localStorage.getItem("token")



    const axiosInstance = axios.create({
      baseURL,
      headers: { Authorization: `Token ${authTokens}` },
      
    });
     
      
        axiosInstance.get(`/api/v1.0/appcentro/`).then(data =>{
          console.log(data)
          this.Alumnos = data.data;
          this.pagina
        })
          },
    
            editar(Documento){
              console.log(Documento)
              this.$router.push('/edit/' + Documento);
            }
        },
           
        created() {
            this.getAlumnos();
            
        },        
}
</script>
<style lang="css" scoped>


</style>
    