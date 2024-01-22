#include <ESP8266WiFi.h>

const char index_html[] PROGMEM = R"=====(<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <link href="https://fonts.googleapis.com/css?family=Roboto:100,300,400,500,700,900" rel="stylesheet">
  <link href="https://cdn.jsdelivr.net/npm/@mdi/font@4.x/css/materialdesignicons.min.css" rel="stylesheet">
  <link href="https://cdn.jsdelivr.net/npm/vuetify@2.x/dist/vuetify.min.css" rel="stylesheet">
  <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no, minimal-ui">
  <link rel="stylesheet" href="http://at.alicdn.com/t/font_1593799_o4yereoam1.css">
  <title>wifi LCX的Tank</title>
</head>
<body>
  <div id="app">
    <v-app>
      <v-app-bar
      app
      color="primary"
      dark
    >
      <div class="d-flex align-center">
        <i class="iconfont icon-car" style="font-size:200%"></i>
        <span class="ml-3 display-2">WIFI car</span>
      </div>
    </v-app-bar>

    <v-content>
        <v-container>
          <v-row class="justify-center">
            <v-col cols="6" md="4" class="text-center">
              <v-btn class="primary" x-large @click="forward()">
                <i class="iconfont icon-Uparrow" style="font-size:200%"></i>
                <span>前进</span>
              </v-btn>
            </v-col>
          </v-row>
          <v-row class="justify-center">
            <v-col cols="12" sm="2" class="text-center text-sm-right">
              <v-btn class="primary" x-large @click="left()">
                <i class="iconfont icon-Leftarrow" style="font-size:200%"></i>
                <span>左转</span>
              </v-btn>
            </v-col>
            <v-col cols="12" sm="2" class="text-center">
              <v-btn class="primary" x-large @click="stop()">
                <i class="iconfont icon-Stopit_px" style="font-size:200%"></i>
                <span>停止</span>
              </v-btn>
            </v-col>
            <v-col cols="12" sm="2" class="text-center text-sm-left">
              <v-btn class="primary" x-large @click="right()">
                 <span>右转</span>
                <i class="iconfont icon-Rightarrow" style="font-size:200%"></i>
              </v-btn>
            </v-col>
          </v-row>
          <v-row class="justify-center">
            <v-col cols="6" md="4" class="text-center">
              <v-btn class="primary" x-large @click="backward()">
                <i class="iconfont icon-Downarrow" style="font-size:200%"></i>
                <span d-flex>后退</span>
              </v-btn>
            </v-col>
          </v-row>
        </v-container>
    </v-content>
    </v-app>
  </div>

  <script src="https://cdn.jsdelivr.net/npm/vue@2.x/dist/vue.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/vuetify@2.x/dist/vuetify.js"></script>
  <script src="https://cdn.bootcss.com/axios/0.19.0-beta.1/axios.min.js"></script>
  <script>
    new Vue({
      el: '#app',
      vuetify: new Vuetify(),
      methods: {
        forward(){
          axios.get('/move?dir=F')
          .then((res)=>console.log(res.data))
          .catch(()=>console.log('出错了。'))
        },
        backward(){
          axios.get('/move?dir=B')
          .then((res)=>console.log(res.data))
          .catch(()=>console.log('出错了。'))
        },
        left(){
          axios.get('/move?dir=L')
          .then((res)=>console.log(res.data))
          .catch(()=>console.log('出错了。'))
        },
        right(){
          axios.get('/move?dir=R')
          .then((res)=>console.log(res.data))
          .catch(()=>console.log('出错了。'))
        },
        stop(){
          axios.get('/move?dir=S')
          .then((res)=>console.log(res.data))
          .catch(()=>console.log('出错了。'))
        }
      },
    });
  </script>
</body>
</html>
)=====";