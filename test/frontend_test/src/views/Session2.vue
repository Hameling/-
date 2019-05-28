  <template>
  <div class="container-fluid main-container">
    <Section v-bind:sections="sections" v-on:del-section="delSection"></Section>
  </div>
  <!--content-fulid-->

  <!--<a class="btn btn-primary btn-block" href="#">Confirm</a>-->
</template>

<script>
import Section from "@/components/Section"
export default {
  name: "project",
  data() {
    return {
      sections: []
    };
  },
  props:["select_item"],
  methods: {
    getAllElement() {
      this.$http.post("http://211.109.53.216:20000/member/call-all/", {
        titleid: "8"
      })
      .then(res => {
        this.sections = res.data;
      });
    },
    delSection() {
      
    }
  },
  mounted() {
    this.getAllElement();
    //console.log(select_item)
  },

  components: {
    Section: Section
  }
};
</script>