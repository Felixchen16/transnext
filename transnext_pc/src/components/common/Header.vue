<template>
  <!-- Header -->
  <header class="header header-2">
    <!-- Header Bottom Area -->
    <div class="header-bottom" v-bind:class="{ 'header-white': isActive || isShow }">
      <div class="container">
        <div class="row align-items-center">

            <a href="/">
              <img src="../../../static/images/logo/logo_new.png" style="width: 200px; height: 60px;" alt="TransNext">
            </a>

          <div class="col-lg-7 col-md-5 col-sm-5">
            <!-- Navigation -->
            <nav class="ho-navigation ho-navigation-2">
              <ul v-on:mouseover="mouseover" v-on:mouseout="mouseout">
                <li class="dropdown-holder ">
                  <router-link to="/" class="hodropdown3">Home</router-link>
                </li>
                <li class="dropdown-holder">
                  <a href="javascript:void(0);"
                     class="hodropdown3"
                     v-bind:style="{ color: products_color }">
                    Products
                    <Icon type="ios-arrow-down" size="16"/>
                  </a>
                  <ul class="hodropdown">
                    <li v-bind:key="index" v-for="(item, index) in menu_product">
                      <router-link v-bind:to="'/categroy/' + item.id + item.link">{{ item.title }}</router-link>
                      <ul v-if="item.children">
                        <li v-bind:key="index" v-for="(child, index) in item.children">
                          <router-link v-bind:to="'/products/' + child.id + child.link">{{ child.title }}</router-link>
                        </li>
                      </ul>
                    </li>
                  </ul>
                </li>

                <li class="dropdown-holder">
                  <a href="javascript:void(0);"
                     class="hodropdown3"
                     v-bind:style="{ color: support_color }">
                    Support
                    <Icon type="ios-arrow-down" size="16"/>
                  </a>
                  <ul class="hodropdown">
                    <li v-bind:key="index" v-for="(item, index) in menu_support">
                      <router-link v-bind:to="item.link">{{ item.title }}</router-link>
                    </li>
                  </ul>
                </li>
                <li class="dropdown-holder">
                  <a href="javascript:void(0);"
                     class="hodropdown3"
                     v-bind:style="{ color: about_color }">
                    About
                    <Icon type="ios-arrow-down" size="16"/>
                  </a>
                  <ul class="hodropdown">
                    <li v-bind:key="index" v-for="(item, index) in menu_about">
                      <router-link v-bind:to="item.link">{{ item.title }}</router-link>
                    </li>
                  </ul>
                </li>
              </ul>
            </nav>
            <!--// Navigation -->

          </div>
          <div class="col-lg-3 col-md-5 col-sm-5" style="margin-left: -10px;">
            <div class="header-contactinfo" v-on:mouseover="mouseover" v-on:mouseout="mouseout">
              <i class="flaticon-support"/>
              <span>Call Us Now:</span>
              <span>Skype: 15989276058</span>
            </div>
          </div>
          <div class="col-12 d-block d-lg-none">
            <div class="mobile-menu clearfix"></div>
          </div>
        </div>
      </div>
    </div>
    <!--// Header Bottom Area -->
  </header>
  <!--// Header -->
</template>

<script>
  export default {
    props: ['isShow', 'products_color', 'support_color', 'about_color'],
    data() {
      return {
        isActive: false,
        scrollTop: 0,
      };
    },
    created() {
      if (this.menu_list.length === 0) {
        this.get_products_list();
      }
    },
    mounted() {
      window.addEventListener('scroll', this.handleScroll);
      this.$router.afterEach((to, from, next) => {
        window.scrollTo(0, 0)
      });
    },
    watch: {
      menu_list: function (items) {
        /**
         * @param item.product {Object}
         * @param item.support {Object}
         * @param item.about {Object}
        */
        let product = items.filter(item => item.product);
        product.forEach(v => {
          this.$store.commit('change_menu_product', v['product'])
        });
        let support = items.filter(item => item.support);
        support.forEach(v => {
          this.$store.commit('change_menu_support', v['support'])
        });
        let about = items.filter(item => item.about);
        about.forEach(v => {
          this.$store.commit('change_menu_about', v['about'])
        })
      }
    },
    computed: {
      menu_list: function () {
        return this.$store.state.menu_list
      },
      menu_product: function () {
          return this.$store.state.menu_product
      },
      menu_support: function () {
          return this.$store.state.menu_support
      },
      menu_about: function () {
          return this.$store.state.menu_about
      },
    },
    methods: {
      mouseover: function () {
        if (this.scrollTop === 0) {
          this.isActive = true;
        }
      },
      mouseout: function () {
        if (this.scrollTop === 0) {
          this.isActive = false
        }
      },
      handleScroll: function () {
        let _this = this;
        _this.scrollTop = window.pageYOffset || document.documentElement.scrollTop || document.body.scrollTop;
        // console.log(_this.scrollTop);
        _this.isActive = !!this.scrollTop;
      },
      get_products_list: function () {
         // 获取产品菜单信息
        this.$axios.get(`${this.$settings.HOST}/nav/menu/`, {}).then(response => {
          this.$store.commit('change_menu_list', response.data)
        }).catch(error => {
          console.log(error.response)
        })
      },
    },
  }
</script>

<style scoped>
  .header {
  width: 100%;
  min-width: 1201px;
  position: fixed;
  z-index: 999;
  }

  .header-white {
    background: hsla(0, 0%, 100%, .9);
  }

  .hodropdown3:after {
    content: ' ';
    position: absolute;
    z-index: 2;
    bottom: 0;
    left: 50%;
    display: block;
    width: 165px;
    height: 1px;
    transform: translate(-50%);
  }

  .hodropdown3:hover:after {
    height: 2px;
    animation: ad_width .3s linear forwards;
    background: #00a7e1;
  }

  .hodropdown3:hover {
    color: #00a7e1;
  }

  .is-blue {
    color: #00a7e1;
  }

  @keyframes ad_width {
    from {
      width: 0
    }

    to {
      width: 80px
    }
  }

  {
    color: #454545
  }

  .header-contactinfo a, .header-contactinfo span, .header-contactinfo i, .ho-navigation-2 ul li a, .ho-navigation-3 ul li a {
    color: #FFFFFF;
  }

  .header-white .header-contactinfo a, .header-white .header-contactinfo i, .header-white .header-contactinfo span, .header-white .ho-navigation-2 ul li a, .header-white .ho-navigation-3 ul li a {
    color: #454545
  }

</style>
