<template>
  <CommonBase>
    <template #lefter>
      <IndexMenu @changePath="changePath"/>
    </template>
    <template #righter>
      <div class="anchorBox" v-if="readmeStatus">
        <MdCatalog :editorId="readmeId" class="MdCatalog" :scrollElement="scrollElement" @onClick="goAnchor($event)"/>
      </div>
    </template>
    <template #center>
      <div v-loading="loading" style="min-height:50vh">
        <MdPreview :editorId="readmeId" v-if="readmeContent" @onHtmlChanged="onHtmlChanged" :modelValue="readmeContent"/>
      </div>
    </template>
  </CommonBase>

</template>

<script setup>
import {MdPreview, MdCatalog} from 'md-editor-v3';

import CommonBase from "@/views/common/CommonBase.vue";
import IndexMenu from "@/views/home/index/IndexMenu.vue"
import {useRoute} from "vue-router";
import {ElMessage} from 'element-plus'
import '@/assets/preview.css';
</script>
<script>

export default {
  mixins: [],
  components: {
    CommonBase,
    IndexMenu
  },
  data() {
    return {
      readmeId: 'editorId',
      readmeStatus: false,
      readmeContent: ``,
      readmePath: 'install.intro',
      loading: true,
      scrollElement: document.documentElement
    };
  },
  mounted() {
    this.start()
  },
  setup() {

  },
  methods: {
    start(path = '', title = '') {
      path = path || useRoute().params.path
      this.readmeStatus = false
      this.http(this).get({
        url: 'https://saas.maoren.la/app/ipyweb/home/readme',
        data: {path: path}
      }).then(res => {
        if (res.data.md) {
          this.readmeStatus = true
          this.readmeContent = res.data.md
        } else {
          this.readmeStatus = false
          this.readmeContent = `未能读取 [${title}] 文档请重试`
        }

      }).catch(err => {
        ElMessage({
          message: err,
          type: 'error',
        })
      })
    },
    changePath(path, title) {
      this.start(path, title)
    },
    goAnchor(event) {
      this.anchor(event.target.textContent)
    },
    anchor(anchorName) {
      let anchorElement = document.getElementById(anchorName);
      if (anchorElement) {
        anchorElement.scrollIntoView();
      }
    },
    onHtmlChanged(html){

    }
  }
};
</script>
<style scoped>

.anchorBox {
  margin: 20px;
  padding: 0 10px;
  border-left: 1px solid #eee;
}


</style>
  