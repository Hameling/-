<template>
  <b-modal id="TitleSetting" title="Title Setting" centered @hidden="resetState">
    <b-tabs>
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

      <b-tab title="Enroll">
        <!--Enroll된 멤버 확인 및 삭제 : 기존 리스트 사용-->
        <!--Enroll 시킬 대상 추가 : 셀렉터 활용-->
      </b-tab>
      <b-tab title="Title Delete"></b-tab>
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

    titlename:"",
    titleinfo:""
  }),
  props: ["select_item"],

  methods: {
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
          .post("http://211.109.53.216:20000/content/update-content/", {
            contentid: sessionStorage.contentid,
            token: sessionStorage.accessToken,
            titlename: this.titlename,
            titleinfo: this.titleinfo,
            contentstate: "1"
          })
          .then(res => {
            if (this.checkToken(res.data)) {
              this.getContent();
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
    }
  }
};
</script>