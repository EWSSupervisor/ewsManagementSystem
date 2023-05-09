<template>
  <div class="home">

  <!-- <HelloWorld msg="Welcome to Your Vue.js App"/>  
     
          <StartBarcodeScanner />

    --> 
  <EnterUserInfo /> 
      
  </div>
</template>

<script>
// @ is an alias to /src
import EnterUserInfo from '@/components/EnterUserInfo.vue'
import StartBarcodeScanner from '@/components/StartBarcodeScanner.vue'

export default {
  name: 'HomeView',
  components: {
    EnterUserInfo
  // StartBarcodeScanner
  }
}
</script>
