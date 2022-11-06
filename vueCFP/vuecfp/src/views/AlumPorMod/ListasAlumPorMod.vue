<template>
	<nav>
		<NavBar/>
	</nav>
	<div>
		<h1>Alumnos Por MOdulos</h1>
		<div>
			<table class="table table-hover">
				<thead>
					<tr>
						<th scope="col">IDAlumPorMod</th>
						<th scope="col">Documento</th>
						<th scope="col">IDModulo</th>
						<th scope="col">IDCurso</th>
						<th scope="col">CFP</th>
						<th scope="col">Nota</th>
						<th scope="col">Vencimiento</th>
					</tr>
				</thead>
				<tbody>
					<tr v-for="Alum in AlumPorMods" :key="Alum.IDAlumPorMod">
						<th scope="row"><button type="button" class="btn btn-secondary btn-outline-info" style="background-color: #008080" v-on:click="editar(Alum.IDAlumPorMod)">{{Alum.IDAlumPorMod}}</button></th>
						<td>{{Alum.Documento}}</td>
						<td>{{Alum.IDModulo}}</td>
						<td>{{Alum.IDCurso}}</td>
						<td>{{Alum.CFP}}</td>
						<td>{{Alum.Nota}}</td>
						<td>{{Alum.Vencimiento}}</td>
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
	name:'ListAlumPorMod',
	data(){
		return{
			AlumPorMods:[],
			pagina:1
		}
	},
	methods: {
		getAlumPorMod() {
			axios
				const baseURL = "http://localhost:8000";
		
		let authTokens = localStorage.getItem("token")
		
		const axiosInstance = axios.create({
			baseURL,
			headers: {Authorization: `Token ${authTokens}`},
		});

		axiosInstance.get(`/api/v1.0/AlumPorMod/`).then(data =>{
			console.log(data)
			this.AlumPorMods = data.data;
			this.pagina
		})

		},

		editar(IDAlumPorMod){
			console.log(IDAlumPorMod)
			this.$router.push('/editAlumPorMod/' + IDAlumPorMod);
		}
	},
	created() {
		this.getAlumPorMod();
	},
	
}
</script>