System.register(["./_plugin-vue_export-helper-legacy-DKqiQNGd.js","./index-legacy-Bq7BrVzS.js"],(function(n,e){"use strict";var t,i,o,r,u,c,a;return{setters:[function(n){t=n._},function(n){i=n.f,o=n.x,r=n.c,u=n.k,c=n.h,a=n.m}],execute:function(){var e=document.createElement("style");e.textContent=".btn{margin:0 20px 20px 0}\n",document.head.appendChild(e);var l={style:{padding:"30px"}};n("default",t({mixins:[],components:{},data:function(){return{mainWindows:"main",targetWindows:"myNewWindows"}},mounted:function(){},setup:function(){},methods:{create_window:function(n){pywebview.api.invoke("ipyweb/create_window",{name:n||this.targetWindows,url:"https://www.baidu.com",debug:!1}).then((function(n){console.error(n)}))},set_title:function(n){pywebview.api.invoke("ipyweb/set_title@"+n,"新的标题").then((function(n){console.error(n)}))},change_url:function(n,e){pywebview.api.invoke("ipyweb/change_url@"+n,e).then((function(n){console.error(n)}))},load_html:function(n,e){pywebview.api.invoke("ipyweb/load_html@"+n,e).then((function(n){console.error(n)}))},hide:function(n){pywebview.api.invoke("ipyweb/hide@"+n).then((function(n){console.error(n)}))},show:function(n){pywebview.api.invoke("ipyweb/show@"+n).then((function(n){console.error(n)}))},destroy:function(n){pywebview.api.invoke("ipyweb/destroy@"+n).then((function(n){console.error(n)}))},minimize:function(n){pywebview.api.invoke("ipyweb/minimize@"+n).then((function(n){console.error(n)}))},toggle_fullscreen:function(n){pywebview.api.invoke("ipyweb/toggle_fullscreen@"+n).then((function(n){console.error(n)}))},move:function(n){pywebview.api.invoke("ipyweb/move@"+n,{x:10,y:30}).then((function(n){console.error(n)}))},resize:function(n){pywebview.api.invoke("ipyweb/resize@"+n,{width:800,height:600}).then((function(n){console.error(n)}))},open_file_dialog:function(n){pywebview.api.invoke("ipyweb/open_file_dialog@"+n,{file_type:"Image Files (*.bmp;*.jpg;*.gif)"}).then((function(n){console.error(n)}))},save_file_dialog:function(n){pywebview.api.invoke("ipyweb/save_file_dialog@"+n,{directory:"/",filename:"file.txt"}).then((function(n){console.error(n)}))}}},[["render",function(n,e,t,s,f,p){var w=i("el-button");return c(),o("div",l,[r(w,{type:"primary",class:"btn",onClick:e[0]||(e[0]=function(n){return p.create_window(f.targetWindows)})},{default:u((function(){return[a("打开新窗口")]})),_:1}),r(w,{type:"primary",class:"btn",onClick:e[1]||(e[1]=function(n){return p.set_title(f.mainWindows)})},{default:u((function(){return[a("改变主窗口标题")]})),_:1}),r(w,{type:"primary",class:"btn",onClick:e[2]||(e[2]=function(n){return p.set_title(f.targetWindows)})},{default:u((function(){return[a("改变新窗口标题")]})),_:1}),r(w,{type:"primary",class:"btn",onClick:e[3]||(e[3]=function(n){return p.change_url(f.targetWindows,"https://www.qq.com")})},{default:u((function(){return[a(" 在打开的新窗口加载URL ")]})),_:1}),r(w,{type:"primary",class:"btn",onClick:e[4]||(e[4]=function(n){return p.load_html(f.targetWindows,"<h1>This is dynamically loaded HTML</h1>")})},{default:u((function(){return[a(" 在打开的新窗口加载HTML ")]})),_:1}),r(w,{type:"primary",class:"btn",onClick:e[5]||(e[5]=function(n){return p.hide(f.targetWindows)})},{default:u((function(){return[a("隐藏新窗口")]})),_:1}),r(w,{type:"primary",class:"btn",onClick:e[6]||(e[6]=function(n){return p.show(f.targetWindows)})},{default:u((function(){return[a("显示新窗口")]})),_:1}),r(w,{type:"primary",class:"btn",onClick:e[7]||(e[7]=function(n){return p.destroy(f.targetWindows)})},{default:u((function(){return[a("销毁新窗口")]})),_:1}),r(w,{type:"primary",class:"btn",onClick:e[8]||(e[8]=function(n){return p.minimize(f.mainWindows)})},{default:u((function(){return[a("最小化主窗口")]})),_:1}),r(w,{type:"primary",class:"btn",onClick:e[9]||(e[9]=function(n){return p.toggle_fullscreen(f.mainWindows)})},{default:u((function(){return[a("主窗口切换全屏")]})),_:1}),r(w,{type:"primary",class:"btn",onClick:e[10]||(e[10]=function(n){return p.move(f.mainWindows)})},{default:u((function(){return[a("移动主窗口")]})),_:1}),r(w,{type:"primary",class:"btn",onClick:e[11]||(e[11]=function(n){return p.resize(f.mainWindows)})},{default:u((function(){return[a("设置主窗口尺寸")]})),_:1}),r(w,{type:"primary",class:"btn",onClick:e[12]||(e[12]=function(n){return p.open_file_dialog(f.mainWindows)})},{default:u((function(){return[a("打开文件")]})),_:1}),r(w,{type:"primary",class:"btn",onClick:e[13]||(e[13]=function(n){return p.save_file_dialog(f.mainWindows)})},{default:u((function(){return[a("保存文件")]})),_:1})])}]]))}}}));
