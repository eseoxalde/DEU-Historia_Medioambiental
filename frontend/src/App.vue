<template>
  <div id="app">

    <nav class="navbar navbar-expand-lg navbar-light bg-light">
      <div class="container-fluid justify-content-between">
        <!-- izq-->
        <b-navbar-brand class="hm-nombre navbar-brand me-2 mb-1 d-flex align-items-center" :to="{ name: 'LogIn' }">
          HM</b-navbar-brand>
        <div class="container-menu">
          <ul class="navbar-nav flex-row">
            <li class="nav-item me-3 me-lg-1">
              <a class="nav-link d-sm-flex align-items-sm-center" :to="{ name: 'singUp' }">
                ¿Quienes somos?
              </a>
            </li>
            <li class="nav-item me-3 me-lg-1">
              <a class="nav-link d-sm-flex align-items-sm-center" :to="{ name: 'singUp' }">
                Contacto
              </a>
            </li>
          </ul>
        </div>

      </div>
    </nav>
    <router-view />
  </div>
</template>

<script>
import axios from 'axios';
export default {
  name: 'App',
  beforeCreate() {
    this.$store.commit('initializeStore')

    const token = this.$store.state.token

    if (token) {
      axios.defaults.headers.common['Authorization'] = "Token " + token
    } else {
      axios.defaults.headers.common['Authorization'] = ''
    }
  }
}
</script>


<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 40px;
  background-color: #808B96;
  width: 100%;
  height: 100vh;
}

.hm-nombre {
  font-weight: bold;
  font-size: 60px;
}

.container-menu {
  background-color: #E5E8E8;
  padding: 15px;
  border-radius: 10%;
}

.nav-link {
  margin: 5px;
  font-size: 16px;
}
</style>
