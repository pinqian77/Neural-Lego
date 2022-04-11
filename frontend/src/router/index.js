import { createRouter, createWebHistory } from "vue-router";

const routes = [
  {
    path: "/",
    name: "welcome",
    component: () =>
      import(/* webpackChunkName: "welcome" */ "../views/WelcomeView.vue"),
  },
  {
    path: "/login",
    name: "login",
    component: () =>
      import(/* webpackChunkName: "login" */ "../views/LoginView.vue"),
  },
  {
    path: "/register",
    name: "register",
    component: () =>
      import(/* webpackChunkName: "register" */ "../views/RegisterView.vue"),
  },
  {
    path: "/train",
    name: "train",
    component: () =>
      import(/* webpackChunkName: "train" */ "../views/TrainView.vue"),
  },
  {
    path: "/profile",
    name: "profile",
    component: () =>
      import(/* webpackChunkName: "config" */ "../views/ProfileView.vue"),
  },
  {
    path: "/project",
    name: "project",
    component: () =>
      import(/* webpackChunkName: "project" */ "../views/ProjectView.vue"),
  },
  {
    path: "/dataset",
    name: "dataset",
    component: () =>
      import(/* webpackChunkName: "dataset" */ "../views/DatasetView.vue"),
  },
  {
    path: "/template",
    name: "template",
    component: () =>
      import(/* webpackChunkName: "template" */ "../views/TemplateView.vue"),
  },
  {
    path: "/canvas",
    name: "canvas",
    component: () =>
      import(/* webpackChunkName: "canvas" */ "../views/CanvasView.vue"),
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
