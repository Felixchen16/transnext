import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router);

export default new Router({
  mode: "history",
  routes: [
    {
      path: '/',
      name: "Home",
      component: resolve => require(['../components/Home'], resolve),
      meta: {
        title: 'TransNext | Home'
      },
    },
    {
      path: '/products/:pid/:pro',
      name: "products",
      component: resolve => require(['../components/Products'], resolve),
      meta: {},
    },
    {
      path: '/categroy/:pid/:pro',
      name: "categroy",
      component: resolve => require(['../components/Categroy'], resolve),
      meta: {},
    },
    {
      path: '/details/:title/:id.html',
      name: "product_detail",
      component: resolve => require(['../components/Productdetail'], resolve),
    },
    {
      path: '/blog/',
      name: "blog",
      component: resolve => require(['../components/Blog'], resolve),
      meta: {
        title: 'TransNext | Blog'
      },
    },
    {
      path: '/blog/:id.html',
      name: "blogdetail",
      component: resolve => require(['../components/Blogdetail'], resolve),
      meta: {
        title: 'TransNext | Blog'
      },
    },
    {
      path: '/faq/',
      name: "faq",
      component: resolve => require(['../components/FAQ'], resolve),
      meta: {
        title: 'TransNext | FAQ'
      },
    },
    {
      path: '/video/',
      name: "video",
      component: resolve => require(['../components/Video'], resolve),
      meta: {
        title: 'TransNext | Video'
      },
    },
    {
      path: '/company-profile/',
      name: "profile",
      component: resolve => require(['../components/Profile'], resolve),
      meta: {
        title: 'TransNext | Company Profile'
      },
    },
    {
      path: '/company-culture/',
      name: "culture",
      component: resolve => require(['../components/Culture'], resolve),
      meta: {
        title: 'TransNext | Company Culture'
      },
    },
    {
      path: '/factory-show/',
      name: "factory",
      component: resolve => require(['../components/Factory'], resolve),
      meta: {
        title: 'TransNext | Factory Show'
      },
    },
    {
      path: '/certifications/',
      name: "certifications",
      component: resolve => require(['../components/Certifications'], resolve),
      meta: {
        title: 'TransNext | Certifications'
      },
    },
    {
      path: '/contact-us/',
      name: "contact",
      component: resolve => require(['../components/Contact'], resolve),
      meta: {
        title: 'TransNext | Contact Us'
      },
    },
  ]
})
