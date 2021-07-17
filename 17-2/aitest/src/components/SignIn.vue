<template>
    <div class="login-form">
        <h1>登录</h1>
        <v-text-field label="用户名" v-model="userName" outlined clearable></v-text-field>
        <v-text-field label="密码" v-model="password" outlined clearable type="password"></v-text-field>
        <v-btn elevation="4" @click="signUp()">注册</v-btn>
        <v-btn color="primary" elevation="4" @click="login()">登录</v-btn>

    </div>
</template>

<script>
export default {
  data () {
    return {
      userName:'',
      password:''
    }
  },
  methods: {
    signUp () {
      console.log('123123')
      this.$router.push({ name: 'SignUp' })
    },
    login(){
      let post_data = {
        userName : this.userName,
        password : this.password
      }
      this.$api.user.signIn(post_data).then(res => {
        console.log(res)
      })
    }
  }
}
</script>

<style scoped>
.login-form{
    width: 500px;
    margin: 0 auto;
    text-align: center;
}
</style>
