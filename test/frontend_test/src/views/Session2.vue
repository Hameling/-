  <template>
      <div class="container-fluid  main-container">
            <div class="row h-100">
              <div class="col-md-2" id="sessionbar">
                <section>
                  <router-link to="">
                    <ol class="breadcrumb">
                      <li class="breadcrumb-item">
                        <a href="#">Create New Session</a>
                      </li>
                    </ol>
                  </router-link>
                </section>
              </div>


              <div class="col-md-4 " id="newsession">
                <section>
                  <div class="session text-white o-hidden h-100" style="background:gray" >
                    <div class="card-body">
                      <div class="breadcrumb-item">
                        <div>Test Session 01</div>
                      </div>
                    </div>

                    <!--작성된 컨텐트-->
                    <a class="card-footer text-white clearfix small z-1">
                      <span class="float-left">Create New content</span>
                      <span class="float-right">
                        <i class="fas fa-angle-right"></i>
                      </span>
                    </a>
                   

                    <a class="card-footer text-white clearfix small z-1">
                      <!--새 컨텐트 작성-->
                      <span class="float-left">Create New content</span>
                      <span class="float-right">
                        <i class="fas fa-angle-right"></i>
                      </span>
                    </a>
                  </div>
                </section>
              </div>



              <div class="col-md-4" id="newsession">
                <section>
                  <div class="session text-white o-hidden h-100" style="background:gray" >
                    <div class="card-body">
                      <div class="breadcrumb-item">
                        <div>Test Session 01</div>
                      </div>
                    </div> 
                    <a class="card-footer text-white clearfix small z-1" href="#">
                      <!--프로젝트 생성 페이지 링크-->
                      <span class="float-left">Create New content</span>
                      <span class="float-right">
                        <i class="fas fa-angle-right"></i>
                      </span>
                    </a>
                  </div>
                </section>
              </div>


              <div class="col-md-4" id="newsession">
                <section>
                  <div class="session text-white o-hidden h-100" style="background:gray" >
                    <div class="card-body">
                      <div class="breadcrumb-item">
                        <div>Test Session 01</div>
                      </div>
                    </div> 
                    <a class="card-footer text-white clearfix small z-1" href="#">
                      <!--프로젝트 생성 페이지 링크-->
                      <span class="float-left">Create New content</span>
                      <span class="float-right">
                        <i class="fas fa-angle-right"></i>
                      </span>
                    </a>
                  </div>
                </section>
              </div>


              <div class="col-md-4" id="newsession">
                <section>
                  <div class="session text-white o-hidden h-100" style="background:gray" >
                    <div class="card-body">
                      <div class="breadcrumb-item">
                        <div>Test Session 01</div>
                      </div>
                    </div> 
                    <a class="card-footer text-white clearfix small z-1" href="#">
                      <!--프로젝트 생성 페이지 링크-->
                      <span class="float-left">Create New content</span>
                      <span class="float-right">
                        <i class="fas fa-angle-right"></i>
                      </span>
                    </a>
                  </div>
                </section>
              </div>





            </div> <!--row-->

      </div>  <!--content-fulid-->

          <!--<a class="btn btn-primary btn-block" href="#">Confirm</a>-->
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