<template>
  <div class="card mb-3">
    <!--<div class="card-header">
      <i class="fas fa-chart-area"></i>
      Calendar Check
    </div>-->
      <vue-cal
        style="height: 500px"
        :time-from="7*60"
        :time-to="22*60"
        :time-step="30"
        :disable-views="['years', 'year', 'day']"
        default-view="month"
        :events="events"
        events-on-month-view="short"
        :on-event-click="onEventClick"
      ></vue-cal>
    <div class="card-footer small text-muted"></div>
  </div>
</template>

<script>
import VueCal from "vue-cal";
import "vue-cal/dist/vuecal.css";
export default {
  data:() =>({
    events: []
  }),
  methods: {
    onEventClick(){
      
    }
  },
  components: { VueCal }
};
</script>