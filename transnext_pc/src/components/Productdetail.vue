<template>
  <div>
    <Header v-bind:products_color="products_color" v-bind:isShow="true"/>

    <div class="product-detail">
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
                    <router-link :to="bread.breadcrumb.path_two">{{ bread.category }}</router-link>
                  </li>
                  <li class="trail-item trail-end active">
                    <Icon class="icon" type="ios-arrow-forward" size="14"/>
                    {{ productInfo.title }}
                  </li>
                </ul>
              </div>
            </div>
          </div>

          <div class="banner">
            <div class="left">
              <div class="left-content">
                <div class="imgList" ref="elememt">
                  <div class="image-gallery-thumbnails">
                    <div class="image-gallery-thumbnails-container" v-bind:style="{ transform: getTransform2() }">
                      <a v-for="(item, index) in imglist" :key="index" v-on:mouseenter="imgEnter(index)"
                         class="image-gallery-thumbnail " v-bind:class="{ active:isImg(index)  }">
                        <div class="image-gallery-thumbnail-inner">
                          <img :src="item" alt="TransNext">
                        </div>
                      </a>
                    </div>
                  </div>
                </div>
                <div class="big-img-warp">
                  <div v-for="(item, index) in imglist" :key="index" v-on:click="clickImg" class="image-gallery-slide"
                       v-bind:style="{ transform: getTransform(index) }" v-bind:class="{ center:isImg(index)  }">
                    <img class="big-img" :src="item" alt="TransNext">
                  </div>
                  <span>
                                <button type="button" class="image-gallery-left-nav" aria-label="Previous Slide"
                                        v-on:click="leftImg"
                                        style="width: 50px;height: 70px"/>
                                <button type="button" class="image-gallery-right-nav" aria-label="Next Slide"
                                        v-on:click="rightImg"
                                        style="width: 50px;height: 70px"/>
                            </span>
                </div>
              </div>
            </div>
            <div class="right">
              <div>
                <h1 class="title">{{ productInfo.title }}</h1>
                <!--                <div class="description">{{description}}</div>-->
              </div>
              <!--              <div class="Reviews">-->
              <!--                <img class="Reviews-img" src="../../static/img/a.png" alt="">-->
              <!--                <a class="Reviews-a">-->
              <!--                  <div class="Reviews-d">-->
              <!--                                <span class="stars">-->
              <!--                                    <span>-->
              <!--                                        <i class="iconfont fa fa-star-o"></i>-->
              <!--                                        <i class="iconfont fa fa-star-o"></i>-->
              <!--                                        <i class="iconfont fa fa-star-o"></i>-->
              <!--                                        <i class="iconfont fa fa-star-o"></i>-->
              <!--                                        <i class="iconfont fa fa-star-o"></i>-->
              <!--                                    </span>-->
              <!--                                    <span class="mask" v-bind:style="{ width: getstarWidth() }">-->
              <!--                                        <i class="iconfont fa fa-star"></i>-->
              <!--                                        <i class="iconfont fa fa-star"></i>-->
              <!--                                        <i class="iconfont fa fa-star"></i>-->
              <!--                                        <i class="iconfont fa fa-star"></i>-->
              <!--                                        <i class="iconfont fa fa-star"></i>-->
              <!--                                    </span>-->
              <!--                                </span>-->
              <!--                  </div>-->
              <!--                  <span style="margin-left: 16px; ">{{Reviews}} ({{ReviewsNum}} Reviews)</span>-->
              <!--                </a>-->
              <!--              </div>-->
              <!--              <div class="Reviews" style="margin-top: 8px;">-->
              <!--                <div class="Review-title">A</div>-->
              <!--                <a class="Reviews-a">-->
              <!--                  <div class="Reviews-d">-->
              <!--                                <span class="stars">-->
              <!--                                    <span>-->
              <!--                                        <i class="iconfont2 fa fa-star"></i>-->
              <!--                                        <i class="iconfont2 fa fa-star"></i>-->
              <!--                                        <i class="iconfont2 fa fa-star"></i>-->
              <!--                                        <i class="iconfont2 fa fa-star"></i>-->
              <!--                                        <i class="iconfont2 fa fa-star"></i>-->
              <!--                                    </span>-->
              <!--                                    <span class="mask" v-bind:style="{ width: getstarWidth2() }">-->
              <!--                                        <i class="iconfont3 fa fa-star"></i>-->
              <!--                                        <i class="iconfont3 fa fa-star"></i>-->
              <!--                                        <i class="iconfont3 fa fa-star"></i>-->
              <!--                                        <i class="iconfont3 fa fa-star"></i>-->
              <!--                                        <i class="iconfont3 fa fa-star"></i>-->
              <!--                                    </span>-->
              <!--                                </span>-->
              <!--                  </div>-->
              <!--                  <span class="Review-num"-->
              <!--                        style="color: #00a7e1;margin-left: 16px;margin-right: 16px; ">({{ReviewsA}})</span>-->
              <!--                  <a class="Review-a-btn">Write a review</a>-->
              <!--                </a>-->
              <!--              </div>-->
              <div class="ul-warp" v-html="productInfo.specs">
                <!--                  {{ productInfo.specs }}-->
                <!--                  <li v-for="(item, index) in desList" :key="index">{{item}}</li>-->
              </div>
              <!--              <div class="price-warp">-->
              <!--                        <span>-->
              <!--                            <b>${{price1}}</b>-->
              <!--                            <i>.</i>-->
              <!--                            <b style="font-size: 1.33rem;vertical-align: 0;">{{price2}}</b>-->
              <!--                        </span>-->
              <!--              </div>-->
              <!--              <div class="color-warp">-->
              <!--                <div class="color-name">-->
              <!--                  <span>Color:</span>-->
              <!--                  Black-->
              <!--                </div>-->
              <!--                <div class="color-color">-->
              <!--                  <a class="color-btn">-->
              <!--                    <img title="Black" src="../../static/img/black.png">-->
              <!--                  </a>-->
              <!--                </div>-->
              <!--              </div>-->
              <!--              <div style="font-size: 14px;">-->
              <!--                <div class="quantity-warp">-->
              <!--                  <div class="quantity-name">Quantity:</div>-->
              <!--                  <div class="quantity-input-warp">-->
              <!--                    <div class="quantity-input">-->
              <!--                      <a role="button" v-bind:class="{ bAble: isBAble('minus'), bDisable: !isBAble('minus') }"-->
              <!--                         v-on:click="minusQuantity">-->
              <!--                        <i class="fa fa-minus"/>-->
              <!--                      </a>-->
              <!--                      <input autocomplete="off" type="text" v-model="Quantity">-->
              <!--                      <a role="button" v-bind:class="{ bAble: isBAble(), bDisable: !isBAble() }"-->
              <!--                         v-on:click="addQuantity">-->
              <!--                        <i class="fa fa-plus"/>-->
              <!--                      </a>-->
              <!--                    </div>-->
              <!--                  </div>-->
              <!--                </div>-->
              <!--                <div class="buy-btn-warp">-->
              <!--                  <a role="button" tabindex="0" class="button-normal alpha">ADD TO CART</a>-->
              <!--                  <a role="button" tabindex="0" class="button-normal submit">BUY NOW</a>-->
              <!--                </div>-->
              <!--                <div class="buy-des">Please allow 3-5 business days for shipping</div>-->
              <!--              </div>-->
            </div>
          </div>
        </div>

        <!--        <div class="wrap">-->

        <!--        </div>-->

        <div class="img-p-warp" v-bind:class="{ active: showBigImg  }">
          <div class="img-p-warp-mask">
            <div style="position: absolute; top: 0px; left: 0px; padding: 15px; color: white; font-weight: bold;"><span>{{showImgNum2 + 1 }}</span>
              / <span>{{imglist.length}}</span></div>
            <svg v-on:click="closeImg" class="jss1" focusable="false" viewBox="0 0 24 24" aria-hidden="true"
                 style="position: absolute; top: 0px; right: 0px; padding: 10px; color: rgb(255, 255, 255); cursor: pointer; font-size: 40px;">
              <g>
                <path
                  d="M19 6.41L17.59 5 12 10.59 6.41 5 5 6.41 10.59 12 5 17.59 6.41 19 12 13.41 17.59 19 19 17.59 13.41 12z"/>
              </g>
            </svg>
            <svg v-on:click="leftImg2" class="jss1 qhjt_left" focusable="false" viewBox="0 0 24 24" aria-hidden="true">
              <g>
                <path d="M15.41 7.41L14 6l-6 6 6 6 1.41-1.41L10.83 12z"/>
              </g>
            </svg>
            <svg v-on:click="rightImg2" class="jss1 qhjt_right" focusable="false" viewBox="0 0 24 24"
                 aria-hidden="true">
              <g>
                <path d="M10 6L8.59 7.41 13.17 12l-4.58 4.59L10 18l6-6z"/>
              </g>
            </svg>
            <img :src="imglist[showImgNum2]" alt="TransNext"
                 style="pointer-events: auto; max-width: 100%; max-height: 100%; transform: translate(0px, 0px) scale(1); transition: transform 0.5s ease-out 0s;">
          </div>
        </div>
      </div>
    </div>
    <div class="container" v-html="productInfo.context" style="padding-top: 10px;">

    </div>

    <Footer/>
  </div>
</template>

<script>
  import Header from "./common/Header"
  import Footer from "./common/Footer"

  export default {
    data() {
      return {
        showImgNum: 0,
        showImgNum2: 0,
        showBigImg: false,
        products_color: '#00a7e1',
        bread: {
          category: '',
          breadcrumb: {
            title: '',
            path_one: '',
            path_two: ''
          }
        },
        productInfo: {
          title: '',
          specs: '',
          context: '',
          image_url: [],
        },
        imglist: [],

        Reviews: 4.6,
        ReviewsNum: 178,
        ReviewsA: 0,
        Quantity: 1
      };
    },
    components: {
      Header,
      Footer
    },
    created() {
      this.get_product();
    },
    methods: {
      get_product: function () {
        // 获取产品信息
        this.$axios.get(`${this.$settings.HOST}/products/`, {
          params: {
            id: this.$route.params.id
          }
        }).then(response => {
          this.productInfo = response.data[0];
          this.productInfo.image_url.forEach(url => {
            this.imglist.push(url.image_url)
          });
          this.bread = {
            category: this.productInfo.category,
            breadcrumb: this.productInfo.breadcrumb
          };
          window.document.title = 'TransNext | ' + this.productInfo.title
        }).catch(error => {
          console.log(error.response)
        });
      },

      isImg: function (index) {
        return this.showImgNum === index
      },

      getTransform: function (index) {
        return 'translate3d(' + (index - this.showImgNum) + '00%, 0px, 0px)'
      },

      getTransform2: function () {
        var height = 2000;
        if (this.$refs.elememt) {
          height = this.$refs.elememt.offsetHeight;
        }
        var imglistHeight = this.imglist.length * 68.5;
        if (imglistHeight - height > 0) {
          return 'translate3d(0px, -' + ((imglistHeight - height) / (this.imglist.length - 1) * this.showImgNum) + 'px, 0px)'
        } else {
          return 'translate3d(0px, 0px, 0px)'
        }
      },

      imgEnter: function (index) {
        this.showImgNum = index
      },

      leftImg: function (event) {
        if (this.showImgNum > 0) {
          this.showImgNum--;
        } else {
          this.showImgNum = this.imglist.length - 1
        }
      },

      rightImg: function (event) {
        if (this.showImgNum < this.imglist.length - 1) {
          this.showImgNum++;
        } else {
          this.showImgNum = 0
        }
      },

      leftImg2: function (event) {
        if (this.showImgNum2 > 0) {
          this.showImgNum2--;
        } else {
          this.showImgNum2 = this.imglist.length - 1
        }
      },

      rightImg2: function (event) {
        if (this.showImgNum2 < this.imglist.length - 1) {
          this.showImgNum2++;
        } else {
          this.showImgNum2 = 0
        }
      },

      clickImg: function (event) {
        this.showImgNum2 = this.showImgNum;
        this.showBigImg = true
      },

      closeImg: function (event) {
        this.showBigImg = false
      },

      getstarWidth: function () {
        return this.Reviews / 5 * 100 + '%'
      },

      getstarWidth2: function () {
        return this.ReviewsA / 5 * 100 + '%'
      },

      isBAble: function (type) {
        if (type === 'minus') {
          return this.Quantity !== 0;
        } else {
          return this.Quantity !== 999;
        }
      },

      minusQuantity: function () {
        if (this.Quantity > 0) {
          this.Quantity--
        }
      },

      addQuantity: function () {
        if (this.Quantity < 999) {
          this.Quantity++
        }
      }
    }
  }
</script>

<style scoped>
  .product-detail {
    padding-top: 60px;
    padding-bottom: 30px;
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

  .no-sidebar .content-area {
    width: 100% !important;
  }

  .full-width .details-thumd {
    padding-right: 70px;
  }

  .details-thumd {
    width: 51.7241%;
    float: left;
    padding-right: 50px;
    position: relative;
  }

  .details-thumd .image-preview-container {
    position: relative;
    margin-bottom: 10px;
    overflow: hidden;
    border: 1px solid #eee;
  }

  img {
    max-width: 100%;
    height: auto;
  }

  .btn-zoom.open_qv {
    position: absolute;
    width: 40px;
    height: 40px;
    right: 10px;
    top: 10px;
    border-radius: 50%;
    overflow: hidden;
    border: 1px solid #dddddd;
    text-align: center;
    line-height: 38px;
    z-index: 32;
  }

  a {
    color: inherit;
    text-decoration: none;
  }

  .full-width .details-thumd .product-preview {
    padding: 0;
  }

  .owl-carousel.owl-loaded {
    display: block;
  }

  .owl-carousel {
    display: none;
    width: 100%;
    -webkit-tap-highlight-color: transparent;
    position: relative;
    z-index: 1;
  }

  .owl-carousel .owl-stage-outer {
    position: relative;
    overflow: hidden;
    -webkit-transform: translate3d(0px, 0px, 0px);
  }

  .details-infor {
    width: 48.2759%;
    float: right;
  }

  .wrap {
    position: relative;
    -webkit-box-sizing: border-box;
    box-sizing: border-box;
    width: 100%;
    max-width: 1200px;
    margin: 0 auto;

  }

  .banner {
    display: table;
    width: 100%;
    -webkit-box-sizing: border-box;
    box-sizing: border-box;
    /*padding: 1rem;*/
  }

  .banner .left, .banner .right {
    position: relative;
    width: 50%;
    display: table-cell;
    vertical-align: top;
    -webkit-box-sizing: border-box;
    box-sizing: border-box;
  }

  .banner .left {
    padding: 0 2% 0 .6rem;
  }

  .banner .right {
    padding: 0 0 0 2%;
  }

  .left-content {
    position: relative;
    padding-left: 64px;
  }

  .big-img-warp {
    position: relative;
    width: 100%;
    overflow: hidden;
  }

  .image-gallery-slide {
    background: #fff;
    left: 0;
    position: absolute;
    top: 0;
    width: 100%;
    transition: all 150ms ease-out 0s;

    /*transform: translate3d(100%, 0px, 0px);*/
  }

  .image-gallery-slide.center {
    position: relative;
  }

  .big-img {
    width: 100%;
    height: 520px;
    cursor: -webkit-zoom-in;
  }

  .image-gallery-left-nav, .image-gallery-right-nav {

    font-family: sans-serif;
    font-size: 100%;
    line-height: 1.15;
    margin: 0;

    overflow: visible;

    text-transform: none;

    -webkit-appearance: none;
    -moz-appearance: none;
    appearance: none;
    background-color: transparent;
    border: 0;
    cursor: pointer;
    outline: none;
    position: absolute;
    z-index: 4;

    color: #fff;
    font-size: 5em;
    padding: 35px 25px;
    top: 50%;
    -webkit-transform: translateY(-50%);
    transform: translateY(-50%);
    background-color: rgba(0, 0, 0, .2);
    background-size: 2rem;
    background-repeat: no-repeat;
    background-position: 50%;


  }

  .image-gallery-left-nav {
    left: 0;
    background-image: url("data:image/svg+xml;charset=utf-8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='6rem' height='6rem' viewBox='0 0 1000 1000'%3E%3Cpath fill='%23fff' d='M723.1 990l43.3-43.3L320.2 500 766.3 53.3 723.1 10 233.7 500l489.4 490z'/%3E%3C/svg%3E");
  }

  .image-gallery-right-nav {
    right: 0;
    background-image: url("data:image/svg+xml;charset=utf-8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='6rem' height='6rem' viewBox='0 0 1000 1000'%3E%3Cpath fill='%23fff' d='M276.9 10l-43.3 43.3L679.8 500 233.7 946.7 277 990l489.4-490L276.9 10z'/%3E%3C/svg%3E");

  }

  .imgList {
    position: absolute;
    height: 100%;
    width: 56px;
    top: 0;
    left: 0;
    overflow: hidden;
  }

  .image-gallery-thumbnails-container {
    position: relative;
    width: 100%;
  }

  .imgList img {
    width: 100%;
    height: 62px;
  }

  .image-gallery-thumbnail {
    display: inline-block;
    border: 3px solid transparent;
    -webkit-transition: border .3s ease-out;
    transition: border .3s ease-out;
    cursor: pointer;
  }

  .image-gallery-thumbnail.active {
    border: 3px solid #00a7e1;
  }

  .title {
    /*font-size: 38px;*/
    margin: 0;
    color: #3e3a39;
    line-height: 1.2;
    padding-bottom: 5px;
  }

  .description {
    color: #727171;
    font-size: 18px;
    padding-bottom: 10px;
    line-height: 1.2;
  }

  .Reviews, .Review {
    position: relative;
    padding: 0 0 0 30px;
  }

  .Reviews-img {
    width: 20px;
    color: #00a7e1;
    font-size: 18px;
    position: absolute;
    top: 50%;
    left: 0;
    -webkit-transform: translateY(-50%);
    transform: translateY(-50%);
  }

  .Reviews-a {
    display: inline-block;
    color: #333;
    font-size: 1.2rem;
    line-height: 1.5rem;
    cursor: pointer;
  }

  .Reviews-d {
    display: inline-block;
  }

  .iconfont, .icons {
    font-style: normal;
  }

  .iconfont, .iconfont2, .iconfont3 {
    display: inline-block;
    margin: 0;
    color: #fec93b;
    font-size: 14px;
    overflow: hidden;
    vertical-align: top;
  }

  .iconfont2 {
    color: #a4a4a4
  }

  .iconfont3 {
    color: #00a7e1
  }

  .Reviews i, .Review i {
    margin: 0 .7px;
    font-size: 1.8rem;
  }

  .stars {
    position: relative;
    display: inline-block;
    vertical-align: middle;
    text-align: left;
    white-space: nowrap;
    margin-left: 0 !important;
  }

  .mask {
    display: inline-block;
    color: #333;
    font-size: 1.2rem;
    line-height: 1.5rem;
    cursor: pointer;
    position: relative;
    display: inline-block;
    vertical-align: middle;
    text-align: left;
    white-space: nowrap;
    margin-left: 0 !important;
    position: absolute;
    top: 0;
    left: 0;
    bottom: 0;
    overflow: hidden;
  }

  .Review-title {
    width: 20px;
    color: #00a7e1;
    font-size: 24px;
    font-weight: bold;
    text-align: center;
    position: absolute;
    top: 50%;
    left: 0;
    -webkit-transform: translateY(-50%);
    transform: translateY(-50%);
  }

  .Review-num {
    white-space: nowrap !important;
    color: #00A7E1 !important;
    font-size: 14px !important;
    font-family: Whitney, Helvetica, Arial, sans-serif !important;
    text-transform: none !important;
    font-weight: normal !important;
    font-style: normal !important;
    text-decoration: none !important;
  }

  .Review-a-btn {
    font-weight: bold !important;
    color: #00A7E1 !important;
    font-size: 14px !important;
    font-family: Whitney, Helvetica, Arial, sans-serif !important;
    text-transform: none !important;
    font-style: normal !important;
    text-decoration: none !important;


  }

  .ul-warp {
    position: relative;
    margin: 30px 0 0;
    font-size: 14px;
    line-height: 2;
  }

  .ul-warp ul {
    margin: 0;
    padding: 0 0 0 15px;
  }

  .ul-warp li {
    margin-bottom: 5px;
    color: #595757;
  }

  .price-warp {
    line-height: 1.5;
    padding: 2rem 0 0;
  }

  .price-warp span {
    font-size: 0;
  }

  .price-warp b {
    font-weight: 400;
    font-size: 26px;
  }

  .price-warp i {
    font-style: normal;
    vertical-align: 0;
    font-size: 26px;
  }

  .color-warp {

  }

  .color-name, .color-color {
    display: inline-block;
    vertical-align: middle;
  }

  .color-name {
    font-size: 14px;
  }

  .color-btn {
    position: relative;
    display: inline-block;
    width: 2rem;
    height: 2rem;
    overflow: hidden;
    margin: 5px;
    padding: 2px;
    -webkit-box-sizing: border-box;
    box-sizing: border-box;
    border-radius: 50%;
    border: 2px solid #e5e5e5;
    vertical-align: middle;
    border-color: #00a7e1;
  }

  .color-btn img {
    cursor: pointer;
    float: left;
    width: 100%;
    height: 100%;
    border-radius: 50%;
  }

  .quantity-warp {
    padding-bottom: 1rem;
  }

  .quantity-name {
    display: inline-block;
    font-size: 14px;
    vertical-align: middle;
  }

  .quantity-input-warp {
    display: inline-block;
    vertical-align: middle;
    margin: 5px;

  }

  .quantity-input {
    display: table;
    border: 1px solid #f4f4f4;
    border-radius: 14px;
    background: #fff;
  }

  .quantity-input a {
    width: 28px;
    line-height: 28px;
    text-align: center;
    display: table-cell;
    cursor: pointer;
    color: #6b6b6b;
    vertical-align: middle;
  }

  .quantity-input a.bAble:hover {
    background: -webkit-gradient(linear, left top, right top, from(#00a7e1), to(#00a7e1));
    background: linear-gradient(90deg, #00a7e1, #00a7e1);
    color: #fff;
  }

  .quantity-input a.bDisable {
    color: #cfcfcf;
    cursor: not-allowed;
  }

  .quantity-input a:first-of-type {
    border-radius: 14px 0 0 14px;
  }

  .quantity-input a:nth-of-type(2) {
    border-radius: 0 14px 14px 0;
  }


  .quantity-input input {
    display: table-cell;
    vertical-align: middle;
    border: none;
    padding: 0;
    font-size: 16px;
    width: 45px;
    height: 28px;
    line-height: normal;
    text-align: center;
    -webkit-appearance: none;
    -moz-appearance: none;
    appearance: none;
  }

  .quantity-input input:focus {
    outline: none !important;
  }

  .buy-des {
    color: #00a7e1;
    margin: 0 1rem 1.5rem;
    max-width: 32rem;
  }

  .button-normal {
    position: relative;
    -webkit-box-sizing: border-box;
    box-sizing: border-box;
    vertical-align: middle;
    -webkit-transition: .2s;
    transition: .2s;

    display: inline-block;
    text-align: center;
    border: none;
    height: 36px;
    line-height: 36px;
    border-radius: 18px;
    text-decoration: none;
    font-size: 16px;
    color: #00a7e1;
    cursor: pointer;
    -webkit-transition: .2s;
    transition: .2s;
    white-space: nowrap;

    padding: 0 15px;

    outline: none !important;
  }

  .button-full.alpha, .button-normal.alpha {
    border: 1px solid #00a7e1;
    color: #00a7e1;
    background: rgba(0, 167, 225, .05);
  }

  .button-full.submit, .button-normal.submit {
    background: -webkit-gradient(linear, left top, right top, from(#00a7e1), to(#00a7e1));
    background: linear-gradient(90deg, #00a7e1, #00a7e1);
    background-image: -webkit-gradient(linear, left top, right top, from(#00a7e1), to(#00a7e1));
    background-image: linear-gradient(90deg, #00a7e1, #00a7e1);
    color: #fff;
    margin-right: 0;
  }

  .buy-btn-warp a {
    min-width: 163px;
    margin: 1rem 10px 1rem 0;
  }

  .button-full.alpha:hover, .button-normal.alpha:hover {
    background: rgba(0, 167, 225, .02);
  }

  .button-full.submit:hover, .button-normal.submit:hover {
    background: #0090c2;
    background-image: -webkit-gradient(linear, left top, right top, from(#10b5ec), to(#0eb5ec));
    background-image: linear-gradient(90deg, #10b5ec, #0eb5ec);
    color: #fff;
  }

  /*图片放大*/
  .img-p-warp {
    position: fixed;
    z-index: 10000001;
    top: 0;
    right: 0;
    bottom: 0;
    left: 0;
    display: none;
  }

  .img-p-warp.active {
    display: block;
  }

  .img-p-warp-mask {
    top: 0;
    left: 0;
    overflow: hidden;
    position: absolute;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-direction: row;
    height: 100%;
    width: 100%;
    background-color: rgba(0, 0, 0, .85) !important;
  }

  .jss1 {
    fill: currentColor;
    width: 1em;
    height: 1em;
    display: inline-block;
    font-size: 24px;
    transition: fill 200ms cubic-bezier(0.4, 0, 0.2, 1) 0ms;
    user-select: none;
    flex-shrink: 0;
  }

  .qhjt_left {
    position: absolute;
    left: 0;
    z-index: 1;
    color: rgb(255, 255, 255);
    cursor: pointer;
    font-size: 50px;
  }

  .qhjt_right {
    position: absolute;
    right: 0;
    z-index: 1;
    color: rgb(255, 255, 255);
    cursor: pointer;
    font-size: 50px;
  }

  @media only screen and (max-width: 767px) {
    .product-detail {
      padding-top: 0;
      padding-bottom: 30px;
      font-family: 'Roboto', sans-serif;
      font-size: 15px;
      line-height: 24px;
      color: #888;
      background-color: #f2f2f2;
      overflow-x: hidden;
    }

    .banner .left, .banner .right {
      position: relative;
      width: 100%;
      display: inline;
      vertical-align: top;
      -webkit-box-sizing: border-box;
      box-sizing: border-box;
    }

    .big-img[data-v-78718c00] {
      width: 100%;
      height: auto;
      cursor: -webkit-zoom-in;
    }

    .qhjt_left {
      position: absolute;
      left: 0;
      z-index: 1;
      color: #01c6fb;
      cursor: pointer;
      font-size: 50px;
    }

    .qhjt_right {
      position: absolute;
      right: 0;
      z-index: 1;
      color: #01c6fb;
      cursor: pointer;
      font-size: 50px;
    }
  }
</style>
