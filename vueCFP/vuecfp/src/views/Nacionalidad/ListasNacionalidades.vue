<template>
	<nav>
		<NavBar/>
	</nav>
	<div>
		<h1>Nacionalidades</h1>
		<div>
			<table class="table table-hover">
				<thead>
					<tr>
						<th scope="col">IDNacionalidad</th>
						<th scope="col">Nacionalidad</th>
					</tr>
				</thead>
				<tbody>
					<tr v-for="Pais in Nacionalidad" :key="Pais.IDNacionalidad">
						<th scope="row"><button type="button" class="btn btn-secondary btn-outline-info" style="background-color: #008080" v-on:click="editar(Pais.IDNacionalidad)">{{Pais.IDNacionalidad}}</button></th>
						<td>{{Pais.Nacionalidad}}</td>
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
	name:'ListNacion',
	data(){
		return{
			Nacionalidad:[],
			pagina:1
		}
	},
	methods: {
		getNacion() {
			axios
				const baseURL = "http://localhost:8000";
		
		let authTokens = localStorage.getItem("token")
		
		const axiosInstance = axios.create({
			baseURL,
			headers: {Authorization: `Token ${authTokens}`},
		});

		axiosInstance.get(`/api/v1.0/Nacionalidad/`).then(data =>{
			console.log(data)
			this.Nacionalidad = data.data;
			this.pagina
		})

		},

		editar(IDNacionalidad){
			console.log(IDNacionalidad)
			this.$router.push('/editNac/' + IDNacionalidad);
		}
	},
	created() {
		this.getNacion();
	},
	
}
</script>