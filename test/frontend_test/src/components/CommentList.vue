<template>
  <div>
    <ul v-for="(comment, i) in comments" :key="i" class="list-unstyled">
      <li>
        {{comment.memberid}} : {{comment.comcomment}} [{{comment.commenttime}}]
        <span v-on:click="delComment(comment.comnumber)" class="close" aria-hidden="true">&times;</span>
        <!--<span v-if="comment != null" v-on:click="delComment(comnumber)" class="close" aria-hidden="true">&times;</span>
          <span v-else v-on:click="delComment(i)" class="close" aria-hidden="tru">&times;</span>-->
      </li>
    </ul>
  </div>
</template> 

<script>
export default {
  name: 'CommentList',
  props: ['comments'],
  methods: {
    delComment (comment) {
      this.$emit('del-comment', comment)
    }
  }
}
</script>