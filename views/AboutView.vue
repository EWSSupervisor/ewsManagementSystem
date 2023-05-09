<template>
  <div>
    <n-button @click="toggleDialog">Show dialog</n-button>
    <n-dialog
      v-model:visible="dialogVisible"
      title="Dialog Title"
      width="30%"
      :body-style="{ padding: '20px' }"
    >
      <p>Dialog content goes here</p>
      <n-button type="primary" @click="dialogVisible = false">Close</n-button>
    </n-dialog>
  </div>
</template>

<script>
import { defineComponent, ref } from 'vue'
import { NButton, NDialog } from 'naive-ui'

export default defineComponent({
  name: 'MyComponent',
  components: {
    NButton,
    NDialog,
  },
  setup() {
    const dialogVisible = ref(false)
    const toggleDialog = () => {
      dialogVisible.value = !dialogVisible.value
    }
    return {
      dialogVisible,
      toggleDialog,
    }
  },
})
</script>
