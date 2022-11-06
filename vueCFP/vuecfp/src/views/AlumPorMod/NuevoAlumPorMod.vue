<template>
    <div>
        <NavBar/>
    </div>
    <div>
        <div class="container">
            <form action="" class="form-horizontal"> 
                <div class="form-group left " >
                <label for="" class="control-label col-sm-2">IDAlumPorMod</label>
                <div class="col-sm-5">
                <input type="text" class="form-control" name="IDAlumPorMod" id="IDAlumPorMod" v-model="form.IDAlumPorMod">
                </div>
                <div class="form-group left " >
                <label for="" class="control-label col-sm-2">Documento</label>
                <div class="col-sm-5">
                <input type="text" class="form-control" name="Documento" id="Documento" v-model="form.Documento">
                </div>
                <div class="form-group left " >
                <label for="" class="control-label col-sm-2">IDModulo</label>
                <div class="col-sm-5">
                <input type="text" class="form-control" name="IDModulo" id="IDModulo" v-model="form.IDModulo">
                </div>
                <div class="form-group left ">
                <label for="" class="control-label col-sm-2">IDCurso</label>
                <div class="col-sm-5">
                <input type="text" class="form-control" name="IDCurso" id="IDCurso" v-model="form.IDCurso">
                </div>
                <div class="form-group left " >
                <label for="" class="control-label col-sm-2">CFP</label>
                <div class="col-sm-5">
                <input type="text" class="form-control" name="CFP" id="CFP" v-model="form.CFP">
                </div>
                <div class="form-group left " >
                <label for="" class="control-label col-sm-2">Nota</label>
                <div class="col-sm-5">
                <input type="text" class="form-control" name="Nota" id="Nota" v-model="form.Nota">
                </div>
                <div class="form-group left " >
                <label for="" class="control-label col-sm-2">Vencimiento</label>
                <div class="col-sm-5">
                <input type="date" required pattern="\d{4}-\4{2}-\d{2}" class="form-control" name="Vencimiento" id="Vencimiento" v-model="form.Vencimiento">
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
                "IDAlumPorMod":"",
                "Documento": "",
                "IDModulo": "",
                "IDCurso": "",
                "CFP" : "",
                "Nota": "",
                "Vencimiento": ""
            }
        }
    },

    methods:{
        guardar(){
            let authTokens = localStorage.getItem("token")
            const axiosInstance = axios.create({
                headers: { Authorization: `Token ${authTokens}` },
            });
            axiosInstance.post("http://localhost:8000/api/v1.0/AlumPorMod/", this.form).then((data)=>{
                console.log(data)
                swal("Hecho","Alumno creado","success");
                this.$router.push("/listAlumPorMod");
            })
            .catch(error =>{
                console.log(error);
                swal("Error","Error al guardar","error");
            })
        },
        salir(){
            this.$router.push("/listAlumPorMod");
        },
        
    }, 
}
</script>

<style scoped>
.left{
    text-align:  left;
}
</style>