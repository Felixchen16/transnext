<template>
  <!--[if lte IE 9]>
  <p class="browserupgrade">You are using an <strong>outdated</strong> browser. Please <a
    href="https://browsehappy.com/">upgrade your browser</a> to improve your experience and security.</p>
  <![endif]-->
  <div id="wrapper" class="wrapper">
    <Header/>
    <Banner/>
<!--    <Main/>-->
    <Footer/>
  </div>
</template>

<script>
  import Header from "./common/Header"
  import Banner from "./common/Banner"
  import Footer from "./common/Footer"
  import Main from "./common/Main"
  export default {
    name: "Home",
    data() {
      return {}
    },
    methods: {},
    components: {
      Header,
      Banner,
      Main,
      Footer,
    }
  }
</script>


<style scoped>

</style>
