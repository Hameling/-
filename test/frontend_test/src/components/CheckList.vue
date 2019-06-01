<template>
  <div>
    <ul v-for="(checklist, i) in checklists" :key="i" class="list-unstyled">
      <li v-on:click='checked'>
       {{checklist.listname}}
       <span v-on:click="delCheckList(checklist.listnumber)" class="close" aria-hidden="true">&times;</span>
        <!--<span v-if="checklist.listnumber != null" v-on:click="delCheckList(checklist.listnumber)" class="close" aria-hidden="true">&times;</span>
        <span v-else v-on:click="delCheckList(i)" class="close" aria-hidden="true">&times;</span>-->
      </li>
    </ul>
  </div>
</template> 

<script>
export default {
  name: 'Checklist',
  props: ['checklists'],
  methods: {
    delCheckList (checklist) {
      this.$emit('del-checklist', checklist)
    },
    checked: function (event){

    }
  }
}
</script>