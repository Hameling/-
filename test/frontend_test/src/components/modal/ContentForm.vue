  <template>
  <b-modal id="contentForm" size="xl" scrollable hide-footer centered>
      <div class="card card-content mx-auto 5grid-layout">
        <div class="card-header">Content</div>
        <div class="card-body 5grid-layout">
          <div class="row">
            <div class="7u" id="leftcontent">
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
                    <input 
                      type="text"
                      id="NewComment"
                      class="form-control"
                      placeholder="NewComment"
                      required="requiired"
                      autofocus="autofocus"
                      v-model="cmt_content" v-on:keyup.enter="addComment(cmt_content)"
                    >
                    <label for="NewComment"> New Comment </label>

                    <div class="comment-box" style="overflow:auto">
                      <CommentList v-bind:comments="comments" v-on:del-comment="delComment" style="background: #d1d3d4"> </CommentList>
                    </div>
                  </div>
  
              </section>
            </div>

            <div class="4u" id="sidebar1">
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
              <div><br></div>
              <section>
              <div class="box">
                <div id="myDIV" class="header">
                  <a>Schedule</a>
                </div>

              <a>Start time </a>
              <VueCtkDateTimePicker v-model='start_date' :no-header='true'  :format="date_form" :no-label="true" :min-date="now_time"/>
         
              <div><br></div>
              
              <a>End Game </a>
              <VueCtkDateTimePicker v-model='end_date' :no-header='true'  :format="date_form" :no-label="true" :min-date="now_time"/>
            
              </div>
              </section>
              <div><br></div>
              <section>
                <div id="myDIV" class="header"> 
                  <input type="text" id="myInput" class="form-control" placeholder="New List" v-model="ckl_content" v-on:keyup.enter="addCheckList(ckl_content)">
                  <!--<button id="cklAdd" v-on:click="addCheckList(ckl_content)">Add</button>-->
                  <div class="file-box" style="overflow:auto">
                    <Checklist v-bind:checklists="checklists" v-on:del-checklist="delCheckList"> </Checklist>
                  </div>
                </div>
              </section>
              <div>
                <br>
              </div>
              <section>
                <div class="file-box">
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
                    <a>Drag & Drop</a>
                  </div>
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
        <!--<a class="btn btn-primary btn-block" href="#">Confirm</a>-->
      </div>
  </b-modal>
</template>

<script>
import moment from 'moment'
import Checklist from '@/components/CheckList'
import CommentList from '@/components/CommentList'
export default {
  name: 'contentForm',
  data(){
      return {
        //Day Picker를 위한 변수
          start_date : moment().format('YYYY-MM-DD HH:mm'),
          end_date : moment().format('YYYY-MM-DD HH:mm'),
          date_form : "YYYY-MM-DD HH:mm",
          now_time: moment().format('YYYY-MM-DD HH:mm'),
          
          cmt_content: '',
          ckl_content: '',
          comments:[],
          checklists:[],
      }
  },
  methods:{
    //코멘트
      getComments() {
          this.$http.post('http://211.109.53.216:20000/comment/checkcomment/', {
            memberid:"jjhw9882", contentname:"사전조사(1)", contentid:"8", token: sessionStorage.accessToken
          }).then((res) => {
              //console.log('getTodos:', res.data)
              this.comments = res.data
          })
      },
      addComment(cmt_content){
          if(cmt_content){
              this.$http.post('http://211.109.53.216:20000/comment/create-comment/',{
                  comcomment:cmt_content, memberid:"jjhw9882", contentid:"8", token: sessionStorage.accessToken
              }).then((res) => {
                  //this.comments.push(res.data);
                  //this.comments = res.data
                  this.getComments()
                  this.cmt_content = ''
              })
          }
      },
      delComment(comment_id){
          this.$http.post('http://211.109.53.216:20000/comment/delete-comment/',{
            comnumber : comment_id, memberid:'jjhw9882', token: sessionStorage.accessToken
          })
          .then((res) => {
              this.getComments()
          })
      },

    
    //체크리스트
      getCheckLists() {
          this.$http.post('http://211.109.53.216:20000/checklist/search-checklist/', {
            contentid: "8", token: sessionStorage.accessToken
          })
          .then((res) => {
              this.checklists = res.data
          })
      },
      addCheckList(ckl_content){
          if(ckl_content){
              this.$http.post('http://211.109.53.216:20000/checklist/create-checklist/',{
                  contentid:"8" , listname:ckl_content, token: sessionStorage.accessToken
              }).then((res) => {
                  this.getCheckLists()
                  this.ckl_content = ''
              })
          }
      },
      delCheckList(checklist_id){
          this.$http.post('http://211.109.53.216:20000/checklist/delete-checklist/',{
            listnumber: checklist_id, token: sessionStorage.accessToken
          })
          .then((res) => {
              this.getCheckLists()
          })
      },

      addSchedule(start, end) {

      },
      delSchedule(scehdule_id){

      }
  },
  mounted() {
      this.getComments();
      this.getCheckLists();   
    },

  components: {
    'CommentList': CommentList,
    'Checklist': Checklist,
  }
}
</script>