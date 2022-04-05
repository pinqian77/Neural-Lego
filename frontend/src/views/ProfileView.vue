<template>
<body>
    <div id="title">
        Neural LEGO
    </div>
    <div class="box">
        <ul>
            <li>
                <div class="left">
                    <a href="#" class="Username">User name</a>
                    <a href="/project">Projects</a>
                    <a href="#">Datasets</a>
                    <a href="#">Templates</a>
                </div>
            </li>
            <li class="middle">
                <div class='avatar'>
                    <img src="" alt="">
                </div>
                <div class="username">
                    username
                </div>
                <div>
                    <input id="btn" type="button" value="edit profile">
                </div>
                <div>
                    <ul>
                        <li><img src="../assets/follow.png" width="60px"></li>
                        <li class="follow">
                            following<br> follower
                        </li>
                    </ul>
                </div>
            </li>
            <li>
                <div class="line1"></div>
            </li>
            <li class="right">
                <div class="star"><img src="../assets/star.png" width="60px">stars</div>
                <div class="line2"></div>

                <div>list</div>
                <div class="list">
                    <p>list</p>
                    <div class="line2"></div>
                    <div class="listcontent"></div>
                </div>

                <div>project</div>
                <div class="project">
                    <p>test</p>
                    <div class="line2"></div>
                    <div class="projectcontent"></div>
                </div>
            </li>
        </ul>
    </div>

</body>
</template>

<script>
// @ is an alias to /src

export default {
  name: 'ProfileView',
}
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

.left .Username {
    background-color: #292a2b;
}

.left a:hover {
    background-color: #292a2b;
}

.box .middle {
    width: 300px;
}

.middle div {
    margin-top: 10px;
}

.avatar {
    width: 100px;
    height: 100px;
}

.avatar img {
    width: 100%;
    height: 100%;
    border-radius: 50px;
    background-color: aquamarine;
}

.username {
    font-size: 25px;
    margin-top: 20px;
}

.middle #btn {
    width: 150px;
    height: 40px;
    border-radius: 10px;
    border: 0;
    background-color: rgb(252, 135, 1);
    /* background-image: linear-gradient(to top, #30324d 0%, #5f6298 100%); */
    color: black;
    font-size: 25px;
    text-decoration: none;
    margin-top: 20px;
}

.follow {
    font-size: 25px;
}

.line1 {
    background: black;
    width: 3px;
    height: 500px;
    position: relative;
}

.right div {
    margin-left: 20px;
    margin-top: 10px;
    font-size: 25px;
}

.line2 {
    width: 500px;
    height: 2px;
    background-image: linear-gradient(to right, #000 0%, #000 50%, transparent 75%);
    background-size: 20px 10px;
    background-repeat: repeat-x;
}

.list {
    width: 540px;
    height: 150px;
    background-color: white;
    border-radius: 40px;
    border-width: 2px;
    border-style: solid;
}

.list p {
    margin-left: 20px;
    margin-top: 20px;
    font-size: 20px;
    color: blue;
}

.list .listcontent {
    word-wrap: break-word;
    word-break: normal;
    margin-right: 20px;
    font-size: 20px;
}

.project {
    width: 540px;
    height: 150px;
    background-color: white;
    border-radius: 40px;
    border-width: 2px;
    border-style: solid;
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
</style>
