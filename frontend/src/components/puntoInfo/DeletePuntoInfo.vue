<template lang="html">
    <div class="container">
        <div class="row">
            <div class="col">
                <h3>¿Seguro que desea eliminar ese punto de información?</h3>
                <p>Título: {{ this.element.title }}</p>
                <p>Descripción: {{ this.element.description }}</p>
            </div>
        </div>
        <div class="row">
        <div class="col">
            <b-button v-on:click="deletePuntoInfo" variant="danger">
                Eliminar
            </b-button>
        </div>
    </div>
    </div>

</template>

<script>
    import axios from 'axios'
    import swal from 'sweetalert'

    export default{
        data(){
            return {
                puntoInfoId: this.$route.params.puntoInfoId,
                element: {
                    title:'',
                    description:'',
                }
            }
        },
        methods: {
            getPuntoInfo() {
                const path = `${process.env.BASE_URI}/puntosInfo/${this.puntoInfoId}/`
                axios.get(path).then((response => {
                    this.element.title = response.data.title
                    this.element.description = response.data.description
                }))
            .catch((error) => {
                   console.log(error)
            })
        },
        deletePuntoInfo(){
            const path = `${process.env.BASE_URI}/puntosInfo/${this.puntoInfoId}/`
            axios.delete(path).then((response =>{
                location.href='/puntos'
            }))
            .catch((error =>{
                swal("No es posible eliminar el Punto de Información","","error")
            }))
        }
    },
    created(){
        this.getPuntoInfo()
    }
}
</script>

<style lang="css" scoped>

</style>