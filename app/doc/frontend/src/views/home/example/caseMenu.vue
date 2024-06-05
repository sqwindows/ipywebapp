<template>

  <div class="caseMenu">
    <el-menu :default-active="menus.actives" class="menu" :collapse="isCollapse" style="height:100vh" :router="true">
      <el-sub-menu v-for="item in menus.lists" :key="item" :index="item.name">
        <template #title>
          <el-icon v-if="item.name =='install'">
            <Lightning color="#409EFF"/>
          </el-icon>


          <span style="padding-right: 100px;">{{ item.title }}</span>
        </template>
        <el-menu-item :index="`${item.name}.${x.name}`" v-for="x in item.child" :key="x"
                      @click="changePath(`${item.name}.${x.name}`,x.title)">{{ x.title }}
        </el-menu-item>
      </el-sub-menu>

    </el-menu>


  </div>

</template>

<script>
import caseData from "@/views/home/example/CaseData";
import {ref, onMounted, onUnmounted} from 'vue';
export default {
  name: "caseMenu",
  data() {
    return {
      menus: caseData.menus,
    };
  },
  mounted() {
    window.addEventListener('resize', this.resize);
  },
  setup() {
    const isCollapse = ref(window.innerWidth < 800);
    const resize = () => {
      isCollapse.value = window.innerWidth < 800;
    }
    onMounted(() => {
      window.addEventListener('resize', resize);
    });

    onUnmounted(() => {
      window.removeEventListener('resize', resize);
    });
    return {isCollapse};
  },
  props: {},
  methods: {
    changePath(path,title) {
      this.$emit('changePath', path,title)
    }
  }


}
</script>

<style scoped>


</style>