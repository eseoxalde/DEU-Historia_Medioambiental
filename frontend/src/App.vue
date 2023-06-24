<template>
  <div id="app">
    <div id="nav">
      <nav class="b-container navbar navbar-expand-lg navbar-light bg-light">
        <b-navbar-brand class="navbar-brand" :to="{ name: 'logIn' }">HM</b-navbar-brand>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent"
          aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarSupportedContent">
          <div class="navbar-nav ml-auto">
            <router-link :to="{ name: 'registrarse' }" class="nav-item nav-link">Registrarse</router-link>
            <router-link :to="{ name: 'nosotros' }" class="nav-item nav-link">¿Quienes somos?</router-link>
            <router-link :to="{ name: 'enConstruccion' }" class="nav-link" aria-label="Notificaciones"><i
                class="fi fi-rr-bell"></i></router-link>
            <router-link :to="{ name: 'enConstruccion' }" class="nav-link" aria-label="Buscar"><i
                class="fi fi-rr-search"></i></router-link>
            <router-link :to="{ name: 'enConstruccion' }" class="nav-link" aria-label="configuracion"><i
                class="fi fi-rr-settings-sliders"></i></router-link>
            <router-link :to="{ name: 'enConstruccion' }" class="nav-link" aria-label="mi perfil"><i
                class="fi fi-rr-user"></i></router-link>
          </div>
        </div>
      </nav>
    </div>
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
@import url('https://cdn-uicons.flaticon.com/uicons-regular-rounded/css/uicons-regular-rounded.css');

#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 10px;
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
