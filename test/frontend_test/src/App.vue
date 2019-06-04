<template>
  <div id="app">
    <!--로그인 Modal 시작부-->
    <LoginForm v-on:sessionCheck="sessionCheck"/>
    <LogoutForm v-on:sessionCheck="sessionCheck"/>
    <RegisterForm/>
    <!--로그인 Modal 끝 -->

    <nav class="navbar navbar-expand navbar-dark bg-dark static-top">
      <!--세션이 있을때-->
      <router-link to="/workspace" class="navbar-brand mr-1" v-if="session_checked">HOME</router-link>
      <!--세션이 없을때-->
      <router-link to="/" class="navbar-brand mr-1" v-else>HOME</router-link>

      <button class="btn btn-link btn-sm text-white order-1 order-sm-0" id="sidebarToggle" href="#">
        <i class="fas fa-bars"></i>
      </button>

      <!-- Navbar Search -->
      <form class="d-none d-md-inline-block form-inline ml-auto mr-0 mr-md-3 my-2 my-md-0">
        <div class="input-group">
          <input
            type="text"
            class="form-control"
            placeholder="Search for..."
            aria-label="Search"
            aria-describedby="basic-addon2"
          >
          <div class="input-group-append">
            <button class="btn btn-primary" type="button">
              <i class="fas fa-search"></i>
            </button>
          </div>
        </div>
      </form>

      <!-- Navbar -->
      <ul class="navbar-nav ml-auto ml-md-0">
        <li class="nav-item dropdown no-arrow mx-1">
          <a
            class="nav-link dropdown-toggle"
            href="#"
            id="alertsDropdown"
            role="button"
            data-toggle="dropdown"
            aria-haspopup="true"
            aria-expanded="false"
          >
            <i class="fas fa-bell fa-fw"></i>
            <span class="badge badge-danger">9+</span>
          </a>
          <div class="dropdown-menu dropdown-menu-right" aria-labelledby="alertsDropdown">
            <a class="dropdown-item" href="#">Action</a>
            <a class="dropdown-item" href="#">Another action</a>
            <div class="dropdown-divider"></div>
            <a class="dropdown-item" href="#">Something else here</a>
          </div>
        </li>
        <li class="nav-item dropdown no-arrow mx-1">
          <a
            class="nav-link dropdown-toggle"
            href="#"
            id="messagesDropdown"
            role="button"
            data-toggle="dropdown"
            aria-haspopup="true"
            aria-expanded="false"
          >
            <i class="fas fa-envelope fa-fw"></i>
            <span class="badge badge-danger">7</span>
          </a>
          <div class="dropdown-menu dropdown-menu-right" aria-labelledby="messagesDropdown">
            <a class="dropdown-item" href="#">Action</a>
            <a class="dropdown-item" href="#">Another action</a>
            <div class="dropdown-divider"></div>
            <a class="dropdown-item" href="#">Something else here</a>
          </div>
        </li>
        <li class="nav-item dropdown no-arrow">
          <a
            class="nav-link dropdown-toggle"
            href="#"
            id="userDropdown"
            role="button"
            data-toggle="dropdown"
            aria-haspopup="true"
            aria-expanded="false"
          >
            <i class="fas fa-user-circle fa-fw"></i>
          </a>
          <div class="dropdown-menu dropdown-menu-right" aria-labelledby="userDropdown">
            <a class="dropdown-item" href="#">Settings</a>
            <a class="dropdown-item" href="#">Activity Log</a>
            <div class="dropdown-divider"></div>
            <a class="dropdown-item" href="#" data-toggle="modal" data-target="#logoutModal">Logout</a>
          </div>
        </li>
      </ul>
    </nav>

    <div id="wrapper">
      <!-- Sidebar -->
      <!--세션이 있을때-->
      <ul class="sidebar navbar-nav" v-show="session_checked">
        <li class="nav-item active">
          <a class="nav-link" href="/workspace">
            <i class="fas fa-fw fa-tachometer-alt"></i>
            <span>Private Space</span>
          </a>
        </li>

        <li class="nav-item">
          <div class="nav-link" @click="$bvModal.show('test')">
            <i class="fas fa-fw"></i>   <!--fa-chart-area 버튼 이미지 -->
            <span>Project</span>
          </div>
        </li> 
        <center>
        <div class="sidebar-divider"></div>
        </center>
        <!--프로젝트 생성 및 목록 코드는 이 밑에 작성-->



        <!--로그아웃 버튼-->
        <li class="nav-item logout-footer">
          <div class="nav-link" @click="$bvModal.show('Logout')">
            <i class="fas fa-fw"></i>   <!--fa-chart-area 버튼 이미지 -->
            <span>Logout</span>
          </div>
        </li> 

        <!--
      <li class="nav-item">
        <a class="nav-link" href="tables.html">
          <i class="fas fa-fw fa-table"></i>
          <span>Tables</span></a>
        </li>-->
      </ul>


      <!--세션이 없을때-->
      <ul class="sidebar navbar-nav" v-show="!session_checked">
        <li class="nav-item">
          <div class="nav-link" @click="$bvModal.show('Login')">
            <i class="fas fa-fw"></i>   <!--fa-chart-area 버튼 이미지 -->
            <span>Sign in</span>
          </div>
        </li> 

        <li class="nav-item">
          <div class="nav-link" @click="$bvModal.show('Register')">
            <i class="fas fa-fw fa-chart-area"></i>
            <span>Sign UP</span>
          </div>
        </li> 


        <!--
      <li class="nav-item">
        <a class="nav-link" href="tables.html">
          <i class="fas fa-fw fa-table"></i>
          <span>Tables</span></a>
        </li>-->
      </ul>

      <router-view/>

      <!-- Scroll to Top Button-->
      <a class="scroll-to-top rounded" href="#page-top">
        <i class="fas fa-angle-up"></i>
      </a>

      <!-- Logout Modal-->
      <div
        class="modal fade"
        id="logoutModal"
        tabindex="-1"
        role="dialog"
        aria-labelledby="exampleModalLabel"
        aria-hidden="true"
      >
        <div class="modal-dialog" role="document">
          <div class="modal-content">
            <div class="modal-header">
              <h5 class="modal-title" id="exampleModalLabel">Ready to Leave?</h5>
              <button class="close" type="button" data-dismiss="modal" aria-label="Close">
                <span aria-hidden="true">×</span>
              </button>
            </div>
            <div
              class="modal-body"
            >Select "Logout" below if you are ready to end your current session.</div>
            <div class="modal-footer">
              <button class="btn btn-secondary" type="button" data-dismiss="modal">Cancel</button>
              <a class="btn btn-primary" href="login.html">Logout</a>
            </div>
          </div>
        </div>
      </div>
    </div>
    <footer class="sticky-footer">
      <div class="container my-auto">
        <div class="copyright text-center my-auto">
          <span>Copyright © Troller 2019</span>
        </div>
      </div>
    </footer>
  </div>
</template>

<script>
import LoginForm from "@/components/modal/LoginForm"
import LogoutForm from "@/components/modal/LogoutForm"
import RegisterForm from "@/components/modal/RegisterForm"

export default {
  name: "app",
  data: () => ({
    session_checked:false
  }),
  methods: {
    sessionCheck(value){
      this.session_checked = value
    }
  },
  mounted() {
    //console.log(session_checked())
    if (sessionStorage.getItem("accessToken") != null) {
      this.session_checked = true;
    }
  },
  computed: {
    // session_checked:{
    //   get:() => {
    //     console.log(sessionStorage.accessToken != null)
    //     return sessionStorage.accessToken != null
    //   },
    //   set:(value) => {
    //     console.log("값 변경")
    //   }
    // }
  },
  components: {
    LoginForm: LoginForm,
    LogoutForm : LogoutForm,
    RegisterForm : RegisterForm
  }
};
</script>