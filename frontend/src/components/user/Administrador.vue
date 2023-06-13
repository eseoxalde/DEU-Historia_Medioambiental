<!--
    {% extends "base_generic.html" %}
    {% block_content %}

    {% if user.is_authenticated %}
    

-->

<template>
    <b-container class="admin-contenedor">
        <b-row>
            <b-col><i class="imagen fi fi-rr-users-alt"></i>
                <p>Usuarios</p>
            </b-col>
            <b-col><i class="imagen fi fi-rr-marker"></i>
                <p>Puntos de Información</p>
            </b-col>
        </b-row>
        <b-row>
            <b-col><i class="imagen fi fi-rr-chart-histogram"></i>
                <p>Estadísticas</p>
            </b-col>
            <b-col><i class="imagen fi fi-rr-settings"></i>
                <p>Configuración</p>
            </b-col>
        </b-row>
    </b-container>
</template>
  
<script>
export default {
}
</script>
<style>
.admin-contenedor {
    background-color: beige;
    margin: auto;
    margin-top: 10%;
    padding-bottom: 20%;
    padding-top: 10%;
}

.imagen {
    font-size: 40px
}
</style>