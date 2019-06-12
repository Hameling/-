<template>
  <b-modal
    id="TitleSetting"
    title="Title Setting"
    centered
    @show="getElement()"
    @hidden="resetState"
    ok-only
  >
    <b-tabs>
      <!--타이틀 정보 표시-->
      <b-tab title="Infomation">
        <section class="box">
          <div v-if="nameState" class="form-label-group">
            <input
              type="text"
              v-model="titlename"
              id="TitleName"
              class="form-control"
              placeholder="Title"
              required="required"
              autofocus="autofocus"
              @keyup.enter="updateName"
            >
            <label for="TitleName">Content Title</label>
          </div>
          <div v-else class="form-label-group">
            <label for="TitleName" @click="setNameState" class="form-control">
              <strong>{{titlename}}</strong>
            </label>

            <br>
            <i class="far fa-edit close-right"></i>
            <br>
          </div>
        </section>

        <section class="box">
          <div v-if="subjectState" class="form-label-group">
            <input
              type="text"
              v-model="titleinfo"
              id="TitleInfo"
              class="form-control"
              placeholder="Subject"
              required="required"
              @keyup.enter="updateInfo"
            >
            <label for="TitleInfo">Title Description</label>
          </div>
          <div v-else class="form-label-group">
            <label for="TitleInfo" @click="setSubjectState" class="form-control">{{titleinfo}}</label>
            <br>
            <i class="far fa-edit close-right"></i>
            <br>
          </div>
        </section>
      </b-tab>
      <!-- Enroll -->
      <b-tab title="Enroll">
        <!--Enroll된 멤버 확인 및 삭제 : 기존 리스트 사용-->
        <div class="box" style="overflow:auto">
          <div id="myDIV" class="header">
            <a>Enrolled Member</a>
          </div>

          <ul v-for="(enrolledMember,i) in enrolledMembers" :key="i">
            <li>
              {{enrolledMember.memberid}}
              <!--나인 경우에만 탈출이 가능하도록-->
              <span
                v-if="checkid(enrolledMember.memberid)"
                v-on:click="exitEnroll()"
                class="close"
                aria-hidden="true"
              >&times;</span>
            </li>
          </ul>
        </div>
        <div class="box">
          <!--Enroll 시킬 대상 추가 : 셀렉터 활용-->
          <multiselect
            v-model="selected"
            :options="memberList"
            :multiple="true"
            :preselect-first="true"
            label="memberid"
            track-by="memberid"
            placeholder="Please Enter Memberid"
          >
            <template slot="option" slot-scope="props">
              <span>{{ props.option.memberid }}({{ props.option.email }})</span>
            </template>
          </multiselect>
          <b-button class="mt-3 bg-primary" block @click="createEnroll">Add</b-button>
        </div>
      </b-tab>

      <!--삭제탭-->
      <b-tab title="Delete">
        <h4>Title을 삭제하시겠습니까?</h4>
        <br>
        <h5>Title 내의 Section 및 Content의 내용이 전부 삭제됩니다.</h5>
        <b-button class="mt-3 bg-danger" block @click="$bvModal.show('TiDelCheck')">삭제하기</b-button>
      </b-tab>

      <b-modal id="TiDelCheck" title="TitleDeleteCheck" hide-footer hide-header centered>
        <div class="d-block text-center">
          <h4>정말 {{titlename}}을 삭제 하시겠습니까?</h4>
          <br>
        </div>
        <b-button class="mt-3 bg-danger" block @click="delTitle">예</b-button>
        <b-button class="mt-3 bg-primary" block @click="$bvModal.hide('TiDelCheck')">아니오</b-button>
      </b-modal>
    </b-tabs>
  </b-modal>
</template>

<script>
import Multiselect from "vue-multiselect";
import "vue-multiselect/dist/vue-multiselect.min.css";
export default {
  name: "titlesetting",
  data: () => ({
    nameState: null,
    subjectState: null,

    titlename: "",
    titleinfo: "",

    enrolledMembers: [],

    //multiselect를 위한 변수
    selected: [],
    memberList: []
  }),
  props: ["select_item", "enrollMember"],

  methods: {
    getElement() {
      this.selected = [];
      this.getTitle();
      this.getEnrollMember();
      this.getAllMember();
    },

    getEnrollMember() {
      if (sessionStorage.getItem("accessToken") != null) {
        this.$http
          .post("http://211.109.53.216:20000/enroll/search-enrolltitle/", {
            titleid: sessionStorage.titleid,
            token: sessionStorage.accessToken
          })
          .then(res => {
            if (this.checkToken(res.data[0])) {
              this.enrolledMembers = res.data;
            }
          });
      } else {
        alert("잘못된 접근입니다.");
        this.session_checked = false;
        this.$router.push("/");
      }
    },

    getAllMember() {
      if (sessionStorage.getItem("accessToken") != null) {
        this.$http
          .post("http://211.109.53.216:20000/member/search-allmember/", {
            titleid: sessionStorage.titleid,
            token: sessionStorage.accessToken
          })
          .then(res => {
            if (this.checkToken(res.data)) {
              this.memberList = res.data;
            }
          });
      } else {
        alert("잘못된 접근입니다.");
        this.session_checked = false;
        this.$router.push("/");
      }
    },

    getTitle() {
      if (sessionStorage.getItem("accessToken") != null) {
        this.$http
          .post("http://211.109.53.216:20000/title/search-title/", {
            titleid: sessionStorage.titleid,
            token: sessionStorage.accessToken
          })
          .then(res => {
            if (this.checkToken(res.data[0])) {
              this.titlename = res.data[0].titlename;
              this.titleinfo = res.data[0].titleinfo;
            }
          });
      } else {
        alert("잘못된 접근입니다.");
        this.session_checked = false;
        this.$router.push("/");
      }
    },

    //TitleUpdate - 탭1
    setNameState() {
      this.nameState = !this.nameState;
    },
    setSubjectState() {
      this.subjectState = !this.subjectState;
    },

    async updateName() {
      await this.updateTitle();
      await this.setNameState();
      await this.$emit("updateTitle", this.titlename)
    },

    updateInfo() {
      this.updateTitle();
      this.setSubjectState();
    },
    updateTitle() {
      if (sessionStorage.getItem("accessToken") != null) {
        this.$http
          .post("http://211.109.53.216:20000/title/update-title/", {
            titleid: sessionStorage.titleid,
            token: sessionStorage.accessToken,
            titlename: this.titlename,
            titleinfo: this.titleinfo
          })
          .then(res => {
            if (this.checkToken(res.data)) {
              this.getTitle();
            }
          });
      } else {
        alert("잘못된 접근입니다.");
        this.session_checked = false;
        this.$router.push("/");
      }
    },

    resetState() {
      this.nameState = false;
      this.subjectState = false;
    },

    //탭2
    async createEnroll() {
      if (this.selected.length > 0) {
        for (var i in this.selected) {
          if (sessionStorage.getItem("accessToken") != null) {
            await this.$http
              .post("http://211.109.53.216:20000/enroll/join-enroll/", {
                titleid: sessionStorage.titleid,
                token: sessionStorage.accessToken,
                memberid: this.selected[i].memberid
              })
              .then(res => {
                !this.checkToken(res.data);
              });
          } else {
            alert("잘못된 접근입니다.");
            this.session_checked = false;
            this.$router.push("/");
          }
        }
        this.selected = [];
        this.getEnrollMember();
        this.getAllMember();
        this.$emit("get-enroll");
      } else {
        alert("선택된 사용자가 없습니다");
      }
    },
    checkid(memberid) {
      if (sessionStorage.getItem("uid") == memberid) return true;
      else return false;
    },
    exitEnroll() {
      console.log("탈출 코드");
      if (sessionStorage.getItem("accessToken") != null) {
        this.$http
          .post("http://211.109.53.216:20000/enroll/delete-enroll/", {
            titleid: sessionStorage.titleid,
            token: sessionStorage.accessToken
          })
          .then(res => {
            if (this.checkToken(res.data)) {
              this.$router.replace("/workspace");
            }
          });
      } else {
        alert("잘못된 접근입니다.");
        this.session_checked = false;
        this.$router.push("/");
      }
    },

    //탭3
    delTitle() {
      if (sessionStorage.getItem("accessToken") != null) {
        this.$http
          .post("http://211.109.53.216:20000/title/delete-title/", {
            titleid: sessionStorage.titleid,
            token: sessionStorage.accessToken
          })
          .then(res => {
            if (this.checkToken(res.data)) {
              this.$bvModal.hide("TiDelCheck");
              this.$bvModal.hide("TitleSetting");
              this.$emit("go-home");
            }
          });
      } else {
        alert("잘못된 접근입니다.");
        this.session_checked = false;
        this.$router.push("/");
      }
    }
  },
  components: {
    Multiselect
  }
};
</script>