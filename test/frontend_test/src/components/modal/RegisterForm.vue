<template>
  <div>
    <b-modal id="Register" title="Register" hide-footer hide-header centered>
      <div class="card-header">Register an Account</div>
      <div class="card-body">
        <form
          role="form"
          @submit.prevent="onSubmit(uid, firstname, lastname, email, pwd, pwdconfirm)"
        >
          <div class="form-group">
            <div class="form-label-group">
              <input
                type="text"
                id="inputUID"
                class="form-control"
                placeholder="ID"
                required="required"
                v-model="uid"
              >
              <label for="inputUID">ID</label>
            </div>
          </div>

          <div class="form-group">
            <div class="form-row">
              <div class="col-md-6">
                <div class="form-label-group">
                  <input
                    type="text"
                    id="firstName"
                    class="form-control"
                    placeholder="First name"
                    required="required"
                    autofocus="autofocus"
                    v-model="firstname"
                  >
                  <label for="firstName">First name</label>
                </div>
              </div>
              <div class="col-md-6">
                <div class="form-label-group">
                  <input
                    type="text"
                    id="lastName"
                    class="form-control"
                    placeholder="Last name"
                    required="required"
                    v-model="lastname"
                  >
                  <label for="lastName">Last name</label>
                </div>
              </div>
            </div>
          </div>
          <div class="form-group">
            <div class="form-label-group">
              <input
                type="email"
                id="inputEmail"
                class="form-control"
                placeholder="Email address"
                required="required"
                v-model="email"
              >
              <label for="inputEmail">Email address</label>
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
            <div class="form-label-group">
              <input
                type="password"
                id="confirmPassword"
                class="form-control"
                placeholder="Confirm password"
                required="required"
                v-model="pwdconfirm"
              >
              <label for="confirmPassword">Confirm password</label>
            </div>
          </div>
          <input type="submit" class="btn btn-primary btn-block" value="Register">
        </form>
        <div class="text-center">
          <a class="d-block small mt-3" style="color:blue; text-decoration: underline;" @click="moveLogin">Login Page</a>
          <!-- <a class="d-block small" href="forgot-password.html">Forgot Password?</a> -->
        </div>
      </div>
    </b-modal>
    <b-modal id="RegisterOk" title="RegisterOk" ok-only hide-header centered>
      <p>성공적으로 회원가입되었습니다.</p>
    </b-modal>
  </div>
</template>

<script>
export default {
  name: "register",
  data: () => ({
    uid: "",
    pwd: "",
    pwdconfirm: "",
    email: "",
    firstname: "",
    lastname: ""
  }),
  methods: {
    onSubmit(uid, firstname, lastname, email, pwd, pwdconfirm) {
      if (pwd != pwdconfirm) {
        alert("비밀번호가 같지 않습니다. 다시 확인해주세요");
        this.pwd = "";
        this.pwdconfirm = "";
      } else {
        this.$http
          .post("http://211.109.53.216:20000/member/create-member/", {
            memberid: uid,
            memberpwd: pwd,
            membername: firstname + lastname,
            memberemail: email
          })
          .then(res => {
            if (res.data.create == "fail") {
              alert("해당 아이디가 이미 존재합니다");
              this.uid = "";
              this.pwd = "";
              this.pwdconfirm = "";
            } else {
              this.uid = "";
              this.pwd = "";
              this.pwdconfirm = "";
              this.email = "";
              this.firstname = "";
              this.lastname = "";
              this.$bvModal.show("RegisterOk");
              this.$bvModal.hide("Register");
            }
          });
      }
    },
    moveLogin(){
      this.$bvModal.hide("Register");
      this.$bvModal.show("Login");
    }
  }
};
</script>