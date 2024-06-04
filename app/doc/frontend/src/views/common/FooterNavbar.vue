<template>

  <div class="footer">

  </div>

</template>

<script>
export default {
  name: "FooterNavbar",
  props: {
    footer: {
      type: Object,
      default() {
        return {}
      }
    }
  }
}
</script>

<style scoped>
.footer {
  width: 100%;
  text-align: center;

}
</style>