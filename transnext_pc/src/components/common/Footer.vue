<template>
  <!-- Footer -->
  <footer class="footer">

    <!-- Footer Top Area -->
    <div v-bind:class="{ 'footer-toparea': isActive }">
      <div class="footer-row">

        <div class="col-lg-2 col-md-4">
          <div class="footer-widget widget-links">
            <h5 class="footer-widget-title">Products</h5>
            <ul>
              <li v-bind:key="index" v-for="(item, index) in menu_product">
                <router-link :to="item.link">{{ item.title }}</router-link>
              </li>
            </ul>
          </div>
        </div>

        <div class="col-lg-2 col-md-4">
          <div class="footer-widget widget-links">
            <h5 class="footer-widget-title">Support</h5>
            <ul>
              <li v-bind:key="index" v-for="(item, index) in menu_support">
                <router-link :to="item.link">{{ item.title }}</router-link>
              </li>
            </ul>
          </div>
        </div>

        <div class="col-lg-2 col-md-4">
          <div class="footer-widget widget-links">
            <h5 class="footer-widget-title">About</h5>
            <ul>
              <li v-bind:key="index" v-for="(item, index) in menu_about">
                <router-link :to="item.link">{{ item.title }}</router-link>
              </li>
            </ul>
          </div>
        </div>

        <div class="col-lg-3 col-12">
          <div class="footer-widget widget-info">
            <h5 class="footer-widget-title">Contact Us</h5>
            <ul>
              <li>
                <Icon type="ios-phone-portrait"/>
                +86 (0)15918590138
              </li>
              <li>
                <Icon type="logo-skype"/>
                15989276058
              </li>
              <li>
                <Icon type="ios-mail-outline"/>
                info@transnext.com.hk
              </li>
            </ul>
          </div>
        </div>


        <div class="footer-widget widget-customerservice">
          <div class="info">
            <h5 class="footer-widget-title" style="color: #000000">Please leave us a message, and we will reply to you
              as soon as
              possible.</h5>
            <Form ref="formValidate" :model="formValidate" :rules="ruleValidate" :label-width="80">
              <FormItem label="Name" prop="name">
                <Input v-model="formValidate.name" placeholder="Enter your name"/>
              </FormItem>
              <FormItem label="E-mail" prop="mail">
                <Input v-model="formValidate.mail" placeholder="Enter your e-mail"/>
              </FormItem>
              <FormItem label="Message" prop="msg">
                <Input v-model="formValidate.msg" type="textarea" :autosize="{minRows: 2,maxRows: 8}"
                       placeholder="Enter your message" style="width: 200px"/>
              </FormItem>
              <FormItem>
                <Button type="primary" @click="handleSubmit('formValidate')" style="width: 100px">Submit</Button>
                <Button @click="handleReset('formValidate')" style="margin-left: 8px; width: 100px">Reset</Button>
              </FormItem>
            </Form>
          </div>
        </div>
      </div>

    </div>
    <!--// Footer Top Area -->

    <!-- Footer Bottom -->
    <div v-bind:class="{ 'footer-bottomarea': isActive }">
      <div class="footer-copyright">
        <p class="copyright">Copyright &copy; {{ year }} TransNext Technology (Ch) Ltd</p>
      </div>
    </div>
    <!--// Footer Bottom -->

  </footer>
  <!--// Footer -->
</template>

<script>
  export default {
    props: {
      isActive: {
        type: Boolean,
        default: true
      }
    },
    data() {
      return {
        formValidate: {
          name: '',
          mail: '',
          msg: ''
        },
        ruleValidate: {
          name: [
            {required: true, message: 'The name cannot be empty', trigger: 'blur'}
          ],
          mail: [
            {required: true, message: 'Mailbox cannot be empty', trigger: 'blur'},
            {type: 'email', message: 'Incorrect email format', trigger: 'blur'}
          ],
          msg: [
            {required: true, message: 'Message cannot be empty', trigger: 'blur'}
          ],
        },
        year: new Date().getFullYear(),
      };
    },
    computed: {
      menu_product: function () {
        return this.$store.state.menu_product
      },
      menu_support: function () {
        return this.$store.state.menu_support
      },
      menu_about: function () {
        return this.$store.state.menu_about
      },
    },
    methods: {
      handleSubmit(name) {
        this.$refs[name].validate((valid) => {
          if (valid) {
            this.$axios.post(
              `${this.$settings.HOST}/message/`,
              {name:this.formValidate.name, email:this.formValidate.mail, msg:this.formValidate.msg}
            ).then(() => {
              this.$Message.success('Send messages success!');
            }).catch(error => {
              this.$Message.error(error.response)
            });
            this.$refs[name].resetFields();
          } else {
            this.$Message.error('Send messages fail!');
          }
        })
      },
      handleReset(name) {
        this.$refs[name].resetFields();
      }
    }
  }
</script>

<style scoped>
  .footer-toparea {
    background: #F1F1F1;
  }

  .footer-bottomarea {
    background: #F1F1F1;
  }

  .footer-row {
    display: table;
    width: 100%;
    max-width: 1200px;
    margin: 1.5em auto 0;
  }

  .footer-row div {
    float: left;
  }
</style>
