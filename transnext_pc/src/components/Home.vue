<template>
<div>
    <Header/>
    <Banner/>
    <Main/>
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
