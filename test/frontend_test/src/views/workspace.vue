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

        <b-form-group label="Title Info(Optional)" label-for="info-input">
          <b-form-input id="info-input" v-model="titleinfo"></b-form-input>
        </b-form-group>
      </form>
    </b-modal>
    <ContentForm/>

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
                <TitleList v-bind:titles="enrollList"></TitleList>
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
                  <!--기존 라우트 뷰 영역
                    <router-view/>-->
                  <div class="card mb-3">
                    <vue-cal
                      style="height: 500px"
                      :time-from="7*60"
                      :time-to="22*60"
                      :time-step="30"
                      :disable-views="['years', 'year', 'day']"
                      default-view="month"
                      :events="events"
                      events-on-month-view="short"
                      :on-event-click="onEventClick"
                    ></vue-cal>
                    <div class="card-footer small text-muted"></div>
                  </div>
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
                <AssignList v-bind:assigns="assignList"></AssignList>
              </div>
            </div>
          </div>
          <!--할당된 작업 끝-->
        </div>
      </div>

      <!-- /.container-fluid -->

      <!-- Sticky Footer -->
    </div>
    <!-- /.content-wrapper -->
  </div>
  <!-- /#wrapper router 끝-->
</template>

<script>
import TitleList from "@/components/TitleList";
import AssignList from "@/components/AssignList";
import ContentForm from "@/components/modal/ContentForm";
import VueCal from "vue-cal";
import "vue-cal/dist/vuecal.css";
export default {
  name: "workspace",
  data: () => ({
    titlename: "",
    titleinfo: "",
    nameState: null,
    enrollList: [],
    assignList: [],
    events: []
  }),
  methods: {
    getBaseData() {
      if (sessionStorage.getItem("accessToken") != null) {
        this.$http
          .post("http://211.109.53.216:20000/member/search-member/", {
            token: sessionStorage.accessToken
          })
          .then(res => {
            this.checkToken(res.data[0]);
            this.enrollList = res.data[0].enrollTitle;
            this.assignList = res.data[0].assignContent;
          });
      } else {
        alert("잘못된 접근입니다.");
        this.session_checked = false;
        this.$router.push("/");
      }
    },

    createProject() {
      if (sessionStorage.getItem("accessToken") != null) {
        this.$http
          .post("http://211.109.53.216:20000/title/create-title/", {
            token: sessionStorage.accessToken,
            titlename: this.titlename,
            titleinfo: this.titleinfo
          })
          .then(res => {
            this.getBaseData();
          });
      } else {
        alert("잘못된 접근입니다.");
        this.session_checked = false;
        this.$router.push("/");
      }
    },

    //Calendar 관련코드
    onEventClick(){
      //클릭하면 커져요
      //popover 적용하기
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
  },
  components: {
    TitleList: TitleList,
    AssignList: AssignList,
    ContentForm: ContentForm,
    VueCal
  }
};
</script>