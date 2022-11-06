<template>

	<div id="app">
	
		<div class="login-page">
				<transition name="fade">
					<div v-if="!registerActive" class="wallpaper-login"></div>
				</transition>
				<div class="wallpaper-register"></div>
	
				<div class="container">
					<div class="row">
							<div class="col-lg-4 col-md-6 col-sm-8 mx-auto">
								<div v-if="!registerActive" class="card login" v-bind:class="{ error: emptyFields }">
										<h1>Registro</h1>
										<form @submit.prevent="submitForm">
											<input v-model="username" type="username" name="username" class="form-control" placeholder="Email" required>
											<input v-model="password" type="password" name="password " class="form-control" placeholder="Password" required>
											<input type="submit" class="btn btn-primary" @click="doLogin" value="Registrar">	 
										</form>
								</div>
	
							</div>
					</div>
	
				</div>
		</div>
	
	</div>
	</template>
	<script>
import swal from 'sweetalert'
import axios from 'axios'
	
/* eslint-disable */
export default{
		name: 'Registro',
		data(){
				return{
						username:'',
						password:'',
						email:''
				}
		},
		methods:{
			  submitForm(e){ 
					const formData = {
						username: this.username,
						password: this.password,
						email: this.username
					}
					
					axios
						.post('/api/v1.0/users/', formData)
						.then(response => {
								this.$router.push('/log-in')
								console.log(response)
								swal ("Reistro realizado correctamente!", "", "success") 
						})
			 .catch(error => {
							 console.log(error)
							 swal ("Verifique que rellenó correctamente todos los campos y que la contraseña sea segura!", "", "error") 
				})
				}
		}
}

</script>
