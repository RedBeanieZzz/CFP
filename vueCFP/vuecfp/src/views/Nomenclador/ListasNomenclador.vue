<template>
	<nav>
		<NavBar/>
	</nav>
	<div>
		<h1>Nomencladores</h1>
		<div>
			<table class="table table-hover">
				<thead>
					<tr>
						<th scope="col">CodigoDeArea</th>
						<th scope="col">CodigoDePerfil</th>
						<th scope="col">NombreDeArea</th>
						<th scope="col">NombreDePerfil</th>
						<th scope="col">CargaHoraria</th>
						<th scope="col">Requisitos</th>
						<th scope="col">NivelDeCertificacion</th>
						<th scope="col">Programacion</th>
						<th scope="col">TipoDeCapacitacion</th>
						<th scope="col">Anexo</th>
						<th scope="col">Observaciones</th>
					</tr>
				</thead>
				<tbody>
					<tr v-for="Nom in Nomenclador" :key="Nom.CodigoDeArea">
						<th scope="row"><button type="button" class=" btn btn-secondary btn-outline-info" style="background-color: #008080" v-on:click="editar(Nom.CodigoDeArea)">{{Nom.CodigoDeArea}}</button></th>
						<td>{{Nom.CodigoDePerfil}}</td>
						<td>{{Nom.NombreDeArea}}</td>
						<td>{{Nom.NombreDePerfil}}</td>
						<td>{{Nom.CargaHoraria}}</td>
						<td>{{Nom.Requisitos}}</td>
						<td>{{Nom.NivelDeCertificacion}}</td>
						<td>{{Nom.Programacion}}</td>
						<td>{{Nom.TipoDeCapacitacion}}</td>
						<td>{{Nom.Anexo}}</td>
						<td>{{Nom.Observaciones}}</td>
						
					</tr>
				</tbody>
			</table>
		</div>
	</div>
	<footer>
		<FooterComp/>
	</footer>
</template>

<script>
import axios from 'axios';

export default{
	name:'ListNomenc',
	data(){
		return{
			Nomenclador:[],
			pagina:1
		}
	},
	methods: {
		getNomenc() {
			axios
				const baseURL = "http://localhost:8000";
		
		let authTokens = localStorage.getItem("token")
		
		const axiosInstance = axios.create({
			baseURL,
			headers: {Authorization: `Token ${authTokens}`},
		});

		axiosInstance.get(`/api/v1.0/Nomencladors/`).then(data =>{
			console.log(data)
			this.Nomenclador = data.data;
			this.pagina
		})

		},

		editar(CodigoDeArea){
			console.log(CodigoDeArea)
			this.$router.push('/editNomenc/' + CodigoDeArea);
		}
	},
	created() {
		this.getNomenc();
	},
	
}
</script>