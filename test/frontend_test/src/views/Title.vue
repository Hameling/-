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
  data: function() {
    return {
      selectedid: "",
      sections: [],
      enrollMember: []
    };
  },
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
    }
  },
  mounted() {
    this.$nextTick(() => {
      if (this.select_item.titleid != undefined) {
        this.$store.commit("selectedTitle", this.select_item.titleid);
        //이부분을 TitleList로
      }
      this.getAllElement();
      this.getEnrollMember();
    });
  },
  beforeRouteUpdate(to, from, next) {
    bus.$on("reloadItem", titleid => {
      //if (this.select_item.titleid != undefined) { 
        this.$store.commit("selectedTitle", titleid);
      //} 
      //이부분은 select_item을 검사하는게 아니라???? 아니 도데체 뭐녕
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