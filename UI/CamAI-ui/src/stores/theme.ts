import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import { darkTheme } from 'naive-ui'

export const ThemeStore = defineStore('Theme', () => {
  /**
   * null or BuiltInGlobalTheme
   */
  const ThemeUsed = ref(null)
  /**
   * Change theme
   */
  function inv() {
    if (ThemeUsed.value){
      ThemeUsed.value = null
    }
    else{
      ThemeUsed.value = darkTheme
    }
   }

  return { ThemeUsed, inv }
})
