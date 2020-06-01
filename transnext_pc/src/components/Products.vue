<template>
  <div>
    <Header v-bind:products_color="products_color" v-bind:isShow="true"/>

    <div class="products">
      <div class="main-content main-content-product no-sidebar">
        <div class="container">
          <div class="row">
            <div class="col-lg-12">
              <div class="breadcrumb-trail breadcrumbs">
                <ul class="trail-items breadcrumb">
                  <li class="trail-item trail-begin">
                    <a href="/">Home</a>
                  </li>
                  <li class="trail-item trail-end active">
                    <Icon class="icon" type="ios-arrow-forward" size="14"/>
                    <router-link :to="bread.breadcrumb.path_one">{{ bread.breadcrumb.title }}</router-link>
                  </li>
                  <li class="trail-item trail-end active">
                    <Icon class="icon" type="ios-arrow-forward" size="14"/>
                    {{ bread.category }}
                  </li>
                </ul>
              </div>
            </div>
          </div>
          <div class="row">
            <div class="content-area shop-grid-content full-width col-lg-12 col-md-12 col-sm-12 col-xs-12">
              <div class="site-main">
                <ul class="row list-products auto-clear equal-container product-grid">
                  <li v-bind:key="index" v-for="(item, index) in show_list"
                      class="product-item col-lg-3 col-md-4 col-sm-6 col-xs-6 col-ts-12 style-1">
                    <div class="product-inner equal-element"
                         v-on:mouseover="clickCategory(index)"
                         v-on:mouseout="clickCategory(-1)">
                      <div v-if="item.is_new" class="product-top">
                        <div class="flash">
                          <span>new</span>
                        </div>
                      </div>
                      <div class="product-thumb">
                        <div class="thumb-inner">
                          <router-link v-bind:to="`/details/${changeCategory(item.category)}/${item.id}.html`">
                            <img v-bind:src="item.image_url[0].image_url" alt="img">
                          </router-link>
                        </div>
                      </div>
                      <div class="product-info">
                        <h5 class="product-name" v-bind:class="{ 'product-title': categoryIndex===index }">
                          <router-link v-bind:to="`/details/${changeCategory(item.category)}/${item.id}.html`">
                            {{ item.title }}
                          </router-link>
                        </h5>
                      </div>
                    </div>
                  </li>
                </ul>

                <div class="pagination clearfix style2">
                  <div v-if="product_total > pagesize" class="nav-link">
                    <Page :total="product_total" :page-size="pagesize" @on-change="changePage"/>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <Footer v-bind:isActive="false"/>
  </div>
</template>

<script>
  import Header from "./common/Header"
  import Footer from "./common/Footer"

  export default {
    data() {
      return {
        product_list: [],
        show_list: [],
        product_total: 0,
        pagesize: 12,
        categoryIndex: -1,
        products_color: '#00a7e1',
        bread: {
          category: '',
          breadcrumb: {
            title: '',
            path_one: '',
          }
        },
      };
    },
    beforeRouteEnter(to, from, next) {
      // 路由变更后修改title
      window.document.title = 'TransNext | ' + to.params.pro;
      next()
    },
    beforeRouteUpdate(to, from, next) {
      // 路由变更后修改title
      window.document.title = 'TransNext | ' + to.params.pro;
      next()
    },
    created() {
      this.get_products();
    },
    watch: {
      // 如果路由有变化，会再次执行该方法
      '$route': 'get_products',
    },
    methods: {
      get_products: function () {
        // 请求分类数据信息
        this.$axios.get(`${this.$settings.HOST}/products/`, {
          params: {
            category: this.$route.params.pid
          }
        }).then(response => {
          this.product_list = response.data;
          this.product_total = this.product_list.length;
          this.bread = {
            category: this.product_list[0].category,
            breadcrumb: this.product_list[0].breadcrumb
          };
          if (this.product_total < this.pagesize) {
            this.show_list = this.product_list
          } else {
            this.show_list = this.product_list.slice(0, this.pagesize)
          }
        }).catch(error => {
          console.log(error.response)
        });
      },

      clickCategory: function (index) { // 这里我们传入一个当前值
        this.categoryIndex = index
      },

      changeCategory: function (value) {
        return value.replace(/\s+/g, "-")
      },

      changePage: function (index) {
        let _start = (index - 1) * this.pagesize;
        let _end = index * this.pagesize;
        this.show_list = this.product_list.slice(_start, _end)
      },
    },
    components: {
      Header,
      Footer
    },
  }
</script>

<style scoped>
  .products {
    padding-top: 60px;
    font-family: 'Roboto', sans-serif;
    font-size: 15px;
    line-height: 24px;
    color: #888;
    background-color: #f2f2f2;
    overflow-x: hidden;
  }

  .breadcrumb {
    padding: 34px 0 30px;
    background: #f2f2f2;
    margin: 0;
  }

  .breadcrumb > li {
    display: inline-block;
    list-style: none;
    font-weight: 500;
    font-size: 14px;
  }

  .breadcrumb > .active {
    color: #000000;
  }

  .breadcrumb a {
    color: #888888;
    /*color: inherit;*/
    text-decoration: none;
  }

  .breadcrumb a:hover {
    color: #00aced;
    text-decoration: none;
  }

  .icon {
    padding: 0 8px;
    content: "\f105";
    font-weight: 400;
    color: #ccc;
  }

  .container {
    margin: 0 auto;
    width: 100%;
    max-width: 1200px;
  }

  ul.list-products {
    padding: 0;
    margin-top: 0;
    margin-bottom: 0;
  }

  .product-item {
    list-style: none;
    margin-bottom: 30px;
  }

  .product-item .product-inner {
    /*border: 2px solid #F1F1F1;*/
    background-color: #fff;
    padding: 20px;
    overflow: hidden;
    position: relative;
    padding-bottom: 25px;
    height: 350px;
  }

  .product-inner {
    position: relative;
    float: left;
    width: 100%;
    text-align: center;
    text-decoration: none;
    -webkit-transition: .4s;
    transition: .4s;
    color: #323232;
  }

  .product-inner:hover {
    -webkit-box-shadow: #ccc 0 5px 30px;
    -moz-box-shadow: #ccc 0 5px 30px;
    box-shadow: #ccc 0 5px 30px;
    -webkit-transform: translateY(-5px);
    -ms-transform: translateY(-5px);
    transform: translateY(-5px);
  }

  .product-item .product-top {
    overflow: hidden;
    z-index: 1;
    position: absolute;
    left: 20px;
    top: 20px;
    right: 20px;
  }

  .product-item .flash {
    font-size: 11px;
    font-weight: 700;
    text-transform: uppercase;
    display: inline-block;
    float: left;
    line-height: 16px;
    height: 22px;
    padding: 3px 10px;
    background: linear-gradient(to right, #01c6fb, #0065eb 100%);
    color: #fff;
    position: relative;
  }

  .product-item .flash::before {
    content: '';
    position: absolute;
    right: -8px;
    top: 0;
    border-style: solid;
    border-width: 11px 8px 11px 0;
    border-color: #0065eb transparent #0065eb #0065eb;
  }

  .product-item .product-thumb {
    margin-top: 30px;
    margin-bottom: 15px;
    position: relative;
    text-align: center;
  }

  .product-item .product-info {
    text-align: center;
    position: relative;
  }

  .product-item .product-name a {
    color: #000;
  }

  .product-item .product-title a {
    color: #2d8cf0;
  }

  .shop-grid-content .pagination {
    margin-top: 10px;
  }

  .pagination.style2 {
    text-align: center;
  }

  .pagination {
    display: block;
    margin: 50px 0 0;
    padding: 0;
  }

  .pagination .page-numbers:first-child {
    margin-left: 0;
  }

  .pagination .page-numbers {
    display: inline-block;
    width: 42px;
    height: 42px;
    line-height: 38px;
    text-align: center;
    border: 2px solid #dfdfdf;
    font-size: 15px;
    color: #888;
    font-weight: 500;
    margin-left: 5px;
  }

  .pagination .page-numbers.current, .pagination .page-numbers:hover {
    color: #fff;
    border-color: transparent;
    background: #00a7e1;
  }

  .pagination .page-numbers .icon {
    font-weight: 500;
  }

  .fa {
    display: inline-block;
    font: normal normal normal 14px/1 FontAwesome;
    font-size: inherit;
    text-rendering: auto;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
  }

  @media only screen and (max-width: 767px) {
    .products {
      padding-top: 0;
      font-family: 'Roboto', sans-serif;
      font-size: 15px;
      line-height: 24px;
      color: #888;
      background-color: #f2f2f2;
      overflow-x: hidden;
    }

    .product-item .product-inner {
      background-color: #fff;
      padding: 20px;
      overflow: hidden;
      position: relative;
      padding-bottom: 25px;
      height: auto;
    }
  }
</style>
