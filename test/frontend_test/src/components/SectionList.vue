<template>
  <div class="row inner-row">
    <!--Modal 선언부 -->
    <b-modal
      id="create-section"
      title="Create Section"
      centered
      ok-only
      ref = 'modal'
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

    <!--메인 코드 시작부-->
    <div class="col-md-2" id="sessionbar">
      <section>
        <ol class="breadcrumb">
          <li class="breadcrumb-item">
            <a @click="$bvModal.show('create-section')">Create New Session</a>
          </li>
        </ol>
      </section>
    </div>

    <div v-for="(section, i) in sections" :key="i" class="col-md-4" id="newsession">
      <section>
        <div class="session text-white o-hidden h-100" style="background:gray">
          <div class="card-body">
            <div class="breadcrumb-item">
              <div>{{section.sectionname}}</div>
            </div>
          </div>

          <Content v-bind:contents="section.includeContent" v-on:del-content="delContent"></Content>

          <div class="card-footer text-white clearfix small z-1">
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
</template>

<script>
import Content from "@/components/Content";
export default {
  name: "Section",
  props: ["sections", "select_item"],
  data() {
    return {
      sectionname: "",
      nameState: null,
    };
  },
  methods: {
    getSection() {
      //기존과 조금 다르게 emit을 이용하여 모든 정보를 로드해야할듯
    },
    
    createSection() {
      this.$http.post('http://211.109.53.216:20000/section/create-section/', {
           titleid: this.select_item, sectionname:this.sectionname, token:sessionStorage.accessToken
          }).then((res) => {
              this.getSection()
          })
    },
    delContent() {},

    //Modal 관련코드
    checkFormValidity() {
      const valid = this.$refs.form.checkValidity();
      this.nameState = valid ? "valid" : "invalid";
      return valid;
    },
    resetModal() {
      this.name = "";
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
    Content: Content
  }
};
</script>