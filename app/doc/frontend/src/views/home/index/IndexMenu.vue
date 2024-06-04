<template>

  <div class="indexMenu">
    <el-menu default-active="install.intro" class="menu" :collapse="isCollapse" style="height:100vh">
      <el-sub-menu v-for="item in menus.lists" :key="item" :index="item.name">
        <template #title>
          <el-icon v-if="item.name =='install'">
            <Lightning color="#409EFF"/>
          </el-icon>
           <el-icon v-else-if="item.name =='framework'">
            <Setting color="#409EFF"/>
          </el-icon>
           <el-icon v-else-if="item.name =='builder'">
            <Cpu color="#409EFF"/>
          </el-icon>
           <el-icon v-else-if="item.name =='help'">
            <Warning color="#409EFF"/>
          </el-icon>
          <el-icon v-else-if="item.name =='other'">
            <ToiletPaper color="#409EFF"/>
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
import IndexData from "@/views/home/index/IndexData";
import {ref, onMounted, onUnmounted} from 'vue';
export default {
  name: "IndexMenu",
  data() {
    return {
      menus: IndexData.menus,
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
.indexMenu {


}


</style>