<template>
  <div>
    <ul v-for="(comment, i) in comments" :key="i" class="list-unstyled">
      <!-- 내가 쓴 코멘트 일때 -->
      <li v-if="comment.memberid == memberid" style="background: #d1d3d4; text-align: right;">
        {{comment.memberid}} : {{comment.comcomment}} [{{formattingTime(comment.commenttime)}}]
        <span v-on:click="delComment(comment.comnumber)" class="close" aria-hidden="true">&times;</span>
      </li>
      <!-- 다른 사람이 쓴 코멘트 일때 -->
      <li v-else style="background: rgba(158, 170, 177, 0.9); text-align: left;">
        {{comment.memberid}} : {{comment.comcomment}} [{{formattingTime(comment.commenttime})}]
      </li>
    </ul>
  </div>
</template> 

<script>
export default {
  name: 'CommentList',
  props: ['comments'],
  data:() =>({
    memberid : sessionStorage.uid
  }),
  methods: {
    delComment (comment) {
      this.$emit('del-comment', comment)
    },
    formattingTime(time){
      var tmp = time.substring(0, time.length - 3)
      return tmp
    }
  }
}
</script>