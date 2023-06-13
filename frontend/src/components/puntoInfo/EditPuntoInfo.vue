<template lang="html">
    <div class="container">
        <div class="row">
            <div class="col text-left">
                <h2>Editar punto de información</h2>
            </div>
        </div>

        <div class="row">
            <div class="col">
                <div class="card">
                    <div class="card-body">
                        <form @submit="onSubmit">
                            
                            <div class="form-group row">
                                <label for="title" class="col-sm-2 col-form-label">Título</label>
                                <div class="col-sm-6">
                                    <input type="text" placeholder="Título" name="title" class="form-control" v-model.trim="form.title">
                                </div>
                            </div>

                            <div class="form-group row">
                                <label for="description" class="col-sm-2 col-form-label">Descripción</label>
                                <div class="col-sm-6">
                                    <textarea name="description" class="form-control" placeholder="Descipcion" rows="3" v-model.trim="form.description"></textarea>
                                </div>
                            </div>
                            <div class="rows">
                                <div class="col text-left">
                                    <b-button type="submit" variant="primary">
                                        Editar
                                    </b-button>
                                    <b-button type="submit" class="btn-large-space" :to="{name:'ListPuntoInfo'}">
                                        Cancelar
                                    </b-button>
                                </div>
                            </div>
                        </form>

                    </div>
                </div>
            </div>
        </div>

    </div>
</template>

<script>
import axios from 'axios'
import swal from 'sweetalert'

    export default {
        data(){
            return{
                puntoInfoId: this.$route.params.puntoInfoId,
                form:{
                    title:'',
                    description:'',
                }
            }
        },
        methods:{
            onSubmit(evt){
                evt.preventDefault()
                const path = `${process.env.BASE_URI}/puntosInfo/${this.puntoInfoId}/`
                axios.put(path, this.form).then((response)=>{
                    this.form.title = response.data.title
                    this.form.description = response.data.description

                    swal("Punto actualizado exitosamente", "","success")

                })
                .catch((error)=>{
                    console.log(error)
                })
            },
            getPuntoInfo(){
                const path = `${process.env.BASE_URI}/puntosInfo/${this.puntoInfoId}/`
                axios.get(path).then((response=>{
                    this.form.title = response.data.title
                    this.form.description = response.data.description
                }))
                .catch((error)=> {
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
