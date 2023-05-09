<template>
  <div class="container">
    <div class="logo-container">
      <img alt="EWS Logo" src="../assets/OGLogo.png" width="250" height="250">
    </div>
    <div class="divider"> 

</div>
    <div class="form-container">

      <n-text type="success"   style="color: #a2a2a2">
        それでは始めましょう
      </n-text>
      <n-h1 align-text type="success" style="margin-top: 1px;">
   
      <n-text type="success"   style="color: black">
        Let's get started
      </n-text>
    </n-h1>
      <n-input
        round
        size = "large"
        v-model="userName"
        placeholder="Your full name (please)"
        style="margin: 10px; width: 100%;"
      /> 
      <n-input
        round
        size = "large"
   
        v-model="projectName"
        placeholder="Project name?"
        style="margin: 10px; width: 100%;"
      /> 
      <n-button type="primary" @click="handleSubmit" round size ="large"    style="margin: 10px; width: 125px; color:white; background-color: black"
>
        Enter
      </n-button>
      
    </div>
  </div>
</template>

<script>
import { defineComponent, ref } from 'vue'
import { NInput, NButton } from 'naive-ui'

export default defineComponent({
  name: 'EnterUserInfo',
  components: {
    NInput,
    NButton,
  },
  setup() {
    const userName = ref('')
    const projectName = ref('')
    const handleSubmit = () => {
      // handle form submission here
      console.log('Submitting form...')
      console.log('User name:', userName.value)
      console.log('Project name:', projectName.value)
    }
    return {
      userName,
      projectName,
      handleSubmit,
    }
  },
})
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
  margin-left: 50%;


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
