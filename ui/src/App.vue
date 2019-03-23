<template>
    <div id="app">
        <PrivateKey/>
        <Balance/>
    </div>
</template>

<script>
import Balance from './components/Balance.vue'
import PrivateKey from './components/PrivateKey.vue'

export default {
    name: 'app',
    components: {
        Balance,
        PrivateKey
    }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
