import Vue from 'vue'
import Router from 'vue-router'

import ListPuntoInfo from '@/components/puntoInfo/ListPuntoInfo'
import EditPuntoInfo from '@/components/puntoInfo/EditPuntoInfo'
import DeletePuntoInfo from '@/components/puntoInfo/DeletePuntoInfo'
import NewPuntoInfo from '@/components/puntoInfo/NewPuntoInfo'

import SignUp from '@/components/user/SignUp'
import LogIn from '@/components/user/LogIn'

import Nosotros from '@/components/sitio/Nosotros'
import PaginaEnConstruccion from '@/components/sitio/PaginaEnConstruccion'

import Investigador from '@/components/user/Investigador'
import Espectador from '@/components/user/Espectador'
import Administrador from '@/components/user/Administrador'


Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'logIn',
      component: LogIn
    },
    {
      path: '/registrarse',
      name: 'registrarse',
      component: SignUp
    },
    {
      path: '/nosotros',
      name: 'nosotros',
      component: Nosotros
    },
    {
      path: '/enConstruccion',
      name: 'enConstruccion',
      component: PaginaEnConstruccion
    },
    {
      path: '/investigador',
      name: 'investigador',
      component: Investigador
    },
    {
      path: '/espectador',
      name: 'espectador',
      component: Espectador
    },
    {
      path: '/administrador',
      name: 'administrador',
      component: Administrador
    },
    {
      path: '/puntos',
      name: 'listPuntoInfo',
      component: ListPuntoInfo
    },
    {
      path: '/puntos/:puntoInfoId/edit',
      name: 'EditPuntoInfo',
      component: EditPuntoInfo
    },
    {
      path: '/puntos/:puntoInfoId/delete',
      name: 'DeletePuntoInfo',
      component: DeletePuntoInfo
    },
    {
      path: '/puntos/new',
      name: 'NewPuntoInfo',
      component: NewPuntoInfo
    },
  ],
  mode: 'history'
})
