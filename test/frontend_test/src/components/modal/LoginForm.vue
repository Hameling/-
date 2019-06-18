<template>
  <b-modal id="Login" title="Login" hide-footer hide-header centered>
    <div class="login-card-header">Login</div>
    <div class="card-body">
      <form role="form" @submit.prevent="onSubmit(id, pwd)">
        <div class="form-group">
          <div class="form-label-group">
            <input
              type="ID"
              id="inputID"
              class="form-control"
              placeholder="ID"
              required="required"
              autofocus="autofocus"
              v-model="id"
              v-on:keyup.enter="onSubmit"
            >
            <label for="inputID">ID</label>
          </div>
        </div>
        <div class="form-group">
          <div class="form-label-group">
            <input
              type="password"
              id="inputPassword"
              class="form-control"
              placeholder="Password"
              required="required"
              v-model="pwd"
              v-on:keyup.enter="onSubmit"
            >
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
        <input type="submit" class="btn btn-primary btn-block" value="Login">
      </form>
      <!--<button type = "button" class="btn btn-primary btn-block" v-on:click="addEmail(id, pwd)">Login</button>-->

      <div class="text-center">
        <a class="d-block small mt-3" style="color:blue; text-decoration: underline;" @click="moveRegister">Register an Account</a>
        <!-- <a class="d-block small mt-3" style="color:blue; text-decoration: underline;" @click="forgotPassword">Forgot Password?</a> -->
      </div>
    </div>
  </b-modal>
</template>

<script>
export default {
  name: "login",
  data: () => ({
    id: "",
    pwd: "",
  }),
  methods: {
    async onSubmit(id, pwd) {
      if(this.doubleSubmitCheck()) return;

      await this.$store
        .dispatch("LOGIN", { id, pwd })
        .then(() => {
          this.id = "";
          this.pwd = "";
          this.$bvModal.hide("Login");
          this.$router.push("workspace");
        })
        .catch(msg => {
          if (msg == "Not Matched") {
            this.pwd = "";
            alert("아이디 혹은 비밀번호가 잘못되었습니다 ");
          }
        });
      if (sessionStorage.getItem("accessToken") != null) {
          this.$emit('sessionCheck', true)
      }
    },
    moveRegister(){
      this.$bvModal.hide("Login");
      this.$bvModal.show("Register");
    }
  }
};
</script>