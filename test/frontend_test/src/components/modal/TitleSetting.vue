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
      <b-tab title="Title Info">
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
                v-on:click="delEnroll()"
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
          <!--버튼 추가가 필요한 부분-->
        </div>
      </b-tab>

      <!--삭제탭-->
      <b-tab title="Title Delete">
        <h4>Title을 삭제하시겠습니까?</h4>
        <br>
        <h5>Title 내의 Section 및 Content의 내용이 전부 삭제됩니다.</h5>
        <b-button class="mt-3 bg-danger" block>예</b-button>
        <b-button class="mt-3 bg-primary" block>아니오</b-button>
      </b-tab>
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
    selected: "",
    memberList: [],
    selected_members: []
  }),
  props: ["select_item", "enrollMember"],

  methods: {
    getElement() {
      this.getTitle();
      this.enrolledMembers = this.enrollMember;
      this.getAllMember();
    },

    getEnrollMember() {
      this.$emit("get-enroll");
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

    //titleUpdate
    setNameState() {
      this.nameState = !this.nameState;
    },
    setSubjectState() {
      this.subjectState = !this.subjectState;
    },

    updateName() {
      this.updateTitle();
      this.setNameState();
    },

    updateInfo() {
      this.updateTitle();
      this.setSubjectState();
    },
    //수정 요먕
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
    createEnroll(event) {
      console.log(event);
    },
    checkid(memberid) {
      if (sessionStorage.getItem("uid") == memberid) return true;
      else return false;
    }
  },
  components: {
    Multiselect
  }
};
</script>