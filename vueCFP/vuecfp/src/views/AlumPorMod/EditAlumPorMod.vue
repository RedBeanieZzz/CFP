<template>
	<div>
		<h1> Editar Alumno por Modulo </h1>
		<div class="container">
			<form action="" class="form-horizontal"> 
				<div class="form-group left " >
					<label for="" class="control-label col-sm-2">IDAlumPorMod</label>
					<div class="col-sm-5">
					<input type="text" class="form-control" name="IDAlumPorMod" id="IDAlumPorMod" v-model="form.IDAlumPorMod">
					</div>
				</div>
				<div>
					<label for="" class="control-label col-sm-2">Documento</label>
					<div class="col-sm-5">
					<input type="text" class="form-control" name="Documento" id="Documento" v-model="form.Documento">
					</div>
				</div>
				<div class="form-group left " >
					<label for="" class="control-label col-sm-2">IDModulo</label>
					<div class="col-sm-5">
						<input type="text" class="form-control" name="IDModulo" id="IDModulo" v-model="form.IDModulo">
					</div>
				</div>
				<div class="form-group left " >
					<label for="" class="control-label col-sm-2">IDCurso</label>
					<div class="col-sm-5">
						<input type="text" class="form-control" name="IDCurso" id="IDCurso" v-model="form.IDCurso">
					</div>
				</div>
				<div class="form-group left ">
					<label for="" class="control-label col-sm-2">CFP</label>
					<div class="col-sm-5">
						<input type="text" class="form-control" name="CFP" id="CFP" v-model="form.CFP">
					</div>
				</div>
				<div class="form-group left " >
					<label for="" class="control-label col-sm-2">Nota</label>
					<div class="col-sm-5">
						<input type="text" class="form-control" name="Nota" id="Nota" v-model="form.Nota">
					</div>
				</div>
				<div class="form-group left " >
					<label for="" class="control-label col-sm-2">Vencimiento</label>
					<div class="col-sm-5">
						<input type="text" class="form-control" name="Vencimiento" id="Vencimiento" v-model="form.Vencimiento">
					</div>
				</div>
				<div class="form-group" >
					<button type="button" class="btn btn-primary" v-on:click="editar()">Editar</button>
					<button type="button" class="btn btn-danger margen" v-on:click="eliminar()">Eliminar</button>
					<button type="button" class="btn btn-dark margen" v-on:click="salir()">Salir</button>
				</div>
			</form>
		</div>
	</div>
</template>
<script>
import swal from 'sweetalert'
import axios from 'axios';
export default{
	name:"EditAlumPorMod",

data:function(){
		return {
			AlumIDAlumPorMod:null,
			form:{
				"IDAlumPorMod":"",
				"Documento" : "",
				"IDModulo": "",
				"IDCurso": "",
				"CFP": "",
				"Nota" : "",
				"Vencimiento" : "",
			},
		}
	},
	methods:{
		editar(){
			this.form.IDAlumPorMod = this.$route.params.IDAlumPorMod;
			axios
			const baseURL = "http://localhost:8000";
			let authTokens = localStorage.getItem("token")
			const axiosInstance = axios.create({
				baseURL,
				headers: { Authorization: `Token ${authTokens}` },
			});
			axiosInstance.put("/api/v1.0/AlumPorMod/" + this.form.IDAlumPorMod + "/", this.form).then((data)=>{
				console.log(data)
				swal ("Alumno editado satisfactoriamente :-)!", "", "success")
				this.$router.push('/listAlumPorMod')
			})
		},

		salir(){
			this.$router.push("/listAlumPorMod")
	},
		eliminar(){
			let authTokens = localStorage.getItem("token")
			const axiosInstance = axios.create({
			headers: { Authorization: `Token ${authTokens}` },
		});
			const path = `http://localhost:8000/api/v1.0/AlumPorMod/${this.form.IDAlumPorMod}`;
						axiosInstance.delete(path).then((response)=>{
								console.log(response)
								swal("Eliminado correctamente", "Perfil eliminado")
								this.$router.push('/listAlumPorMod')
		})
	},
	},
	
		mounted:function(){
		this.form.IDAlumPorMod = this.$route.params.IDAlumPorMod;
		axios
						const baseURL = "http://localhost:8000";

// obtengo token del localstorage
let authTokens = localStorage.getItem("token")


const axiosInstance = axios.create({
	baseURL,
	headers: { Authorization: `Token ${authTokens}` },
});

		axiosInstance.get(`/api/v1.0/AlumPorMod/`+ this.form.IDAlumPorMod).then(data =>{
			
			this.AlumPorMods = data.data;
			this.form.IDAlumPorMod = data.data.IDAlumPorMod;
			this.form.Documento = data.data.Documento;
			this.form.IDModulo = data.data.IDModulo;
			this.form.IDCurso = data.data.IDCurso;
			this.form.CFP = data.data.CFP;
			this.form.Nota = data.data.Nota;
			this.form.Vencimiento = data.data.Vencimiento;
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