<template>
	<div>
		<h1> Editar Alumno </h1>
		<div class="container">
			<form action="" class="form-horizontal"> 
				<div class="form-group left " >
				<label for="" class="control-label col-sm-2">IDModulo</label>
				<div class="col-sm-5">
				<input type="text" class="form-control" name="IDModulo" id="IDModulo" v-model="form.IDModulo">
				</div>
				<div class="form-group left " >
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
					<button type="button" class="btn btn-primary" v-on:click="editar()">Editar</button>
					<button type="button" class="btn btn-danger margen" v-on:click="eliminar()">Eliminar</button>
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
import swal from 'sweetalert'
import axios from 'axios';
export default{
	name:"EditarModulo",

data:function(){
		return {
			ModIDModulo:null,
			form:{
				"IDModulo":"",
				"IDCurso": "",
				"Nombre": "",
			},
		}
	},
	methods:{
		editar(){
			this.form.IDModulo = this.$route.params.IDModulo;
			axios
			const baseURL = "http://localhost:8000";
			let authTokens = localStorage.getItem("token")
			const axiosInstance = axios.create({
				baseURL,
				headers: { Authorization: `Token ${authTokens}` },
			});
			axiosInstance.put("/api/v1.0/Modulos/" + this.form.IDModulo + "/", this.form).then((data)=>{
				console.log(data)
				swal ("Modulo editado satisfactoriamente :-)!", "", "success")
				this.$router.push('/listModulos')
			})
		},

		salir(){
			this.$router.push("/listModulos")
	},
		eliminar(){
			let authTokens = localStorage.getItem("token")
			const axiosInstance = axios.create({
			headers: { Authorization: `Token ${authTokens}` },
		});
			const path = `http://localhost:8000/api/v1.0/Modulos/${this.form.IDModulo}`;
						axiosInstance.delete(path).then((response)=>{
								console.log(response)
								swal("Eliminado correctamente", "Perfil eliminado")
								this.$router.push('/listModulos')
		})
	},
	},
	
		mounted:function(){
		this.form.IDModulo = this.$route.params.IDModulo;
		axios
						const baseURL = "http://localhost:8000";

// obtengo token del localstorage
let authTokens = localStorage.getItem("token")


const axiosInstance = axios.create({
	baseURL,
	headers: { Authorization: `Token ${authTokens}` },
});

		axiosInstance.get(`/api/v1.0/Modulos/`+ this.form.IDModulo).then(data =>{
			
			this.Modulos = data.data;
			this.form.IDModulo = data.data.IDModulo;
			this.form.IDCurso = data.data.IDCurso;
			this.form.Nombre = data.data.Nombre;
			
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