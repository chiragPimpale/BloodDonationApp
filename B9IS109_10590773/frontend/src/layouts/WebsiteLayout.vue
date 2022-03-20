<!--WebsiteLayout is the main layout of website view-->
<template>
<div>
    <div class="header">
        <div class="container d-flex justify-content-between">
            <div class="header-left">
                <router-link to="/"><img width="200" src="https://user-images.githubusercontent.com/60983778/97785070-d8d24480-1bc8-11eb-9de5-4b628da15a06.jpg" alt="logo" /></router-link>
            </div>
            <div class="header-right">
                <nav>
                    <ul>
                        <li>
                            <router-link class="btn btn-sm btn-danger" to="signup">Signup</router-link>
                        </li>
                        <li>|</li>
                        <li>
                            <router-link class="btn btn-sm btn-danger" to="login">Login</router-link>
                        </li>
                    </ul>
                </nav>
            </div>
        </div>
    </div>
    <router-view></router-view>
    <div class="footer d-flex align-items-center">
        <div class="container justify-content-between d-flex flex-row">
            <div class="footer-left">
                <h3 style="font-family:Bungee Inline;color:white;width:400px">A liitle sacrifice ca save some one life</h3>
            </div>
            <div class="footer-right">
                <p style="color:white">Allright Served &copy; 2022</p>
            </div>
        </div>
    </div>
</div>
</template>

<style scoped>
@import url("../assets/website/website.css");
</style>

<script>
export default {
    name: "WebsiteLayout"
}
</script>
