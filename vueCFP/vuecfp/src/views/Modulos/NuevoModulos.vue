<template>
    <div>
        <NavBar/>
    </div>
    <div>
        <div class="container">
            <form action="" class="form-horizontal"> 
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
                <label for="" class="control-label col-sm-2">Nombre</label>
                <div class="col-sm-5">
                <input type="text" class="form-control" name="Nombre" id="Nombre" v-model="form.Nombre">
                </div>
                <div class="form-group" >
                    <button type="button" class="btn btn-primary" v-on:click="guardar()">Guardar</button>
                    <button type="button" class="btn btn-dark margen" v-on:click="salir()">Salir</button>
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
                "IDModulo":"",
                "IDCurso": "",
                "Nombre": "",
            }
        }
    },

    methods:{
        guardar(){
            let authTokens = localStorage.getItem("token")
            const axiosInstance = axios.create({
                headers: { Authorization: `Token ${authTokens}` },
            });
            axiosInstance.post("http://localhost:8000/api/v1.0/Modulos/", this.form).then((data)=>{
                console.log(data)
                swal("Hecho","Modulo creado","success");
                this.$router.push("/listModulos");
            })
            .catch(error =>{
                console.log(error);
                swal("Error","Error al guardar","error");
            })
        },
        salir(){
            this.$router.push("/listModulos");
        },
        
    }, 
}
</script>

<style scoped>
.left{
    text-align:  left;
}
</style>