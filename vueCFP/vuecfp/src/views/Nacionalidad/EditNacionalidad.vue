<template>
	<div>
		<h1> Editar Nacionalidad </h1>
		<div class="container">
			<form action="" class="form-horizontal"> 
				<div class="form-group left " >
					<label for="" class="control-label col-sm-2">IDNacionalidad</label>
					<div class="col-sm-5">
						<input type="text" class="form-control" name="IDNacionalidad" id="IDNacionalidad" v-model="form.IDNacionalidad">
					</div>
				</div>
				<div class="form-group left " >
					<label for="" class="control-label col-sm-2">Nacionalidad</label>
					<div class="col-sm-5">
						<input type="text" class="form-control" name="Nacionalidad" id="Nacionalidad" v-model="form.Nacionalidad">
					</div>
				</div>
					<button type="button" class="btn btn-primary" v-on:click="editar()">Editar</button>
					<button type="button" class="btn btn-danger margen" v-on:click="eliminar()">Eliminar</button>
					<button type="button" class="btn btn-dark margen" v-on:click="salir()">Salir</button>
			</form>
		</div>
	</div>				
</template>
<script>
import swal from 'sweetalert'
import axios from 'axios';
export default{
	name:"EditNac",

data:function(){
		return {
			PaisIDNacionalidad:null,
			form:{
				"IDNacionalidad":"",
				"Nacionalidad": "",
				
			},
		}
	},
	methods:{
		editar(){
			this.form.IDNacionalidad = this.$route.params.IDNacionalidad;
			axios
			const baseURL = "http://localhost:8000";
			let authTokens = localStorage.getItem("token")
			const axiosInstance = axios.create({
				baseURL,
				headers: { Authorization: `Token ${authTokens}` },
			});
			axiosInstance.put("/api/v1.0/Nacionalidad/" + this.form.IDNacionalidad + "/", this.form).then((data)=>{
				console.log(data)
				swal ("Nacionalidad editada satisfactoriamente :-)!", "", "success")
				this.$router.push('/listNac')
			})
		},

		salir(){
			this.$router.push("/listNac")
	},
		eliminar(){
			let authTokens = localStorage.getItem("token")
			const axiosInstance = axios.create({
			headers: { Authorization: `Token ${authTokens}` },
		});
			const path = `http://localhost:8000/api/v1.0/Nacionalidad/${this.form.IDNacionalidad}`;
						axiosInstance.delete(path).then((response)=>{
								console.log(response)
								swal("Eliminado correctamente", "Perfil eliminado")
								this.$router.push('/listNac')
		})
	},
	},
	
		mounted:function(){
		this.form.IDNacionalidad = this.$route.params.IDNacionalidad;
		axios
						const baseURL = "http://localhost:8000";

// obtengo token del localstorage
let authTokens = localStorage.getItem("token")


const axiosInstance = axios.create({
	baseURL,
	headers: { Authorization: `Token ${authTokens}` },
});

		axiosInstance.get(`/api/v1.0/Nacionalidad/`+ this.form.IDNacionalidad).then(data =>{
			
			this.Nacionalidad = data.data;
			this.form.IDNacionalidad = data.data.IDNacionalidad;
			this.form.Nacionalidad = data.data.Nacionalidad;
			
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