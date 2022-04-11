<template>
  <body id="page-top">
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
        <li class="nav-item">
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
        <li class="nav-item active">
          <a class="nav-link" href="/canvas">
            <i class="fas fa-fw fa-palette"></i>
            <span>Canvas</span></a
          >
        </li>

        <hr class="sidebar-divider my-0" />

        <!-- Nav Item - Dashboard -->
        <li class="nav-item">
          <a class="nav-link" href="/welcome">
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
                  type="text"
                  class="form-control bg-light border-0 small"
                  placeholder="Search for..."
                  aria-label="Search"
                  aria-describedby="basic-addon2"
                />
                <div class="input-group-append">
                  <button class="btn btn-primary" type="button">
                    <i class="fas fa-search fa-sm"></i>
                  </button>
                </div>
              </div>
            </form>

            <!-- Topbar Navbar -->
            <ul class="navbar-nav ml-auto">
              <!-- Nav Item - Search Dropdown (Visible Only XS) -->
              <li class="nav-item dropdown no-arrow d-sm-none">
                <a
                  class="nav-link dropdown-toggle"
                  href="#"
                  id="searchDropdown"
                  role="button"
                  data-toggle="dropdown"
                  aria-haspopup="true"
                  aria-expanded="false"
                >
                  <i class="fas fa-search fa-fw"></i>
                </a>
                <!-- Dropdown - Messages -->
                <div
                  class="
                    dropdown-menu dropdown-menu-right
                    p-3
                    shadow
                    animated--grow-in
                  "
                  aria-labelledby="searchDropdown"
                >
                  <form class="form-inline mr-auto w-100 navbar-search">
                    <div class="input-group">
                      <input
                        type="text"
                        class="form-control bg-light border-0 small"
                        placeholder="Search for..."
                        aria-label="Search"
                        aria-describedby="basic-addon2"
                      />
                      <div class="input-group-append">
                        <button class="btn btn-primary" type="button">
                          <i class="fas fa-search fa-sm"></i>
                        </button>
                      </div>
                    </div>
                  </form>
                </div>
              </li>
            </ul>
          </nav>
          <!-- End of Topbar -->

          <!-- Begin Page Content -->
          <div class="container-fluid">
            <div class="row">
              <div class="col-xl-10 col-lg-5">
                <div class="card shadow mb-4">
                  <!-- Card Header - Dropdown -->
                  <div
                    class="
                      card-header
                      py-3
                      d-flex
                      flex-row
                      align-items-center
                      justify-content-between
                    "
                  >
                    <h6 class="m-0 font-weight-bold text-primary">Setting</h6>
                  </div>
                  <!-- Sidebar -->
                  <!-- <ul class="navbar-nav bg-gradient-primary sidebar sidebar-dark accordion" id="accordionSidebar"> -->
                  <ul id="accordionSidebar">
                    <!-- Nav Item - Pages Collapse Menu -->
                    <li class="nav-item">
                      <a
                        class="nav-link collapsed"
                        href="#"
                        data-toggle="collapse"
                        data-target="#collapseTwo"
                        aria-expanded="true"
                        aria-controls="collapseTwo"
                      >
                        <i class="fas fa-fw fa-cog"></i>
                        <span>Dataset</span>
                      </a>
                      <div
                        id="collapseTwo"
                        class="collapse"
                        aria-labelledby="headingTwo"
                        data-parent="#accordionSidebar"
                      >
                        <div class="form-group col-lg-2">
                          <label for="dataset">select dataset:</label>
                          <select
                            v-model="config.dataset"
                            class="form-control"
                            id="dataset"
                          >
                            <option
                              v-for="ds in dataset_data"
                              :key="ds.id"
                              :label="ds.dataset_name"
                              :value="ds.dataset_name"
                            ></option>
                          </select>
                        </div>
                      </div>
                    </li>

                    <!-- Nav Item - Pages Collapse Menu -->
                    <li class="nav-item">
                      <a
                        class="nav-link collapsed"
                        href="#"
                        data-toggle="collapse"
                        data-target="#collapseTwo"
                        aria-expanded="true"
                        aria-controls="collapseTwo"
                      >
                        <i class="fas fa-fw fa-cog"></i>
                        <span>Optimizer</span>
                      </a>
                      <div
                        id="collapseTwo"
                        class="collapse"
                        aria-labelledby="headingTwo"
                        data-parent="#accordionSidebar"
                      >
                        <div class="form-group col-lg-2">
                          <label for="sel1">select optimizer:</label>
                          <select
                            class="form-control"
                            id="sel1"
                            v-model="config.optimizer"
                          >
                            <option value="Adam">Adam</option>
                            <option value="SGD">SGD</option>
                            <option value="Adagrad">Adagrad</option>
                          </select>
                        </div>
                      </div>
                    </li>

                    <!-- Nav Item - Pages Collapse Menu -->
                    <li class="nav-item">
                      <a
                        class="nav-link collapsed"
                        href="#"
                        data-toggle="collapse"
                        data-target="#collapsePages"
                        aria-expanded="true"
                        aria-controls="collapsePages"
                      >
                        <i class="fas fa-fw fa-wrench"></i>
                        <span>Hyperparameters</span>
                      </a>
                      <div
                        id="collapsePages"
                        class="collapse"
                        aria-labelledby="headingPages"
                        data-parent="#accordionSidebar"
                      >
                        <div class="bg-white py-2 collapse-inner rounded">
                          <div class="form-group">
                            <div class="col-lg-2">
                              <label for="ex1">learning rate</label>
                              <input
                                class="form-control input-sm"
                                id="ex1"
                                type="text"
                                v-model="config.lr"
                              />
                            </div>
                            <div class="col-lg-2">
                              <label for="ex2">test batch size</label>
                              <input
                                class="form-control input-sm"
                                id="ex2"
                                type="text"
                                v-model="test_batch_size"
                              />
                            </div>
                            <div class="col-lg-2">
                              <label for="ex3">batch size</label>
                              <input
                                class="form-control input-sm"
                                id="ex3"
                                type="text"
                                v-model="batch_size"
                              />
                            </div>
                            <div class="col-lg-2">
                              <label for="ex3">epoch</label>
                              <input
                                class="form-control input-sm"
                                id="ex3"
                                type="text"
                                v-model="epoch"
                              />
                            </div>
                            <div class="col-lg-2">
                              <label for="ex3">seed</label>
                              <input
                                class="form-control input-sm"
                                id="ex3"
                                type="text"
                                v-model="seed"
                              />
                            </div>
                          </div>
                        </div>
                      </div>
                    </li>

                    <li class="nav-item">
                      <a class="nav-link collapsed">
                        <button
                          type="submit"
                          class="btn btn-primary"
                          @click="apply()"
                        >
                          Apply
                        </button>
                      </a>
                      <!-- <button>Apply</button> -->
                    </li>
                  </ul>
                  <!-- End of Sidebar -->
                </div>
              </div>

              <div class="container-fluid">
                <div class="row">
                  <div class="col-xl-10 col-lg-5">
                    <div class="card shadow mb-4">
                      <!-- Card Header - Dropdown -->
                      <div
                        class="
                          card-header
                          py-3
                          d-flex
                          flex-row
                          align-items-center
                          justify-content-between
                        "
                      >
                        <h6 class="m-0 font-weight-bold text-primary">
                          progress
                        </h6>

                        <div class="col-xl-10 col-lg-5">
                          <!-- progress bar -->
                          <div class="progress">
                            <div
                              class="
                                progress-bar
                                progress-bar-striped
                                progress-bar-animated
                              "
                              role="progressbar"
                              style="width: 25%"
                              aria-valuenow="25"
                              aria-valuemin="0"
                              aria-valuemax="100"
                            >
                              25%
                            </div>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>

              <!-- Area Chart -->
              <div class="col-xl-5 col-lg-5">
                <div class="card shadow mb-4">
                  <!-- Card Header - Dropdown -->
                  <div
                    class="
                      card-header
                      py-3
                      d-flex
                      flex-row
                      align-items-center
                      justify-content-between
                    "
                  >
                    <h6 class="m-0 font-weight-bold text-primary">
                      Accuracy Curve
                    </h6>
                  </div>
                  <!-- Card Body -->
                  <div class="card-body">
                    <a href="#"
                      ><img
                        class="card-img-top"
                        src="https://dummyimage.com/450x300/dee2e6/6c757d.jpg"
                        alt="..."
                    /></a>
                  </div>
                </div>
              </div>

              <!-- Area Chart -->
              <div class="col-xl-5 col-lg-5">
                <div class="card shadow mb-4">
                  <!-- Card Header - Dropdown -->
                  <div
                    class="
                      card-header
                      py-3
                      d-flex
                      flex-row
                      align-items-center
                      justify-content-between
                    "
                  >
                    <h6 class="m-0 font-weight-bold text-primary">ROC Curve</h6>
                  </div>
                  <!-- Card Body -->
                  <div class="card-body">
                    <a href="#"
                      ><img
                        class="card-img-top"
                        src="https://dummyimage.com/450x300/dee2e6/6c757d.jpg"
                        alt="..."
                    /></a>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <!-- End of Content Wrapper -->
    </div>
    <!-- End of Page Wrapper -->
  </body>
</template>

<script>
export default {
  name: "ConfigView",
  data() {
    return {
      config: {
        dataset: "",
        optimizer: "",
        lr: 0.0,
        test_batch_size: 0,
        batch_size: 0,
        epoch: 0,
        seed: 0,
      },
      dataset_data: {},
    };
  },

  // mounted() {
  //   this.getData();
  // },

  methods: {
    getData() {
      getDatasetName();

      axios({
        method: "get",
        url: "/train/" + localStorage.uid + "/" + localStorage.pid + "/",
      }).then((res) => {
        console.log(res.data);
        if (res.data.status == 200) {
          this.config.optimizer = res.data.optimizer;
          this.config.lr = res.data.lr;
          this.config.test_batch_size = res.data.test_batch_size;
          this.config.batch_size = res.data.batch_size;
          this.config.epoch = res.data.epoch;
          this.config.seed = res.data.seed;
          this.config.dataset = res.data.dataset_name;
        } else {
          alert("project loading error!");
        }
      });
    },

    getDatasetName() {
      axios({
        method: "get",
        url: "/dataset/" + localStorage.uid + "/",
      }).then((res) => {
        if (res.data.status == 200) {
          this.dataset_data = res.data.dataset_detail;
        } else {
          alert("dataset loading error!");
        }
      });
    },

    apply() {
      var form_data = new FormData();
      var dataset = document.getElementById("dataset").files[0];

      form_data.append("dataset", dataset, dataset.name);
      form_data.append("config", this.config);

      axios({
        method: "post",
        url: "/train/apply/" + localStorage.uid + "/" + localStorage.pid + "/",
        data: form_data,
        headers: { "Content-Type": "multipart/form-data" },
      }).then((res) => {
        console.log(res.data);
        if (res.data.status == "200") {
          console.log("apply ok!");
          this.getData();
        } else {
          alert.log("apply fail!");
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
