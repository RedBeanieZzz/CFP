<template>
	<nav>
		<NavBar/>
	</nav>
	<div>
		<h1>Cursos</h1>
		<div>
			<table class="table table-hover">
				<thead>
					<tr>
						<th scope="col">IDCurso</th>
						<th scope="col">CFP</th>
						<th scope="col">CicloLectivo</th>
						<th scope="col">Nombre</th>
						<th scope="col">CodigoDeArea</th>
						<th scope="col">CodigoDePerfil</th>
						<th scope="col">Resolucion</th>
						<th scope="col">Anexo</th>
						<th scope="col">CantidadDeClases</th>
						<th scope="col">Inicio</th>
						<th scope="col">Final</th>
						<th scope="col">Horario</th>
					</tr>
				</thead>
				<tbody>
					<tr v-for="Cur in Cursos" :key="Cur.IDCurso">
						<th scope="row"><button type="button" class="btn btn-secondary btn-outline-info" style="background-color: #008080" v-on:click="editar(Cur.IDCurso)">{{Cur.IDCurso}}</button></th>
						<td>{{Cur.CFP}}</td>
						<td>{{Cur.CicloLectivo}}</td>
						<td>{{Cur.Nombre}}</td>
						<td>{{Cur.CodigoDeArea}}</td>
						<td>{{Cur.CodigoDePerfil}}</td>
						<td>{{Cur.Resolucion}}</td>
						<td>{{Cur.Anexo}}</td>
						<td>{{Cur.CantidadDeClases}}</td>
						<td>{{Cur.Inicio}}</td>
						<td>{{Cur.Final}}</td>
						<td>{{Cur.Horario}}</td>
						
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
	name:'ListCursos',
	data(){
		return{
			Cursos:[],
			pagina:1
		}
	},
	methods: {
		getCursos() {
			axios
				const baseURL = "http://localhost:8000";
		
		let authTokens = localStorage.getItem("token")
		
		const axiosInstance = axios.create({
			baseURL,
			headers: {Authorization: `Token ${authTokens}`},
		});

		axiosInstance.get(`/api/v1.0/Cursos/`).then(data =>{
			console.log(data)
			this.Cursos = data.data;
			this.pagina
		})

		},

		editar(IDCursos){
			console.log(IDCursos)
			this.$router.push('/editCurso/' + IDCursos);
		}
	},
	created() {
		this.getCursos();
	},
	
}
</script>