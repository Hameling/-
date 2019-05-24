<template>
  <router-link to="/content">
    <!--작성된 컨텐트-->
    <div
      v-for="(content, i) in contents"
      :key="i"
      class="card-footer text-white clearfix small z-1"
    >
      <span class="float-left">{{content.contentname}}</span>
      <span class="float-right">
        <i class="fas fa-angle-right"></i>
      </span>
    </div>
  </router-link>
</template>

<script>
export default {
  name: "Content",
  props: ["contents"]
};
</script>