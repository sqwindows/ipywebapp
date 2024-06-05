<template>

  <CommonBase>
    <template #lefter>
      <caseMenu @changePath="changePath"/>
    </template>
    <template #righter>

    </template>
    <template #center>
      <div style="min-height:50vh;padding:30px">
        陆续完善中
      </div>
    </template>
  </CommonBase>

</template>

<script>

import CommonBase from "@/views/common/CommonBase.vue";
import caseMenu from "@/views/home/example/caseMenu.vue";
import {ElMessage} from 'element-plus'

export default {
  mixins: [],
  components: {
    CommonBase,
    caseMenu
  },
  data() {
    return {
      mainWindows: 'main',
      targetWindows: 'myNewWindows',
      pywebviewready: false
    }
  },
  mounted() {
    this.ready()
  },
  setup() {

  },
  methods: {
    ready() {
      window.addEventListener('pywebviewready', function () {
        this.pywebviewready = true
      })
    },
    check() {
      if (!this.pywebviewready)
        ElMessage({
          message: '请使用ipyweb窗口软件打开',
          type: 'error',
        })
      return this.pywebviewready
    },
    create_window(windows) {
      if (!this.check())
        return

      pywebview.api.invoke('ipyweb/create_window', {
        'name': windows || this.targetWindows,
        'url': 'https://www.baidu.com',
        'debug': false
      }).then(response => {
        console.error(response)
      })
    },
    set_title(windows) {
      if (!this.check())
        return
      pywebview.api.invoke('ipyweb/set_title@' + windows, '新的标题').then(response => {
        console.error(response)
      })
    },
    change_url(windows, url) {
      pywebview.api.invoke('ipyweb/change_url@' + windows, url).then(response => {
        console.error(response)
      })
    },
    load_html(windows, html) {
      if (!this.check())
        return
      pywebview.api.invoke('ipyweb/load_html@' + windows, html).then(response => {
        console.error(response)
      })
    },
    hide(windows) {
      if (!this.check())
        return
      pywebview.api.invoke('ipyweb/hide@' + windows).then(response => {
        console.error(response)
      })
    },
    show(windows) {
      if (!this.check())
        return
      pywebview.api.invoke('ipyweb/show@' + windows).then(response => {
        console.error(response)
      })
    },
    destroy(windows) {
      if (!this.check())
        return
      pywebview.api.invoke('ipyweb/destroy@' + windows).then(response => {
        console.error(response)
      })
    },
    minimize(windows) {
      if (!this.check())
        return
      pywebview.api.invoke('ipyweb/minimize@' + windows).then(response => {
        console.error(response)
      })
    },
    toggle_fullscreen(windows) {
      if (!this.check())
        return
      pywebview.api.invoke('ipyweb/toggle_fullscreen@' + windows).then(response => {
        console.error(response)
      })
    },
    move(windows) {
      if (!this.check())
        return
      pywebview.api.invoke('ipyweb/move@' + windows, {x: 10, y: 30}).then(response => {
        console.error(response)
      })
    },
    resize(windows) {
      if (!this.check())
        return
      pywebview.api.invoke('ipyweb/resize@' + windows, {width: 800, height: 600}).then(response => {
        console.error(response)
      })
    },
    open_file_dialog(windows) {
      if (!this.check())
        return
      pywebview.api.invoke('ipyweb/open_file_dialog@' + windows, {file_type: 'Image Files (*.bmp;*.jpg;*.gif)'}).then(response => {
        console.error(response)
      })
    },
    save_file_dialog(windows) {
      if (!this.check())
        return
      pywebview.api.invoke('ipyweb/save_file_dialog@' + windows, {
        directory: '/',
        filename: 'file.txt'
      }).then(response => {
        console.error(response)
      })
    },
  }
};
</script>
<style>
.btn {
  margin: 0 20px 20px 0
}
</style>
