<template>
    <div class="privkey">
    <form class="md-layout">
        <md-field>
            <label for="privkey">Private Key</label>
            <md-input name="privkey" id="privkey" v-model="dprivkey"/>
        </md-field>
        <md-field>
            <label for="address">Address</label>
            <md-input name="address" id="address" v-model="daddress"/>
        </md-field>
        <md-field>
            <label for="blindingkey">Blinding Key</label>
            <md-input name="blindingkey" id="blindingkey" v-model="dblindingkey"/>
        </md-field>
        <md-button class="md-icon-button md-primary md-raised" v-on:click="submit_privkey">
            <md-icon>add</md-icon>
        </md-button>
    </form>
    </div>
</template>

<script>
import Client from 'bitcoin-core'

export default {
    name: 'PrivateKey',
    data() {
        return {
          dprivkey: "",
          daddress: "",
          dblindingkey: ""
        }
    },
    methods: {
        submit_privkey: function(e) {
            e.preventDefault();
            const client = new Client({ port: 8888, username: 'alice', password: 'bob' });
            (async () => await client.importPrivKey(`${this.dprivkey}`))();
            let headers = new Headers();
            let username = 'alice';
            let password = 'bob';
            headers.append('Authorization', 'Basic ' + btoa(username + ":" + password));


            fetch("http://localhost:8888", {
                method: "POST",
                headers: headers,
                body: JSON.stringify({
                    method: "importblindingkey",
                    params: [this.daddress, this.dblindingkey]
                    })
                }).then(function(resp) {
                    console.log(resp)
                    })
                  .catch(function(err) {
                    console.log('There has been a problem with your fetch operation: ', err.message);
                    })
        }
    }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
a {
    color: #42b983;
}
</style>
