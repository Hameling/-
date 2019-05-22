<template>
  <div>
    <ul v-for="(comment, i) in comments" :key="i" class="list-unstyled">
      <li>
        {{comment.comnumber}}.{{comment.memberid}}: {{comment.comcomment}} [{{comment.commenttime}}]
        <!--<span v-if="comment != null" v-on:click="delComment(comcoment)" class="close" aria-hidden="true">&times;</span>
        <span v-else v-on:click="delComment(i)" class="close" aria-hidden="true">&times;</span>-->
      </li>
    </ul>
  </div>
</template> 

<script>
export default {
  name: 'cComment',
  props: ['comments'],
  methods: {
    delComment (comment) {
      this.$emit('del-comment', comment)
    }
  }
}
</script>