<template class="row">
  <div class="text-center">
    <form class="form-group" v-on:submit.prevent="getPhrase">
        <select v-model="lang" name="select_locale" id="select_locale" class="form-control col-xs-6">
          <option value='' selected disabled>Choose your language.</option>
          <option value="PT" disabled>Portuguese 
            <h6 class="text-danger">(Unfortunatelly, still not working.)</h6>
          </option>
          <!--For some reason, we end up mixing english and portuguese phrases -->
          <option value="EN">English</option>
        </select>
        <br>
        <button class="btn btn-success">Generate!</button>
        <hr>
        <Phrase v-bind:msg="msg" v-bind:isLoading="isLoading"/>
    </form>
  </div>
</template>

<script lang="ts">
import Phrase from './Phrase.vue'
import { Component, Vue } from 'vue-property-decorator'

@Component({
  components: {
    Phrase
  }
})
export default class BasicForm extends Vue {
  isLoading = false
  lang = ''
  msg = 'your fortune will appear here'
  getPhrase () {
    this.isLoading = true
    if (this.lang === '') {
      this.lang = 'EN'
    } 
    this.$http.get(`http://localhost:5000/language/${this.lang}`, null, {
      headers: {
        'Access-Control-Allow-Origin': true
      }
      }).then(
      response => {
        this.msg = response.data
        this.isLoading = false
      }, error => {
        this.msg = 'error...'
        this.isLoading =  false
      }
    )
  }
}
</script>

<style scoped>

</style>
