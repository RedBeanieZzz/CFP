<template>
    <div>
        <NavBar/>
    </div>
    <div>
        <div class="container">
            <form action="" class="form-horizontal"> 
                <div class="form-group left " >
                <label for="" class="control-label col-sm-2">IDCurso</label>
                <div class="col-sm-5">
                <input type="text" class="form-control" name="IDCurso" id="IDCurso" v-model="form.IDCurso">
                </div>
                </div>
                <div class="form-group left " >
                <label for="" class="control-label col-sm-2">CFP</label>
                <div class="col-sm-5">
                <input type="text" class="form-control" name="CFP" id="CFP" v-model="form.CFP">
                </div>
                </div>
                <div class="form-group left " >
                <label for="" class="control-label col-sm-2">CicloLectivo</label>
                <div class="col-sm-5">
                <input type="text" class="form-control" name="CicloLectivo" id="CicloLectivo" v-model="form.CicloLectivo">
                </div>
                </div>
                <div class="form-group left ">
                <label for="" class="control-label col-sm-2">Nombre</label>
                <div class="col-sm-5">
                <input type="text" class="form-control" name="Nombre" id="Nombre" v-model="form.Nombre">
                </div>
                </div>
                <div class="form-group left " >
                <label for="" class="control-label col-sm-2">CodigoDeArea</label>
                <div class="col-sm-5">
                <input type="text" class="form-control" name="CodigoDeArea" id="CodigoDeArea" v-model="form.CodigoDeArea">
                </div>
                </div>
                <div class="form-group left " >
                <label for="" class="control-label col-sm-2">CodigoDePerfil</label>
                <div class="col-sm-5">
                <input type="text" class="form-control" name="CodigoDePerfil" id="CodigoDePerfil" v-model="form.CodigoDePerfil">
                </div>
                </div>
                <div class="form-group left " >
                <label for="" class="control-label col-sm-2">Resolucion</label>
                <div class="col-sm-5">
                <input type="text" class="form-control" name="Resolucion" id="Resolucion" v-model="form.Resolucion">
                </div>
                </div>
                <div class="form-group left " >
                <label for="" class="control-label col-sm-2">Anexo</label>
                <div class="col-sm-5">
                <input type="text" class="form-control" name="Anexo" id="Anexo" v-model="form.Anexo">
                </div>
                </div>
                <div class="form-group left " >
                <label for="" class="control-label col-sm-2">CantidadDeClases</label>
                <div class="col-sm-5">
                <input type="text" class="form-control" name="CantidadDeClases" id="CantidadDeClases" v-model="form.CantidadDeClases">
                </div>
                </div>
                <div class="form-group left " >
                <label for="" class="control-label col-sm-2">Inicio</label>
                <div class="col-sm-5">
                <input type="text" class="form-control" name="Inicio" id="Inicio" v-model="form.Inicio">
                </div>
                </div>
                <div class="form-group left " >
                <label for="" class="control-label col-sm-2">Final</label>
                <div class="col-sm-5">
                <input type="text" class="form-control" name="Final" id="Final" v-model="form.Final">
                </div>
                </div>
                <div class="form-group left " >
                <label for="" class="control-label col-sm-2">Horario</label>
                <div class="col-sm-5">
                <input type="text" class="form-control" name="Horario" id="Horario" v-model="form.Horario">
                </div>
                </div>
                <div class="form-group" >
                    <button type="button" class="btn btn-primary" v-on:click="guardar()">Guardar</button>
                    <button type="button" class="btn btn-dark margen" v-on:click="salir()">Salir</button>
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
                "IDCurso":"",
                "CFP": "",
                "CicloLectivo": "",
                "Nombre": "",
                "CodigoDeArea" : "",
                "CodigoDePerfil": "",
                "Resolucion": "",
                "Anexo" : "",
                "CantidadDeClases": "",
                "Inicio": "",
                "Final": "",
                "Horario": ""
            }
        }
    },

    methods:{
        guardar(){
            let authTokens = localStorage.getItem("token")
            const axiosInstance = axios.create({
                headers: { Authorization: `Token ${authTokens}` },
            });
            axiosInstance.post("http://localhost:8000/api/v1.0/Cursos/", this.form).then((data)=>{
                console.log(data)
                swal("Hecho","Curso creado","success");
                this.$router.push("/listCurso");
            })
            .catch(error =>{
                console.log(error);
                swal("Error","Error al guardar","error");
            })
        },
        salir(){
            this.$router.push("/listCurso");
        },
        
    }, 
}
</script>

<style scoped>
.left{
    text-align:  left;
}
</style>