<template>
  <!-- Header -->
  <header class="header header-2">
    <!-- Header Bottom Area -->
    <div class="header-bottom" v-bind:class="{ 'header-white': isActive }">
      <div class="container">
        <div class="row align-items-center">

            <a href="/"><img src="../../../static/images/logo/logo_new.png" alt="TransNext"></a>

          <div class="col-lg-7 col-md-5 col-sm-5">
            <!-- Navigation -->
            <nav class="ho-navigation ho-navigation-2">
              <ul v-on:mouseover="mouseover" v-on:mouseout="mouseout">
                <li class="dropdown-holder ">
                  <a href="index.html" class="hodropdown3">Home</a>
                </li>
                <li class="dropdown-holder">
                  <a href="shop-rightsidebar.html" class="hodropdown3">Products
                    <Icon type="ios-arrow-down" size="16"/>
                  </a>
                  <ul class="hodropdown">
                    <li><a href="shop-rightsidebar.html">Shop Grid</a>
                      <ul>
                        <li><a href="shop-rightsidebar.html">Shop Right Sidebar</a></li>
                        <li><a href="shop-leftsidebar.html">Shop Left Sidebar</a></li>
                        <li><a href="shop-3-column.html">Shop 3 Column</a></li>
                        <li><a href="shop-4-column.html">Shop 4 Column</a></li>
                        <li><a href="shop-list.html">Shop List</a></li>
                        <li><a href="shop-list-rightsidebar.html">Shop List Right Sidebar</a></li>
                        <li><a href="shop-list-leftsidebar.html">Shop List Left Sidebar</a></li>
                      </ul>
                    </li>
                    <li><a href="product-details.html">Product Details</a>
                      <ul>
                        <li><a href="product-details.html">Product Details</a></li>
                        <li><a href="product-details-reverse.html">Product Details Reverse</a></li>
                        <li><a href="product-details-variable.html">Product Details Variable</a></li>
                        <li><a href="product-details-vertical.html">Product Details Vertical</a></li>
                        <li><a href="product-details-gallery.html">Product Details Gallery</a></li>
                        <li><a href="product-details-group.html">Product Details Group</a></li>
                        <li><a href="product-details-affiliate.html">Product Details Affiliate</a></li>
                        <li><a href="product-details-slider.html">Product Details Slider</a></li>
                      </ul>
                    </li>
                    <li><a href="cart.html">Cart</a></li>
                    <li><a href="wishlist.html">Wishlist</a></li>
                    <li><a href="checkout.html">Checkout</a></li>
                    <li><a href="compare.html">Compare</a></li>
                  </ul>
                </li>

                <li class="dropdown-holder">
                  <a href="blog-rightsidebar.html" class="hodropdown3">Support
                    <Icon type="ios-arrow-down" size="16"/>
                  </a>
                  <ul class="hodropdown">
                    <li><a href="blog-rightsidebar.html">Blog Right Sidebar</a></li>
                    <li><a href="blog-leftsidebar.html">Blog Left Sidebar</a></li>
                    <li><a href="blog-details.html">Blog Details</a></li>
                    <li><a href="blog-details-rightsidebar.html">Blog Details Right Sidebar</a></li>
                    <li><a href="blog-details-leftsidebar.html">Blog Details Left Sidebar</a></li>
                  </ul>
                </li>
                <li>
                  <a href="about-us.html" class="hodropdown3">About Us
                    <Icon type="ios-arrow-down" size="16"/>
                  </a>
                </li>
              </ul>
            </nav>
            <!--// Navigation -->

          </div>
          <div class="col-lg-3 col-md-5 col-sm-5" style="margin-left: -60px;">
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
    data() {
      return {
        isActive: false,
        scrollTop: 0,
      };
    },
    mounted() {
      window.addEventListener('scroll', this.handleScroll)
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
    }
  }
</script>

<style scoped>
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
