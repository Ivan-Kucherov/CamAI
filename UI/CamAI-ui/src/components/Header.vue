<template>
  <n-layout-header style="height: 3em;
    display: flex;
    align-items: flex-start;
    flex-direction: row;
    margin: 0px;
    " bordered>
    <n-button @click="handleClick('Home')" style="font-size: 2.5em;
                      margin: 2px;
                      margin-right: 1em;
                      margin-left: 0.5em;
                      height: 100%;" text type="default">
      <n-icon>
        <CamIcon />
      </n-icon>
    </n-button>
    <n-button @click="handleClick('Editor')" style="font-size: 2em;height: 100%;" type="default">
      <n-icon>
        <EditorIcon />
      </n-icon>
      Editor
    </n-button>
    <n-button @click="handleClick('Settings')" style="font-size: 2em;height: 100%;" type="default">
      <n-icon>
        <SettingsIcon />
      </n-icon>
      Settings
    </n-button>
    <n-button @click="handleClick('Moon')" style="font-size: 2em;height: 100%;margin-left: auto;" circle quaternary type="default">
      <n-icon>
        <Moon />
      </n-icon>
    </n-button>
  </n-layout-header>
</template>
<script lang="ts">
import { defineComponent, h, ref, type Component } from 'vue'
import { NIcon } from 'naive-ui'
import type { MenuOption } from 'naive-ui'
import {
  SettingsOutline as SettingsIcon,
  ApertureOutline as EditorIcon,
  VideocamOutline as CamIcon,
  MoonOutline as Moon,
} from '@vicons/ionicons5'
import { RouterLink } from 'vue-router'
import router from '../router/index'
import { ThemeStore } from '@/stores/theme'

export default {
  setup() {
    const themeStore = ThemeStore()
    /**
     * 
     * @param name Идентификатор кнопки(str)
     */
    function handleClick(name: string) {
      if (name !== 'Moon') {
        router.replace({
          name: name
        })
        //console.log(name);
      }
      else{
        themeStore.inv()
      }
    }
    return {
      handleClick
    };
  },
  components:
  {
    
    Moon,
    CamIcon,
    EditorIcon,
    SettingsIcon
  }
}

</script>