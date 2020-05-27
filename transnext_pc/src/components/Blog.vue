<template>
  <div>
    <Header v-bind:support_color="support_color" v-bind:isShow="true"/>
    <div class="support">
      <div style="background: url('../../static/images/support/4.jpg') center bottom no-repeat;height: 400px;"></div>
      <div class="containers">
        <ul class="hdlist" style="clear: both; padding-left: 0;">
          <li v-bind:key="index" v-for="(item, index) in blog_list">
            <div class="new_img wow fadeInLeft animated" data-wow-delay="0.6s"
                 v-bind:style="act === index ? col : col2"
                 v-on:mouseover="clickCategory(index)"
                 v-on:mouseout="clickCategory(-1)" >
              <router-link :to="'/blog/' + item.id + '.html'">
                <img v-bind:src="item.img" width="200" height="152" alt="TransNext">
              </router-link>
            </div>
            <div class="new_brief wow fadeInLeft animated" data-wow-delay="0.6s"
                 style="visibility: visible; animation-delay: 0.6s; animation-name: fadeInLeft;">
              <router-link :to="'/blog/' + item.id + '.html'">
                {{ item.title }}
              </router-link>
              <div>{{ item.remark }}
              </div>
              <span>{{ item.created_time | formatTime }}</span>
            </div>
          </li>
        </ul>
      </div>
    </div>
    <Footer/>
  </div>
</template>

<script>
  import Header from "./common/Header"
  import Footer from "./common/Footer"

  export default {
    name: "Support",
    data() {
      return {
        support_color: '#00a7e1',
        blog_list: [],
        act: -1,
        col: 'visibility: visible; animation-delay: 0.6s; animation-name: fadeInLeft; border-color: rgb(36, 148, 214);',
        col2: 'visibility: visible; animation-delay: 0.6s; animation-name: fadeInLeft; border-color: rgb(239, 239, 239);'
      }
    },
    created() {
      this.get_blog()
    },
    filters: {
      formatTime: function (value) {
        return value.split('T')[0]
      }
    },
    methods: {
      get_blog: function () {
        this.$axios.get(`${this.$settings.HOST}/blog/`, {}).then(response => {
          this.blog_list = response.data
        }).catch(error => {
          console.log(error.response)
        })
      },
      clickCategory: function (index) {
        this.act = index
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
    padding-bottom: 30px;
    font-family: 'Roboto', sans-serif;
    font-size: 15px;
    line-height: 24px;
    /*color: #888;*/
    /*background-color: #f2f2f2;*/
    overflow-x: hidden;
  }

  .containers {
    width: 1200px;
    padding-top: 30px;
    margin: 0 auto;
    /*text-align: center*/
  }

  .hdlist li {
    clear: both;
    height: 170px;
    margin-top: 20px;
    border-bottom: 1px dashed #CCC;
    list-style-type: none;
  }

  .hdlist li .new_img {
    float: left;
    width: 200px;
    border: 1px solid #efefef;
    text-align: center;
  }

  .hdlist li a {
    font-size: 18px;
    color: #000000;
    font-weight: bold;
    line-height: 40px;
  }

  .hdlist li a:hover {
    color: #0097E6;
  }

  .hdlist li .new_brief {
    float: right;
    width: 950px;
    height: 119px;
  }

  .hdlist li .new_brief div {
    clear: both;
    margin-top: 10px;
    margin-bottom: 10px;
    font-size: 14px;
  }
</style>
