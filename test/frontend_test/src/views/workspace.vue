<template>
  <!--routing 시작부분 -->
  <div id="content-wrapper">
    <div class="container-fluid">
      <div class="container show-grid" style="width: 1080px;">
        <div class="row">
          <div class="col-md-3">
            <!--프로젝트 목록 구역 시작-->
            <div class="row">
              <div class="col-md-11">
                <ol class="breadcrumb">
                  <li class="breadcrumb-item">
                    <a href="#">Project Space</a>
                  </li>
                </ol>
                <div class="column">
                  <div class="col-md-10 offset-md-1">
                    <div class="card text-white bg-primary o-hidden h-100">
                      <div class="card-body">
                        <div class="card-body-icon">
                          <i class="fas fa-fw fa-comments"></i>
                        </div>
                        <div>Project selection area</div>
                      </div>
                      <a class="card-footer text-white clearfix small z-1">
                        <!--프로젝트 생성 페이지 링크-->
                        <span class="float-left">Create New Project</span>
                        <span class="float-right">
                          <i class="fas fa-angle-right"></i>
                        </span>
                      </a>
                    </div>
                  </div>
                </div>
                <div>
                  <br>
                </div>
                <!--카드와 카드 사이줄-->
                <div class="col-md-10 offset-md-1">
                  <!--프로젝트 01-->
                  <router-link to="/project">
                    <div class="card text-white bg-primary o-hidden h-100">
                      <div class="card-body">
                        <div class="card-body-icon">
                          <i class="fas fa-fw fa-comments"></i>
                        </div>
                        <div>
                          <!--<a class="text-white" href="#">Project 01</a>-->
                          <a class="text-white">Project 01</a>
                        </div>
                      </div>
                    </div>
                  </router-link>
                </div>
                <div>
                  <br>
                </div>
                <!--카드와 카드 사이줄-->
                <div class="col-md-10 offset-md-1">
                  <!--프로젝트 02-->
                  <router-link to="/content">
                    <div class="card text-white bg-primary o-hidden h-100">
                      <div class="card-body">
                        <div class="card-body-icon">
                          <i class="fas fa-fw fa-comments"></i>
                        </div>
                        <div>
                          <a class="text-white">Project 02</a>
                        </div>
                      </div>
                    </div>
                  </router-link>
                </div>
                
                


              </div>
            </div>
          </div>
          <!--프로젝트 목록 구역 끝-->

          <div class="col-md-6">
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