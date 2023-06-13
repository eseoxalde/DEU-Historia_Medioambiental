<!--
    {% extends "base_generic.html" %}
    {% block_content %}

    {% if user.is_authenticated %}
    

-->

<template>
    <div class="todo">
        <div class="mapa">

        </div>
        <div class="seleccion-notas">
            <b-form-select v-model="selected" :options="options" size="sm" class="mt-3 "
                aria-label="Buscador de notas"></b-form-select>
        </div>
    </div>
</template>
  
<script>
export default {
    data() {
        return {
            selected: null,
            options: [
                { value: null, text: 'Seleccione una opción' },
                { value: 'a', text: 'Notas de río' },
                { value: 'b', text: 'Notas de cultivo' },
                { value: 'b', text: 'Notas de terreno' },
            ]
        }
    }
}
</script>
<style>
.todo {
    display: flex;
    justify-content: center;
    align-items: center;

}

.seleccion-notas {
    margin: auto;
    position: absolute;
    bottom: 10%;
}
</style>