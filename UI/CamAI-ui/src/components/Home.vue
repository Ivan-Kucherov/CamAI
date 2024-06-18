<script lang="ts">
export default {
    
  setup() {

  },
  mounted(){
    fetch("127.0.0.1/8000/test/video_feed").then((response) => response.body);
    },
  components: {
}}
</script>
<img v-if="Show" src="{{ url_for('video_feed') }}"></img>
<template>

</template>

<style scoped>

</style>
