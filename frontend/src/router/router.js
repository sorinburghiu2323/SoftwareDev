import Vue from 'vue'
import VueRouter from 'vue-router'
import Feed from '../views/Feed.vue'
import LoginPage from '../views/LoginPage.vue'
import RegisterPage from '../views/RegisterPage.vue'

import Communities from '../components/Communities.vue'
import Profile from '../components/Profile.vue'
import Leaderboard from '../components/Leaderboard.vue'
import axios from 'axios'

// import store from '../store.js'

Vue.use(VueRouter)

const routes = [
    {
        path: '/',
        name: 'Feed',
        component: Feed
    },
    {
        path: '/login',
        name: 'LoginPage',
        component: LoginPage
    },

    {
        path: '/register',
        name: 'RegisterPage',
        component: RegisterPage,
    },
    {
        path: '/communities',
        name: 'Communities',
        component: Communities
    },
    {
        path: '/profile',
        name: 'Profile',
        component: Profile
    },
    {
        path: '/leaderboard',
        name: 'Leaderboard',
        component: Leaderboard
    }
]

const router = new VueRouter({
    routes
})

router.beforeEach((to, from, next) => {
    if (to.name !== from.name) {
        // Direct user to login if they are not authenticated
        axios.get('api/communities?type=all')
        .catch((err)=> {
            console.log(err);
            if(to.path !== '/login' && to.path !== '/register') {
                console.log('3');
                return next({
                    path: '/login',
                });
            }
        });
    }
    next();
});
export default router