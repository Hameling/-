  <template>
  <div class="container-fluid main-container" >
    <SectionList
      v-bind:sections="sections"
      v-bind:enrollMember="enrollMember"
      v-bind:select_item="select_item"
      v-on:get-element="getAllElement"
      v-on:get-enroll="getEnrollMember"
    ></SectionList>
  </div>
  <!--content-fulid-->

  <!--<a class="btn btn-primary btn-block" href="#">Confirm</a>-->
</template>

<script>
import SectionList from "@/components/SectionList";
import { bus } from "@/eventbus";
export default {
  name: "Title",
  props: ["select_item"],
  data:() => ({
          selectedid: "",
      sections: [],
      enrollMember: [],
  }),
  methods: {
    getAllElement() {
      if (sessionStorage.getItem("accessToken") != null) {
        this.$http
          .post("http://211.109.53.216:20000/member/call-all/", {
            titleid: sessionStorage.titleid,
            token: sessionStorage.accessToken
          })
          .then(res => {
            if (this.checkToken(res.data[0])) {
              this.sections = res.data;
            }
          });
      } else {
        alert("잘못된 접근입니다.");
        this.session_checked = false;
        this.$router.push("/");
      }
    },

    getEnrollMember() {
      if (sessionStorage.getItem("accessToken") != null) {
        this.$http
          .post("http://211.109.53.216:20000/enroll/search-enrolltitle/", {
            titleid: sessionStorage.titleid,
            token: sessionStorage.accessToken
          })
          .then(res => {
            if (this.checkToken(res.data[0])) {
              this.enrollMember = res.data;
            }
          });
      } else {
        alert("잘못된 접근입니다.");
        this.session_checked = false;
        this.$router.push("/");
      }
    },
  
    //App.vue에 Title 정보를 넘겨주기 위한 메소드
    getBaseData() {
      if (sessionStorage.getItem("accessToken") != null) {
        this.$http
          .post("http://211.109.53.216:20000/member/search-member/", {
            token: sessionStorage.accessToken
          })
          .then(res => {
            if (this.checkToken(res.data[0])) {
              this.$store.commit("updateTitleList", res.data[0].enrollTitle)
            }
          });
      } else {
        alert("잘못된 접근입니다.");
        this.session_checked = false;
        this.$router.push("/");
      }
    },
  },
  mounted() {
    this.$nextTick(() => {
      this.getAllElement();
      this.getEnrollMember();
      this.getBaseData();
    });
  },
  //URL주소의 변경시 마다 화면을 re-render 
  beforeRouteUpdate(to, from, next) {
    bus.$on("reloadItem", titleid => {
        this.$store.commit("selectedTitle", titleid);
    });
    this.$nextTick(() => {
      this.getAllElement();
      this.getEnrollMember();
    });
    next();
  },
  components: {
    SectionList: SectionList
  }
};
</script>