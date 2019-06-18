  <template>
  <b-modal
    id="contentForm"
    size="xl"
    scrollable 
    hide-footer
    hide-header
    centered
    @show="getContent"
    @hidden="resetState"
  >
    <b-modal id="ContDelCheck" title="ContentDeleteCheck" hide-footer hide-header centered>
      <div class="d-block text-center">
        <h4>{{contentname}}을 삭제 하시겠습니까?</h4>
        <br>
        <h5>{{contentname}} 내의 모든 정보도 같이 삭제됩니다</h5>
      </div>
      <b-button class="mt-3 bg-danger" block @click="delContent">예</b-button>
      <b-button class="mt-3 bg-primary" block @click="$bvModal.hide('ContDelCheck')">아니오</b-button>
    </b-modal>


    <div class="content-card card-content mx-auto content-max-width">
      <div class="content-card-header content-title-position"> <strong> Content </strong>
        <button class="button-close" block @click="$bvModal.hide('contentForm')"> Close</button>
      </div>
      <div class="card-body content-max-width" style="background-color: #f7f7f7;">
        <div class="row">
          <div class="col-md-8" id="leftcontent">
            <section class="box" style="background-color: white;">
              <div v-if="nameState" class="form-label-group">
                <input
                  type="text"
                  v-model="contentname"
                  id="ContentTitle"
                  class="form-control"
                  placeholder="Title"
                  required="required"
                  autofocus="autofocus"
                  @keyup.enter="updateName"
                >
                <label for="ContentTitle">Content Title</label>
              </div>
              <div v-else class="form-label-group">
                <label for="ContentTitle" @click="setNameState" class="form-control">
                  <strong>{{contentname}}</strong>
                  <i class="far fa-edit close-right"></i>
                </label>
                <br>
                <br>
              </div>
            </section>
            <div>
              <br>
            </div>

            <section class="box" style="background-color: white;">
              <div v-if="subjectState" class="form-label-group">
                <input
                  type="text"
                  v-model="contentinfo"
                  id="ContentInfo"
                  class="form-control"
                  placeholder="Subject"
                  required="required"
                  @keyup.enter="updateInfo"
                >
                <label for="ContentInfo">Content Description</label>
              </div>
              <div v-else class="form-label-group">
                <label
                  for="ContentInfo"
                  @click="setSubjectState"
                  class="form-control"
                >{{contentinfo}}
                
                  <i class="far fa-edit close-right"></i>
                  
                </label>
                
                <br>
                <br>
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
                  v-model="cmt_content"
                  v-on:keyup.enter="addComment(cmt_content)"
                >
                <label for="NewComment">New Comment</label>

                <div class="comment-box inner-comment" style="overflow:auto" id="scrollbar-style">
                  <CommentList
                    v-bind:comments="comments"
                    v-on:del-comment="delComment"
                  ></CommentList>
                </div>
              </div>
            </section>
          </div>

          <!-- Assign 영역 -->
          <div class="col-md-4" id="rightcontent">
            <section>
              <div class="box" v-if="enrollMember" style="background-color: white;">
                <div id="myDIV" class="header">
                  <a>Assigned Area</a>
                </div>
                <multiselect
                  v-model="selected"
                  :options="enrollMember"
                  :searchable="false"
                  label="memberid"
                  placeholder="Not Assigned"
                  @input="doAssign"
                ></multiselect>
              </div>
              <div class="box" v-else>
                <div id="myDIV" class="header">
                  <a> I'm Assigned</a>
                </div>
              </div>

              
            </section>

            <div>
              <br>
            </div>

            <!-- Schedule 영역 -->
            <createScehdule v-on:get-scehdule="getScehdule"/>
            <section>
              <div class="box" style="background-color: white;">
                <button
                  class="btn btn-primary btn-block"
                  @click="$bvModal.show('create-scehdule')"
                >Add Schedule</button>
              </div>

              <div>
                <br>
              </div>

              <div class="schedule-box" style="overflow:auto; background-color: white;" id="scrollbar-style">
                <div id="myDIV" class="header schedule-title">
                  <strong>
                    <a>Schedule</a>
                  </strong>
                </div>
                <ScehduleList style="padding-top: 5px;" v-bind:scehdules="scehdules" v-on:del-scehdule="delSchedule"/>
              </div>
            </section>


            <div>
              <br>
            </div>


            <section>
              <div id="myDIV" class="header" style="background-color: white;">
                <input
                  type="text"
                  id="myInput"
                  class="form-control"
                  placeholder="New List"
                  v-model="ckl_content"
                  v-on:keyup.enter="addCheckList(ckl_content)"
                >
                <!--<button id="cklAdd" v-on:click="addCheckList(ckl_content)">Add</button>-->
                <div class="list-box" style="overflow:auto" id="scrollbar-style">
                  <Checklist v-bind:checklists="checklists" v-on:get-checklist="getCheckLists" v-on:del-checklist="delCheckList"></Checklist>
                </div>
              </div>
            </section>
            <div>
              <br>
            </div>

            <!-- 파일 업로드 및 다운로드 영역 -->
            <section>
              <div class="file-box" style="background-color: white;">
                <div class="dropbox">
                  <input 
                    class="input-file" 
                    type="file"
                    id="File"
                    placeholder="File"
                    required="required"
                    @change="upload($event.target.name, $event.target.files)"
                    @drop="upload($event.target.name, $event.target.files)"
                    >
                  <a>FileSelect / Drag & Drop</a>
                </div>
              </div>
              <div class="list-box" style="background-color: white;">              
              </div>
            </section>
            <div>
              <br>
            </div>
            <section>
              <div>
                <button
                  class="btn btn-primary btn-block"
                  @click="$bvModal.show('ContDelCheck')"
                >
                Delete Content
                </button>
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
import Multiselect from "vue-multiselect";
import "vue-multiselect/dist/vue-multiselect.min.css";

import Checklist from "@/components/CheckList";
import CommentList from "@/components/CommentList";
import ScehduleList from "@/components/ScehduleList";
import createScehdule from "@/components/modal/createScehdule";
export default {
  name: "contentForm",
  props: ["enrollMember"],
  data: () => ({
    //Content 내부 변수
    contentname: "",
    contentinfo: "",
    comments: [],
    checklists: [],
    scehdules: [],

    //Comment&CheckList 입력을 위한 변수
    cmt_content: "",
    ckl_content: "",

    //Assign 이용을 위한 변수
    selected: null,
    selected_tmp: null,

    //input <-> Label을 위한 변수
    nameState: false,
    subjectState: false
  }),
  methods: {
    getContent() {
      if (sessionStorage.getItem("accessToken") != null) {
        this.$http
          .post("http://211.109.53.216:20000/content/search-content/", {
            contentid: sessionStorage.contentid,
            token: sessionStorage.accessToken
          })
          .then(res => {
            if (this.checkToken(res.data)) {
              this.contentname = res.data[0].contentname;
              this.contentinfo = res.data[0].contentinfo;
              this.comments = res.data[0].commentlist;
              this.checklists = res.data[0].checklistlist;
              this.scehdules = res.data[0].calender;
              this.getAssign();
            }
          });
      } else {
        alert("잘못된 접근입니다.");
        this.session_checked = false;
        this.$router.push("/");
      }
    },

    //업무 할당에 대한 부분
    getAssign() {
      if (sessionStorage.getItem("accessToken") != null) {
        this.$http
          .post("http://211.109.53.216:20000/assign/search-assigncontent/", {
            contentid: sessionStorage.contentid,
            token: sessionStorage.accessToken
          })
          .then(res => {
            if (this.checkToken(res.data[0])) {
              if (res.data[0] != undefined) {
                //초기값이 있을떄
                for (var i in this.enrollMember) {
                  if (this.enrollMember[i].memberid == res.data[0].memberid) {
                    this.selected = this.enrollMember[i];
                    this.selected_tmp = this.selected;
                    break;
                  }
                }
              } else {
                //초기값이 없을때
                this.selected = res.data[0];
                this.selected_tmp = this.selected;
              }
            }
          });
      } else {
        alert("잘못된 접근입니다.");
        this.session_checked = false;
        this.$router.push("/");
      }
    },
    doAssign(title) {
      //사용자가 선택을 취소 했을 경우
      if (title == null) {
        if (sessionStorage.getItem("accessToken") != null) {
          this.$http
            .post("http://211.109.53.216:20000/assign/delete-assign/", {
              contentid: sessionStorage.contentid,
              token: sessionStorage.accessToken,
              memberid: this.selected_tmp.memberid
            })
            .then(res => {
              if (this.checkToken(res.data)) {
                this.selected_tmp = null;
              }
            });
        } else {
          alert("잘못된 접근입니다.");
          this.session_checked = false;
          this.$router.push("/");
        }
      } else {
        //사용자가 다른 사용자를 입력했을경우
        //초기값이 null이 아닌경우
        if (this.selected_tmp != null) {
          if (sessionStorage.getItem("accessToken") != null) {
            this.$http
              .post("http://211.109.53.216:20000/assign/delete-assign/", {
                contentid: sessionStorage.contentid,
                token: sessionStorage.accessToken,
                memberid: this.selected_tmp.memberid
              })
              .then(res => {
                if (this.checkToken(res.data)) {
                  this.selected_tmp = null;
                }
              });
          } else {
            alert("잘못된 접근입니다.");
            this.session_checked = false;
            this.$router.push("/");
          }
          if (sessionStorage.getItem("accessToken") != null) {
            this.$http
              .post("http://211.109.53.216:20000/assign/create-assign/", {
                contentid: sessionStorage.contentid,
                token: sessionStorage.accessToken,
                memberid: title.memberid
              })
              .then(res => {
                if (this.checkToken(res.data)) {
                  this.selected_tmp = title;
                }
              });
          } else {
            alert("잘못된 접근입니다.");
            this.session_checked = false;
            this.$router.push("/");
          }
        } else {
          //초기값이 null인경우
          if (sessionStorage.getItem("accessToken") != null) {
            this.$http
              .post("http://211.109.53.216:20000/assign/create-assign/", {
                contentid: sessionStorage.contentid,
                token: sessionStorage.accessToken,
                memberid: title.memberid
              })
              .then(res => {
                if (this.checkToken(res.data)) {
                  this.selected_tmp = title;
                }
              });
          } else {
            alert("잘못된 접근입니다.");
            this.session_checked = false;
            this.$router.push("/");
          }
        }
      }
    },

    //코멘트
    getComments() {
      if (sessionStorage.getItem("accessToken") != null) {
        this.$http
          .post("http://211.109.53.216:20000/comment/checkcomment/", {
            contentid: sessionStorage.contentid,
            token: sessionStorage.accessToken
          })
          .then(res => {
            if (this.checkToken(res.data)) {
              this.comments = res.data;
            }
          });
      } else {
        alert("잘못된 접근입니다.");
        this.session_checked = false;
        this.$router.push("/");
      }
    },
    addComment(cmt_content) {
      if(this.doubleSubmitCheck()) return;
      if (sessionStorage.getItem("accessToken") != null) {
        if (cmt_content.length > 0) {
          this.$http
            .post("http://211.109.53.216:20000/comment/create-comment/", {
              comcomment: cmt_content,
              memberid: sessionStorage.uid,
              contentid: sessionStorage.contentid,
              token: sessionStorage.accessToken
            })
            .then(res => {
              if (this.checkToken(res.data)) {
                this.getComments();
                this.cmt_content = "";
              }
            });
        }
      } else {
        alert("잘못된 접근입니다.");
        this.session_checked = false;
        this.$router.push("/");
      }
      this.resetSubmitFlag()
    },
    delComment(comment_id) {
      if (sessionStorage.getItem("accessToken") != null) {
        this.$http
          .post("http://211.109.53.216:20000/comment/delete-comment/", {
            comnumber: comment_id,
            memberid: sessionStorage.uid,
            token: sessionStorage.accessToken
          })
          .then(res => {
            if (this.checkToken(res.data)) {
              this.getComments();
            }
          });
      } else {
        alert("잘못된 접근입니다.");
        this.session_checked = false;
        this.$router.push("/");
      }
    },

    //체크리스트
    getCheckLists() {
      if (sessionStorage.getItem("accessToken") != null) {
        this.$http
          .post("http://211.109.53.216:20000/checklist/search-checklist/", {
            contentid: sessionStorage.contentid,
            token: sessionStorage.accessToken
          })
          .then(res => {
            if (this.checkToken(res.data)) {
              this.checklists = res.data;
            }
          });
      } else {
        alert("잘못된 접근입니다.");
        this.session_checked = false;
        this.$router.push("/");
      }
    },
    addCheckList(ckl_content) {
      if(this.doubleSubmitCheck()) return;
      if (sessionStorage.getItem("accessToken") != null) {
        if (ckl_content.length > 0) {
          this.$http
            .post("http://211.109.53.216:20000/checklist/create-checklist/", {
              contentid: sessionStorage.contentid,
              listname: ckl_content,
              token: sessionStorage.accessToken
            })
            .then(res => {
              if (this.checkToken(res.data)) {
                this.getCheckLists();
                this.ckl_content = "";
              }
            });
        }
      } else {
        alert("잘못된 접근입니다.");
        this.session_checked = false;
        this.$router.push("/");
      }
      this.resetSubmitFlag()
    },
    delCheckList(checklist_id) {
      if (sessionStorage.getItem("accessToken") != null) {
        this.$http
          .post("http://211.109.53.216:20000/checklist/delete-checklist/", {
            listnumber: checklist_id,
            token: sessionStorage.accessToken
          })
          .then(res => {
            if (this.checkToken(res.data)) {
              this.getCheckLists();
            }
          });
      } else {
        alert("잘못된 접근입니다.");
        this.session_checked = false;
        this.$router.push("/");
      }
    },

    //스케줄
    getScehdule() {
      if (sessionStorage.getItem("accessToken") != null) {
        this.$http
          .post("http://211.109.53.216:20000/calender/search-calender/", {
            contentid: sessionStorage.contentid,
            token: sessionStorage.accessToken
          })
          .then(res => {
            if (this.checkToken(res.data)) {
              this.scehdules = res.data;
              this.$emit("get-basedata");
            }
          });
      } else {
        alert("잘못된 접근입니다.");
        this.session_checked = false;
        this.$router.push("/");
      }
    },

    delSchedule(scehdule_id) {
      if (sessionStorage.getItem("accessToken") != null) {
        this.$http
          .post("http://211.109.53.216:20000/calender/delete-calender/", {
            contentid: sessionStorage.contentid,
            token: sessionStorage.accessToken,
            indexnumber: scehdule_id
          })
          .then(res => {
            if (this.checkToken(res.data)) {
              this.getScehdule();
            }
          });
      } else {
        alert("잘못된 접근입니다.");
        this.session_checked = false;
        this.$router.push("/");
      }
    },

    //값 수정을 위한 함수
    setNameState() {
      this.nameState = !this.nameState;
    },
    setSubjectState() {
      this.subjectState = !this.subjectState;
    },

    updateName() {
      this.updateContent();
      this.setNameState();
    },

    updateInfo() {
      this.updateContent();
      this.setSubjectState();
    },

    updateContent() {
      if (sessionStorage.getItem("accessToken") != null) {
        this.$http
          .post("http://211.109.53.216:20000/content/update-content/", {
            contentid: sessionStorage.contentid,
            token: sessionStorage.accessToken,
            contentname: this.contentname,
            contentinfo: this.contentinfo,
            contentstate: "1"
          })
          .then(res => {
            if (this.checkToken(res.data)) {
              this.getContent();
            }
          });
      } else {
        alert("잘못된 접근입니다.");
        this.session_checked = false;
        this.$router.push("/");
      }
    },

    resetState() {
      this.nameState = false;
      this.subjectState = false;
    },
    delContent(){
      if (sessionStorage.getItem("accessToken") != null) {
        this.$http
          .post("http://211.109.53.216:20000/content/delete-content/", {
            contentid: sessionStorage.contentid,
            token: sessionStorage.accessToken
          })
          .then(res => {
            if (this.checkToken(res.data)) {
              this.$bvModal.hide('ContDelCheck')
              this.$bvModal.hide('contentForm')
              this.$emit("get-section");
            }
          });
      } else {
        alert("잘못된 접근입니다.");
        this.session_checked = false;
        this.$router.push("/");
      }
    }
  },
  mounted() {},

  components: {
    CommentList: CommentList,
    Checklist: Checklist,
    ScehduleList: ScehduleList,
    createScehdule: createScehdule,
    Multiselect
  }
};
</script>