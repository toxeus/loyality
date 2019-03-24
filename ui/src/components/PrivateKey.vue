<template>
    <div class="privkey">
    <form>
       Private key: <input v-model="dprivkey"><br>
       Address: <input v-model="daddress"><br>
       Blinding key: <input v-model="dblindingkey"><br>
        <button v-on:click="submit_privkey">Submit</button>
    </form>
    </div>
</template>

<script>
import Client from 'bitcoin-core'

export default {
    name: 'PrivateKey',
    data() {
        return {
          dprivkey: "L5QBsFQDHff4grRWJUGRdnVZ7BeHYtBsHnokBYbKLQ5UKYgH2YzF",
          daddress: "VTpxwbfyAvfZPvJHZPHLp3p88L2hWpwuXdRLxqHmmHNFZWGx6ZxxZQxt2MTWAXcNpNjxYNB7bBvbYdkH",
          dblindingkey: "017e1b2c1540e06d80c2b662ac59c2f17eb715280fa6e979cf375f1f0e9d580f"
        }
    },
    methods: {
        submit_privkey: function() {
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
