<template>
  <div class="container">
    <div class="card card-login mx-auto mt-5">
      <div class="card-header">Login</div>
      <div class="card-body">
        <form role="form" @submit.prevent = "onSubmit(id, pwd)">
          <div class="form-group">
            <div class="form-label-group">
              <input type="ID" id="inputID" class="form-control" placeholder="ID" required="required" autofocus="autofocus"
                v-model="id">

              <label for="inputID">ID</label>
            </div>
          </div>
          <div class="form-group">
            <div class="form-label-group">
              <input type="password" id="inputPassword" class="form-control" placeholder="Password" required="required"
                v-model="pwd">

              <label for="inputPassword">Password</label>
            </div>
          </div>
          <div class="form-group">
            <div class="checkbox">
              <label>
                <input type="checkbox" value="remember-me">
                Remember Password
              </label>
            </div>
          </div>
          <input type = "submit" class="btn btn-primary btn-block" value = 'Login'>
        </form>
        <!--<button type = "button" class="btn btn-primary btn-block" v-on:click="addEmail(id, pwd)">Login</button>-->
        
        <div class="text-center">
          <a class="d-block small mt-3" href="register.html">Register an Account</a>
          <a class="d-block small" href="forgot-password.html">Forgot Password?</a>
        </div>
      </div>
    </div>
  </div> 
</template>
<script>
 export default {
    name: 'login',
    data: () => ({
        id: '',
        pwd: '',
        msg: ''
    }),
    methods: {
      onSubmit(id, pwd){
        if(id){
        this.$http.post('http://211.109.53.216:20000/member/login/', {
          memberid:id, memberpwd:pwd
        }).then((res)=>{
          alert(res)
          this.id = ""
          this.pwd = ""
        })
       }
      }
    },
    // mounted() {
    //   this.getEmail()
    // },
  }
</script>
