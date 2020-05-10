<template class="container">
  <div class="row">
    <div class="col-md-3"></div>
    <div class="col-md-6 text-center">
      <h1>Welcome to Fortune Cookov!</h1>
      <h5>The only Fortune Cookie Message Generator based on Markov Chains</h5>
      <br>
      <BasicForm />
    </div>
    <div class="col-md-3"></div>
  </div>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator'
import BasicForm from './components/BasicForm.vue'

@Component({
  components: {
    BasicForm
  }
})
export default class App extends Vue {}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
