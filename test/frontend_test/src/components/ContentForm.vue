  <template>
  <div class="bg-dark">
    <div class="container">
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
                      <cComment v-bind:comments="comments" v-on:del-comment="delComment"> </cComment>
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

              <div class="dropdown">
                <button class="dropbtn">MM</button>
                <div class="dropdown-content">
                  <a >1</a>
                  <a >2</a>
                  <a >3</a>
                  <a >4</a>
                  <a >5</a>
                  <a >6</a>
                  <a >7</a>
                  <a >8</a>
                  <a >9</a>
                  <a >10</a>
                  <a >11</a>
                  <a >12</a>
                </div>
              </div>
              <div class="dropdown">
                <button class="dropbtn">dd</button>
                <div class="dropdown-content">
                  <a>1</a>
                  <a>2</a>
                  <a>3</a>
                  <a>4</a>
                  <a>5</a>
                  <a>6</a>
                  <a>7</a>
                  <a>8</a>
                  <a>9</a>
                  <a>10</a>
                  <a>11</a>
                  <a>12</a>
                  <a>13</a>
                  <a>14</a>
                  <a>15</a>
                  <a>16</a>
                  <a>17</a>
                  <a>18</a>
                  <a>19</a>
                  <a>20</a>
                  <a>21</a>
                  <a>22</a>
                  <a>23</a>
                  <a>24</a>
                  <a>25</a>
                  <a>26</a>
                  <a>27</a>
                  <a>28</a>
                  <a>29</a>
                  <a>30</a>
                  <a>31</a>
                  
                </div>
              </div>

              </div>
              </section>
              <div><br></div>
              <section>
                <div id="myDIV" class="header"> 
                  <input type="text" id="myInput" class="form-control" placeholder="New List" v-model="ckl_content" v-on:keyup.enter="addCheckList(ckl_content)">
                  <!--<button id="cklAdd" v-on:click="addCheckList(ckl_content)">Add</button>-->
                  <div class="file-box" style="overflow:auto">
                    <cChecklist v-bind:checklists="checklists" v-on:del-checklist="delCheckList"> </cChecklist>
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
            memberid:"jjhw9882", contentname:"사전조사(1)", contentid:"8"
          }).then((res) => {
              //console.log('getTodos:', res.data)
              this.comments = res.data
          })
      },
      addComment(cmt_content){
          if(cmt_content){
              this.$http.post('http://211.109.53.216:20000/comment/create-comment/',{
                  comcomment:cmt_content, memberid:"jjhw9882", contentid:"8"
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
            comnumber : comment_id, memberid:'jjhw9882'
          })
          .then((res) => {
              this.getComments()
          })
      },

    
    //체크리스트
      getCheckLists() {
          this.$http.post('http://211.109.53.216:20000/checklist/search-checklist/', {
            contentid: "8"
          })
          .then((res) => {
              this.checklists = res.data
          })
      },
      addCheckList(ckl_content){
          if(ckl_content){
              this.$http.post('http://211.109.53.216:20000/checklist/create-checklist/',{
                  contentid:"8" , listname:ckl_content
              }).then((res) => {
                  this.getCheckLists()
                  this.ckl_content = ''
              })
          }
      },
      delCheckList(checklist_id){
          this.$http.post('http://211.109.53.216:20000/checklist/delete-checklist/',{
            listnumber: checklist_id
          })
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