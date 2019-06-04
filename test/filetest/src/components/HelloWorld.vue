<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    <div class="dropbox">
      <input
        class="input-file"
        type="file"
        name="filename"
        @change="upload($event.target.name, $event.target.files)"
        @drop="upload($event.target.name, $event.target.files)"
      >
      <h2>파일을 드래그해서 드랍해주세요.</h2>
    </div>
    <input type="text" placeholder="token" v-model="token">
    <br>
    <input type="text" placeholder="contentid" v-model="contentid">
    <br>
    <input type="text" placeholder="filename" v-model="filename">
    <br>
    <button @click="download()">다운로드</button>
  </div>
</template>a

<script>
export default {
  name: "HelloWorld",
  data: () => ({
    token: "",
    contentid: "",
    filename: ""
  }),
  props: {
    msg: String
  },
  methods: {
    upload(name, files) {
      console.log(this.token);
      console.log(this.contentid);
      const formData = new FormData();
      formData.append(name, files[0], files[0].name);
      formData.append("contentid", this.contentid);
      formData.append("key", this.token);
      this.$http.post("", formData).then(res => {
        console.log(res);
      });
    },
    donwload() {
      this.$http.post("", {
        filename:this.filename, contentid:this.contentid, token:this.token
      }).then(res => {
        console.log(res);
      });
    }
  }
};
</script>

<style scoped>
.dropbox {
  outline: 2px dashed #aaa;
  background: #7fb4dd;
  width: 300px;
  height: 300px;
  position: relative;
  margin: 0 auto;
}
.dropbox > h2 {
  position: absolute;
  top: 50px;
  left: 0;
  z-index: 2;
}
.input-file {
  position: absolute;
  opacity: 0;
  width: 100%;
  height: 100%;
  top: 0;
  left: 0;
  z-index: 3;
}
</style>