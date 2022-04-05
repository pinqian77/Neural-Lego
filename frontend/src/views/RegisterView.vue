<template>
  <div class="container">
    <div class="title">Neural LEGO</div>

    <div class="register-box">
      <h2>Sign up</h2>
      <form method="POST">
        <div class="input-box">
          <label for="username" class="form-label">Username</label>
          <input
            v-model="registerForm.email"
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
            v-model="registerForm.password"
            type="password"
            class="form-control"
            id="password"
            name="password"
            required
          />
        </div>

        <input
          v-model="registerForm.next_url"
          type="hidden"
          class="form-control"
          id="next_url"
          name="next_url"
        />

        <div class="register-btn">
          <button type="submit" @click="submitFrom($event)">Sign up</button>
        </div>

        <p><a href="/login">Back to login</a></p>
      </form>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src

export default {
  name: "RegisterView",
  data() {
    return {
      registerForm: {
        username: "",
        password: "",
        next_url: "/login",
      },
    };
  },
  methods: {
    submitForm(event) {
      event.preventDefault();

      axios.post({
        url: "/register",
        data: {
          username: this.registerForm.email,
          password: this.registerForm.password,
          next_url: this.registerForm.next_url,
        },
        headers: {
          "Content-Type": "application/x-www-form-urlencoded",
        },
      });
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

.register-box {
  width: 20%;
  height: 350px;
  background: white;
  margin: auto;
  margin-top: 5%;
  text-align: center;
  border-radius: 10px;
  padding: 50px 50px;
}

.register-box:hover {
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
</style>
