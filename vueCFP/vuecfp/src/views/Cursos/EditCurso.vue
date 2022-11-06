<template>
	<div>
		<h1> Editar Curso </h1>
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
				<div class="form-group left">
					<label for="" class="control-label col-sm-2">Nombre</label>
					<div class="col-sm-5">
						<input type="text" class="form-control" name="Nombre" id="Nombre" v-model="form.Nombre">
					</div>
				</div>
				<div class="form-group left">
					<label for="" class="control-label col-sm-2">CodigoDeArea</label>
					<div class="col-sm-5">
						<input type="text" class="form-control" name="CodigoDeArea" id="CodigoDeArea" v-model="form.CodigoDeArea">
					</div>
				</div>
				<div class="form-group left">
					<label for="" class="control-label col-sm-2">CodigoDePerfil</label>
					<div class="col-sm-5">
						<input type="text" class="form-control" name="CodigoDePerfil" id="CodigoDePerfil" v-model="form.CodigoDePerfil">
					</div>
				</div>
				<div class="form-group left">
					<label for="" class="control-label col-sm-2">Resolucion</label>
					<div class="col-sm-5">
						<input type="text" class="form-control" name="Resolucion" id="Resolucion" v-model="form.Resolucion">
					</div>
				</div>
				<div class="form-group left">
					<label for="" class="control-label col-sm-2">Anexo</label>
					<div class="col-sm-5">
						<input type="text" class="form-control" name="Anexo" id="Anexo" v-model="form.Anexo">
					</div>
				</div>
				<div class="form-group left">
					<label for="" class="control-label col-sm-2">CantidadDeClases</label>
					<div class="col-sm-5">
						<input type="text" class="form-control" name="CantidadDeClases" id="CantidadDeClases" v-model="form.CantidadDeClases">
					</div>
				</div>
				<div class="form-group left">
					<label for="" class="control-label col-sm-2">Inicio</label>
					<div class="col-sm-5">
						<input type="text" class="form-control" name="Inicio" id="Inicio" v-model="form.Inicio">
					</div>
				</div>
				<div class="form-group left">
					<label for="" class="control-label col-sm-2">Final</label>
					<div class="col-sm-5">
						<input type="text" class="form-control" name="Final" id="Final" v-model="form.Final">
					</div>
				</div>
				<div class="form-group left">
					<label for="" class="control-label col-sm-2">Horario</label>
					<div class="col-sm-5">
						<input type="text" class="form-control" name="Horario" id="Horario" v-model="form.Horario">
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
	name:"EditarCurso",

data:function(){
		return {
			CurIDCurso:null,
			form:{
				"IDCurso":"",
				"CFP": "",
				"CicloLectivo": "",
				"Nombre": "",
				"CodigoDeArea": "",
				"CodigoDePerfil": "",
				"Resolucion": "",
				"Anexo": "",
				"CantidadDeClases": "",
				"Inicio": "",
				"Final": "",
				"Horario": "",
			},
		}
	},
	methods:{
		editar(){
			this.form.IDCurso = this.$route.params.IDCurso;
			axios
			const baseURL = "http://localhost:8000";
			let authTokens = localStorage.getItem("token")
			const axiosInstance = axios.create({
				baseURL,
				headers: { Authorization: `Token ${authTokens}` },
			});
			axiosInstance.put("/api/v1.0/Cursos/" + this.form.IDCurso + "/", this.form).then((data)=>{
				console.log(data)
				swal ("Modulo editado satisfactoriamente :-)!", "", "success")
				this.$router.push('/listCurso')
			})
		},

		salir(){
			this.$router.push("/listCurso")
	},
		eliminar(){
			let authTokens = localStorage.getItem("token")
			const axiosInstance = axios.create({
			headers: { Authorization: `Token ${authTokens}` },
		});
			const path = `http://localhost:8000/api/v1.0/Cursos/${this.form.IDCurso}`;
						axiosInstance.delete(path).then((response)=>{
								console.log(response)
								swal("Eliminado correctamente", "Perfil eliminado")
								this.$router.push('/listCurso')
		})
	},
	},
	
		mounted:function(){
		this.form.IDCurso = this.$route.params.IDCurso;
		axios
						const baseURL = "http://localhost:8000";

// obtengo token del localstorage
let authTokens = localStorage.getItem("token")


const axiosInstance = axios.create({
	baseURL,
	headers: { Authorization: `Token ${authTokens}` },
});

		axiosInstance.get(`/api/v1.0/Cursos/`+ this.form.IDCurso).then(data =>{
			
			this.Cursos = data.data;
			this.form.IDCurso = data.data.IDCurso;
			this.form.CFP = data.data.CFP;
			this.form.CicloLectivo = data.data.CicloLectivo;
			this.form.Nombre = data.data.Nombre ;
			this.form.CodigoDeArea = data.data.CodigoDeArea ;
			this.form.CodigoDePerfil = data.data.CodigoDePerfil ;
			this.form.Resolucion = data.data.Resolucion ;
			this.form.Anexo = data.data.Anexo ;
			this.form.CantidadDeClases = data.data.CantidadDeClases ;
			this.form.Inicio = data.data.Inicio ;
			this.form.Final = data.data.Final ;
			this.form.Horario = data.data.Horario ;
			
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