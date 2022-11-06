<template>
<nav class="navbar navbar-expand-lg bg-light" >
  <div class="container-fluid" style="background-color: #008080">
    <a class="navbar-brand text-light" href="#">C.F.P</a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarSupportedContent">
      <ul class="navbar-nav me-auto mb-2 mb-lg-0">
        <li class="nav-item">
          <a class="nav-link active text-light"  aria-current="page" href="/">Home</a>
        </li>
        <li class="nav-item dropdown">
          <a class="nav-link dropdown-toggle text-light" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
            Alumnos
          </a>
          <ul class="dropdown-menu text-light">
            <li><a class="dropdown-item" href="/listas">Listas</a></li>
            <li><a class="dropdown-item" href="/nuevo">Nuevo Alumno</a></li>
          </ul>
        </li>
        <li class="nav-item dropdown">
          <a class="nav-link dropdown-toggle text-light" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
            Nacionalidad
          </a>
          <ul class="dropdown-menu">
            <li><a class="dropdown-item" href="/listNac">Listas Nacionalidad</a></li>
            <li><a class="dropdown-item" href="/nuevoNacionalidad">Nueva Nacionalidad</a></li>
          </ul>
        </li>
        <li class="nav-item dropdown">
          <a class="nav-link dropdown-toggle text-light" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
            Nomencladores
          </a>
          <ul class="dropdown-menu">
            <li><a class="dropdown-item" href="/listNomenc">Listas Nomenclador</a></li>
            <li><a class="dropdown-item" href="/nuevoNomenclador">Nuevo Nomenclador</a></li>
          </ul>
        </li>
        <li class="nav-item dropdown">
          <a class="nav-link dropdown-toggle text-light" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
            Cursos
          </a>
          <ul class="dropdown-menu">
            <li><a class="dropdown-item" href="/listCurso">Listas Cursos</a></li>
            <li><a class="dropdown-item" href="/nuevoCurso">Nuevo Cursos</a></li>
          </ul>
        </li>
        <li class="nav-item dropdown">
          <a class="nav-link dropdown-toggle text-light" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
            Modulos
          </a>
          <ul class="dropdown-menu">
            <li><a class="dropdown-item" href="/listModulos">Listas Modulos</a></li>
            <li><a class="dropdown-item" href="/nuevoModulo">Nuevo Modulos</a></li>
          </ul>
        </li>
        <li class="nav-item dropdown">
          <a class="nav-link dropdown-toggle text-light" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
            Alumnos por modulo
          </a>
          <ul class="dropdown-menu">
            <li><a class="dropdown-item" href="/listAlumPorMod">Listas AlumPorMod</a></li>
            <li><a class="dropdown-item" href="/nuevoAlumPorMod">Nuevo AlumPorMod</a></li>
          </ul>
        </li>
      </ul>
      <div class="nav-item active" v-if="this.$store.state.isAuthenticated" style="text-align:right" >
        <ul class="navbar-nav ml-auto">
          <li class="nav-item active">
          <div class="text">Logged
          <a href="/log-in">
          <button style="text-align: right; background-color:#008080" v-on:click="LimpiarStorage" type="button" class="btn btn-secondary btn-outline-info">Log Out</button>
          </a>
          </div>
          </li>
        </ul>
     </div>
     <div v-else>
      <a href="/log-in">
        <button style="text-align: right; background-color:#008080" type="button" class="btn btn-secondary btn-outline-info">Iniciar Sesion</button>
      </a>
    </div>
    </div>
  </div>
</nav>
</template>

<script>
import axios from 'axios'
import swal from 'sweetalert'

 
export default{
    name: "NavBar",
    beforeCreate() {
        this.$store.commit("initializeStore");
        const token = this.$store.state.token;
        if (token) {
            axios.defaults.headers.common["Authorization"] = "Token" + token;
        }
        else {
            axios.defaults.headers.common["Authorization"] = "";
        }
    },
    methods: {
        LimpiarStorage() {
            localStorage.clear();
            swal("Sesión cerrada con éxito", "", "success");
        },
        ObtenerUsuario() {
            localStorage.getItem("Username");
        }
    },
}
  
 
</script>