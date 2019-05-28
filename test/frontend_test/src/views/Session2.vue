  <template>
  <div class="container-fluid main-container">
    <Section v-bind:sections="sections" v-on:del-section="delSection"></Section>
  </div>
  <!--content-fulid-->

  <!--<a class="btn btn-primary btn-block" href="#">Confirm</a>-->
</template>

<script>
import Section from "@/components/Section";
export default {
  name: "project",
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
    Section: Section
  }
};
</script>