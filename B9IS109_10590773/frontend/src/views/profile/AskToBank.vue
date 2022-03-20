<!--This is a componnet inhertied by AccountLayout-->
<template>
<div class="col-8 p-3 d-flex flex-wrap flex-row" style="width: 1100px" v-if="account_type == 'accepter'">
    <div class="alert alert-success text-center" role="alert" v-if="message!= ''">
        {{message}}
    </div>
    <div style="width: 1000px">
        <select class="form-control" v-model="blood_group">
            <option value="">-- Select Blood --</option>
            <option value="ap">A+ (A Positive)</option>
            <option value="ap">A- (A Negative)</option>
            <option value="op">O+ (A Positive)</option>
            <option value="op">O- (A Negative)</option>
            <option value="bp">B+ (A Positive)</option>
            <option value="bn">B- (A Negative)</option>
            <option value="abp">AB+ (AB Positive)</option>
            <option value="abn">AB- (AB Negative)</option>
        </select>
        <button class="btn btn-outline-danger mb-5" type="button" @click="generateToken">
            Generate Token
        </button>
        <table class="table">
            <thead>
                <tr>
                    <th scope="col">Token</th>
                    <th scope="col">Blood Group</th>
                    <th scope="col">Created at</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="token in tokens" v-bind:key="token.id">
                    <td>{{token.secret_key}}</td>
                    <td>
                      {{ token.requested_group == "ap"?"A+":"" }}
                        {{ token.requested_group == "an"?"A-":"" }}
                        {{ token.requested_group == "bp"?"B+":"" }}
                        {{ token.requested_group == "bn"?"B-":"" }}
                        {{ token.requested_group == "op"?"O+":"" }}
                        {{ token.requested_group == "on"?"O-":"" }}
                        {{ token.requested_group == "abp"?"AB+":"" }}
                        {{ token.requested_group == "abn"?"AB-":"" }}
                    </td>
                    <td>{{token.requested_at}}</td>
                </tr>
            </tbody>
        </table>
    </div>
</div>
</template>

<script>
export default {
    name: "AskToBank",
    // all states of accepter , doner and others profile
    data() {
        return {
            account_type: "",
            message: "",
            tokens: [],
            blood_group: ""
        };
    },
    // lifecycle method
    mounted() {
        var token = localStorage.getItem("token");
        var user_id = localStorage.getItem("user_id");
        const headers = {
            Authorization: `Bearer ${token}`
        };
        // axios to send request to server
        this.$axios
            .get(this.$base_url + "/api/user/" + user_id + "/", {
                headers
            })
            .then((response) => {
                this.account_type = response.data.user_type;
            });

        this.$axios
            .get(this.$base_url + "/api/all-tokens/" + user_id + "/", {
                headers
            })
            .then((response) => {
                this.tokens = response.data
            });
    },
    methods: {
        // generate token methods to send create token request to server
        generateToken() {
            if (this.blood_group != "") {
                var token = localStorage.getItem("token");
                var user_id = localStorage.getItem("user_id");
                const headers = {
                    Authorization: `Bearer ${token}`
                };
                this.$axios
                    .post(this.$base_url + "/api/request-blood-bank/", {
                        requested_by: user_id,
                        requested_group: this.blood_group
                    }, {
                        headers
                    })
                    .then((response) => {
                        this.message = response.data.message
                    });
            } else {
                alert("Must select a blood group");
            }
        },
    },
};
</script>
