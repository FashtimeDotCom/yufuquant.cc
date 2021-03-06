import VueRouter from "vue-router";
import Ranking from "../views/Ranking";
import RobotList from "../views/RobotList";
import RobotView from "../views/RobotView";
import LoginView from "../views/LoginView";
import ConnectView from "../views/ConnectView";
import Account from "../views/Account";
import Market from "../views/Market";
import Vue from 'vue'

Vue.use(VueRouter)
const routes = [
    {path: '/', component: Market},
    {path: '/ranking', component: Ranking},
    {path: '/robot/list', component: RobotList},
    {path: '/robot/:id', component: RobotView},
    {path: '/login', component: LoginView},
    {path: '/connect', component: ConnectView},
    {path: '/account', component: Account},
    {path: '/market', component: Market},
]
const router = new VueRouter({
    routes // (缩写) 相当于 routes: routes
})

export default router