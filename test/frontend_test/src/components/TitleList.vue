<template>
  <div class="col-md-10 offset-md-1">
    <router-link :to="{name: 'title', params:{select_item:title.titleid}}" 
    v-for="(title,i) in titles" :key="i" 
    class="card text-white bg-primary o-hidden h-100"
    >
        <div class="card-body">
          <div class="card-body-icon">
            <i class="fas fa-fw fa-comments"></i>
          </div>
          <div>
            <a class="text-white">{{title.titlename}}</a>
          </div>
        </div>
    </router-link>
  </div>
</template>

<script>
export default {
  name: "TitleList",
  props: ["titles"]
};
</script>