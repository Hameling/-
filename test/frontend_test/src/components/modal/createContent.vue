<template>
  <b-modal
    id="create-content"
    title="Create Content"
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
        label="Content Name"
        label-for="name-input"
        invalid-feedback="Content Name is required"
      >
        <b-form-input id="name-input" v-model="contentname" :state="nameState" required></b-form-input>
      </b-form-group>

      <b-form-group label="Content Info(Optional)" label-for="info-input">
        <b-form-input id="info-input" v-model="contentinfo"></b-form-input>
      </b-form-group>
    </form>
  </b-modal>
</template>

<script>
export default {
  name: "createContent",
  data: () => ({
    contentname: "",
    contentinfo: "",
    nameState : null
  }),
  methods: {
    getSection() {
        this.$emit('get-element')
    },
    createContent() {
      

         if (sessionStorage.getItem("accessToken") != null) {
        this.$http
        .post("http://211.109.53.216:20000/content/create-content/", {
          contentname: this.contentname,
          contentinfo: this.contentinfo,
          contentstate: "1",
          sectionid: sessionStorage.sectionid,
          token: sessionStorage.accessToken
        })
        .then(res => {
          this.getSection();
        });
      } else {
        alert("잘못된 접근입니다.");
        this.session_checked = false;
        this.$router.push("/");
      }
    },

    //Modal 관련코드
    checkFormValidity() {
      const valid = this.$refs.form.checkValidity();
      this.nameState = valid ? "valid" : "invalid";
      return valid;
    },
    resetModal() {
      this.contentname = "";
      this.contentinfo = "";
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
        this.createContent();
      });
    }
  }
};
</script>