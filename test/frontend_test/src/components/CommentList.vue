<template>
  <div>
    <ul v-for="(comment, i) in comments" :key="i" class="list-unstyled">
      <!-- 내가 쓴 코멘트 일때 -->
      <li v-if="comment.memberid == memberid" class="my-comment-border" v-bind:id="'mycomment'+i">
        {{comment.memberid}} : {{comment.comcomment}} [{{formattingTime(comment.commenttime)}}]
        <span
          v-on:click="delComment(comment.comnumber)"
          class="close"
          aria-hidden="true"
        >&times;</span>

        <!-- popover 시작부분 -->
        <b-popover v-bind:target="'mycomment'+i">
          <div>
            <p>Comment를 삭제하시겠습니까?</p>
            <!-- 디자인 수정요망 -->
            <div class="row">
              <b-button class="col-md-5 col-md-offset-1" variant="primary">Ok</b-button>
              <b-button class="col-md-5 col-md-offset-1" variant="danger">Cancel</b-button>
            </div>
          </div>
        </b-popover>
      </li>
      <!-- 다른 사람이 쓴 코멘트 일때 -->
      <li
        v-else
        class="other-comment-border"
      >{{comment.memberid}} : {{comment.comcomment}} [{{formattingTime(comment.commenttime)}}]</li>
    </ul>
  </div>
</template> 

<script>
export default {
  name: "CommentList",
  props: ["comments"],
  data: () => ({
    memberid: sessionStorage.uid
  }),
  methods: {
    delComment(comment) {
      this.$emit("del-comment", comment);
    },
    formattingTime(time) {
      var tmp = time.substring(0, time.length - 3);
      return tmp;
    }
  }
};
</script>