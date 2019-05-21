<template>
  <div class="container">
    <div class="card card-content mx-auto 5grid-layout">
      <div class="card-header">Content</div>
      <div class="card-body 5grid-layout">
        <div class="row">
          <div class="7u">
            <section>
              <div class="form-label-group">
                <input
                  type="text"
                  id="ContentTitle"
                  class="form-control"
                  placeholder="Title"
                  required="required"
                  autofocus="autofocus"
                >
                <label for="ContentTitle">Content Title</label>
              </div>
            </section>
            <div>
              <br>
            </div>
            <section>
              <div class="form-label-group">
                <input
                  type="text"
                  id="Subject"
                  class="form-control"
                  placeholder="Subject"
                  required="required"
                  autofocus="autofocus"
                >
                <label for="Subject">Subject</label>
              </div>
            </section>
            <div>
              <br>
            </div>
            <section>
              <div class="form-label-group">
                <input type="text" id="inputText" v-model="cmt_info" v-on:keyup.enter="addComment(cmt_info)">
                <button id="btnAdd" v-on:click="addComment(cmt_info)">Add</button>
                <cComment v-bind:comments="comments" v-on:del-comment="delComment"> </cComment>
              </div>
            </section>
          </div>

          <div class="3u" id="sidebar1">
            <section>
              <div class="form-label-group">
                <input
                  type="text"
                  id="AssignedPerson"
                  class="form-control"
                  placeholder="AssignedPerson"
                  required="required"
                >
                <label for="AssignedPerson">Assigned Person</label>
              </div>
            </section>
            <div>
              <br>
            </div>
            <section>
              <div class="form-label-group">
                <input
                  type="text"
                  id="Schedule"
                  class="form-control"
                  placeholder="Schedule"
                  required="required"
                >
                <label for="Schedule">Schedule</label>
              </div>
            </section>
            <div>
              <br>
            </div>
            <section>
              <div id="myDIV" class="header">
                <h2>Schedule</h2>
                <input type="text" id="myInput" placeholder="Title..." v-model="ckl_info" v-on:keyup.enter="addCheckList(ckl_info)">
                <span onclick="newElement()" class="addBtn" v-on:click="addCheckList(ckl_info)">Add</span>
                <cChecklist v-bind:checklists="checklists" v-on:del-checklist="delCheckList"> </cChecklist>
              </div>
            </section>
            <div>
              <br>
            </div>
            <section>
              <div class="form-label-group">
                <input
                  type="file"
                  id="File"
                  class="dropbox"
                  placeholder="File"
                  required="required"
                  @change="upload($event.target.name, $event.target.files)"
                  @drop="upload($event.target.name, $event.target.files)"
                >
                <h2>파일을 드래그해서 드랍해주세요.</h2>
              </div>
            </section>
            <div>
              <br>
            </div>
            <section>
              <div class="form-label-group">
                <input
                  type="text"
                  id="UpdateDate"
                  class="form-control"
                  placeholder="UpdateDate"
                  required="required"
                >
                <label for="UpdateDate">Update Date</label>
              </div>
            </section>
          </div>
        </div>
      </div>
      <a class="btn btn-primary btn-block" href="#">Confirm</a>
    </div>
  </div>
</template>

<script>
import cChecklist from '@/components/Cont_CheckList'
import cComment from '@/components/Cont_Comment'
export default {
  name: 'contentForm',
  data(){
      return {
          cmt_info: '',
          ckl_info: '',
          comments:[],
          checklists:[],
      }
  },
  methods:{
    //코멘트
      getComments() {
          this.$http.get('http://211.109.53.216:20000/comment')
          .then((res) => {
              //console.log('getTodos:', res.data)
              this.comments = res.data
          })
      },
      addComment(cmd_info){
          if(cmt_info){
              this.$http.post('http://211.109.53.216:20000/comment/create-comment',{
                  title:title
              }).then((res) => {
                  this.comments.push(res.data);
                  this.cmt_info = ''
              })
          }
      },
      delComment(comment){
          this.$http.delete('http://211.109.53.216:20000/comment/create-comment'+comment)
          .then((res) => {
              this.getComments()
          })
      },

    
    //체크리스트
      getCheckLists() {
          this.$http.get('http://211.109.53.216:20000/checklist')
          .then((res) => {
              //console.log('getTodos:', res.data)
              this.checklists = res.data
          })
      },
      addCheckList(ckl_info){
          if(ckl_info){
              this.$http.post('http://211.109.53.216:20000/checklist',{
                  title:title
              }).then((res) => {
                  this.ckl_info.push(res.data);
                  this.ckl_info = ''
              })
          }
      },
      delCheckList(checklist){
          this.$http.delete('http://211.109.53.216:20000/checklist'+checklist)
          .then((res) => {
              this.getCheckLists()
          })
      }
  },
  mounted() {
      this.getComments();
      this.getCheckLists();   
    },

  components: {
    'cChecklist': cChecklist,
    'cComment' : cComment
  }
}
</script>