<template>
    <div>
        <NavBar/>
    </div>
    <div>
        <div class="container">
            <form action="" class="form-horizontal"> 
                <div class="form-group left " >
                <label for="" class="control-label col-sm-2">CodigoDeArea</label>
                <div class="col-sm-5">
                <input type="text" class="form-control" name="CodigoDeArea" id="CodigoDeArea" v-model="form.CodigoDeArea">
                </div>
                <div class="form-group left " >
                <label for="" class="control-label col-sm-2">CodigoDePerfil</label>
                <div class="col-sm-5">
                <input type="text" class="form-control" name="CodigoDePerfil" id="CodigoDePerfil" v-model="form.CodigoDePerfil">
                </div>
                <div class="form-group left " >
                <label for="" class="control-label col-sm-2">NombreDeArea</label>
                <div class="col-sm-5">
                <input type="text" class="form-control" name="NombreDeArea" id="NombreDeArea" v-model="form.NombreDeArea">
                </div>
                <div class="form-group left ">
                <label for="" class="control-label col-sm-2">NombreDePerfil</label>
                <div class="col-sm-5">
                <input type="text" class="form-control" name="NombreDePerfil" id="NombreDePerfil" v-model="form.NombreDePerfil">
                </div>
                <div class="form-group left " >
                <label for="" class="control-label col-sm-2">CargaHoraria</label>
                <div class="col-sm-5">
                <input type="text" class="form-control" name="CargaHoraria" id="CargaHoraria" v-model="form.CargaHoraria">
                </div>
                <div class="form-group left " >
                <label for="" class="control-label col-sm-2">Requisitos</label>
                <div class="col-sm-5">
                <input type="text" class="form-control" name="Requisitos" id="Requisitos" v-model="form.Requisitos">
                </div>
                <div class="form-group left " >
                <label for="" class="control-label col-sm-2">NivelDeCertificacion</label>
                <div class="col-sm-5">
                <input type="text" class="form-control" name="NivelDeCertificacion" id="NivelDeCertificacion" v-model="form.NivelDeCertificacion">
                </div>
                <div class="form-group left " >
                <label for="" class="control-label col-sm-2">Programacion</label>
                <div class="col-sm-5">
                <input type="text" class="form-control" name="Programacion" id="Programacion" v-model="form.Programacion">
                </div>
                </div>
                <div class="form-group left " >
                <label for="" class="control-label col-sm-2">TipoDeCapacitacion</label>
                <div class="col-sm-5">
                <input type="text" class="form-control" name="TipoDeCapacitacion" id="TipoDeCapacitacion" v-model="form.TipoDeCapacitacion">
                </div>
                </div>
                <div class="form-group left " >
                <label for="" class="control-label col-sm-2">Anexo</label>
                <div class="col-sm-5">
                <input type="text" class="form-control" name="Anexo" id="Anexo" v-model="form.Anexo">
                </div>
                </div>
                <div class="form-group left " >
                <label for="" class="control-label col-sm-2">Observaciones</label>
                <div class="col-sm-5">
                <input type="text" class="form-control" name="Observaciones" id="Observaciones" v-model="form.Observaciones">
                </div>
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
                "CodigoDeArea":"",
                "CodigoDePerfil": "",
                "NombreDeArea": "",
                "NombreDePerfil": "",
                "CargaHoraria" : "",
                "Requisitos": "",
                "NivelDeCertificacion": "",
                "Programacion": "",
                "TipoDeCapacitacion": "",
                "Anexo": "",
                "Observaciones": ""
            }
        }
    },

    methods:{
        guardar(){
            let authTokens = localStorage.getItem("token")
            const axiosInstance = axios.create({
                headers: { Authorization: `Token ${authTokens}` },
            });
            axiosInstance.post("http://localhost:8000/api/v1.0/Nomencladors/", this.form).then((data)=>{
                console.log(data)
                swal("Hecho","Nomenclador creado","success");
                this.$router.push("/listNomenc");
            })
            .catch(error =>{
                console.log(error);
                swal("Error","Error al guardar","error");
            })
        },
        salir(){
            this.$router.push("/listNomenc");
        },
        
    }, 
}
</script>

<style scoped>
.left{
    text-align:  left;
}
</style>