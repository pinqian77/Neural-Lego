<template>
  <!-- old version -->
  <!-- <div class="container">
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
  </div> -->

  <div class="body bg-gradient-primary">
    <div class="container">
      <div class="card o-hidden border-0 shadow-lg my-5">
        <div class="card-body p-0">
          <!-- Nested Row within Card Body -->
          <div class="row">
            <div class="col-lg-5 d-none d-lg-block bg-register-image"></div>
            <div class="col-lg-7">
              <div class="p-5">
                <div class="text-center">
                  <h1 class="h4 text-gray-900 mb-4">Create an Account!</h1>
                </div>
                <form class="user">
                  <div class="form-group row"></div>
                  <div class="form-group">
                    <input
                      v-model="registerForm.email"
                      type="username"
                      class="form-control form-control-user"
                      id="username"
                      name="username"
                      requiredtype="email"
                      placeholder="Username"
                      required
                    />
                  </div>
                  <div class="form-group row">
                    <div class="col-sm-6 mb-3 mb-sm-0">
                      <input
                        v-model="registerForm.password"
                        type="password"
                        class="form-control form-control-user"
                        placeholder="Password"
                        id="password"
                        name="password"
                        required
                      />
                    </div>
                    <div class="col-sm-6">
                      <input
                        type="password"
                        class="form-control form-control-user"
                        id="exampleRepeatPassword"
                        placeholder="Repeat Password"
                      />
                    </div>
                    <input
                      v-model="registerForm.next_url"
                      type="hidden"
                      class="form-control"
                      id="next_url"
                      name="next_url"
                    />
                  </div>
                  <button
                    type="submit"
                    class="btn btn-primary btn-user btn-block"
                    @click="submitFrom($event)"
                  >
                    Register Account
                  </button>
                </form>
                <hr />

                <div class="text-center">
                  <a class="small" href="/login"
                    >Already have an account? Login!</a
                  >
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
