<template>
  <!--routing 시작부분 -->
  <div id="content-wrapper">
    <div class="container">
     <div class="mx-auto 5grid-layout">
        <div class="card-body 5grid-layout">
            <div class="row">
              <div class="2u leftcontent">
              <router-link to="">
                <ol class="breadcrumb">
                  <li class="breadcrumb-item">
                    <a href="#">Create New Session</a>
                  </li>
                </ol>
              </router-link>
              </div>
            </div>
          </div>
          <!--프로젝트 목록 구역 끝-->

          <div class="4u sidebar1">
            <!--일정체크 구역-->
            <div class="row">
              <div class="col-md-12">
                <ol class="breadcrumb">
                  <li class="breadcrumb-item">
                    <a href="#">Calender Check</a>
                  </li>
                </ol>
                <div class="column">
                  <router-view/>
                </div>
              </div>
            </div>
          </div>

          <div class="col-md-3">
            <!--할당된 작업-->
            <div class="row">
              <div class="col-md-11 offset-md-1">
                <ol class="breadcrumb">
                  <li class="breadcrumb-item">
                    <a href="#">Assigned Tasks</a>
                  </li>
                </ol>
                <div class="col-md-10 offset-md-1">
                  <!--프로젝트 02-->
                  <router-link to="Assigned01">  
                    <div class="card text-white bg-danger o-hidden h-100">
                      <div class="card-body">
                        <div class="card-body-icon">
                          <i class="fas fa-fw fa-comments"></i>
                        </div>
                        <div>
                          <a class="text-white">Assigned 01</a>
                        </div>
                      </div>
                    </div>
                  </router-link>
                </div>
              </div>
            </div>
          <!--할당된 작업 끝-->
        </div>
      </div>

      <!-- /.container-fluid -->

      <!-- Sticky Footer -->
      <footer class="sticky-footer">
        <div class="container my-auto">
          <div class="copyright text-center my-auto">
            <span>Copyright © Your Website 2019</span>
          </div>
        </div>
      </footer>
    </div>
    <!-- /.content-wrapper -->
  </div>
  <!-- /#wrapper router 끝-->
</template>

<script>
export default {
  name: "workspace"
};
</script>