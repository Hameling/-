<template>
  <b-modal
    id="create-scehdule"
    title="Create Scehdule"
    hide-header
    centered
    ref="modal"
    @show="resetModal"
    @hidden="resetModal"
    @ok="handleOk"
  >
    <form ref="form" @submit.stop.prevent="handleSubmit">
      <b-form-group
        :state="nameState"
        label="Scehdule Name"
        label-for="name-input"
        invalid-feedback="Scehdule Name is required"
      >
        <b-form-input id="name-input" v-model="scehdulename" :state="nameState" required></b-form-input>
      </b-form-group>

      <b-form-group
        label="Start Time"
        label-for="start-input"
        :state="startState"
        invalid-feedback="Start Time is required"
      >
        <VueCtkDateTimePicker
          id="start-input"
          v-model="start_date_tmp"
          :no-header="true"
          :format="date_form"
          :no-label="true"
          :min-date="now_time"
          :max-date="end_date"
          :right="true"
          :state="startState"
          required
        />
      </b-form-group>

      <b-form-group
        label="End Time"
        label-for="end-input"
        :state="endState"
        invalid-feedback="End Time is required"
      >
        <VueCtkDateTimePicker
          id="end-input"
          v-model="end_date_tmp"
          :no-header="true"
          :format="date_form"
          :no-label="true"
          :min-date="start_date"
          :right="true"
          state="endState"
          required
        />
      </b-form-group>
    </form>
  </b-modal>
</template>


<script>
import moment from "moment";
export default {
  name: "createScehdule",
  data: () => ({
    scehdulename: "",
    nameState: null,
    startState: null,
    endState: null,

    //Day Picker를 위한 변수
    // start_date: moment().format("YYYY-MM-DD HH:mm"),
    // end_date: moment().format("YYYY-MM-DD HH:mm"),
    start_date_tmp: null,
    end_date_tmp: null,
    date_form: "YYYY-MM-DD HH:mm",
    now_time: moment().format("YYYY-MM-DD HH:mm")
  }),
  computed: {
    start_date :{
        get: function (){
            if(this.start_date_tmp != null)return this.start_date_tmp
            else return this.now_time
        },
        set: function (newDate){
            this.start_date_tmp = newDate
        }
    },
    end_date :{
        get: function (){
            if(this.end_date_tmp != null)return this.end_date_tmp
            else return null
        },
        set: function (newDate){
            this.end_date_tmp = newDate
        }
    }
  },
  methods: {
    getScehdule() {
      this.$emit("get-scehdule");
    },
    createScehdule() {
      if (sessionStorage.getItem("accessToken") != null) {
        this.$http
          .post("http://211.109.53.216:20000/calender/create-calender/", {
            contentid: sessionStorage.contentid,
            token: sessionStorage.accessToken,
            starttime: this.start_date_tmp,
            duetime: this.end_date_tmp,
            calendername: this.scehdulename
          })
          .then(res => {
            if (this.checkToken(res.data)) {
              this.getScehdule();
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
      this.startState = valid ? "valid" : "invalid";
      this.endState = valid ? "valid" : "invalid";
      return valid;
    },
    resetModal() {
      this.scehdulename = "";
      this.start_date = null;
      this.end_date = null;
      this.nameState = null;
      this.startState = null;
      this.endState = null;
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
        this.createScehdule();
      });
    }
  }
};
</script>