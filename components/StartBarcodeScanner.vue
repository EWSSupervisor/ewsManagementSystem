<template>
    <div style="width: 100%; align-items: center; justify-content: center;">
      

 <n-alert title="Error" type="error" style="width: 50%; margin-left: 25%; margn-right: 25%;">
    Before you start, please turn on the Barcode Reader.
  </n-alert>
    </div>
  </template>
  
  <script>
  import { defineComponent, ref } from 'vue'
  import {IosAirplane} from '@vicons/ionicons4'

  export default defineComponent({
    name: 'StartBarcodeScanner',
    components: {
      IosAirplane,

    },})
  </script>
  
  <style scoped>
  .container {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    grid-template-rows: 1fr;
    height: 95vh;
    align-items: center;
    justify-content: center;
  
  }
  .divider {
  
    border-left: 1px solid #e2e2e2;
    vertical-align: center;
    height: 5%;
    width: 1px;
    margin: 50%;
  }
  .logo-container {
    display: flex;
    justify-content: center;
    align-items: center;
    margin-left: 20%;
  
  
  }
  
  .form-container {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    width: 75%;
    margin-right: 20%;
  
  
    
  }
  </style>
  