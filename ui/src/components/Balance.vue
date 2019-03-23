<template>
    <div class="balance">
        Your balance is:
        {{ this.balance }}
    </div>
</template>

<script>
import Client from 'bitcoin-core'

export default {
    name: 'Balance',
    data() {
        return {
            balance: null,
            timer: null,
        }
    },
    mounted() {
        this.timer = setInterval(function () {
            const client = new Client({ port: 8888, username: 'alice', password: 'bob' });
            (async () => this.balance = await client.getBalance('"*"'))();
        }.bind(this), 1000);
    }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
a {
    color: #42b983;
}
</style>
