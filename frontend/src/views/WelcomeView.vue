<template>
  <div id="page-top">
    <!-- Navigation-->
    <nav class="navbar navbar-expand-lg navbar-dark navbar-custom fixed-top">
      <div class="container px-5">
        <a class="navbar-brand">Neural Lego</a>
        <button
          class="navbar-toggler"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#navbarResponsive"
          aria-controls="navbarResponsive"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarResponsive">
          <ul class="navbar-nav ms-auto">
            <li class="nav-item">
              <a class="nav-link" href="/login/">Log In</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="/register/">Register</a>
            </li>
          </ul>
        </div>
      </div>
    </nav>

    <header class="masthead d-flex align-items-center bg-gradient-primary">
      <div class="container px-4 px-lg-5">
        <h1 class="mb-1">Neural Lego</h1>
        <h3 class="mb-5">
          <em>Building Block for Artificial Intelligence</em>
        </h3>
      </div>
    </header>
    <!-- Content section 1-->
    <section id="scroll">
      <div class="container px-5">
        <div class="row gx-5 align-items-center">
          <div class="col-lg-6 order-lg-2">
            <div class="p-5">
              <img
                class="img-fluid rounded-circle"
                src="img/c3po.jpg"
                alt="..."
              />
            </div>
          </div>
          <div class="col-lg-6 order-lg-1">
            <div class="p-5">
              <h2 class="display-4">For AI beginners...</h2>
              <p>
                As artificial intelligence advances, a rising number of people
                from various industries and research fields are keen to master
                deep learning. Our project is tailored for all those AI
                enthusiasts, whether novices or specialists, allowing them to
                develop AI models without writing any code.
              </p>
            </div>
          </div>
        </div>
      </div>
    </section>
    <!-- Content section 2-->
    <section>
      <div class="container px-5">
        <div class="row gx-5 align-items-center">
          <div class="col-lg-6">
            <div class="p-5">
              <img
                class="img-fluid rounded-circle"
                src="img/blocks.jpg"
                alt="..."
              />
            </div>
          </div>
          <div class="col-lg-6">
            <div class="p-5">
              <h2 class="display-4">Like building blocks</h2>
              <p>
                Concretely, considering that constructing an AI model comes with
                a lot of repeatability and modularity, such as data
                preprocessing, network construction and result visualization, we
                facilitate users to build models by drawing a flowchart of the
                network topology via graphical interfaces.
              </p>
            </div>
          </div>
        </div>
      </div>
    </section>
    <!-- Content section 3-->
    <section>
      <div class="container px-5">
        <div class="row gx-5 align-items-center">
          <div class="col-lg-6 order-lg-2">
            <div class="p-5">
              <img
                class="img-fluid rounded-circle"
                src="img/logo.jpg"
                alt="..."
              />
            </div>
          </div>
          <div class="col-lg-6 order-lg-1">
            <div class="p-5">
              <h2 class="display-4">We are group 35</h2>
              <p>
                Pin Qian
                &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                Haonan Wang
              </p>
              <p>
                Qirui Bao &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                Shujie Yang
              </p>
              <p>
                Ruijie Ye
                &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                Haomiao Ji
              </p>
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
// export default {
//   name: 'WelcomeView',
//   components: {
//     Welcome
//   }
// }
</script>




<!-- Add "scoped" attribute to limit CSS to this component only -->
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
<style scoped src="../../new_pages/css/style_home.css"></style>