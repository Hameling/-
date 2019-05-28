<template>
                    <div class="col-md-10 offset-md-1">
                  <router-link to="Assigned01" v-for="(assign, i) in assigns" :key="i" class="card text-white bg-danger o-hidden h-100">  
                      <div class="card-body">
                        <div class="card-body-icon">
                          <i class="fas fa-fw fa-comments"></i>
                        </div>
                        <div>
                          <a class="text-white">{{assign.contentname}}</a>
                        </div>
                      </div>

                  </router-link>
                </div>
</template>

<script>
export default {
    name: "Assign",
    props:["assigns"]
};
</script>