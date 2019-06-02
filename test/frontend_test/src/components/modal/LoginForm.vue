<template>
  <b-modal id="test" title="Login" hide-footer hide-header centered>
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
        <a class="d-block small mt-3" href="register.html">Register an Account</a>
        <a class="d-block small" href="forgot-password.html">Forgot Password?</a>
      </div>
    </div>
  </b-modal>
</template>

<script>
export default {
  name: "login",
  data: () => ({
    id: "",
    pwd: ""
  }),
  methods: {
    async onSubmit(id, pwd) {
      await this.$store
        .dispatch("LOGIN", { id, pwd })
        .then(() => {
          this.id = "";
          this.pwd = "";
          this.$bvModal.hide("test");
          this.$router.push("workspace");
        })
        .catch(msg => {
          if (msg == "Not Matched") {
            this.pwd = "";
            alert("아이디 혹은 비밀번호가 잘못되었습니다 ");
          }
        });
      if (sessionStorage.accessToken != null) {
        this.session_checked = true;
      }
    }
  }
};
</script>