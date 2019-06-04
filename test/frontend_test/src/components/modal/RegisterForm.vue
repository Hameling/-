<template>
  <b-modal id="test2" title="Register" hide-footer hide-header centered>
    <div class="card-header">Register an Account</div>
    <div class="card-body">
      <form role="form" @submit.prevent="onSubmit(id, pwd)">
        <div class="form-group">
          <div class="form-label-group">
            <div class="form-row">
              <div class="col-md-9">
                <input
                  type="text"
                  id="inputUID"
                  class="form-control"
                  placeholder="ID"
                  required="required"
                  v-modal="uid"
                >
                <label for="inputID">ID</label>
              </div>
              <div class="col-md-3">
                <button class="btn btn-primary btn-block" @click="checkUID(uid)">Check</button>
              </div>
            </div>
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
                  v-modal="firstname"
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
                  v-modal="lastname"
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
              v-modal="email"
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
              v-modal="pwd"
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
              v-modal="pwd"
            >
            <label for="confirmPassword">Confirm password</label>
          </div>
        </div>
        <input type="submit" class="btn btn-primary btn-block" value="Register">
      </form>
      <div class="text-center">
        <a class="d-block small mt-3" href="login.html">Login Page</a>
        <a class="d-block small" href="forgot-password.html">Forgot Password?</a>
      </div>
    </div>
  </b-modal>
</template>

<script>
export default {
    name:"register",
    data:() => ({
        uid :"",
        pwd :"",
        pwdconfirm :"",
        email :"",
        firstname :"",
        lastname :"",
        checkState : false
    }),
    methods: {
        onSubmit(){
            //아이디 중복체크 여부
            //비밀번호 동일 여부
            //post
            //필드 초기화
            //확인화면 출력
            //modal닫기
        },
        checkUID(id){
            //중복여부 확인창
        }
    },
};
</script>