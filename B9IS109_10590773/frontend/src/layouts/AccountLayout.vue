<!--Account layout its profile main layout-->
<template>
  <div>
    <nav class="navbar navbar-dark bg-danger">
      <h3 class="text-white" style="margin-left: 30px">{{full_name}} ({{account_type}}) </h3>
      <button @click="Logout" class="btn btn-outline-light btn-sm" style="margin-right:20px">Logout</button>
    </nav>
    <div class="d-flex">
      <div
        class="col-2"
        style="background-color: #dc3545; min-height: 100%; min-height: 100vh"
      >
        <ul class="list-group">
          <router-link to="account" style="text-decoration: none" v-if="account_type == 'accepter'">
            <li class="list-group-item">Doner List</li>
          </router-link>
          <router-link to="ask-to-bank" style="text-decoration: none" v-if="account_type == 'accepter'">
              <li class="list-group-item">Ask to Blood Bank</li>
          </router-link>
          <router-link to="ask-to-bank" style="text-decoration: none" v-if="account_type == 'donor'">
              <li class="list-group-item">Blood Requests </li>
          </router-link>
          <router-link to="ask-to-bank" style="text-decoration: none" v-if="account_type == 'bloodbank'">
              <li class="list-group-item">Validate Token</li>
          </router-link>
          <router-link to="ask-to-bank" style="text-decoration: none" v-if="account_type == 'admin'">
              <li class="list-group-item">User List</li>
          </router-link>
        </ul>
      </div>
      <router-view></router-view>
    </div>
  </div>
</template>

<script>
export default {
  name: "UserAccount",
  data () {
    // component states
    return {
      full_name: "",
      account_type: ""
    }
  },
  // life cycle methods
  mounted() {
    var token = localStorage.getItem("token");
    var user_id = localStorage.getItem("user_id");
    const headers = { Authorization: `Bearer ${token}` };
    this.$axios.get(this.$base_url+"/api/user/"+user_id+"/", { headers})
      .then(response => {
        this.full_name = response.data.full_name;
        this.account_type = response.data.user_type
        document.title = "Website | "+this.account_type
      })
  },
  methods: {
    // logout methods 
    Logout() {
      localStorage.removeItem("token");
      localStorage.removeItem("user_id");
      this.$router.push("/login");
    }
  }
};
</script>