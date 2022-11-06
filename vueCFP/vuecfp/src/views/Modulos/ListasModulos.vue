<template>
	<nav>
		<NavBar/>
	</nav>
	<div>
		<h1>Modulos</h1>
		<div>
			<table class="table table-hover">
				<thead>
					<tr>
						<th scope="col">IDModulo</th>
						<th scope="col">IDCurso</th>
						<th scope="col">Nombre</th>
					</tr>
				</thead>
				<tbody>
					<tr v-for="Mod in Modules" :key="Mod.IDModulo">
						<th scope="row"><button type="button" class="btn btn-secondary btn-outline-info" style="background-color: #008080" v-on:click="editar(Mod.IDModulo)">{{Mod.IDModulo}}</button></th>
						<td>{{Mod.IDCurso}}</td>
						<td>{{Mod.Nombre}}</td>						
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
	name:'ListModulos',
	data(){
		return{
			Modules:[],
			pagina:1
		}
	},
	methods: {
		getModulo() {
			axios
				const baseURL = "http://localhost:8000";
		
		let authTokens = localStorage.getItem("token")
		
		const axiosInstance = axios.create({
			baseURL,
			headers: {Authorization: `Token ${authTokens}`},
		});

		axiosInstance.get(`/api/v1.0/Modulos/`).then(data =>{
			console.log(data)
			this.Modules = data.data;
			this.pagina
		})

		},

		editar(IDModulos){
			console.log(IDModulos)
			this.$router.push('/editModulos/' + IDModulos);
		}
	},
	created() {
		this.getModulo();
	},
	
}
</script>