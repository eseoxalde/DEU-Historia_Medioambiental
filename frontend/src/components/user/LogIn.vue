<template>
    <div class="container">
        <div class="login">
            <h1>Inicio de sesión</h1>
            <hr/>
            <form>
              <div class="form-outline mb-4">
                <label for="email">Correo electrónico</label>
                <input type="email" id="email" class="form-control w-75" />
              </div>
              <div class="form-outline mb-4">
                <label class="form-label" for="password">Constraseña</label>
                <input type="password" id="password" class="form-control w-75" />
              </div>
              <div class="col">
                <a href="#!">¿Olvidaste la contraseña?</a>
              </div>
              <button type="button" class="btn btn-primary active">Iniciar sesión</button>
              <hr/>
              <p>Registrate como investigador</p>
              <div class="text-center">
                <button type="button" class="btn btn-primary" href="#!">Registrarse</button>
              </div>
            </form>
          </div>
      </div>
</template>

<script>
    export default {
        name: 'LogIn',
    }
</script>

<style>

.login{
    margin: 15px;
    padding-bottom: 20px;
    width: 60%;
    margin-left: auto;
    margin-right: auto;
    background-color:#E5E8E8;
    border-radius: 10%;
}
input{
  margin-left: 10%;
}
label{
  text-align:left;
}
</style>

