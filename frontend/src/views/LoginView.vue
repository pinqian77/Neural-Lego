<template>
  <!-- <div class="container">
    <div class="title">Neural LEGO</div>

    <div class="login-box">
      <h2>Log in</h2>
      <form method="POST">
        <div class="input-box">
          <label for="username" class="form-label">Username</label>
          <input
            v-model="loginForm.email"
            type="text"
            class="form-control"
            id="username"
            name="username"
            required
          />
        </div>

        <div class="input-box">
          <label for="password" class="form-label">Password</label>
          <input
            v-model="loginForm.password"
            type="password"
            class="form-control"
            id="password"
            name="password"
            required
          />
        </div>

        <input
          v-model="loginForm.next_url"
          type="hidden"
          class="form-control"
          id="next_url"
          name="next_url"
        />

        <div class="login-btn">
          <button type="submit" @click="submitFrom($event)">Login</button>
        </div>

        <div class="register">
          <p><a href="/register">Register</a></p>
        </div>
      </form>
    </div>
  </div> -->

  <div class="bg-gradient-primary body">
    <div class="container">
      <!-- Outer Row -->
      <div class="row justify-content-center">
        <div class="col-xl-10 col-lg-12 col-md-9">
          <div class="card o-hidden border-0 shadow-lg my-5">
            <div class="card-body p-0">
              <!-- Nested Row within Card Body -->
              <div class="row">
                <div class="col-lg-6 d-none d-lg-block bg-login-image"></div>
                <div class="col-lg-6">
                  <div class="p-5">
                    <div class="text-center">
                      <h1 class="h4 text-gray-900 mb-4">Welcome Back!</h1>
                    </div>

                    <div class="form-group">
                      <input
                        class="form-control form-control-user"
                        aria-describedby="emailHelp"
                        placeholder="Enter Username"
                        v-model="loginForm.email"
                        type="text"
                        id="username"
                        name="username"
                        required
                      />
                    </div>
                    <div class="form-group">
                      <input
                        type="password"
                        class="form-control form-control-user"
                        placeholder="Password"
                        v-model="loginForm.password"
                        id="password"
                        name="password"
                        required
                      />
                    </div>
                    <input
                      v-model="loginForm.next_url"
                      type="hidden"
                      class="form-control"
                      id="next_url"
                      name="next_url"
                    />

                    <button
                      type="submit"
                      class="btn btn-primary btn-user btn-block"
                      @click="submitForm()"
                    >
                      Login
                    </button>

                    <hr />

                    <div class="text-center">
                      <a class="small" href="/register">Create an Account!</a>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>


<script>
import axios from "axios";

export default {
  name: "LoginView",
  data() {
    return {
      loginForm: {
        username: "",
        password: "",
        next_url: "/project",
      },
    };
  },
  methods: {
    submitForm() {
      // Declare a form
      let formData = new FormData();
      formData.append("username", this.loginForm.username);
      formData.append("password", this.loginForm.password);
      formData.append("next_url", this.loginForm.next_url);

      // Send form to backend and get response data
      axios({
        method: "post",
        url: "/login/",
        data: formData,
      }).then((res) => {
        if (res.data.isLogin == true) {
          console.log("login ok!");
        } else {
          console.log("login fail!");
        }
      });
    },
  },
};
</script>

<style scoped>
.body {
  position: fixed;
  background-size: cover;
  padding: 0;
  margin: 0;
  height: 100%;
  width: 100%;
}
</style>
<style scoped src="../../new_pages/vendor/fontawesome-free/css/all.min.css"></style>
<style scoped src="../../new_pages/css/sb-admin-2.min.css"></style>