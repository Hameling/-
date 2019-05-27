<template>
    <!--프로젝트 01-->
    <router-link to="/project" class="col-md-10 offset-md-1">
      <div v-for="(title,i) in titles"
      :key="i"
      class="card text-white bg-primary o-hidden h-100">
        <div class="card-body">
          <div class="card-body-icon">
            <i class="fas fa-fw fa-comments"></i>
          </div>
          <div>
            <!--<a class="text-white" href="#">Project 01</a>-->
            <a class="text-white">{{title.titlename}}</a>
          </div>
        </div>
      </div>
    </router-link>
</template>

<script>
export default {
  name: "Project",
  props :["titles"]
};
</script>