import { createRouter, createWebHistory } from "vue-router";
import WebsiteLayout from "../layouts/WebsiteLayout.vue"
import AccountLayout from "../layouts/AccountLayout.vue"
import WebsiteHome from "../views/website/WebsiteHome.vue"
import WebsiteSignup from "../views/website/WebsiteSignup.vue"
import WebsiteLogin from "../views/website/WebsiteLogin.vue"
import UserAccount from "../views/profile/UserAccount.vue"
import AskToBank from "../views/profile/AskToBank.vue"

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      // parent rount for website frontend
      path: "/",
      component: WebsiteLayout,
      children: [
        // child routes fro website frontend
        {
          path: "",
          component: WebsiteHome,
        },
        {
          path:"/signup",
          component: WebsiteSignup
        },
        {
          path:"/login",
          component: WebsiteLogin,
          name: "Login"
        }
      ]
    },

    {
      // parent routes for user profile
      path: "/account",
      component: AccountLayout,
      // middleware for checking authentication status
      beforeEnter: (to, from, next) => {
        if(!localStorage.getItem("user_id")) {
          return next({
            name: 'Login'
          })
        }
        next()
      },
      children: [
        //child routes for user account
        {
          path: "",
          component: UserAccount,
        },
        {
          path: "/ask-to-bank",
          component: AskToBank,
        }
      ]
    }
  ],
});

export default router;
