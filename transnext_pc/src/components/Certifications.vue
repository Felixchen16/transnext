<template>
  <div>
    <Header v-bind:about_color="about_color" v-bind:isShow="true"/>
    <div class="about">
      <div style="background: url('./static/images/about/about.jpg') center bottom no-repeat;height: 400px;"></div>
      <div class="containers" v-html="profile.context"></div>
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
        about_color: '#00a7e1',
        profile: '',
      }
    },
    created() {
      this.get_faq()
    },
    methods: {
      get_faq: function () {
        this.$axios.get(`${this.$settings.HOST}/certifications/`, {}).then(response => {
          this.profile = response.data[0]
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
  .about {
    padding-top: 60px;
    padding-bottom: 30px;
    font-family: 'Roboto', sans-serif;
    font-size: 15px;
    line-height: 24px;
    /*color: #888;*/
    /*background-color: #f2f2f2;*/
    overflow-x: hidden;
  }

  .containers {
    width: 100%;
    padding-top: 30px;
    /*margin: 0 auto;*/
    text-align:center
  }
</style>
