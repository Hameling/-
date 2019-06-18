<template>
  <div class="row inner-row" id="scrollbar-style">
    <!--Section Modal 선언부 -->

    <!--Content Modal 선언부 -->
    <createContent v-on:get-element="getSection"/>
    <createSection v-on:get-section="getSection"/>
    <ContentForm v-bind:enrollMember="this.enrollMember" v-on:get-section="getSection"/>
    <TitleSetting
      v-bind:enrollMember="this.enrollMember"
      v-on:get-enroll="getEnrollMemeber"
      v-on:go-home="goHome"
      v-on:updateTitle="updateTitleName"
    />

    <b-modal id="SecDelCheck" title="SectionDeleteCheck" hide-footer hide-header centered>
      <div class="d-block text-center">
        <h4>{{delSelSec.sectionname}}을 삭제 하시겠습니까?</h4>
        <br>
        <h5>{{delSelSec.sectionname}} 내의 Content도 같이 삭제됩니다</h5>
      </div>
      <b-button class="mt-3 bg-danger" block @click="delSection(delSelSec.sectionid)">예</b-button>
      <b-button class="mt-3 bg-primary" block @click="$bvModal.hide('SecDelCheck')">아니오</b-button>
    </b-modal>

    <!--메인 코드 시작부-->
    <div class="col-md-2" id="sessionbar">
      <section>
        <ol class="title-border section-header">
          <li class="breadcrumb-item">
            <a>
              <strong>{{titlename}}</strong>
              <span @click="$bvModal.show('TitleSetting')">
                <button class="fas fa-cog icon-padding button-icon"></button>
              </span>
            </a>
          </li>
        </ol>

        <!--
        <ol class="breadcrumb">
          <li class="breadcrumb-item">
            <a @click="createSec">Create New Section</a>
          </li>
        </ol>
        -->
        <!--
        <div>
          <div class="section-card o-hidden h-100">
            <div class="card-body">
              <div>
                <a @click="createSec">Create New Section</a>
              </div>
            </div>
          </div>
        </div>
        -->

        <div class="button-section">
          <div class="eff-section"></div>
          <a @click="createSec">Create New Section</a>
        </div>
      </section>
    </div>
    <!--SectionList 수정 부분-->
    <div v-for="(section, i) in sections" :key="i" class="col-md-4" id="newsession">
      <div class="card-padding">
        <section>
          <div class="session text-white o-hidden h-100" v-bind:id="'section'+i" >
            <div class="card-body">
              <div class="breadcrumb-item">
                <div class="float-left">{{section.sectionname}}</div>
                <span @click="delSectionCheck(section)" class="float-right">
                  <!--아이콘이 겹칩니다.
                  <i class="far fa-edit close-right"></i>-->
                  <button class="times-icon button-icon" style="color: white">&times;</button>
                </span>
              </div>
            </div>

            <ContentList v-bind:contents="section.includeContent"></ContentList>

            <div
              @click="createCont(section.sectionid)"
              class="card-footer text-white clearfix small z-1"
            >
              <!--새 컨텐트 작성-->
              <span class="float-left">Create New content</span>
              <span class="float-right">
                <button class="fas fa-plus button-icon" style="color: white;"></button>
              </span>
            </div>
          </div>
        </section>
      </div>
    </div>
  </div>
</template>

<script>
import ContentList from "@/components/ContentList";
import createContent from "@/components/modal/createContent";
import createSection from "@/components/modal/createSection";
import ContentForm from "@/components/modal/ContentForm";
import TitleSetting from "@/components/modal/TitleSetting";
import { bus } from "@/eventbus";
export default {
  name: "Section",
  props: ["sections", "enrollMember"],
  data: () => ({
    titlename: "",
    newTitlename: "",

    contentname: "",
    contentinfo: "",

    //SectionList 스타일 지정용 변수
    color : '#',
    bgcolor :  ['007bff', '6610f2', '6f42c1', '28a745', '20c997', '17a2b8', '007bff', '6c757d', '17a2b8'],

    //삭제될 섹션 정보
    delSelSec: {}
  }),
  methods: {
    //선택된 Title의 정보를 반환받는 메소드
     getTitle() {
      if (sessionStorage.getItem("accessToken") != null) {
        this.$http
          .post("http://211.109.53.216:20000/title/search-title/", {
            titleid: sessionStorage.titleid,
            token: sessionStorage.accessToken
          })
          .then(res => {
            if (this.checkToken(res.data[0])) {
              this.updateTitleName(res.data[0].titlename)
            }
          });
      } else {
        alert("잘못된 접근입니다.");
        this.session_checked = false;
        this.$router.push("/");
      }
    },

    //Title.vue에 Section 정보를 요청하는 메소드
    getSection() {
      this.$emit("get-element");
    },

    //Section 생성을 위한 modal 호출
    createSec() {
      this.$bvModal.show("create-section");
    },

    //Section 삭제시 경고창
    delSectionCheck(section) {
      this.delSelSec = section;
      this.$bvModal.show("SecDelCheck");
    },

    //Section 삭제를 위한 메소드
    delSection(sectionid) {
      if (sessionStorage.getItem("accessToken") != null) {
        this.$http
          .post("http://211.109.53.216:20000/section/delete-section/", {
            sectionid: sectionid,
            token: sessionStorage.accessToken
          })
          .then(res => {
            if (this.checkToken(res.data)) {
              if (res.data.delete == "Delete success") {
                this.checkToken(res.data);
                this.$bvModal.hide("SecDelCheck");
                this.getSection();
              } else {
                alert("잘못된 접근입니다.");
                this.$bvModal.hide("SecDelCheck");
                this.getSection();
              }
            }
          });
      } else {
        alert("잘못된 접근입니다.");
        this.session_checked = false;
        this.$router.push("/");
      }
    },

    //Content 생성을 위한 메소드
    createCont(sectionid) {
      this.$store.commit("selectedSection", sectionid);
      this.$bvModal.show("create-content");
    },

    //Title.vue에 Enroll 정보를 요청하는 메소드
    getEnrollMemeber() {
      this.$emit("get-enroll");
    },

    //workspace 화면으로 이동
    goHome() {
      this.$router.replace("/workspace");
    },

    //Title이름을 갱신하기위한 메소드
    updateTitleName(titlename) {
      this.newTitlename = titlename;
      this.titlename = this.newTitlename;
    },
    
    setColor(){
      for(var i in this.sections) {
        this.color += this.bgcolor[i % this.bgcolor.length]
        document.getElementById('section'+i).style.backgroundColor = this.color
        this.color = "#"
      }
    }
  },
  //화면 갱신시 Title의 이름을 변경
  beforeUpdate() {
    if (this.newTitlename == "") {
      this.getTitle()
     
    } else {
      this.newTitlename = "";
    }
  },

  updated() {
     this.setColor()
  },

  components: {
    ContentList: ContentList,
    createContent: createContent,
    createSection: createSection,
    ContentForm: ContentForm,
    TitleSetting: TitleSetting
  }
};
/*
var color='#';
var bgcolor= ['007bff', '6610f2', '6f42c1', '28a745', '20c997', '17a2b8', '007bff', '6c757d', '17a2b8'];
color += bgcolor[Math.floor(Math.random() *bgcolor.length)];
document.getElementById('sectionbg').style.background = color;
*/
</script>