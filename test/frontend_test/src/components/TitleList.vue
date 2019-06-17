<template>
  <div>
    <li v-for="(title,i) in titles" :key="i" class="nav-item">
      <div @click="selectItem(title)" class="nav-link">
        <!-- <router-link :to="{name: 'title', params:{select_item:title.titleid}}" class="nav-link"> -->
        <i class="fas fa-fw"></i>
        <!--fa-chart-area 버튼 이미지 -->
        <span>{{title.titlename}}</span>
      </div>
    </li>
  </div>
</template>

<script>
import { bus } from "@/eventbus";
import Title from '@/views/Title'
export default {
  name: "TitleList",
  props: ["titles"],
  methods: {
    selectItem(title) {
      this.$store.commit("selectedTitle", title.titleid); 
      this.$router.replace({
        name: "title",
        params: { titleid: title.titleid}
      });
      //bus.$emit("reloadItem", title.titleid);
    },
  }
};
</script>