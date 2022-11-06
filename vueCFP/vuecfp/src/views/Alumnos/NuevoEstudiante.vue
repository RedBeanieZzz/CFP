<template>
    <div>
        <NavBar/>
    </div>
    <div>
        <div class="container">
            <form action="" class="form-horizontal"> 
                <div class="form-group left " >
                <label for="" class="control-label col-sm-2">Documento</label>
                <div class="col-sm-5">
                <input type="text" class="form-control" name="Documento" id="Documento" v-model="form.Documento">
                </div>
                <div class="form-group left " >
                <label for="" class="control-label col-sm-2">ApellidoyNombre</label>
                <div class="col-sm-5">
                <input type="text" class="form-control" name="ApellidoyNombre" id="ApellidoyNombre" v-model="form.ApellidoyNombre">
                </div>
                <div class="form-group left " >
                <label for="" class="control-label col-sm-2">Direccion</label>
                <div class="col-sm-5">
                <input type="text" class="form-control" name="Direccion" id="Direccion" v-model="form.Direccion">
                </div>
                <div class="form-group left ">
                <label for="" class="control-label col-sm-2">Localidad</label>
                <div class="col-sm-5">
                <input type="text" class="form-control" name="Localidad" id="Localidad" v-model="form.Localidad">
                </div>
                <div class="form-group left " >
                <label for="" class="control-label col-sm-2">Telefono</label>
                <div class="col-sm-5">
                <input type="text" class="form-control" name="Telefono" id="Telefono" v-model="form.Telefono">
                </div>
                <div class="form-group left " >
                <label for="" class="control-label col-sm-2">Estudios</label>
                <div class="col-sm-5">
                <input type="text" class="form-control" name="Estudios" id="Estudios" v-model="form.Estudios">
                </div>
                <div class="form-group left " >
                <label for="" class="control-label col-sm-2">Nacimiento</label>
                <div class="col-sm-5">
                <input type="date" required pattern="\d{4}-\4{2}-\d{2}" class="form-control" name="Nacimiento" id="Nacimiento" v-model="form.Nacimiento">
                </div>
                <div class="form-group left " >
                <label for="" class="control-label col-sm-2">LugarDeNacimiento</label>
                <div class="col-sm-5">
                <input type="text" class="form-control" name="LugarDeNacimiento" id="LugarDeNacimiento" v-model="form.LugarDeNacimiento">
                </div>
                <div class="form-group left " >
                <label for="" class="control-label col-sm-2">ProvinciaDeNacimiento</label>
                <div class="col-sm-5">
                <input type="text" class="form-control" name="ProvinciaDeNacimiento" id="ProvinciaDeNacimiento" v-model="form.ProvinciaDeNacimiento">
                </div>
                <div class="form-group left " >
                <label for="" class="control-label col-sm-2">IDNacionalidad</label>
                    
                <div class="col-sm-5">
                <input type="text" class="form-control" name="IDNacionalidad" id="IDNacionalidad" v-model="form.IDNacionalidad">
                </div>
                <div class="form-group left " >
                <label for="" class="control-label col-sm-2">Sexo</label>
                <div class="col-sm-5">
                <input type="text" class="form-control" name="Sexo" id="Sexo" v-model="form.Sexo">
                </div>
                <div class="form-group" >
                    <button type="button" class="btn btn-primary" v-on:click="guardar()">Guardar</button>
                    <button type="button" class="btn btn-dark margen" v-on:click="salir()">Salir</button>
                </div>
                </div>
                </div>
                </div>
                </div>
                </div>
                </div>
                </div>
                </div>
                </div>
                </div>
                </div>
            </form>
        </div>
    </div>
</template>
<script>

import axios from 'axios';
import swal from 'sweetalert'
export default {

    data:function(){
        return {
            form:{
                "Documento":"",
                "ApellidoyNombre": "",
                "Direccion": "",
                "Localidad": "",
                "Telefono" : "",
                "Estudios": "",
                "Nacimiento": "",
                "LugarDeNacimiento": "",
                "ProvinciaDeNacimiento": "",
                "IDNacionalidad": "",
                "Sexo": ""
            }
        }
    },

    methods:{
        guardar(){
            let authTokens = localStorage.getItem("token")
            const axiosInstance = axios.create({
                headers: { Authorization: `Token ${authTokens}` },
            });
            axiosInstance.post("http://localhost:8000/api/v1.0/appcentro/", this.form).then((data)=>{
                console.log(data)
                swal("Hecho","Alumno creado","success");
                this.$router.push("/listas");
            })
            .catch(error =>{
                console.log(error);
                swal("Error","Error al guardar","error");
            })
        },
        salir(){
            this.$router.push("/listas");
        },
        
    }, 
}
</script>

<style scoped>
.left{
    text-align:  left;
}
</style>