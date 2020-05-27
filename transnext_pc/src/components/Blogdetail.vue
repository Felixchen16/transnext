<template>
  <div>
    <Header v-bind:support_color="support_color" v-bind:isShow="true"/>
    <div class="support">
      <div style="background: url('../../static/images/support/4.jpg') center bottom no-repeat;height: 400px;"></div>
      <div class="container" style="padding-top: 30px">
        <div class="new_title">{{ blog.title }}</div>
        <div class="new_share"></div>
        <div v-html="blog.context"></div>
      </div>
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
        blog: '',
      }
    },
    created() {
      this.get_faq()
    },
    methods: {
      get_faq: function () {
        this.$axios.get(`${this.$settings.HOST}/blog/`, {
          params: {
            id: this.$route.params.id
          }
        }).then(response => {
          this.blog = response.data[0]
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

  .new_title {
    height: 80px;
    line-height: 80px;
    text-align: center;
    font-size: 18px;
    font-weight: bold;
    color: #000000;
  }

  .new_share {
    line-height: 45px;
    clear: both;
    border-bottom: 1px dashed #CCC;
    color: #999999;
    padding-left: 10px;
  }
</style>
