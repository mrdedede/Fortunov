<template>
  <div class="text-center">
    <div v-if="isLoading" class="spinner-border">
      <span class="sr-only text-secondary">Loading...</span>
    </div>
    <div v-else>
      <h2>Last Result:</h2>
      <h3 class="font-italic">"{{ capitalize() }}."</h3>
    </div>
  </div>
</template>

<script lang="ts">
import { Component, Prop, Vue } from 'vue-property-decorator'

@Component
export default class Phrase extends Vue {
  @Prop() private msg!: string
  @Prop() private isLoading!: boolean

  capitalize () {
    return this.msg.charAt(0).toUpperCase() + this.msg.slice(1)
  }
}
</script>

<style scoped>

</style>
