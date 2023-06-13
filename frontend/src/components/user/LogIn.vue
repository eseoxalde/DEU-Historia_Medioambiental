<template>
  <div class="b-container">
    <b-row>
      <b-col sm="4"></b-col>
      <b-col sm="4" class="login-title">
        <h1>Inicio de sesión</h1>
      </b-col>
      <b-col sm="4"></b-col>
    </b-row>
    <b-row>
      <b-col sm="4"></b-col>
      <b-col sm="4" align-self="center" class="login">
        <b-form @submit="onSubmit" @reset="onReset">
          <hr />
          <b-form-group id="login-email-group" label="Correo electrónico" label-for="login-email"
            description="Correo electrónico para poder iniciar sesión">
            <b-form-input id="login-email" v-model="form.email" type="email" placeholder="Ingrese su correo electrónico"
              required="required">
            </b-form-input>
          </b-form-group>
          <b-form-group id="login-password-group" label="Contraseña" label-for="login-password"
            description="Contraseña para poder iniciar sesión">
            <b-form-input id="login-password" v-model="form.email" type="password" placeholder="Ingrese su contraseña"
              required="required">
            </b-form-input>
          </b-form-group>
          <div class="col">
            <a href="#!">¿Olvidaste la contraseña?</a>
          </div>
          <b-button type="submit" variant="primary" class="btn active">Iniciar sesión</b-button>
          <hr />
          <p>Registrate como investigador</p>
          <div class="text-center">
            <b-button type="button" variant="primary" class="btn" href="#!">Registrarse</b-button>
          </div>
        </b-form>
      </b-col>
      <b-col sm="4"></b-col>
    </b-row>

  </div>
</template>

<script>
export default {
  data() {
    return {
      form: {
        email: '',
      }
    }
  },
  methods: {
    onSubmit(event) {
      console.log(data)
    },
    onReset(event) {
      this.form.email = ''
      this.form.password = ''
    }
  }
}
</script>

<style>
.login {
  background-color: honeydew;
  padding: 10px
}

.login-title {
  background-color: honeydew;
  margin-top: 5px;
}
</style>

