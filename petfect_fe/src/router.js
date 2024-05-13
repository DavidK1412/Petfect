import { createRouter, createWebHistory } from "vue-router";

import App from "@/App.vue";
import LandingPage from "@/views/LandingPage.vue";
import UserView from "@/views/UserView.vue";
import AdminView from "@/views/AdminView.vue";
import Register from "@/views/Register.vue";

const routes = [
    {
        path: "/",
        name: "home",
        component: App,
        meta: {
            requiresAuth: false
        }

    },
    {
        path: "/landing",
        name: 'LandingPage',
        component: LandingPage,
        meta: {
            requiresAuth: false
        }
    },
    {
        path: "/register",
        name: "Register",
        component: Register,
        meta: {
          requiresAuth: false
        }
    },
    {
        path: "/admin",
        name: 'AdminView',
        component: AdminView,
        meta: {
            requiresAuth: true
        }
    },
    {
        path: "/user",
        name: 'UserView',
        component: UserView,
        meta: {
            requiresAuth: true
        }
    }
]

const router = createRouter({
    history: createWebHistory(),
    routes
});

async function checkAuth() {
    const accessToken = sessionStorage.getItem('access');
    if (accessToken) {
        return true;
    }
    return false;
}

router.beforeEach(async (to, from, next) => {
    if (to.matched.some(record => record.meta.requiresAuth)) {
        const auth = await checkAuth();
        if (!auth) {
            next({
                path: '/landing',
                query: { redirect: to.fullPath }
            })
        } else {
            next();
        }
    } else {
        next();
    }
});


export default router;