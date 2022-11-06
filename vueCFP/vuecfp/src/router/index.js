/*Paths ordenados tal cual los imports, primero componentes,
luego ingresos y registro y por ultimo los new/list/edit de cada model*/

import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

import NavBar from '../components/NavBar.vue'
import FooterComp from '../components/FooterComp.vue'

import Ingreso from '../views/Ingreso.vue'
import Registro from '../views/Registro.vue'

import ListadoEstudiantes from '../views/Alumnos/ListadoEstudiantes.vue'
import EditarEstudiante from '../views/Alumnos/EditarEstudiante.vue'
import NuevoEstudiante from '../views/Alumnos/NuevoEstudiante.vue'

import ListasNacionalidades from '../views/Nacionalidad/ListasNacionalidades.vue'
import EditNacionalidad from '../views/Nacionalidad/EditNacionalidad.vue'
import NuevaNacionalidad from '../views/Nacionalidad/NuevaNacionalidad.vue'

import ListasNomenclador from '../views/Nomenclador/ListasNomenclador.vue'
import EditNomenclador from '../views/Nomenclador/EditNomenclador.vue'
import NuevoNomenclador from '../views/Nomenclador/NuevoNomenclador.vue'

import ListasCurso from '../views/Cursos/ListasCurso.vue'
import EditCurso from '../views/Cursos/EditCurso.vue'
import NuevoCurso from '../views/Cursos/NuevoCurso.vue'

import ListasModulos from '../views/Modulos/ListasModulos.vue'
import EditModulos from '../views/Modulos/EditModulos.vue'
import NuevoModulos from '../views/Modulos/NuevoModulos.vue'

import ListasAlumPorMod from '../views/AlumPorMod/ListasAlumPorMod.vue'
import EditAlumPorMod from '../views/AlumPorMod/EditAlumPorMod.vue'
import NuevoAlumPorMod from '../views/AlumPorMod/NuevoAlumPorMod.vue'



const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },

/* Components */

  {
    path: '/navbar',
    name: 'Navigation bar',
    component: NavBar
  },

  {
    path: '/footer',
    name:'Foot-Er',
    component: FooterComp
  },

/* Login & Registros*/ 

  {
    path: '/log-in',
    name: 'Ingreso',
    component: Ingreso
  },

  {
    path: '/register',
    name: 'Registro',
    component: Registro
  },

/* Alumnos */

  {
    path: '/listas',
    name: 'Listado de estudiantes',
    component: ListadoEstudiantes
  },

  {
    path: '/edit/:Documento',
    name: 'Editar estudiantes',
    component: EditarEstudiante
  },

  {
    path: '/nuevo',
    name: 'Nuevo Estudiante',
    component: NuevoEstudiante
  },

/* Nacionalidades */

  {
    path: '/listNac',
    name: 'ListNacion',
    component: ListasNacionalidades
  },

  {
    path: '/editNac/:IDNacionalidad',
    name: 'EditNac',
    component:EditNacionalidad
  },

  {
    path: '/nuevoNacionalidad',
    name: 'Nueva Nacionalidad',
    component: NuevaNacionalidad
  },

/* Nomenclador */

  {
    path: '/listNomenc',
    name: 'ListNomenc',
    component: ListasNomenclador
  },

  {
    path: '/editNomenc/:CodigoDeArea',
    name: 'EditNomenc',
    component: EditNomenclador
  },

  {
    path: '/nuevoNomenclador',
    name: 'Nuevo Nomenclador',
    component: NuevoNomenclador
  },

/* Cursos */

  {
    path: '/listCurso',
    name: 'ListCurso',
    component: ListasCurso
  },

  {
    path: '/editCurso/:IDCurso',
    name: 'EditCurso',
    component: EditCurso
  },

  {
    path: '/nuevoCurso',
    name: 'Nuevo Curso',
    component: NuevoCurso
  },

/* Modulos */

  {
    path: '/listModulos',
    name: 'ListModulos',
    component: ListasModulos
  },

  {
    path: '/editModulos/:IDModulo',
    name: 'Editar Modulos',
    component: EditModulos
  },

  {
    path: '/nuevoModulo',
    name: 'Nuevo Modulo',
    component: NuevoModulos
  },

/* Alumnos por modulos*/

  {
    path: '/listAlumPorMod',
    name: 'ListAlumPorMod',
    component: ListasAlumPorMod
  },

  {
    path: '/editAlumPorMod/:IDAlumPorMod',
    name: 'EditarAlumPorMod',
    component: EditAlumPorMod
  },

  {
    path: '/nuevoAlumPorMod',
    name: 'NuevoAlumPorMod',
    component: NuevoAlumPorMod
  },

  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
