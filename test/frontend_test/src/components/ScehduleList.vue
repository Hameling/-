<template>
  <div>
    <ul v-for="(scehdule, i) in scehdules" :key="i" class="list-unstyled">
      <li class="schedule-padding">
        <span class= "far fa-clock" v-bind:id="'scehdule'+i"/>
        {{scehdule.calendername}}
        <span
          v-on:click="delScehdule(scehdule.indexnumber)"
          class="close"
          aria-hidden="true"
        >&times;</span>
        <b-popover v-bind:target="'scehdule'+i">
          {{scehdule.starttime}} <br> {{scehdule.duetime}}
        </b-popover>

      </li>
    </ul>
  </div>
</template>

<script>
export default {
  name: "ScehduleList",
  props: ["scehdules"],
  methods: {
    delScehdule(index) {
      this.$emit("del-scehdule", index);
    },
    
    //popover를 이용한 일정 정보 표시 
    getScehuleInfo(scehdule){
      return scehdule.starttime + " \n~ " + scehdule.duetime
    }
  }
};
</script>