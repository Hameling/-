<template>
  <div class="row inner-row">
    <!--Section Modal 선언부 -->

    <!--Content Modal 선언부 -->
    <createContent v-on:get-element="getSection"/>
    <createSection v-bind:select_item="select_item" v-on:get-section="getSection"/>
    <ContentForm v-bind:enrollMember="this.enrollMember"/>
    <TitleSetting v-bind:select_item="select_item"/>

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
              <strong>{{this.select_item.titlename}}</strong>
              <span @click="$bvModal.show('TitleSetting')">
                <i class="fas fa-cog icon-padding"></i>
              </span>
            </a>
          </li>
        </ol>

        <ol class="breadcrumb">
          <li class="breadcrumb-item">
            <a @click="createSec">Create New Section</a>
          </li>
        </ol>
      </section>
    </div>

    <div v-for="(section, i) in sections" :key="i" class="col-md-4" id="newsession">
      <div class="card-padding">
        <section>
          <div class="session text-white o-hidden h-100" style="background:gray">
            <div class="card-body">
              <div class="breadcrumb-item">
                <div class="float-left">{{section.sectionname}}</div>
                <span @click="delSectionCheck(section)" class="float-right">
                  <i class="times-icon">&times;</i>
                </span>
              </div>
            </div>

            <ContentList v-bind:contents="section.includeContent" v-on:del-content="delContent"></ContentList>

            <div
              @click="createCont(section.sectionid)"
              class="card-footer text-white clearfix small z-1"
            >
              <!--새 컨텐트 작성-->
              <span class="float-left">Create New content</span>
              <span class="float-right">
                <i class="fas fa-angle-right"></i>
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
export default {
  name: "Section",
  props: ["sections", "enrollMember", "select_item"],
  data: () => ({
    contentname: "",
    contentinfo: "",

    //삭제될 섹션 정보
    delSelSec: {}
  }),
  methods: {
    getSection() {
      this.$emit("get-element");
    },

    createSec() {
      this.$bvModal.show("create-section");
    },

    delSectionCheck(section) {
      this.delSelSec = section;
      this.$bvModal.show("SecDelCheck");
    },

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
    createCont(sectionid) {
      this.$store.commit("selectedSection", sectionid);
      this.$bvModal.show("create-content");
    },

    delContent() {}
  },
  mounted() {},
  components: {
    ContentList: ContentList,
    createContent: createContent,
    createSection: createSection,
    ContentForm: ContentForm,
    TitleSetting: TitleSetting
  }
};
</script>