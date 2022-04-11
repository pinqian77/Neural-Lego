<template>
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

                <div class="form-group row"></div>
                <div class="form-group">
                  <input
                    v-model="registerForm.username"
                    type="text"
                    class="form-control form-control-user"
                    id="username"
                    name="username"
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
                      v-model="registerForm.repeat_password"
                      type="password"
                      class="form-control form-control-user"
                      id="exampleRepeatPassword"
                      placeholder="Repeat Password"
                      required
                    />
                  </div>
                </div>
                <button
                  type="submit"
                  class="btn btn-primary btn-user btn-block"
                  @click="submitForm()"
                >
                  Register Account
                </button>
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
import axios from "axios";

export default {
  name: "RegisterView",

  data() {
    return {
      registerForm: {
        username: "",
        password: "",
        repeat_password: "",
      },
    };
  },

  methods: {
    // 200
    submitForm() {
      if (this.registerForm.password != this.registerForm.repeat_password) {
        alert("The entered password is inconsistent!");
        return;
      }

      // Declare a form
      let formData = new FormData();
      formData.append("username", this.registerForm.username);
      formData.append("password", this.registerForm.password);

      // Send form to backend and get response data
      axios({
        method: "post",
        url: "/register/",
        data: formData,
      }).then((res) => {
        if (res.data.status == "200") {
          console.log("register ok!");
          location.replace("/login/");
        } else if (res.data.status == "500") {
          alert("Not an unique username!");
        } else {
          console.log("register fails...");
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
