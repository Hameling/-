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
    <!-- <input type="text" placeholder="token" v-model="token">
    <br>
    <input type="text" placeholder="contentid" v-model="contentid">
    <br> -->
    <input type="text" placeholder="filename" v-model="filename">
    <br>
    <button @click="download()">다운로드</button>
  </div>
</template>a

<script>
export default {
  name: "HelloWorld",
  data: () => ({
    token: "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJtZW1iZXJpZCI6ImpqaHc5ODgyIn0.sy99mqSG_5NnnkiA27HsGhdX6Yu86_w8likSNPSY0Zg",
    contentid: "8",
    filename: ""
  }),
  props: {
    msg: String
  },
  methods: {
 forceFileDownload(response){
      const url = window.URL.createObjectURL(new Blob([response.data]))
      const link = document.createElement('a')
      link.href = url
      link.setAttribute('download', this.filename) //or any other extension
      document.body.appendChild(link)
      link.click()
    },

    upload(name, files) {
      const formData = new FormData();
      formData.append(name, files[0], files[0].name);
      formData.append("contentid", this.contentid);
      formData.append("token", this.token);
      this.$http.post("http://127.0.0.1:8000/file/create-file/", formData).then(res => {
        console.log(res.data);
      });
    },
    download() {
      const formData = new FormData();
      formData.append("filename", this.filename);
      formData.append("contentid", this.contentid);
      formData.append("token", this.token);
      this.$http.post("http://127.0.0.1:8000/file/down-file/", formData).then(res => {
        console.log(res);
        this.forceFileDownload(res)
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