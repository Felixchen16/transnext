<template>
  <Carousel
    v-model="value3"
    :autoplay="setting.autoplay"
    :autoplay-speed="setting.autoplaySpeed"
    :dots="setting.dots"
    :radius-dot="setting.radiusDot"
    :trigger="setting.trigger"
    :arrow="setting.arrow"
    height='auto'>
    <CarouselItem v-bind:key="key" v-for="(banner, key) in banner_list">
      <div class="demo-carousel">
        <a v-bind:href="banner.link"><img v-bind:src="banner.image_url" alt="TransNext image"></a>
      </div>
    </CarouselItem>
  </Carousel>
</template>

<script>
  export default {
    data() {
      return {
        value3: 0,
        setting: {
          autoplay: true,
          autoplaySpeed: 5000,
          dots: 'inside',
          radiusDot: true,
          trigger: 'click',
          arrow: 'never'
        },
        banner_list: [],
      }
    },
    created() {
      this.get_banner_list()
    },
    methods: {
      get_banner_list: function () {
        // 获取轮播图信息
        this.$axios.get(`${this.$settings.HOST}/banner/`, {}).then(response => {
          this.banner_list = response.data
        }).catch(error => {
          console.log(error.response)
        })
      },
    }
  }
</script>

<style scoped>
  .demo-carousel img {
    max-width: 100%;
    max-height: 100%;
    display: block;
    margin: auto;
  }

  @media only screen and (max-width: 767px) {
    .demo-carousel img {
      max-width: 100%;
      height: 230px;
      display: block;
      margin: auto;
    }
  }
</style>
