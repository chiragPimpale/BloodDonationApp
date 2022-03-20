<!--
UserAccount is component inherited from AccountLayout component
-->
<template>
<div>
    <div class="alert alert-success text-center" role="alert" v-if="message!= ''">
        {{message}}
    </div>
    <div class="col-8 p-3 d-flex flex-wrap flex-row" style="width: 1100px" v-if="account_type=='accepter'">
        <select class="form-control" style="margin-bottom: 30px" v-model="search_by_group" @change="OnChnageGroup">
            <option value="donor">-- Select Blood --</option>
            <option value="ap">A+ (A Positive)</option>
            <option value="an">A- (A Negative)</option>
            <option value="op">O+ (A Positive)</option>
            <option value="on">O- (A Negative)</option>
            <option value="bp">B+ (A Positive)</option>
            <option value="bn">B- (A Negative)</option>
            <option value="abp">AB+ (AB Positive)</option>
            <option value="abn">AB- (AB Negative)</option>
        </select>
        <!--start card-->
        <div class="card" style="
          width: 15rem;
          margin-right: 20px;
          margin-bottom: 20px;
        " v-for="doner in donors" v-bind:key="doner.id">
            <img class="card-img-top" src="https://previews.123rf.com/images/moremar/moremar1907/moremar190700033/132121691-the-face-of-a-happy-girl-avatar-of-a-laughing-young-woman-portrait-vector-flat-illustration.jpg" alt="Card image cap" v-if="doner.gender == 'female'" />
            <img class="card-img-top" src="https://opportunitysrilanka.com/wp-content/uploads/2017/03/malecostume-512.png" alt="Card image cap" v-if="doner.gender == 'male'" />
            <div class="card-body">
                <h5 class="card-title">{{ doner.full_name }}</h5>
                <div class="card-text">
                    <p>ID: {{ doner.id }}</p>
                    <p>Email: {{ doner.email }}</p>
                    <p>Contact: {{ doner.contact }}</p>
                    <p>
                        Blood Group:
                        {{ doner.blood_group == "ap"?"A+":"" }}
                        {{ doner.blood_group == "an"?"A-":"" }}
                        {{ doner.blood_group == "bp"?"B+":"" }}
                        {{ doner.blood_group == "bn"?"B-":"" }}
                        {{ doner.blood_group == "op"?"O+":"" }}
                        {{ doner.blood_group == "on"?"O-":"" }}
                        {{ doner.blood_group == "abp"?"AB+":"" }}
                        {{ doner.blood_group == "abn"?"AB-":"" }}
                    </p>
                </div>
                <button type="button" class="btn btn-primary w-100" @click="SendRequest(doner.id)">Send Request</button>
            </div>
        </div>
        <!--end card-->
    </div>

    <div class="col-8 p-3 d-flex flex-wrap flex-row" style="width: 1100px" v-if="account_type=='donor'">
        <div class="alert alert-danger w-100" role="alert" v-for="req in blood_request_by_user" v-bind:key="req.id">
            You have a blood donation request from:-
            <br>
            <br>
            Name: {{req.blood_requested_by.full_name}}
            <br>
            Email: {{req.blood_requested_by.email}}
            <br>
            Contact: {{req.blood_requested_by.contact}}
            <br>
            Requested At: {{req.requested_at}}
            <br>
            <br>
            <button type="button" class="btn btn-sm btn-danger" style="float:right" @click="RemoveRequest(req.id)">Remove</button>
        </div>
    </div>

    <div class="col-8 p-3 d-flex flex-wrap flex-row" style="width: 1100px" v-if="account_type=='bloodbank'">
        <form>
            <div class="input-group mb-3">
                <input type="text" class="form-control" style="width:700px" aria-label="Recipient's username" aria-describedby="basic-addon2" placeholder="Paste token and check" v-model="token">
                <div class="input-group-append">
                    <button class="btn btn-outline-danger" type="button" @click="VerifyToken">Check</button>
                </div>
            </div>
        </form>
        <table class="table" v-if="user_from_token.id != undefined">
            <tbody>
                <tr>
                    <td style="width:200px">Id</td>
                    <td>{{user_from_token.id}}</td>
                </tr>
                <tr>
                    <td>Token</td>
                    <td>{{user_from_token.secret_key}}</td>
                </tr>
                <tr>
                    <td>Full Name</td>
                    <td>{{user_from_token.requested_by.full_name}}</td>
                </tr>
                <tr>
                    <td>Email</td>
                    <td>{{user_from_token.requested_by.email}}</td>
                </tr>
                <tr>
                    <td>Contact</td>
                    <td>{{user_from_token.requested_by.contact}}</td>
                </tr>
                <tr>
                    <td>Requested Blood</td>
                    <td>
                        {{user_from_token.requested_group}}
                        {{ user_from_token.requested_group == "ap"?"A+":"" }}
                        {{ user_from_token.requested_group == "an"?"A-":"" }}
                        {{ user_from_token.requested_group == "bp"?"B+":"" }}
                        {{ user_from_token.requested_group == "bn"?"B-":"" }}
                        {{ user_from_token.requested_group == "op"?"O+":"" }}
                        {{ user_from_token.requested_group == "on"?"O-":"" }}
                        {{ user_from_token.requested_group == "abp"?"AB+":"" }}
                        {{ user_from_token.requested_group == "abn"?"AB-":"" }}
                    </td>
                </tr>
            </tbody>
        </table>
    </div>

    <div class="col-8 p-3 d-flex flex-wrap flex-row" style="width: 1100px" v-if="account_type=='admin'">
        <button class="btn btn-sm btn-outline-danger" @click="GenerateBankAccount">Generate Blood Bank User</button>
        <table class="table">
            <thead>
                <tr>
                    <th scope="col">#</th>
                    <th scope="col">Full Name</th>
                    <th scope="col">Email</th>
                    <th scope="col">User Type</th>
                    <th scope="col">Action</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="user in accepter_and_donors" v-bind:key="user.id">
                    <th scope="row">{{user.id}}</th>
                    <td>{{user.full_name}}</td>
                    <td>{{user.email}}</td>
                    <td>{{user.user_type}}</td>
                    <td>
                        <button type="button" class="btn btn-danger btn-sm" @click="removeUser(user.id)">Remove</button>
                    </td>
                </tr>
            </tbody>
        </table>
    </div>
</div>
</template>

<script>
export default {
    name: "UserAccount",
    data() {
        // components states
        return {
            search_by_group: "donor",
            donors: [],
            message: "",
            account_type: "",
            token: "",
            user_from_token: {},
            accepter_and_donors: [],
            blood_request_by_user:{}
        };
    },
    // lifecycle method
    mounted() {
        this.allDoners();
        this.getUser();
        this.allUsers();
        this.allRequest();  
    },
    methods: {

        // send request to server for all doner list
        allDoners() {
            var token = localStorage.getItem("token");
            const headers = {
                Authorization: `Bearer ${token}`
            };
            this.$axios
            .get(this.$base_url + "/api/all-doners/" + this.search_by_group + "/", {
                headers,
            })
            .then((response) => {
                this.donors = response.data;
            });
        },
        // send request to server for ge all user list
        getUser() {
            var token = localStorage.getItem("token");
            var user_id = localStorage.getItem("user_id");
            const headers = {
                Authorization: `Bearer ${token}`
            };
            this.$axios.get(this.$base_url + "/api/user/" + user_id + "/", {
                headers
            })
            .then(response => {
                if(response.data.id === undefined) {
                    this.$route.push("/login");
                }
                this.account_type = response.data.user_type
            })
        },
        // send request to server for all user list
        allUsers() {
            var token = localStorage.getItem("token");
            const headers = {
                Authorization: `Bearer ${token}`
            };
            this.$axios.get(this.$base_url + "/api/all-users/", {
                headers
            })
            .then(response => {
                this.accepter_and_donors = response.data
            })
        },
        // send request to server for getting all request for donor
        allRequest() {
            var token = localStorage.getItem("token");
            var user_id = localStorage.getItem("user_id");
            const headers = {
                Authorization: `Bearer ${token}`
            };
            this.$axios.get(this.$base_url + "/api/my-request/"+user_id+"/", {
                headers
            })
            .then(response => {
                this.blood_request_by_user = response.data
            })
        },
        // live change event for getiing donor list by parameter
        OnChnageGroup() {
            var token = localStorage.getItem("token");
            const headers = {
                Authorization: `Bearer ${token}`
            };
            this.$axios
                .get(this.$base_url + "/api/all-doners/" + this.search_by_group + "/", {
                    headers,
                })
                .then((response) => {
                    this.donors = response.data;
                });
        },
        // send request to server to connect with accepter with donor
        SendRequest(x) {
            var user_id = localStorage.getItem("user_id");
            var token = localStorage.getItem("token");
            var data = {
                blood_requested_by: user_id,
                blood_requested_to: x
            };
            const headers = {
                Authorization: `Bearer ${token}`
            };
            this.$axios
                .post(this.$base_url + "/api/request-donation/", data, {
                    headers
                })
                .then((response) => {
                    this.message = response.data.message
                });
        },
        // send request to server to verufy token and response token data
        VerifyToken() {
            var token = localStorage.getItem("token");
            const headers = {
                Authorization: `Bearer ${token}`
            };
            this.$axios.post(this.$base_url + "/api/verify-secret/", {
                    secret_key: this.token
                }, {
                    headers
                })
                .then((response) => {
                    this.user_from_token = response.data;
                });
        },

        // send request to server to remove user
        removeUser(x) {
            var token = localStorage.getItem("token");
            const headers = {
                Authorization: `Bearer ${token}`
            };
            this.$axios.delete(this.$base_url + "/api/user/" + x + "/remove/", {
                    headers
                })
                .then((response) => {
                    this.message = "User has been deleted";
                });
        },

        // send request to server for removing Request
        RemoveRequest(x) {
            var token = localStorage.getItem("token");
            const headers = {
                Authorization: `Bearer ${token}`
            };
            this.$axios.delete(this.$base_url + "/api/my-request/remove/" + x + "/", {
                    headers
                })
                .then((response) => {
                    this.message = "Request has been removed";
                    this.allRequest();
                });
        },
        // send request for generating back account
        GenerateBankAccount () {
            var token = localStorage.getItem("token");
            const headers = {
                Authorization: `Bearer ${token}`
            };
            this.$axios.get(this.$base_url + "/api/generate-bank-account/", {
                    headers
                })
                .then((response) => {
                    this.message = response.data.message;
                    this.allUsers();
                });
        }
    },
};
</script>
