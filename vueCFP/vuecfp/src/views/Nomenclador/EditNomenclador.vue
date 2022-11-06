<template>
	<div>
		<h1> Editar Nomenclador </h1>
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
				<div class="form-group left " >
				<label for="" class="control-label col-sm-2">TipoDeCapacitacion</label>
				<div class="col-sm-5">
				<input type="text" class="form-control" name="TipoDeCapacitacion" id="TipoDeCapacitacion" v-model="form.TipoDeCapacitacion">
				</div>
				<div class="form-group left " >
				<label for="" class="control-label col-sm-2">Anexo</label>
				<div class="col-sm-5">
				<input type="text" class="form-control" name="Anexo" id="Anexo" v-model="form.Anexo">
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
	name:"EditNomenc",

data:function(){
		return {
			NomCodigoDeArea:null,
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
			},
		}
	},
	methods:{
		editar(){
			this.form.CodigoDeArea = this.$route.params.CodigoDeArea;
			axios
			const baseURL = "http://localhost:8000";
			let authTokens = localStorage.getItem("token")
			const axiosInstance = axios.create({
				baseURL,
				headers: { Authorization: `Token ${authTokens}` },
			});
			axiosInstance.put("/api/v1.0/Nomencladors/" + this.form.CodigoDeArea + "/", this.form).then((data)=>{
				console.log(data)
				swal ("Nomenclador editado satisfactoriamente :-)!", "", "success")
				this.$router.push('/listNomenc')
			})
		},

		salir(){
			this.$router.push("/listNomenc")
	},
		eliminar(){
			let authTokens = localStorage.getItem("token")
			const axiosInstance = axios.create({
			headers: { Authorization: `Token ${authTokens}` },
		});
			const path = `http://localhost:8000/api/v1.0/Nomencladors/${this.form.CodigoDeArea}`;
						axiosInstance.delete(path).then((response)=>{
								console.log(response)
								swal("Eliminado correctamente", "Perfil eliminado")
								this.$router.push('/listNomenc')
		})
	},
	},
	
		mounted:function(){
		this.form.CodigoDeArea = this.$route.params.CodigoDeArea;
		axios
						const baseURL = "http://localhost:8000";

// obtengo token del localstorage
let authTokens = localStorage.getItem("token")


const axiosInstance = axios.create({
	baseURL,
	headers: { Authorization: `Token ${authTokens}` },
});

		axiosInstance.get(`/api/v1.0/Nomencladors/`+ this.form.CodigoDeArea).then(data =>{
			
			this.Nomenclador = data.data;
			this.form.CodigoDeArea = data.data.CodigoDeArea;
			this.form.CodigoDePerfil = data.data.CodigoDePerfil;
			this.form.NombreDeArea = data.data.NombreDeArea;
			this.form.NombreDePerfil = data.data.NombreDePerfil;
			this.form.CargaHoraria = data.data.CargaHoraria;
			this.form.Requisitos = data.data.Requisitos;
			this.form.NivelDeCertificacion = data.data.NivelDeCertificacion;
			this.form.Programacion = data.data.Programacion;
			this.form.TipoDeCapacitacion = data.data.TipoDeCapacitacion;
			this.form.Anexo = data.data.Anexo;
			this.form.Observaciones = data.data.Observaciones;
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