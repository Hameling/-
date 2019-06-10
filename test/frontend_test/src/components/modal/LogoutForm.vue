<template>
  <b-modal id="Logout" title="Logout" hide-footer hide-header centered>
    <div class="d-block text-center">
      <h4>로그아웃 하시겠습니까?</h4>
    </div>
    <b-button class="mt-3  bg-danger "  block @click="doLogout">예</b-button>
    <b-button class="mt-3 bg-primary" block @click="$bvModal.hide('Logout')">아니오</b-button>
  </b-modal>
</template>

<script>
export default {
  name: "logout",

  methods: {
      async doLogout(){
        this.$bvModal.hide('Logout')
        await this.$store.dispatch("LOGOUT")
        this.$router.push("/");
        this.$emit('sessionCheck', false)
      }
  },
};
</script>