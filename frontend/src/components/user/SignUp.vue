<template>
    <div clas="login">
        <h1>Registrarse</h1>

        <form @submit.prevent="submitForm">
            <input type="email" name="username" v-model="username">
            <input type="password" name="password" v-model="password">
            <button type="submit">Registrarse</button>
        </form>
    </div>
</template>

<script>
import axios from 'axios';

    export default {
        name: 'SignUp',
        data(){
            return{
                username:'',
                password:''
            }
        },
        methods:{
            submitForm(e){
                const formData = {
                username:this.username,
                password: this.password
                }

                axios
                    .post('ListPuntoInfo', formData)
                    .then(response => {
                        this.$router.push('/logIn')
                        console.log(response)
                    })
                    .catch(error =>{
                        console.log(error)
                    })
            }
        }
    }
</script>
