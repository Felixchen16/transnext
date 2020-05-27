<template>
  <!-- Page Conttent -->
  <main class="page-content">
    <!-- Banners Area -->
    <div class="banners-area bg-white" style="margin: 0 auto; width: 100%; max-width: 1200px; padding: 1rem 0 0;">
      <div style="display: table;width: 100%;">
        <!-- Single Banner -->
        <div class="main_top" v-bind:key="key" v-for="(banner, key) in main_banner_top">
          <a v-bind:href="banner.link" target="_blank">
            <p>{{ banner.title }}</p>
            <img v-bind:src="banner.image_url" alt="bannner image">
          </a>
        </div>
        <!--// Single Banner -->
      </div>
    </div>
    <!--// Banners Area -->

    <!-- Banners Center -->
    <div style="padding: 1rem 0 0;">
      <div class="wrap">
        <div class="listTitle">
          <div class="listName">
            <span>WHAT'S NEW AT TRANSNEXT</span>
          </div>
        </div>
        <div style="position: relative; height: 916px; display: table; width: 100%;">
          <!-- 第一列大图广告图 -->
          <div class="centerBanner" style="position: absolute; left: 0; top: 0;">
            <a v-bind:href="center_one.link" target="_blank">
              <img v-bind:src="center_one.image_url" alt="">
            </a>
          </div>
          <!--// 第一列大图广告图 -->

          <!-- 第一列小图广告图 -->
          <div class="centerBanner" style="position: absolute; left: 0; top: 600px;">
            <a v-bind:href="center_two.link" target="_blank">
              <img v-bind:src="center_two.image_url" alt="">
            </a>
          </div>
          <!--// 第一列小图广告图 -->

          <!-- 第二列小图广告图 -->
          <div class="centerBanner" style="position: absolute; left: 600px; top: 0;">
            <a v-bind:href="center_three.link" target="_blank">
              <img v-bind:src="center_three.image_url" alt="">
            </a>
          </div>
          <!--// 第二列小图广告图 -->

          <!-- 第二列大图广告图 -->
          <div class="centerBanner" style="position: absolute; left: 600px; top: 316px;">
            <a v-bind:href="center_four.link" target="_blank">
              <img v-bind:src="center_four.image_url" alt="">
            </a>
          </div>
          <!--// 第二列大图广告图 -->
        </div>
      </div>
    </div>
    <!--// Banners Center -->

    <!-- Banners Footer -->
    <div>
      <div class="wrap">
        <div class="listTitle">
          <div class="listName">
            <span>SEE OUR OTHER INNOVATIONS</span>
          </div>
        </div>
        <div>
          <div class="slider "
               style="box-sizing: border-box; display: block; height: inherit; position: relative; width: 100%;">
            <div aria-live="polite" aria-atomic="true" tabindex="-1"
                 style="position: absolute; left: -10000px; top: auto; width: 1px; height: 1px; overflow: hidden;">Slide
              1 of 3
            </div>
            <div class="slider-frame"
                 style="box-sizing: border-box; display: block; height: 100%; margin: 0; overflow: hidden; padding: 0; position: relative; touch-action: pan-y pinch-zoom; transform: translate3d(0px, 0px, 0px);">
              <ul class="slider-list"
                  style="transform: translate3d(0px, 0px, 0px); position: relative; display: block; margin: 0; padding: 0; height: 232px; width: 1200px; cursor: pointer; box-sizing: border-box; touch-action: pan-y pinch-zoom;">
                <li class="slider-slide slide-visible"
                    style="box-sizing: border-box; display: inline-block; height: auto; left: 0; list-style-type: none; margin: auto 0; position: absolute; top: 0; transform: scale(1); transition: transform 0.4s linear 0s; vertical-align: top; width: 400px;">
                  <div class="main_footer">
                    <a v-bind:href="footer_one.link" target="_blank">
                      <img v-bind:src="footer_one.image_url" alt="">
                    </a>
                  </div>
                </li>
                <li class="slider-slide slide-visible"
                    style="box-sizing: border-box; display: inline-block; height: auto; left: 400px; list-style-type: none; margin: auto 0; position: absolute; top: 0; transform: scale(1); transition: transform 0.4s linear 0s; vertical-align: top; width: 400px;">
                  <div class="main_footer">
                    <a v-bind:href="footer_two.link" target="_blank">
                      <img v-bind:src="footer_two.image_url" alt="">
                    </a>
                  </div>
                </li>
                <li class="slider-slide slide-visible"
                    style="box-sizing: border-box; display: inline-block; height: auto; left: 800px; list-style-type: none; margin: auto 0; position: absolute; top: 0; transform: scale(1); transition: transform 0.4s linear 0s; vertical-align: top; width: 400px;">
                  <div class="main_footer">
                    <a v-bind:href="footer_three.link" target="_blank">
                      <img v-bind:src="footer_three.image_url" alt="">
                    </a>
                  </div>
                </li>
              </ul>
            </div>
          </div>
        </div>
      </div>
    </div>
    <!--// Banners Footer -->

  </main>
  <!--// Page Conttent -->
</template>

<script>
  export default {
    data() {
      return {
        main_banner_list: [],
        main_banner_top: [],
        main_banner_footer: [],
        center_banner_list: [],
        footer_one: {},
        footer_two: {},
        footer_three: {},
        center_one: {},
        center_two: {},
        center_three: {},
        center_four: {},
      };
    },
    created() {
      this.get_main_banner_list();
      this.get_center_banner_list()
    },
    watch: {
      main_banner_list: function (items) {
        // 监听横幅广告数据
        items.forEach(v => {
          if (v.position === 1) {
            this.main_banner_top.push(v)
          } else {
            this.main_banner_footer.push(v)
          }
        });
        this.footer_one = this.main_banner_footer[0];
        this.footer_two = this.main_banner_footer[1];
        this.footer_three = this.main_banner_footer[2]
      },
      center_banner_list: function (items) {
        // 监听中间广告数据
        items.forEach(v => {
          if (v.position === 1) {
            this.center_one = v
          }
          if (v.position === 2) {
            this.center_two = v
          }
          if (v.position === 3) {
            this.center_three = v
          }
          if (v.position === 4) {
            this.center_four = v
          }
        })
      },
    },
    methods: {
      get_main_banner_list: function () {
        // 获取横幅广告信息
        this.$axios.get(`${this.$settings.HOST}/main/banner/`, {}).then(response => {
          this.main_banner_list = response.data
        }).catch(error => {
          console.log(error.response)
        })
      },
      get_center_banner_list: function () {
        // 获取中间广告信息
        this.$axios.get(`${this.$settings.HOST}/main/center/banner/`, {}).then(response => {
          this.center_banner_list = response.data
        }).catch(error => {
          console.log(error.response)
        })
      },
    }
  }
</script>

<style scoped>
  .main_top {
    display: inline-block;
    width: 33.333333%;
    padding: 1rem;
    -webkit-box-sizing: border-box;
    box-sizing: border-box;
  }

  .main_top a {
    -webkit-transition: .4s;
    transition: .4s;
    text-align: center;
    text-decoration: none;
    position: relative;
    float: left;
    color: #323232;
    width: 100%;
  }

  .main_top p {
    position: absolute;
    top: 50%;
    left: 8%;
    -webkit-transform: translateY(-50%);
    transform: translateY(-50%);
    margin: 0;
    font-size: 13px;
    font-weight: bold
  }

  .main_top a:hover {
    -webkit-box-shadow: #ccc 0 5px 30px;
    -moz-box-shadow: #ccc 0 5px 30px;
    box-shadow: #ccc 0 5px 30px;
    -webkit-transform: translateY(-5px);
    -ms-transform: translateY(-5px);
    transform: translateY(-5px);
  }

  .wrap {
    position: relative;
    -webkit-box-sizing: border-box;
    box-sizing: border-box;
    width: 100%;
    max-width: 1200px;
    margin: 0 auto;
  }

  .listTitle {
    text-align: center;
    padding-top: 1.5rem;
  }

  .listTitle .listName {
    position: relative;
  }

  .listTitle .listName:after {
    position: absolute;
    z-index: 1;
    top: 50%;
    left: 10%;
    right: 10%;
    content: "";
    border-top: 1px solid #cfcfcf;
  }

  .listTitle .listName span {
    position: relative;
    display: inline-block;
    font-size: 15px;
    z-index: 2;
    background: #fff;
    padding: 0 2rem;
    font-weight: bold
  }

  .centerBanner {
    float: left;
    width: 50%;
    padding: 1rem;
    -webkit-box-sizing: border-box;
    box-sizing: border-box;
  }

  .centerBanner a {
    position: relative;
    float: left;
    width: 100%;
    text-align: center;
    text-decoration: none;
    -webkit-transition: .4s;
    transition: .4s;
    color: #323232;
  }

  .centerBanner a:hover {
    -webkit-box-shadow: #ccc 0 5px 30px;
    -moz-box-shadow: #ccc 0 5px 30px;
    box-shadow: #ccc 0 5px 30px;
    -webkit-transform: translateY(-5px);
    -ms-transform: translateY(-5px);
    transform: translateY(-5px);
  }

  .centerBanner a img {
    z-index: 1;
    float: left;
    width: 100%;
  }

  .slider-slide > img {
    width: 100%;
    display: block;
  }

  .slider-slide > img:focus {
    margin: auto;
  }

  .main_footer {
    display: inline-block;
    padding: 10px;
    -webkit-box-sizing: border-box;
    box-sizing: border-box;
  }

  .main_footer a {
    -webkit-transition: .4s;
    transition: .4s;
    position: relative;
    float: left;
  }

  .main_footer a:hover {
    -webkit-box-shadow: #ccc 0 -1px 5px;
    -moz-box-shadow: #ccc 0 -1px 5px;
    box-shadow: #ccc 0 5px 12px;
    -webkit-transform: translateY(-5px);
    -ms-transform: translateY(-5px);
    transform: translateY(-5px);
  }
</style>
