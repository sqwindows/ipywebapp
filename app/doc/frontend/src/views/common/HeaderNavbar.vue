<template>

  <el-affix :offset="0">
    <el-menu
        default-active="/"
        mode="horizontal"
        :ellipsis="false"
        :router="true"
    >
      <el-menu-item index="/">
        <img
            style="width: 30px; margin-right: 5px"
            src="@/assets/logo.png"
            :alt="header.title||'[ipyweb]一个快速启动多服务python框架'"
        />
        <el-text class="mx-1" size="large">{{ header.title || '[ipyweb]一个快速启动多服务python框架' }}</el-text>
      </el-menu-item>
      <div class="flex-grow"/>
      <!--      <el-menu-item index="/home/down">下载</el-menu-item>-->
      <el-sub-menu index="2">
        <template #title>关于</template>
        <el-menu-item index="/example/windows">例子</el-menu-item>
      </el-sub-menu>
    </el-menu>
  </el-affix>
</template>

<script>
export default {
  name: "HeaderNavbar",
  props: {
    header: {
      type: Object,
      default() {
        return {
          title: ''
        }
      }
    }
  }
}
</script>

<style scoped>
.flex-grow {
  flex-grow: 1;
}
</style>