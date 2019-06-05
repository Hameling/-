<template>
  <div class="row inner-row">
    <!--Section Modal 선언부 -->

    <!--Content Modal 선언부 -->
     <createContent v-on:get-element="getSection"/>
     <createSection v-bind:select_item="select_item" v-on:get-section="getSection"/>
     <ContentForm v-bind:enrollMember="this.enrollMember"/>

     

    <!--메인 코드 시작부-->
    <div class="col-md-2" id="sessionbar">
      <section>
        <ol class="title-border section-header">
<<<<<<< HEAD
          <li class="breadcrumb-item">
            <a>
              <strong>{{this.select_item.titlename}}</strong>
            </a>
          </li>
        </ol>

        <ol class="breadcrumb">
          <li class="breadcrumb-item">
            <a @click="createSec">Create New Section</a>
          </li>
=======
          <div class="column">
            <li class="breadcrumb-item">
              <a>
                <strong>{{this.select_item.titlename}}</strong>
              </a>
              <a @click="$bvModal.show('create-section')">Create New Section</a>
            </li>
          </div>
>>>>>>> 3e07e4465b4100e7315f05f86e104c339a7ee21e
        </ol>
      </section>
    </div>

    
    <div v-for="(section, i) in sections" :key="i" class="col-md-4" id="newsession">
      <div class="card-padding">
        <section>
          <div class="session text-white o-hidden h-100 " style="background:gray">
            <div class="card-body">
              <div class="breadcrumb-item">
                <div class="float-left ">{{section.sectionname}}</div>
                <span class="float-right">
                  <i @click="delSection(section.sectionid)" class="times-icon">&times;</i>
                </span>
              </div>
            </div>

            <ContentList v-bind:contents="section.includeContent" v-on:del-content="delContent"></ContentList>

            <div @click="createCont(section.sectionid)" class="card-footer text-white clearfix small z-1">
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
import createContent from '@/components/modal/createContent';
import createSection from '@/components/modal/createSection';
import ContentForm from '@/components/modal/ContentForm';
export default {
  name: "Section",
  props: ["sections", "enrollMember" ,"select_item"],
  data:() => ({
      contentname: "",
      contentinfo: "",

  }),
  methods: {
    getSection() {
      this.$emit('get-element')
    },

    createSec(){
      this.$bvModal.show('create-section')
    },

    delSection(sectionid){
      if (sessionStorage.getItem("accessToken") != null) {
        this.$http
          .post("http://211.109.53.216:20000/section/delete-section/", {
            sectionid: sectionid,
            token: sessionStorage.accessToken
          })
          .then(res => {
            this.checkToken(res.data);
          });
      } else {
        console.log("잘못된 접근입니다.");
        this.session_checked = false;
        this.$router.push("/");
      }
    },
    createCont(sectionid){
        this.$store.commit('selectedSection', sectionid)
        this.$bvModal.show('create-content')
    },

    delContent() {},


  },
  mounted() {

  },
  components: {
    ContentList: ContentList,
    createContent: createContent,
    createSection: createSection,
    ContentForm: ContentForm
  }
};
</script>