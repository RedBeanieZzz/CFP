<template lang="html">
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
						<h1>Ingreso</h1>
						<form @submit.prevent="submitForm">
							<input v-model="username" name="username" type="email" class="form-control" placeholder="Email" required="no puede ir en blanco">
							<input v-model="password" type="password" name="password" class="form-control" placeholder="Password" required>
							<input type="submit" class="btn btn-primary" @click="doLogin" value="Ingresar">
							<p>Quiere registrar nueva cuenta? <a href="/register" @click="registerActive = !registerActive, emptyFields = false">Registro Aquí</a>
							</p>
							<p><a href="#">Olvidó su password?</a></p>
						</form>
					</div>
				</div>
			</div>
		</div>
	</div>
</div>
</template>
<script>
	
import axios from 'axios'
import swal from 'sweetalert'

/* eslint-disable */
export default{
	name: 'Ingreso',
	data(){
			return{
				username:'',
				password:''	
			}
	},
	methods:{
			submitForm(e){ 
				const formData = {
					username: this.username,
					password: this.password,	
			}
				axios
					.post('/api/v1.0/token/login/', formData)
					.then(response => {
						console.log(response)
						const token= response.data.auth_token
						this.$store.commit('setToken', token)
						axios.defaults.headers.common['Authorization'] = "Token"+token
						localStorage.setItem('token', token)
						swal ("Logueo satisfactorio :-)!", "", "success")
						this.$router.push("listas")
				})
			.catch(error => {
					console.log(error)
					swal ("Fatal Error XXX <<Ingrese correctamente los campos>>")
			})
		}
	}
}

</script>

<style lang="scss">
p {
	line-height: 1rem;
}

.card {
	padding: 20px;
}

.form-group {
	input {
		margin-bottom: 20px;
	}
}

.login-page {
	align-items: center;
	display: flex;
	height: 100vh;

	.wallpaper-login {
		background: url(https://images2.alphacoders.com/985/985341.jpg)
			no-repeat center center;
		background-size: cover;
		height: 100%;
		position: absolute;
		width: 100%;
	}
	
	.fade-enter-active,
	.fade-leave-active {
  transition: opacity .5s;
}
	.fade-enter,
	.fade-leave-to {
		opacity: 0;
	}
	
	.wallpaper-register {
		background: url(https://images2.alphacoders.com/985/985341.jpg)
			no-repeat center center;
		background-size: cover;
		height: 100%;
		position: absolute;
		width: 100%;
		z-index: -1;
	}

	h1 {
		margin-bottom: 1.5rem;
	}
}

.error {
	animation-name: errorShake;
	animation-duration: 0.3s;
}

@keyframes errorShake {
	0% {
		transform: translateX(-25px);
	}
	25% {
		transform: translateX(25px);
	}
	50% {
		transform: translateX(-25px);
	}
	75% {
		transform: translateX(25px);
	}
	100% {
		transform: translateX(0);
	}
}

</style>
