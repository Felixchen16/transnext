import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex);

export const store = new Vuex.Store({
  state: {
    menu_list: [],
    menu_product: [],
    menu_support: [],
    menu_about: [],
  },
  mutations: {
    change_menu_product: (state, payload) => {
      state.menu_product.push(payload)
    },

    change_menu_support: (state, payload) => {
      state.menu_support.push(payload)
    },

    change_menu_about: (state, payload) => {
      state.menu_about.push(payload)
    },

    change_menu_list: (state, payload) => {
      state.menu_list = payload
    },
  }
});
