<template>
  <div >
    <div v-for="(assign, i) in assigns" :key="i" @click="showContentForm(assign.contentid)" class="card text-white bg-danger o-hidden h-100">
      <div class="card-body">
        <div class="card-body-icon">
          <i class="fas fa-fw fa-comments"></i>
        </div>
        <div>
          <a class="text-white">{{assign.contentname}}</a>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "AssignList",
  props: ["assigns"],
  methods: {
     showContentForm(select_item){
      this.$store.commit('selectedContent', select_item)
      this.$bvModal.show('contentForm')
    }
  },
};
</script>