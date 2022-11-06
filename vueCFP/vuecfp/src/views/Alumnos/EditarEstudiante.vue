<template>
	<div>
		<h1> Editar Alumno </h1>
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
					<button type="button" class="btn btn-primary" v-on:click="editar()">Editar</button>
					<button type="button" class="btn btn-danger margen" v-on:click="eliminar()">Eliminar</button>
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
			</form>
		</div>
	</div>
</template>
<script>
import swal from 'sweetalert'
import axios from 'axios';
export default{
	name:"EditarEst",

data:function(){
		return {
			EstudDocumento:null,
			form:{
				"Documento":"",
				"ApellidoyNombre": "",
				"Dirección": "",
				"Localidad": "",
				"Telefono" : "",
				"Estudios": "",
				"Nacimiento": "",
				"LugarDeNacimiento": "",
				"ProvinciaDeNacimiento": "",
				"IDNacionalidad": "",
				"Sexo": ""
			},
		}
	},
	methods:{
		editar(){
			this.form.Documento = this.$route.params.Documento;
			axios
			const baseURL = "http://localhost:8000";
			let authTokens = localStorage.getItem("token")
			const axiosInstance = axios.create({
				baseURL,
				headers: { Authorization: `Token ${authTokens}` },
			});
			axiosInstance.put("/api/v1.0/appcentro/" + this.form.Documento + "/", this.form).then((data)=>{
				console.log(data)
				swal ("Alumno editado satisfactoriamente :-)!", "", "success")
				this.$router.push('/listas')
			})
		},

		salir(){
			this.$router.push("/listas")
	},
		eliminar(){
			let authTokens = localStorage.getItem("token")
			const axiosInstance = axios.create({
			headers: { Authorization: `Token ${authTokens}` },
		});
			const path = `http://localhost:8000/api/v1.0/appcentro/${this.form.Documento}`;
						axiosInstance.delete(path).then((response)=>{
								console.log(response)
								swal("Eliminado correctamente", "Perfil eliminado")
								this.$router.push('/listas')
		})
	},
	},
	
		mounted:function(){
		this.form.Documento = this.$route.params.Documento;
		axios
						const baseURL = "http://localhost:8000";

// obtengo token del localstorage
let authTokens = localStorage.getItem("token")


const axiosInstance = axios.create({
	baseURL,
	headers: { Authorization: `Token ${authTokens}` },
});

		axiosInstance.get(`/api/v1.0/appcentro/`+ this.form.Documento).then(data =>{
			
			this.Alumnos = data.data;
			this.form.Documento = data.data.Documento;
			this.form.ApellidoyNombre = data.data.ApellidoyNombre;
			this.form.Direccion = data.data.Direccion;
			this.form.Localidad = data.data.Localidad;
			this.form.Telefono = data.data.Telefono;
			this.form.Estudios = data.data.Estudios;
			this.form.Nacimiento = data.data.Nacimiento;
			this.form.LugarDeNacimiento = data.data.LugarDeNacimiento;
			this.form.ProvinciaDeNacimiento = data.data.ProvinciaDeNacimiento;
			this.form.IDNacionalidad = data.data.IDNacionalidad;
			this.form.Sexo = data.data.Sexo;
			console.log(this.form);
			this.pagina
		})
	}
}
</script>

	<style scoped>
		.left{
			text-align: left;
		}
</style>