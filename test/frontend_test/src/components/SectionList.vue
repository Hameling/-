<template>
  <div class="row inner-row">
    <!--Section Modal 선언부 -->
    <b-modal
      id="create-section"
      title="Create Section"
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
          label="Section Name"
          label-for="name-input"
          invalid-feedback="Section Name is required"
        >
          <b-form-input id="name-input" v-model="sectionname" :state="nameState" required></b-form-input>
        </b-form-group>
      </form>
    </b-modal>
    <!--Content Modal 선언부 -->
     <createContent v-on:get-element="getSection"/>
     <ContentForm v-bind:enrollMember="this.enrollMember"/>

     

    <!--메인 코드 시작부-->
    <div class="col-md-2" id="sessionbar">
      <section>
        <ol class="title-border section-header">
          <div class="column">
            <li class="breadcrumb-item">
              <a>
                <strong>{{this.select_item.titlename}}</strong>
              </a>
              <a @click="$bvModal.show('create-section')">Create New Section</a>
            </li>
          </div>
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
                  <i class="times-icon">&times;</i>
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
import ContentForm from '@/components/modal/ContentForm';
export default {
  name: "Section",
  props: ["sections", "enrollMember" ,"select_item"],
  data() {
    return {
      sectionname: "",
      contentname: "",
      contentinfo: "",
      nameState: null,
    };
  },
  methods: {
    getSection() {
      this.$emit('get-element')
    },
    
    createSection() {
      this.$http.post('http://211.109.53.216:20000/section/create-section/', {
           titleid: this.select_item.titleid, sectionname:this.sectionname, token:sessionStorage.accessToken
          }).then((res) => {
              this.getSection()
          })
    },

    createCont(sectionid){
        this.$store.commit('selectedSection', sectionid)
        this.$bvModal.show('create-content')
    },

    delContent() {},

    //Modal 관련코드
    checkFormValidity() {
      const valid = this.$refs.form.checkValidity();
      this.nameState = valid ? "valid" : "invalid";
      return valid;
    },
    resetModal() {
      this.sectionname = "";
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
        this.createSection()
      })
    }
  },
  mounted() {

  },
  components: {
    ContentList: ContentList,
    createContent: createContent,
    ContentForm: ContentForm
  }
};
</script>