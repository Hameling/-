<template>
  <div>
    <li v-for="(title,i) in titles" :key="i" class="nav-item">
      <!-- <router-link :to="{name: 'title', params:{titleid:title.titleid,select_item:title.titleid}}" class="nav-link"> -->
      <router-link :to="{name: 'title', params:{select_item:title.titleid}}" class="nav-link">
        <i class="fas fa-fw"></i>
        <!--fa-chart-area 버튼 이미지 -->
        <span>{{title.titlename}}</span>
      </router-link>
    </li>
  </div>
</template>

<script>
export default {
  name: "TitleList",
  props: ["titles"],
  methods: {
    test(data) {
      console.log(data);
    }
  }
};
</script>