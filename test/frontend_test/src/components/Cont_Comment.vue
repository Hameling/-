<template>
  <div>
    <ul v-for="(comment, i) in comments" :key="i" class="list-unstyled">
      <li>
        {{comment.memberid}}: {{comment.comcomment}}
        <span v-if="todo.id != null" v-on:click="delTodo(todo.id)" class="close" aria-hidden="true">&times;</span>
        <span v-else v-on:click="delTodo(i)" class="close" aria-hidden="true">&times;</span>
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