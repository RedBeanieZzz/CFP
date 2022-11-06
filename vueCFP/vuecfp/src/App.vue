<template>
  <nav>
    <NavBar/>
    <router-view/>   
  </nav>
  <footer>
    <FooterComp/>

  </footer>
</template>


<script>
/*import axios from 'axios';*/
import NavBar from '@/components/NavBar.vue'
import FooterComp from '@/components/FooterComp.vue'

export default {
  name : 'Pan-el',
  components : {
    NavBar,FooterComp
  }
}



</script>

<style lang="scss">
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 0px
}

</style>
