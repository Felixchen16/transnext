<template>
  <div>
    <Header v-bind:support_color="support_color" v-bind:isShow="true"/>
    <div class="support">
      <div style="background: url('./images/support/FAQ.jpg') center bottom no-repeat;height: 400px;"></div>
      <div class="container" style="padding-top: 30px" v-html="about.context"></div>
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
        support_color: '#00a7e1',
        about: '',
      }
    },
    created() {
      this.get_faq()
    },
    methods: {
      get_faq: function () {
        this.$axios.get(`${this.$settings.HOST}/faq/`, {}).then(response => {
          this.about = response.data[0]
        }).catch(error => {
          console.log(error.response)
        })
      },
    },
    components: {
      Header,
      Footer
    }
  }
</script>

<style scoped>
  .support {
    padding-top: 60px;
    padding-bottom: 30px;
    font-family: 'Roboto', sans-serif;
    font-size: 15px;
    line-height: 24px;
    /*color: #888;*/
    /*background-color: #f2f2f2;*/
    overflow-x: hidden;
  }

  @media only screen and (max-width: 767px) {
    .support {
      padding-top: 0;
      padding-bottom: 30px;
      font-family: 'Roboto', sans-serif;
      font-size: 15px;
      line-height: 24px;
      overflow-x: hidden;
    }
  }
</style>
