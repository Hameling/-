<template>
  <div>
    <ul v-for="(checklist, i) in checklists" :key="i" class="list-unstyled">
      <li v-if="!checked_array[i]">
        <input
          type="checkbox"
          class="toggle"
          v-model="checked_array[i]"
          @click="updateChecked(checklist)"
        >
        {{checklist.listname}}
        <span
          v-on:click="delCheckList(checklist.listnumber)"
          class="close"
          aria-hidden="true"
        >&times;</span>
      </li>
      <li v-else class="font_through">
        <input
          type="checkbox"
          class="toggle"
          v-model="checked_array[i]"
          @click="updateChecked(checklist)"
        >
        {{checklist.listname}}
        <span
          v-on:click="delCheckList(checklist.listnumber)"
          class="close"
          aria-hidden="true"
        >&times;</span>
      </li>
    </ul>
  </div>
</template> 

<script>
export default {
  name: "Checklist",
  data: () => ({
    checked_tmp: false,
    checked_array: []
  }),
  props: ["checklists"],
  methods: {
    getChecklist() {
      this.$emit("get-checklist");
      this.checked_array = [];
      for (var i in this.checklists) {
        if (this.checklists[i].checked == 0) this.checked_array.push(false);
        else this.checked_array.push(true);
      }
    },
    delCheckList(checklist) {
      this.$emit("del-checklist", checklist);
    },
    updateChecked(checklist) {
      var index = this.checklists.indexOf(checklist);
      if (checklist.checked == 0) {
        this.checklists[index].checked = 1;
        console.log(this.checklists[index].checked);
      } else {
        this.checklists[index].checked = 0;
        console.log(this.checklists[index].checked);
      }

      if (sessionStorage.getItem("accessToken") != null) {
        this.$http
          .post("http://110.11.72.247:20000/checklist/update-checklist/", {
            token: sessionStorage.accessToken,
            listname: this.checklists[index].listname,
            listnumber: this.checklists[index].listnumber,
            checked: this.checklists[index].checked
          })
          .then(res => {
            if (this.checkToken(res.data)) {
              this.getChecklist();
            }
          });
      } else {
        alert("잘못된 접근입니다.");
        this.session_checked = false;
        this.$router.push("/");
      }
    }
  },
  beforeUpdate() {
    this.checked_array = [];
      for (var i in this.checklists) {
        if (this.checklists[i].checked == 0) this.checked_array.push(false);
        else this.checked_array.push(true);
      }
  },
  mounted() {
    this.checked_array = [];
    for (var i in this.checklists) {
      if (this.checklists[i].checked == 0) this.checked_array.push(false);
      else this.checked_array.push(true);
    }
  }
};
</script>

<style>
.font_through {
  text-decoration: line-through;
}
</style>