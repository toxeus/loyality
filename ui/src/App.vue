<template>
    <div id='outer'><div id='middle'>
    <div id="app">
        <md-card class="md-primary" md-theme="purple-card" md-with-hover>
            <md-ripple>
                <md-card-header>
                    <div class="md-title"><Balance/></div>
                </md-card-header>
                <md-card-content>
                    <PrivateKey/>
                </md-card-content>
            </md-ripple>
        </md-card>
    </div>
    </div></div>
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
  width: 40%;
  margin: auto;
  background-color: #ffffff;
}

#outer {
  display: table;
  position: absolute;
  top: 0;
  left: 0;
  height: 100%;
  width: 100%;
}

#middle {
  display: table-cell;
  vertical-align: middle;
}

body {
  background-color: #f5f5f5;
}

</style>
