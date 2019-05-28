<template>
  <!--routing 시작부분 -->
  <div id="content-wrapper">
    <!--Modal 선언부 -->
    <b-modal
      id="create-title"
      title="Create Title"
      centered
      ok-only
      ref="modal"
      @show="resetModal"
      @hidden="resetModal"
      @ok="handleOk"
    >
      <form ref="form" @submit.stop.prevent="handleSubmit">
        <b-form-group
          :state="nameState"
          label="Title Name"
          label-for="name-input"
          invalid-feedback="Title Name is required"
        >
          <b-form-input id="name-input" v-model="titlename" :state="nameState" required></b-form-input>
        </b-form-group>

        <b-form-group
          label="Title Info(Optional)"
          label-for="info-input"
        >
          <b-form-input id="info-input" v-model="titleinfo"></b-form-input>
        </b-form-group>
      </form>
    </b-modal>

    <div class="container-fluid">
      <div class="container show-grid" style="width: 1080px;">
        <div class="row">
          <div class="col-md-3">
            <!--프로젝트 목록 구역 시작-->
            <div class="row">
              <div class="col-md-11">
                <ol class="breadcrumb">
                  <li class="breadcrumb-item">
                    <a href="#">Project Space</a>
                  </li>
                </ol>
                <div class="column">
                  <div class="col-md-10 offset-md-1">
                    <div class="card text-white bg-primary o-hidden h-100">
                      <div class="card-body">
                        <div class="card-body-icon">
                          <i class="fas fa-fw fa-comments"></i>
                        </div>
                        <div>Project selection area</div>
                      </div>
                      <a
                        class="card-footer text-white clearfix small z-1"
                        @click="$bvModal.show('create-title')"
                      >
                        <!--프로젝트 생성 페이지 링크-->
                        <span class="float-left">Create New Project</span>
                        <span class="float-right">
                          <i class="fas fa-angle-right"></i>
                        </span>
                      </a>
                    </div>
                  </div>
                </div>
                <div>
                  <br>
                </div>
                <!--카드와 카드 사이줄-->
                <Project v-bind:titles="enrollList"></Project>
              </div>
            </div>
          </div>
          <!--프로젝트 목록 구역 끝-->

          <div class="col-md-6">
            <!--일정체크 구역-->
            <div class="row">
              <div class="col-md-12">
                <ol class="breadcrumb">
                  <li class="breadcrumb-item">
                    <a href="#">Calender Check</a>
                  </li>
                </ol>
                <div class="column">
                  <router-view/>
                </div>
              </div>
            </div>
          </div>

          <div class="col-md-3">
            <!--할당된 작업-->
            <div class="row">
              <div class="col-md-11 offset-md-1">
                <ol class="breadcrumb">
                  <li class="breadcrumb-item">
                    <a href="#">Assigned Tasks</a>
                  </li>
                </ol>
                <Assign v-bind:assigns="assignList"></Assign>
              </div>
            </div>
          </div>
          <!--할당된 작업 끝-->
        </div>
      </div>

      <!-- /.container-fluid -->

      <!-- Sticky Footer -->
      <footer class="sticky-footer">
        <div class="container my-auto">
          <div class="copyright text-center my-auto">
            <span>Copyright © Your Website 2019</span>
          </div>
        </div>
      </footer>
    </div>
    <!-- /.content-wrapper -->
  </div>
  <!-- /#wrapper router 끝-->
</template>

<script>
import Project from "@/components/Project";
import Assign from "@/components/Assign";
export default {
  name: "workspace",
  data: () => ({
    titlename: "",
    titleinfo: "",
    nameState: null,
    enrollList: [],
    assignList: []
  }),
  methods: {
    getBaseData() {
      this.$http
        .post("http://211.109.53.216:20000/member/search-member/", {
          token: sessionStorage.accessToken
        })
        .then(res => {
          this.enrollList = res.data[0].enrollTitle;
          this.assignList = res.data[0].assignContent;
        })
    },

    createProject() {
      this.$http.post("http://211.109.53.216:20000/title/create-title/", {
        token: sessionStorage.accessToken,titlename: this.titlename, titleinfo: this.titleinfo
      })
      .then(res => {
        this.getBaseData()
      })
    },

    //Modal 관련코드
    checkFormValidity() {
      const valid = this.$refs.form.checkValidity();
      this.nameState = valid ? "valid" : "invalid";
      return valid;
    },
    resetModal() {
      this.titlename = "";
      this.titleinfo = "";
      this.nameState = null;
    },
    handleOk(bvModalEvt) {
      bvModalEvt.preventDefault();
      this.handleSubmit();
    },
    handleSubmit() {
      // Exit when the form isn't valid
      if (!this.checkFormValidity()) {
        return;
      }
      // Hide the modal manually
      this.$nextTick(() => {
        this.$refs.modal.hide();
        this.createProject();
      });
    }
  },

  mounted() {
    this.$nextTick(() => {
      this.getBaseData();
    });
    console.log(sessionStorage.uid);
  },
  components: {
    Project: Project,
    Assign: Assign
  }
};
</script>