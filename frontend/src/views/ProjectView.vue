<template>
  <body>
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
  </body>
</template>

<script>
import axios from "axios";

export default {
  name: "ProjectView",
  data() {
    return {
      page_name: "project_page",
      search_data: "",
      project_datail: {},
    };
  },
  created() {
    // Fetch tasks on page load
    this.getData();
  },
  methods: {
    getData() {
      // 向后端发送一个请求，res是后端发给前端的数据
      axios({
        method: "get",
        url: "/project/",
      }).then((res) => {
        console.log(JSON.stringify(res));
        if (res.data.status == 200) {
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

    search(event) {
      event.preventDefault();

      axios({
        method: "post",
        url: "/project/search/",
        data: {
          page_name: this.page_name,
          keyword: this.search_data,
        },
      });
    },
  },
};
</script>


<style scoped>
body {
  background: #00000020;
  margin: 0%;
}

* {
  margin: 0;
  padding: 0;
}

#title {
  background: #5f6298;
  font-size: 50px;
  color: white;
}

#btn1 {
  width: 8%;
  height: 40px;
  border-radius: 20px;
  border: medium solid white;
  background-color: #5f6298;
  color: white;
  font-size: 15px;
  text-decoration: none;
  vertical-align: 60%;
  text-align: center;
  /* display: inline-block; */
  margin-left: 50%;
}

#btn2 {
  width: 8%;
  height: 40px;
  border-radius: 20px;
  border: medium solid white;
  background-color: #5f6298;
  color: white;
  font-size: 15px;
  text-decoration: none;
  vertical-align: 60%;
}

li {
  list-style: none;
}

.box {
  height: 460px;
  width: 1200px;
  background-color: none;
  margin: 0;
}

.box li {
  float: left;
  margin-right: 10px;
}

.box .right {
  width: 700px;
}

.left {
  width: 230px;
  height: 460px;
  background-color: #55585a;
}

.left a {
  display: block;
  width: 190px;
  height: 80px;
  background-color: #55585a;
  font-size: 20px;
  color: white;
  text-decoration: none;
  line-height: 80px;
  padding-left: 40px;
}

.left .Project {
  background-color: #292a2b;
}

.left a:hover {
  background-color: #292a2b;
}

.search {
  background-color: none;
}

.search .check {
  border: 10;
  width: 30%;
  font-size: 20px;
  background: white;
  border-radius: 10px;
  padding: 5px 10px;
  margin-top: 20px;
  margin-left: 20px;
  margin-bottom: 20px;
}

.project {
  width: 540px;
  height: 150px;
  background-color: white;
  border-width: 2px;
  border-style: solid;
  margin-left: 20px;
}

.project p {
  margin-left: 20px;
  margin-top: 20px;
  font-size: 20px;
  color: blue;
}

.project .projectcontent {
  word-wrap: break-word;
  word-break: normal;
  margin-left: 20px;
  font-size: 20px;
}

.line2 {
  width: 500px;
  height: 2px;
  background-image: linear-gradient(
    to right,
    #000 0%,
    #000 50%,
    transparent 75%
  );
  background-size: 20px 10px;
  background-repeat: repeat-x;
  margin-left: 20px;
}
</style>
