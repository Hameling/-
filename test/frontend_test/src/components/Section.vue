<template>
  <div class="row inner-row">
    <div class="col-md-2" id="sessionbar">
      <section>
        <router-link to>
          <ol class="breadcrumb">
            <li class="breadcrumb-item">
              <a href="#">Create New Session</a>
            </li>
          </ol>
        </router-link>
      </section>
    </div>

    <div v-for="(section, i) in sections" :key="i" class="col-md-4" id="newsession">
      <section>
        <div class="session text-white o-hidden h-100" style="background:gray">
          <div class="card-body">
            <div class="breadcrumb-item">
              <div>{{section.sectionname}}</div>
            </div>
          </div>

 
          <Content v-bind:contents='section.includeContent' v-on:del-content="delContent"> </Content>

          <div class="card-footer text-white clearfix small z-1">
            <!--새 컨텐트 작성-->
            <span class="float-left">Create New content</span>
            <span class="float-right">
              <i class="fas fa-angle-right"></i>
            </span>
          </div>
        </div>
      </section>
    </div>
  </div>
</template>

<script>
import Content from "@/components/Content";
export default {
  name: "Section",
  props: ["sections"],
  data(){
      return {
        contents:[]
      }
  },
  methods: {
      createContent(){

      },
      delContent(){

      }
  },
  mounted() {
    
  },
  components: {
      'Content' : Content
  }
};
</script>