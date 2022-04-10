<template>
  <!-- <body>
    <div id="title">Neural LEGO</div>

    <div>
      <form @submit.prevent="upload">
        <input id="file" type="file" />
        <button>Upload</button>
      </form>
    </div>

    <div class="box">
      <ul>
        <li>
          <div class="left">
            <a href="/profile">Profile</a>
            <a href="/project" class="Project">Projects</a>
            <a href="/template">Templates</a>
          </div>
        </li>

        <li class="right">
          <div class="search">
            <form>
              <input
                type="text"
                placeholder="Find your project..."
                v-model="search_data"
              />
              <button type="submit" @click="search($event)">Search</button>
            </form>
          </div>

          <div class="project">
            <table class="tabx" border="2" cellspacing="1">
              <tr>
                <td>Porject ID</td>
                <td>Project Nane</td>
                <td>Created Time</td>
                <td>Operation</td>
              </tr>

              <tr v-for="project in project_datail" :key="project.project_ID">
                <td>{{ project.project_ID }}</td>
                <td>{{ project.project_name }}</td>
                <td>{{ project.project_time }}</td>
                <td>
                  <button @click="edit(project.project_ID)">Edit</button>
                  <button @click="delx(project.project_ID)">Delete</button>
                </td>
              </tr>
            </table>
          </div>
        </li>
      </ul>
    </div>
  </body> -->
  <div id="page-top">
    <!-- Page Wrapper -->
    <div id="wrapper">
      <!-- Sidebar -->
      <ul
        class="navbar-nav bg-gradient-primary sidebar sidebar-dark accordion"
        id="accordionSidebar"
      >
        <!-- Sidebar - Brand -->

        <a
          class="sidebar-brand d-flex align-items-center justify-content-center"
        >
          <!-- <div class="sidebar-brand-icon rotate-n-15">
                    <i class="fas fa-laugh-wink"></i>
                </div> -->
          <div class="sidebar-brand-text mx-3">NEURAL LEGO</div>
        </a>

        <!-- Divider -->
        <hr class="sidebar-divider my-0" />

        <!-- Nav Item - Dashboard -->
        <li class="nav-item">
          <a class="nav-link" href="/profile">
            <i class="fas fa-fw fa-user"></i>
            <span>User</span></a
          >
        </li>

        <!-- Divider -->
        <hr class="sidebar-divider my-0" />

        <!-- Nav Item - Dashboard -->
        <li class="nav-item active">
          <a class="nav-link" href="/project">
            <i class="fas fa-fw fa-folder"></i>
            <span>Project</span></a
          >
        </li>

        <!-- Divider -->
        <hr class="sidebar-divider my-0" />

        <!-- Nav Item - Dashboard -->
        <li class="nav-item">
          <a class="nav-link" href="/template">
            <i class="fas fa-fw fa-table"></i>
            <span>Template</span></a
          >
        </li>

        <hr class="sidebar-divider my-0" />

        <!-- Nav Item - Dashboard -->
        <li class="nav-item">
          <a class="nav-link" href="/canvas/">
            <i class="fas fa-fw fa-palette"></i>
            <span>Canvas</span></a
          >
        </li>

        <hr class="sidebar-divider my-0" />

        <!-- Nav Item - Dashboard -->
        <li class="nav-item">
          <a class="nav-link" href="/">
            <i class="fas fa-fw fa-arrow-circle-left"></i>
            <span>Log out</span></a
          >
        </li>

        <!-- Divider -->
        <hr class="sidebar-divider d-none d-md-block" />
      </ul>
      <!-- End of Sidebar -->

      <!-- Content Wrapper -->
      <div id="content-wrapper" class="d-flex flex-column">
        <!-- Main Content -->
        <div id="content">
          <!-- Topbar -->
          <nav
            class="
              navbar navbar-expand navbar-light
              bg-white
              topbar
              mb-4
              static-top
              shadow
            "
          >
            <!-- Sidebar Toggle (Topbar) -->
            <button
              id="sidebarToggleTop"
              class="btn btn-link d-md-none rounded-circle mr-3"
            >
              <i class="fa fa-bars"></i>
            </button>

            <!-- Topbar Search -->
            <form
              class="
                d-none d-sm-inline-block
                form-inline
                mr-auto
                ml-md-3
                my-2 my-md-0
                mw-100
                navbar-search
              "
            >
              <div class="input-group">
                <input
                  v-model="search_data"
                  type="text"
                  class="form-control bg-light border-0 small"
                  placeholder="Search for..."
                  aria-label="Search"
                  aria-describedby="basic-addon2"
                />
                <div class="input-group-append">
                  <button
                    class="btn btn-primary"
                    type="button"
                    @click="search()"
                  >
                    <i class="fas fa-search fa-sm"></i>
                  </button>
                </div>
              </div>
            </form>
          </nav>
          <!-- End of Topbar -->

          <!-- Begin Page Content -->
          <div class="container-fluid">
            <!-- Project Card Example -->
            <div class="card shadow mb-4">
              <div class="card-header py-3">
                <h6 class="m-0 font-weight-bold text-primary">Projects</h6>
              </div>
              <div class="card-body">
                <div class="table-responsive-lg">
                  <table class="table table-hover">
                    <thead class="thead-dark">
                      <tr>
                        <th scope="col">ID</th>
                        <th scope="col">Name</th>
                        <th scope="col">Time</th>
                        <th scope="col">Operation</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr
                        v-for="project in project_datail"
                        :key="project.project_ID"
                      >
                        <th scope="col">{{ project.project_ID }}</th>
                        <td>
                          <button
                            type="button"
                            class="btn btn-link"
                            @click="enterCanvas(project.project_ID)"
                          >
                            {{ project.project_name }}
                          </button>
                        </td>

                        <td>
                          <button type="button" class="btn btn-link" disabled>
                            {{ project.project_time }}
                          </button>
                        </td>
                        <td>
                          <button
                            class="btn btn-warning"
                            @click="enterCanvas(project.project_ID)"
                          >
                            Edit</button
                          >&ensp;
                          <button
                            class="btn btn-danger"
                            @click="remove(project.project_ID)"
                          >
                            Delete
                          </button>
                        </td>
                      </tr>
                    </tbody>
                  </table>
                </div>

                <!-- End of Sidebar -->
              </div>
            </div>
          </div>
        </div>
        <!-- End of Content Wrapper -->
      </div>
      <!-- End of Page Wrapper -->

      <!-- Logout Modal-->
      <div
        class="modal fade"
        id="logoutModal"
        tabindex="-1"
        role="dialog"
        aria-labelledby="exampleModalLabel"
        aria-hidden="true"
      >
        <div class="modal-dialog" role="document">
          <div class="modal-content">
            <div class="modal-header">
              <h5 class="modal-title" id="exampleModalLabel">
                Ready to Leave?
              </h5>
              <button
                class="close"
                type="button"
                data-dismiss="modal"
                aria-label="Close"
              >
                <span aria-hidden="true">×</span>
              </button>
            </div>
            <div class="modal-body">
              Select "Logout" below if you are ready to end your current
              session.
            </div>
            <div class="modal-footer">
              <button
                class="btn btn-secondary"
                type="button"
                data-dismiss="modal"
              ></button>
              <a class="btn btn-primary" href="/login">Logout</a>
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
  name: "ProjectView",
  data() {
    return {
      page_name: "project_page",
      search_data: "",
      project_datail: [
        { project_ID: "1", project_name: "name", project_time: "time" },
        { project_ID: "2", project_name: "name", project_time: "time" },
      ],
    };
  },
  mounted() {
    // Fetch tasks on page load
    this.getData();
  },
  methods: {
    getData() {
      // 向后端发送一个请求，res是后端发给前端的数据
      axios({
        method: "get",
        url: "/project/",
        params: { pk: 123 },
      }).then((res) => {
        console.log(JSON.stringify(res));

        if (res.data.status == 200) {
          // window.location = "/project/";
          this.project_datail = res.data.project_datail;
        } else {
          alert("error");
        }
      });
    },

    upload() {
      var form_data = new FormData();
      var file = document.getElementById("file").files[0];
      form_data.append("file", file, file.name);

      axios({
        method: "post",
        url: "/project/upload/",
        data: form_data,
        headers: { "Content-Type": "multipart/form-data" },
      })
        .then((response) => {
          console.log("response:");
        })
        .catch((error) => {
          console.log(error);
        });
    },

    search() {
      console.log("sending search_data");
      // Declare a form
      let formData = new FormData();
      formData.append("page_name", this.page_name);
      formData.append("search_data", this.search_data);

      // Send form to backend and get response data
      axios({
        method: "post",
        url: "/project/search/",
        data: formData,
      }).then((res) => {
        // if (res.data.isLogin == true) {
        //   console.log("login ok!");
        // } else {
        //   console.log("login fail!");
        // }
        console.log(res.data);
      });
    },

    enterCanvas(id) {
      console.log("sending id");
    },

    remove(id) {
      console.log("sending id");
    },
  },
};
</script>

<style scoped src="../../new_pages/vendor/fontawesome-free/css/all.min.css"></style>
<style scoped src="../../new_pages/css/sb-admin-2.min.css"></style>