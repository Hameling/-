<template>
  <!-- <router-link to="/content"> -->
    <!--작성된 컨텐트-->
    <div>    
      <div
      v-for="(content, i) in contents"
      :key="i"
      @click="showContentForm(content.contentid)"
      class="card-footer text-white clearfix small z-1"
    >
      <span class="float-left">{{content.contentname}}</span>
      <span class="float-right">
      </span>
    </div></div>

  <!-- </router-link> -->
</template>

<script>
import ContentForm from '@/components/modal/ContentForm';
export default {
  name: "ContentList",
  props: ["contents"],
  methods: {
    showContentForm(select_item){
      this.$store.commit('selectedContent', select_item)
      this.$bvModal.show('contentForm')
    }
  },
  components: {
    ContentForm: ContentForm
  }
};
</script>