<template>
  <div style="padding: 30px;">
    <el-button type="primary" class="btn" @click="create_window(targetWindows)">打开新窗口</el-button>
    <el-button type="primary" class="btn" @click="set_title(mainWindows)">改变主窗口标题</el-button>
    <el-button type="primary" class="btn" @click="set_title(targetWindows)">改变新窗口标题</el-button>
    <el-button type="primary" class="btn" @click="change_url(targetWindows,'https://www.qq.com')">
      在打开的新窗口加载URL
    </el-button>
    <el-button type="primary" class="btn" @click="load_html(targetWindows,'<h1>This is dynamically loaded HTML</h1>')">
      在打开的新窗口加载HTML
    </el-button>
    <el-button type="primary" class="btn" @click="hide(targetWindows)">隐藏新窗口</el-button>
    <el-button type="primary" class="btn" @click="show(targetWindows)">显示新窗口</el-button>
    <el-button type="primary" class="btn" @click="destroy(targetWindows)">销毁新窗口</el-button>
    <el-button type="primary" class="btn" @click="minimize(mainWindows)">最小化主窗口</el-button>
    <el-button type="primary" class="btn" @click="toggle_fullscreen(mainWindows)">主窗口切换全屏</el-button>
    <el-button type="primary" class="btn" @click="move(mainWindows)">移动主窗口</el-button>
    <el-button type="primary" class="btn" @click="resize(mainWindows)">设置主窗口尺寸</el-button>
    <el-button type="primary" class="btn" @click="open_file_dialog(mainWindows)">打开文件</el-button>
    <el-button type="primary" class="btn" @click="save_file_dialog(mainWindows)">保存文件</el-button>
  </div>
</template>

<script>

export default {
  mixins: [],
  components: {},
  data() {
    return {
      mainWindows: 'main',
      targetWindows: 'myNewWindows'
    }
  },
  mounted() {

  },
  setup() {

  },
  methods: {
    create_window(windows) {
      pywebview.api.invoke('ipyweb/create_window', {
        'name': windows || this.targetWindows,
        'url': 'https://www.baidu.com',
        'debug': false
      }).then(response => {
        console.error(response)
      })
    },
    set_title(windows) {
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
      pywebview.api.invoke('ipyweb/load_html@' + windows, html).then(response => {
        console.error(response)
      })
    },
    hide(windows) {
      pywebview.api.invoke('ipyweb/hide@' + windows).then(response => {
        console.error(response)
      })
    },
    show(windows) {
      pywebview.api.invoke('ipyweb/show@' + windows).then(response => {
        console.error(response)
      })
    },
    destroy(windows) {
      pywebview.api.invoke('ipyweb/destroy@' + windows).then(response => {
        console.error(response)
      })
    },
    minimize(windows) {
      pywebview.api.invoke('ipyweb/minimize@' + windows).then(response => {
        console.error(response)
      })
    },
    toggle_fullscreen(windows) {
      pywebview.api.invoke('ipyweb/toggle_fullscreen@' + windows).then(response => {
        console.error(response)
      })
    },
    move(windows) {
      pywebview.api.invoke('ipyweb/move@' + windows, {x: 10, y: 30}).then(response => {
        console.error(response)
      })
    },
    resize(windows) {
      pywebview.api.invoke('ipyweb/resize@' + windows, {width: 800, height: 600}).then(response => {
        console.error(response)
      })
    },
    open_file_dialog(windows) {
      pywebview.api.invoke('ipyweb/open_file_dialog@' + windows, {file_type: 'Image Files (*.bmp;*.jpg;*.gif)'}).then(response => {
        console.error(response)
      })
    },
    save_file_dialog(windows) {
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
