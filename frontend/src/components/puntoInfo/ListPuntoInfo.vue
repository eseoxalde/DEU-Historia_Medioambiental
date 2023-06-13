<template lang="html">
    <div class="container">
        <div class="row">
            <div class="col text-left">
                <div>
                <h2>Listado de Puntos de Info</h2>
                <b-button size="sm" :to="{name:'NewPuntoInfo' }" variant="primary">
                    Crear
                </b-button>
            </div>
            <br>
                <div calss="col-md-12">
                    <b-table striped hover :items="puntoInfo" :fields="fields">

                        <template v-slot:cell(action)="data">
                            <b-button size="sm" variant="primary" :to="{ name: 'EditPuntoInfo', params: {puntoInfoId: data.item.id} }">
                                Editar
                            </b-button>
                        <b-button size="sm" variant="danger" :to="{ name: 'DeletePuntoInfo', params: {puntoInfoId: data.item.id} }">
                                Eliminar
                        </b-button>
                        </template>
                    </b-table>

                </div>

            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios';

export default{
    data (){
        return{
            fields: [
                { key: 'title', label: 'Título' },
                { key: 'description', label: 'Descripción' },
                { key: 'action', label: '' }
            ],
            puntoInfo: []
        }
    },
    methods:{
        getPuntoInfo(){

            const path = `${process.env.BASE_URI}/puntosInfo/`
            axios.get(path).then((response => {
                this.puntoInfo = response.data
            }))
            .catch((error) =>{
                console.log(error)
            })
        }
    },
    created(){
        this.getPuntoInfo()
    }
}
</script>

<style lang="css" scoped>
</style>