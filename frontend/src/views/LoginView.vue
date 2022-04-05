<template>
  <div class="container">
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
    submitForm(event) {
      event.preventDefault();

      axios({
        method: "post",
        url: "/login/",
        data: {
          username: this.loginForm.username,
          password: this.loginForm.password,
          next_url: this.loginForm.next_url,
        },
      });

      // axios.post({
      //   url: "/login",
      //   data: {
      //     username: this.loginForm.username,
      //     password: this.loginForm.password,
      //     next_url: this.loginForm.next_url,
      //   },
      //   headers: {
      //     "Content-Type": "application/x-www-form-urlencoded",
      //   },
      // });
    },
  },
};
</script>

<style scoped>
container {
  background: #00000020;
  margin: 0%;
}

.title {
  background: #5f6298;
  font-size: 50px;
  color: white;
}

.login-box {
  width: 20%;
  height: 350px;
  background: white;
  margin: auto;
  margin-top: 5%;
  text-align: center;
  border-radius: 10px;
  padding: 50px 50px;
}

.login-box:hover {
  box-shadow: 0px 0px 20px 5px rgba(0, 0, 0, 0.3);
}

.input-box {
  border: 10;
  width: 60%;
  font-size: 15px;
  background: #ffffff00;
  border-radius: 10px;
  padding: 5px 10px;
  margin-top: 10px;
}

/* .form-label{
  text-align: center;
}

.form-control{
  text-align: center;
} */

/* .login-btn {
  margin-top: 30px;
  width: 30%;
  height: 40px;
  border-radius: 10px;
  border: 0;
  background-image: linear-gradient(to top, #30324d 0%, #5f6298 100%);
  color: white;
  font-size: 15px;
  text-decoration: none;
} */

/* .register {
  text-align: center;
  margin-top: 10%;
} */

/* .register.a {
  color: black;
  text-decoration: none;
} */
</style>