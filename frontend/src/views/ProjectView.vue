<template>
  <body>
    <div id="title">
      Neural LEGO
      <input id="btn1" type="button" value="open" onClick="location.href='#'" />
      <input
        id="btn2"
        type="button"
        value="new project"
        onClick="location.href='#'"
      />
    </div>
    <div class="box">
      <ul>
        <li>
          <div class="left">
            <a href="/profile">User name</a>
            <a href="#" class="Project">Projects</a>
            <a href="#">Datasets</a>
            <a href="#">Templates</a>
          </div>
        </li>
        <li class="right">
          <div class="search">
            <input class="check" type="text" placeholder="search" />
          </div>
          <div class="project">
            <p>title</p>
            <div class="line2"></div>
            <div class="projectcontent"></div>
          </div>
        </li>
      </ul>
    </div>
  </body>
</template>

<script>
export default {
  name: "ProjectView",
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
    background-image: linear-gradient(to right, #000 0%, #000 50%, transparent 75%);
    background-size: 20px 10px;
    background-repeat: repeat-x;
    margin-left: 20px;
}
</style>
