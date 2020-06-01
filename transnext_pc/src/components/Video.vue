<template>
  <div>
    <Header v-bind:support_color="support_color" v-bind:isShow="true"/>
    <div class="support">
      <div
        style="background: url('./images/support/support_xibmA.jpg') center bottom no-repeat;height: 400px;"></div>
      <div class="container">
<Row>
        <Col class="demo-spin-col" span="8">
            <Spin fix>
                <Icon type="ios-loading" size=18 class="demo-spin-icon-load"/>
                <div>No Data</div>
            </Spin>
        </Col>
    </Row>
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
      }
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
    font-family: 'Roboto', sans-serif;
    font-size: 15px;
    line-height: 24px;
    /*color: #888;*/
    /*background-color: #f2f2f2;*/
    overflow-x: hidden;
  }

  .demo-spin-icon-load {
    animation: ani-demo-spin 1s linear infinite;
  }

  @keyframes ani-demo-spin {
    from {
      transform: rotate(0deg);
    }
    50% {
      transform: rotate(180deg);
    }
    to {
      transform: rotate(360deg);
    }
  }

  .demo-spin-col {
    height: 100px;
    margin-left: 30%;
    position: relative;
    /*border: 1px solid #eee;*/
  }
</style>
