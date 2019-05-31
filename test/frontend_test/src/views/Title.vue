  <template>
  <div class="container-fluid main-container">
    <SectionList v-bind:sections="sections" v-bind:select_item="select_item" v-on:del-section="delSection"></SectionList>
  </div>
  <!--content-fulid-->

  <!--<a class="btn btn-primary btn-block" href="#">Confirm</a>-->
</template>

<script>
import SectionList from "@/components/SectionList";
export default {
  name: "Title",
  props: ["select_item"],
  data: function() {
    return {
      selectedid: "",
      sections: []
    };
  },
  methods: {
    getAllElement() {
      this.$http
        .post("http://211.109.53.216:20000/member/call-all/", {
          titleid: this.select_item
        })
        .then(res => {
          this.sections = res.data;
        });
    },
    delSection() {}
  },
  mounted() {
    this.$nextTick(() => {
      this.getAllElement();
    });
  },

  components: {
    SectionList: SectionList
  }
};
</script>