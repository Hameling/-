<template>
  <!--routing 시작부분 -->
  <div id="content-wrapper">
    <!--Modal 선언부 -->
    <ContentForm v-on:get-basedata="getBaseData"/>

    <div class="container">
      <div class="mx-auto 5grid-layout height: 100%">
        <div class="row">
          <div class="2u">
            <section>
              <!--할당된 작업-->
              <div class="row">
                <div class="col-md-11">
                  <ol class="breadcrumb">
                    <li class="header-item">
                      <a>Assigned Content</a>
                    </li>
                  </ol>
                  <AssignList v-bind:assigns="assignList"></AssignList>
                </div>
              </div>
            </section>
          </div>

          <div class="8u">
            <section>
              <div class="column">
                <!--기존 라우트 뷰 영역
                <router-view/>-->
                <div class="card mb-3">
                  <vue-cal
                    style="height: 600px "
                    class="vuecal--blue-theme"
                    :time-from="7*60"
                    :time-to="22*60"
                    :time-step="30"
                    :disable-views="['years', 'year', 'day']"
                    default-view="month"
                    :events="events"
                    events-on-month-view="short"
                    :on-event-click="onEventClick"
                  ></vue-cal>
                  <!-- <div class="card-footer small text-muted"></div> -->
                </div>
              </div>
            </section>
          </div>

          <!--할당된 작업 끝-->
        </div>
      </div>
    </div>

    <!-- /.container-fluid -->

    <!-- Sticky Footer -->

    <!-- /.content-wrapper -->
  </div>
  <!-- /#wrapper router 끝-->
</template>

<script>
import TitleList from "@/components/TitleList";
import AssignList from "@/components/AssignList";
import ContentForm from "@/components/modal/ContentForm";
import VueCal from "vue-cal";
import "../../public/css/vuecal.css";
import { bus } from "@/eventbus";
export default {
  name: "workspace",
  data: () => ({
    enrollList: [],
    assignList: [],
    events: []
  }),
  methods: {
    //workspace 첫화면에 보여지는 정보를 불러오는 메소드
    getBaseData() {
      if (sessionStorage.getItem("accessToken") != null) {
        this.$http
          .post("http://211.109.53.216:20000/member/search-member/", {
            token: sessionStorage.accessToken
          })
          .then(res => {
            if (this.checkToken(res.data[0])) {
              this.enrollList = res.data[0].enrollTitle;
              this.assignList = res.data[0].assignContent;
              this.$store.commit("updateTitleList", this.enrollList)
              
              //이하 일정 정보 events에 저장
              this.events = []
              for(var i in this.assignList){
                for(var j in this.assignList[i].calender){
                  this.events.push({
                    "contentid":this.assignList[i].contentid,
                    "start":this.assignList[i].calender[j].starttime,
                    "end":this.assignList[i].calender[j].duetime,
                    "title":this.assignList[i].calender[j].calendername
                  })
                }
              }
            }
          });
      } else {
        alert("잘못된 접근입니다.");
        this.session_checked = false;
        this.$router.push("/");
      }
    },

    //Calendar 일정 클릭시 해당 Content Modal 표시 메소드
    onEventClick(event) {
      this.$store.commit('selectedContent', event.contentid)
      this.$bvModal.show('contentForm')
    }
  },
  created() {
    bus.$on("get-basedata", () => {
      this.getBaseData();
    });
  },

  mounted() {
    this.$nextTick(() => {
      this.getBaseData();
    });
  },
  components: {
    TitleList: TitleList,
    AssignList: AssignList,
    ContentForm: ContentForm,
    VueCal
  }
};
</script>