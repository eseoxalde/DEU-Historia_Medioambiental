import { createRouter, createWebHistory } from "vue-router";
import HomeView from "@/views/Home.vue";
import SignInView from "@/views/user/SignIn.vue";
import SignUpView from "@/views/user/SignUp.vue";
import ProfileView from "@/views/user/Profile.vue"

const routes = [
    {
      path: "/",
      name: "Home",
      component: HomeView,
    },
    {
      path: "/signin",
      name: "SignIn",
      component: SignInView,
    },
    {
      path: "/signup",
      name: "SignUp",
      component: SignUpView,
    },
    {
      path: "/profile",
      name: "Profile",
      component: ProfileView,
    },
  ];
  
  const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes,
  });
  
  export default router;