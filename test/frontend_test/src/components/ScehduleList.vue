<template>
  <div>
    <ul v-for="(scehdule, i) in scehdules" :key="i" class="list-unstyled">
      <li>
        {{scehdule.starttime}} ~ {{scehdule.duetime}}
        <span
          v-on:click="delScehdule(scehdule.indexnumber)"
          class="close"
          aria-hidden="true"
        >&times;</span>
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
    }
  }
};
</script>