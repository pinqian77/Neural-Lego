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
        <li class="nav-item">
          <a class="nav-link" href="/project">
            <i class="fas fa-fw fa-folder"></i>
            <span>Project</span></a
          >
        </li>

        <li class="nav-item active">
          <a class="nav-link" href="/dataset">
            <i class="fas fa-fw fa-folder"></i>
            <span>Dataset</span></a
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
                  type="file"
                  @click="openProject()"
                >
                  Upload
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
                <h6 class="m-0 font-weight-bold text-primary">Datasets</h6>
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
                      <tr v-for="ds in dataset_data" :key="ds.id">
                        <th scope="col"></th>
                        <td>
                          <button type="button" class="btn btn-link" disabled>
                            {{ ds.dataset_name }}
                          </button>
                        </td>

                        <td>
                          <button type="button" class="btn btn-link" disabled>
                            {{ ds.upload_time }}
                          </button>
                        </td>
                        <td>
                          <button class="btn btn-warning" disabled>Edit</button
                          >&ensp;
                          <button class="btn btn-danger" @click="remove(ds)">
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
  name: "DatasetView",

  data() {
    return {
      page_name: "dataset_page",
      search_keyword: "",
      dataset_data: {},

      isModalVisible: false,
    };
  },
  mounted() {
    // Fetch data on page load
    this.getData();
  },

  methods: {
    // 200
    getData() {
      axios({
        method: "get",
        url: "/dataset/" + localStorage.uid + "/",
      }).then((res) => {
        console.log(res.data);
        if (res.data.status == 200) {
          this.dataset_data = res.data.dataset_detail;
        } else {
          alert("dataset loading error!");
        }
      });
    },

    // 200
    openProject() {
      this.$refs.fileRef.dispatchEvent(new MouseEvent("click"));
    },

    // 200
    uploadProject() {
      var form_data = new FormData();
      var file = document.getElementById("file").files[0];
      form_data.append("file", file, file.name);

      axios({
        method: "post",
        url: "/dataset/upload/" + localStorage.uid + "/",
        data: form_data,
        headers: { "Content-Type": "multipart/form-data" },
      }).then((res) => {
        console.log(res.data);
        if (res.data.status == "200") {
          console.log("upload ok!");
        } else {
          alert.log("upload fail!");
        }
      });
      location.replace("/dataset/");
    },

    // 200
    search() {
      let formData = new FormData();
      formData.append("page_name", this.page_name);
      formData.append("keyword", this.search_keyword);

      axios({
        method: "post",
        url: "/dataset/search/" + localStorage.uid + "/",
        data: formData,
      }).then((res) => {
        console.log(res.data);
        if (res.data.status == "200") {
          this.dataset_data = res.data.dataset_datail;
        } else if (res.data.status == "500") {
          console.log("Something wrong...");
        }
        location.replace("/dataset/");
      });
    },

    // 200
    remove(proj) {
      let formData = new FormData();
      formData.append("dataset_id", proj.id);

      axios({
        method: "post",
        url: "/dataset/remove/" + localStorage.uid + "/" + proj.id + "/",
        data: formData,
      }).then((res) => {
        console.log(res.data);
        if (res.data.status == "200") {
          this.dataset_data = res.data.dataset_datail;
        } else if (res.data.status == "500") {
          console.log("Something wrong...");
        }
        location.replace("/dataset/");
      });
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
