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
    <!--  -->
    <div id="setting">
      <div class="text">Settings</div>
      <div class="form">
        <form style="align-self: center">
          <label for="optimizer">optimizer</label> <br />
          <select id="optimizer" name="optimizer">
            <option value="Adam">Adam</option></select
          ><br />

          <label for="dataset">dataset</label> <br />
          <select id="dataset" name="dataset">
            <option value="iris">iris</option></select
          ><br />

          <label for="label">label</label> <br />
          <select id="label" name="label">
            <option value="variety">variety</option>
          </select>
          <br />

          <p style="align-self: center">hyperparameters</p>
          <label for="LR">Learing rate=</label>
          <input type="text" id="LR" name="LR" placeholder="" /><br />

          <label for="TBS">Test batch size=</label>
          <input type="text" id="TBS" name="TBS" placeholder="" /><br />

          <label for="BS">batch size=</label>
          <input type="text" id="BS" name="BS" placeholder="" /><br />

          <label for="epoch">epoch=</label>
          <input type="text" id="epoch" name="epoch" placeholder="" /><br />

          <label for="seed">seed=</label>
          <input type="text" id="seed" name="seed" placeholder="" /><br />

          <input type="submit" value="Apply" align="center" />
        </form>
      </div>
    </div>
    <!-- right hand side -->
    <div style="display: inline-block">
      <div id="graph">
        <p style="margin: -30px">
          <span id="CA">Curve Accuracy</span><span id="ROC">ROC Curve</span>
        </p>
        <div class="curve">
          <img src="img1.png" />
        </div>
        <div class="curve">
          <img src="img2.png" />
        </div>
      </div>

      <div id="progress"></div>
    </div>
  </body>
</template>

<script>
export default {
  name: "ConfigView",
};
</script>


<style scoped>
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

body {
  background: #00000020;
  margin: 0%;
  height: 100%;
}

#setting {
  background-color: #525252;
  width: 300px;
  height: 100%;
  display: inline-block;
  vertical-align: top;
}

.text {
  padding-top: 30px;
  padding-bottom: 30px;
  background-color: rgb(202, 106, 46);
  text-align: center;
  font-size: 50px;
  color: white;
}

input[type="text"],
select {
  width: 60%;
  padding: 12px 20px;
  margin: 8px 0;
  display: inline-block;
  border: 1px solid #ccc;
  border-radius: 4px;
  box-sizing: border-box;
}

input[type="submit"] {
  width: 60%;
  background-color: #4caf50;
  color: white;
  padding: 14px 20px;
  margin: 8px 0;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

input[type="submit"]:hover {
  background-color: #45a049;
}

#form {
  background-color: #f2f2f2;
  padding: 100px;
  text-align: center;
}

label {
  text-align: center;
}

.curve {
  width: 600px;
  height: 350px;
  margin: 50px;
  background-color: white;
  align-self: start;
  display: inline-block;
  vertical-align: top;
}

input[type="text"] {
  width: 20%;
  padding: 12px 20px;
  margin: 8px 0;
  display: inline-block;
  border: 1px solid #ccc;
  border-radius: 4px;
  box-sizing: border-box;
}

#graph {
  padding-top: 30px;
  padding-left: 20px;
  vertical-align: top;
}

#progress {
  background-color: white;
  margin-left: 30px;
  margin-top: -10px;
  width: 1500px;
  height: 300px;
}

.text_curve {
  margin-bottom: -40px;
}

#CA {
  margin-left: 100px;
}

#ROC {
  margin-left: 600px;
}

img {
  padding: 20px;
  max-width: 500px;
  max-height: 300px;
  width: 200%;
}
</style>