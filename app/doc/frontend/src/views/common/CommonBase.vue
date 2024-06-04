<template>
  <header>
    <slot name="header">
      <HeaderNavbar :header="header" class="header"/>
    </slot>
  </header>
  <main>
    <el-scrollbar class="mainScrollbar" :height="container.scrollbarHeight">
      <div class="mainContainer">
        <div class="mainLefter">
          <el-scrollbar :height="container.scrollbarHeight">
            <slot name="lefter"/>
          </el-scrollbar>
        </div>
        <div :class="{ 'mainCenter':true,'mainCenterNoRight': !rightShow,'mainCenterSmallLeft':smallLeft }">
          <slot name="center"/>
        </div>
        <div class="mainRighter" v-if="rightShow">
          <slot name="righter"/>
        </div>
      </div>
    </el-scrollbar>
  </main>
  <footer>
    <slot name="footer">
      <FooterNavbar :footer="footer"/>
    </slot>
  </footer>


</template>

<script>
import HeaderNavbar from './HeaderNavbar.vue'
import FooterNavbar from './FooterNavbar.vue'
import {ref, onMounted, onUnmounted} from 'vue';

export default {
  name: "CommonBase",
  components: {
    HeaderNavbar,
    FooterNavbar
  },
  data() {
    return {
      scrollbarHeight: '95vh',

    }
  },
  setup() {
    const rightShow = ref(window.innerWidth >= 1024);
    const smallLeft = ref(window.innerWidth < 800);
    const resize = () => {
      rightShow.value = window.innerWidth >= 1024;
      smallLeft.value = window.innerWidth < 800
    }
    onMounted(() => {
      window.addEventListener('resize', resize);
    });

    onUnmounted(() => {
      window.removeEventListener('resize', resize);
    });

    return {rightShow, smallLeft};
  },
  props: {
    header: {
      type: Object,
      default() {
        return {}
      }
    },
    footer: {
      type: Object,
      default() {
        return {}
      }
    },
    container: {
      type: Object,
      default() {
        return {}
      }
    },
  },
  computed: {

    width() {
      return () => {
      }
    },
  },
  mounted() {

  },
  methods: {
    resize() {
    }
  }
}
</script>

<style scoped>
.header {
  margin: 0 auto
}

.mainScrollbar {
  height: calc(100vh - 120px);
}


.mainContainer {
}

.mainLefter {
  position: fixed;
  top: 60px;
  left: 0;
  min-width: 70px;
  max-width: 250px;
  min-height: 100vh;
  z-index: 10;
}

.mainCenter {
  padding-left: 270px;
  padding-right: 270px;
}

.mainCenterNoRight {
  padding-right: 20px
}

.mainCenterSmallLeft {
  padding-left: 80px
}

.mainRighter {
  position: fixed;
  top: 60px;
  right: 0;
  width: 250px
}


</style>