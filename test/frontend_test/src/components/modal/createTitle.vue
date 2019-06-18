<template>
  <b-modal
    id="create-title"
    title="Create Title"
    centered
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
        <b-form-input
          id="name-input"
          v-model="titlename"
          :state="nameState"
          v-on:keyup.enter="handleOk"
          required
        ></b-form-input>
      </b-form-group>

      <b-form-group label="Title Description(Option)" label-for="info-input">
        <b-form-input id="info-input" v-model="titleinfo" v-on:keyup.enter="handleOk"></b-form-input>
      </b-form-group>
    </form>
  </b-modal>
</template>

<script>
export default {
  name: "createTitle",
  data: () => ({
    titlename: "",
    titleinfo: "",
    nameState: null
  }),

  methods: {
    getBaseData() {
      this.$emit("get-basedata");
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
            if (this.checkToken(res.data)) {
              this.getBaseData();
            }
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
      this.titlename = "";
      this.titleinfo = "";
      this.nameState = null;
    },
    async handleOk(bvModalEvt) {
      bvModalEvt.preventDefault();
      await this.handleSubmit();
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
  }
};
</script>