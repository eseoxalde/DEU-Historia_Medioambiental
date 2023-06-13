<!--
    {% extends "base_generic.html" %}
    {% block_content %}

    {% if user.is_authenticated %}
    

-->

<template>
    <div class="todo">
        <div class="mapa">

        </div>
        <div class="row">
            <div class="col sm-6 text-right">
                <b-form-select v-model="selected" :options="options" size="sm" class="mt-3 "
                    aria-label="Buscador de notas"></b-form-select>
            </div>
            <div class="col sm-6 text-left" aria-label="Cargar nota">
                <p><i class="fi fi-rr-cloud-upload-alt"></i> </p>
            </div>
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
@import url('https://cdn-uicons.flaticon.com/uicons-regular-rounded/css/uicons-regular-rounded.css');

.todo {
    display: flex;
    justify-content: center;
    align-items: center;
}

.row {
    position: absolute;
    bottom: 10%;
}

p {
    font-size: 40px;
}
</style>