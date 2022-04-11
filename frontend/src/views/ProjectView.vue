<template>
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
                  v-model="search_keyword"
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

            <ul class="navbar-nav ms-auto">
              <li class="nav-item">
                <button
                  class="btn btn-primary"
                  type="button"
                  @click="showModal()"
                >
                  New
                </button>
              </li>
              &ensp;
              <li class="nav-item">
                <button
                  class="btn btn-primary"
                  type="file"
                  @click="openProject()"
                >
                  Open
                </button>

                <input
                  type="file"
                  class="form-control-file"
                  ref="fileRef"
                  id="file"
                  v-show="false"
                  @change="uploadProject()"
                />
              </li>
            </ul>
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
                        <th scope="col"></th>
                        <th scope="col">Name</th>
                        <th scope="col">Time</th>
                        <th scope="col">Operation</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr v-for="proj in proj_data" :key="proj.project_ID">
                        <th scope="col">{{ proj.project_ID }}</th>
                        <td>
                          <button
                            type="button"
                            class="btn btn-link"
                            @click="enterCanvas(proj)"
                          >
                            {{ proj.project_name }}
                          </button>
                        </td>

                        <td>
                          <button type="button" class="btn btn-link" disabled>
                            {{ proj.last_save_time }}
                          </button>
                        </td>
                        <td>
                          <button
                            class="btn btn-warning"
                            @click="enterCanvas(proj)"
                          >
                            Edit</button
                          >&ensp;
                          <button class="btn btn-danger" @click="remove(proj)">
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

    <!-- Modal -->
    <div class="modal-container" v-show="isModalVisible">
      <div class="modal-dialog" role="document">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="exampleModalLabel">New project</h5>
            <button
              type="button"
              class="close"
              data-dismiss="modal"
              aria-label="Close"
              @click="closeModal()"
            >
              <span aria-hidden="true">&times;</span>
            </button>
          </div>
          <!-- create -->
          <form>
            <div class="modal-body">
              <div class="form-group">
                <label for="name">Project Name</label>
                <input
                  type="text"
                  class="form-control"
                  placeholder="Enter project name.."
                  v-model="new_proj.name"
                />
              </div>

              <div class="form-check">
                <input
                  type="checkbox"
                  class="form-check-input"
                  id="share-to-public"
                  v-model="new_proj.is_public"
                />
                <label class="form-check-label" for="exampleCheck1"
                  >Share to public?</label
                >
              </div>
            </div>

            <div class="modal-footer">
              <button
                type="button"
                class="btn btn-secondary"
                data-dismiss="modal"
                @click="closeModal()"
              >
                Close
              </button>
              <button
                type="button"
                class="btn btn-primary"
                @click="newProject()"
              >
                Create
              </button>
            </div>
          </form>
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
      new_proj: {
        name: "",
        is_public: "",
      },
      page_name: "project_page",
      search_keyword: "",
      proj_data: {},
      isModalVisible: false,
    };
  },
  mounted() {
    // Fetch tasks on page load
    this.getData();
  },
  methods: {
    getData() {
      axios({
        method: "get",
        url: "/project/" + localStorage.uid + "/",
      }).then((res) => {
        console.log(res.data);
        if (res.data.status == 200) {
          this.proj_data = res.data.project_detail;
          console.log(res.data.project_detail);
          console.log(this.proj_data);
        } else {
          alert("project loading error!");
        }
      });
    },

    showModal() {
      this.isModalVisible = true;
    },

    closeModal() {
      this.isModalVisible = false;
    },

    newProject() {
      let formData = new FormData();
      formData.append("name", this.new_proj.name);
      formData.append("is_public", this.new_proj.is_public);

      axios({
        method: "post",
        url: "/project/create/" + localStorage.uid + "/",
        data: formData,
      }).then((res) => {
        console.log(res.data);
        if (res.data.status == "200") {
          console.log("create ok!");
          this.getData();
          location.replace("/project/");
        } else {
          console.log("create fail!");
        }
      });
    },

    openProject() {
      this.$refs.fileRef.dispatchEvent(new MouseEvent("click"));
    },

    uploadProject() {
      var form_data = new FormData();
      var file = document.getElementById("file").files[0];
      form_data.append("file", file, file.name);

      axios({
        method: "post",
        url: "/project/upload/" + localStorage.uid + "/",
        data: form_data,
        headers: { "Content-Type": "multipart/form-data" },
      }).then((res) => {
        console.log(res.data);
        if (res.data.status == "200") {
          console.log("upload ok!");
          this.getData();
          location.replace("/project/");
        } else {
          alert.log("upload fail!");
          location.replace("/project/");
        }
      });
    },

    search() {
      let formData = new FormData();
      formData.append("page_name", this.page_name);
      formData.append("keyword", this.search_keyword);

      axios({
        method: "post",
        url: "/project/search/" + localStorage.uid + "/",
        data: formData,
      }).then((res) => {
        console.log(res.data);
        if (res.data.status == "200") {
          this.proj_data = res.data.project_datail;
          this.getData();
          location.replace("/project/");
        } else if (res.data.status == "500") {
          console.log("Something wrong...");
        }
      });
    },

    remove(proj) {
      console.log("Remove id:" + proj.project_id);

      let formData = new FormData();
      formData.append("project_id", proj.project_id);

      axios({
        method: "post",
        url:
          "/project/remove/" + localStorage.uid + "/" + proj.project_id + "/",
        data: formData,
      }).then((res) => {
        console.log(res.data);
        if (res.data.status == "200") {
          this.proj_data = res.data.project_datail;
          this.getData();
          location.replace("/project/");
        } else if (res.data.status == "500") {
          console.log("Something wrong...");
        }
      });
    },

    enterCanvas(proj) {
      localStorage.pid = proj.project_id;
      location.replace("/canvas/");
    },
  },
};
</script>

<style scoped src="../../new_pages/vendor/fontawesome-free/css/all.min.css"></style>
<style scoped src="../../new_pages/css/sb-admin-2.min.css"></style>

<style scoped>
.modal-container {
  position: absolute;
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
}
.modal-dialog {
  position: relative;
  align-self: center;
}
</style>