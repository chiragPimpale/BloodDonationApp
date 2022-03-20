<!--Login templete inhertited from website layout-->
<template>
<div>
    <div class="container mt-5 d-flex">
        <div class="col-8">
            <img src="https://img.freepik.com/free-vector/drop-with-silhoutte-hands_24908-15743.jpg" alt=""/>
        </div>
        <div class="col-4">
            <form @submit.prevent="LoginToAccount" style="margin-top:200px">
                <h2 class="text-danger">Login to account</h2>

                <div class="form-group mb-2">
                    <label for="exampleInputPassword1">Email</label>
                    <input type="text" class="form-control" v-model="email">
                    <span class="text-danger" v-if="email_err != ''">{{email_err}}</span>
                </div>
                <div class="form-group mb-2">
                    <label for="exampleInputPassword1">Passowrd</label>
                    <input type="password" class="form-control" v-model="password">
                    <span class="text-danger" v-if="password_err != ''">{{password_err}}</span>
                </div>
                <span class="text-danger" v-if="login_err !=''" >{{login_err}}</span>
                <button type="submit" class="btn btn-danger mt-3" style="float:right">Submit</button>
            </form>
        </div>
    </div>
    </div>
</template>

<script>
export default {
    name: "WebsiteLogin",
    // components states
    data() {
        return {
            email : "",
            password: "",
            email_err : "",
            password_err: "",

            login_err: ""
        }
    },
    methods: {
        // request to accept credentials and return a token instead
        LoginToAccount () {
            if(this.email == "") {
                    this. email_err = "Email is required";
                }
                if(this.password == "") {
                    this. password_err = "Password is required";
                }
                if(this.email != "" && this.password != "") {
                    var data = {
                        email: this.email,
                        password: this.password
                    }
                    this.$axios.post(this.$base_url+"/api/login/", data)
                    .then(response => {
                        localStorage.setItem("token", response.data.access);
                        localStorage.setItem("user_id", response.data.id);
                        this.$router.push('/account');
                    }).catch(error => {
                        if(error.status == undefined) {
                            this.login_err = "Invalid credentials provided"
                        }
                    })
            }
        }
    },
    mounted() {
    document.title = "Website | Login";
  }
}
</script>