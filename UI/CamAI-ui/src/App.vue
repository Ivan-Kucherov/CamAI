<script lang="ts">
import { RouterLink, RouterView } from 'vue-router'
import {Header} from './Components/Header.vue'
import { darkTheme } from 'naive-ui'
import { ThemeStore} from './stores/theme'
import { computed } from 'vue'

export default {
  setup() {
    const themeStore = ThemeStore()
    const Theme = computed(() => themeStore.ThemeUsed)
    return {
      Theme,
    }
  }
}
</script>

<template>
  <n-config-provider :theme="Theme">
  <Header></Header>
  <RouterView></RouterView>
</n-config-provider>
</template>

<style scoped>

</style>
