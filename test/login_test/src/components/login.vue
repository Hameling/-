<template>
  <div class="container">
    <div class="card card-login mx-auto mt-5">
      <div class="card-header">Login</div>
      <div class="card-body">
        <form role="form">
          <div class="form-group">
            <div class="form-label-group">
              <input type="email" id="inputEmail" class="form-control" placeholder="Email address" required="required" autofocus="autofocus"
                v-model="email">

              <label for="inputEmail">Email address</label>
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
        </form>
        <button type = "button" class="btn btn-primary btn-block" v-on:click="addEmail(email, pwd)">Login</button>
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
      data(){
        return{
          email: "",
          pwd: ""
          //emails: []
        }
      },

      methods: {
        getEmail(){
          this.$http.get('http://110.11.72.247/member/')
          .then((res)=> {
            //this.emails = res.data
            alert(res.data)
          })
        },
        addEmail(email, pwd){
          if(email){
            this.$http.post('http://110.11.72.247/member/create-member/', {
              memberid:"data", membername:"hameli", memberpwd:pwd, memberemail:email
            }).then((res)=>{
              this.email = ""
              this.pwd = ""
            })
          }
        }
      },
      mounted() {
        this.getEmail()
      },
    }
  </script>
