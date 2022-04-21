<template>
  <div id="page-top" class="body">
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
          <a class="nav-link" href="draggable.html">
            <i class="fas fa-fw fa-palette"></i>
            <span>Canvas</span></a
          >
        </li>

        <hr class="sidebar-divider my-0" />

        <!-- Nav Item - Dashboard -->
        <li class="nav-item">
          <a class="nav-link" href="home.html">
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

          <div id="allSampleContent" class="p-4 w-full">
            <div id="sample">
              <div style="width: 100%; margin-bottom: 10px; display: flex">
                <div
                  id="myPaletteDiv"
                  style="
                    width: 150px;
                    margin-right: 10px;
                    border: solid 4px #82929b;
                  "
                ></div>

                <div
                  id="myDiagramDiv_1"
                  style="
                    width: 650px;
                    margin-right: 10px;
                    height: 600px;
                    border: solid 4px #82929b;
                  "
                ></div>
                <div
                  id="myDiagramDiv_2"
                  style="flex-grow: 1; height: 600px; border: solid 4px #82929b"
                >
                  <prism-editor
                    class="my-editor"
                    readonly="false"
                    v-model="canvasData.code"
                    :highlight="highlighter"
                    line-numbers
                  ></prism-editor>
                </div>
              </div>

              <!-- <button class="btn btn-primary" id="SaveButton" @click="save()">
                Save
              </button>
              <button class="btn btn-primary" @click="load()">Load</button>
              <button class="btn btn-primary" @click="layout()">Layout</button>
              <button class="btn btn-primary">Compile</button>
              <a href="/train"
                ><button class="btn btn-primary">Train</button></a
              > -->
              <button class="btn btn-primary" id="func_load" @click="load()">
                Load
              </button>
              <button
                class="btn btn-primary"
                id="func_layout"
                type="submit"
                @click="layout()"
              >
                Layout
              </button>

              <button class="btn btn-primary" type="submit" @click="download()">
                Download
              </button>

              <div style="display: inline-block">
                <input
                  type="hidden"
                  class="form-control"
                  id="file"
                  name="file"
                />
                <button
                  type="submit"
                  class="btn btn-primary"
                  @click="compile()"
                >
                  Compile
                </button>
              </div>

              <button class="btn btn-primary" @click="enterTrain()">
                Train
              </button>
              <br />

              <textarea
                id="mySavedModel"
                style="width: 100%; height: 300px"
                v-model="canvasData.file"
              >
              </textarea>

              <br />
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
            <h5 class="modal-title" id="exampleModalLabel">Ready to Leave?</h5>
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
            Select "Logout" below if you are ready to end your current session.
          </div>
          <div class="modal-footer">
            <button
              class="btn btn-secondary"
              type="button"
              data-dismiss="modal"
            >
              Cancel
            </button>
            <a class="btn btn-primary" href="login.html">Logout</a>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>



<script>
import axios from "axios";
import * as go from "../../public/go.js";

//import Prism Editor
import { PrismEditor } from "vue-prism-editor";
import "vue-prism-editor/dist/prismeditor.min.css"; // import the styles somewhere

// import highlighting library (you can use any library you want just return html string)
import { highlight, languages } from "prismjs/components/prism-core";
import "prismjs/components/prism-clike";
import "prismjs/components/prism-javascript";
import "prismjs/themes/prism-twilight.css"; // import syntax highlighting styles

export default {
  name: "CanvasView",

  components: {
    PrismEditor,
  },

  data() {
    return {
      canvasData: {
        file: {
          class: "GraphLinksModel",
          copiesArrays: true,
          copiesArrayObjects: true,
          nodeDataArray: [
            {
              category: "Data",
              reasonsList: [{}],
              key: -2,
              loc: "-99.10220015417542 -20.151221229488044",
            },
          ],
          linkDataArray: [],
        },
        code: `if __name__ == '__main__':
  main()`,
      },
    };
  },

  methods: {
    getData() {
      this.getJson();
      // this.getPython();
    },

    compile() {
      // document.getElementById("func_layout").click();
      let formData = new FormData();
      formData.append("file", this.canvasData.file);
      axios({
        method: "post",
        url:
          "/canvas/compile/" + localStorage.uid + "/" + localStorage.pid + "/",
        data: formData,
      }).then((res) => {
        console.log(res.data);
        // If 200 compile successful, backend update database, frontend get data and reload
        if (res.data.status == "200") {
          this.getPython();
          console.log("compile ok!");
        }
      });
    },

    getPython() {
      axios({
        method: "post",
        url:
          "/canvas/getPython/" +
          localStorage.uid +
          "/" +
          localStorage.pid +
          "/",
        responseType: "stream",
      }).then((res) => {
        console.log(res.data);

        if (res.status == 200) {
          console.log("200");
          this.canvasData.code = res.code;
        } else {
          alert("can not get user's python!");
        }
      });
    },

    getJson() {
      axios({
        method: "post",
        url:
          "/canvas/getJson/" + localStorage.uid + "/" + localStorage.pid + "/",
        responseType: "stream",
      }).then((res) => {
        console.log(res.data);
        // not first time
        if (res.status == 200) {
          console.log("200");
          // console.log(JSON.stringify(res.data));
          this.canvasData.file = JSON.stringify(res.data);
        }
        // first time
        else if (res.status == 204) {
          console.log("204");
        }
      });
    },

    download() {
      axios({
        method: "get",
        url:
          "/canvas/download/" + localStorage.uid + "/" + localStorage.pid + "/",
        responseType: "blob",
      }).then((res) => {
        console.log(res.data);
        if (res.data.status == 200) {
          let blob = new Blob([res], {
            type: "application/zip;charset-UTF-8",
          });

          const url = URL.createObjectURL(blob);
          const a = document.createElement("a");
          a.style.display = "none";
          a.href = url;
          a.download = "projectttt.zip";
          a.click();
          URL.revokeObjectURL(url);
        } else {
          alert("can not get user's json!");
        }
      });
    },

    // To make canvas tidy 200
    layout() {
      document.getElementById("mySavedModel").value = myDiagram.model.toJson();
      myDiagram.isModified = false;
      myDiagram.layoutDiagram(true);
    },

    load() {
      myDiagram.model = go.Model.fromJson(
        document.getElementById("mySavedModel").value
      );
    },

    highlighter(code) {
      return highlight(code, languages.js); // languages.<insert language> to return html with markup
    },

    // Go to train page 200
    enterTrain() {
      location.replace("/train/");
    },
  },

  mounted() {
    const $ = go.GraphObject.make;

    var bigfont = "bold 13pt Helvetica, Arial, sans-serif";
    var smallfont = "bold 11pt Helvetica, Arial, sans-serif";

    function textStyle() {
      return {
        margin: 6,
        wrap: go.TextBlock.WrapFit,
        textAlign: "center",
        editable: true,
        font: bigfont,
      };
    }

    const myDiagram = $(go.Diagram, "myDiagramDiv_1", {
      "toolManager.mouseWheelBehavior": go.ToolManager.WheelZoom,
      initialAutoScale: go.Diagram.Uniform,
      "linkingTool.direction": go.LinkingTool.ForwardsOnly,
      layout: $(go.LayeredDigraphLayout, {
        isInitial: false,
        isOngoing: false,
        layerSpacing: 50,
      }),
      "undoManager.isEnabled": true,
    });

    var nodeSelectionAdornmentTemplate = $(
      go.Adornment,
      "Auto",
      $(go.Shape, {
        fill: null,
        stroke: "#979dac",
        strokeWidth: 2,
        strokeDashArray: [4, 2],
      }),
      $(go.Placeholder)
    );

    myDiagram.nodeTemplate = $(
      go.Node,
      "Auto",
      {
        locationSpot: go.Spot.Center,
      },
      new go.Binding("location", "loc", go.Point.parse).makeTwoWay(
        go.Point.stringify
      ),
      {
        selectable: true,
        selectionAdornmentTemplate: nodeSelectionAdornmentTemplate,
      },

      $(go.Shape, "Rectangle", {
        stroke: null,
        portId: "",
        fromLinkable: true,
        toLinkable: true,
        cursor: "pointer",
        toEndSegmentLength: 50,
        fromEndSegmentLength: 50,
      }),
      $(
        go.TextBlock,
        "hello",
        {
          margin: 6,
          font: bigfont,
          editable: true,
          minSize: new go.Size(40, NaN),
        },
        new go.Binding("text", "text").makeTwoWay()
      )
    );

    myDiagram.nodeTemplateMap.add(
      "Data",
      $(
        go.Node,
        "Auto",
        {
          locationSpot: go.Spot.Center,
          margin: new go.Margin(0, 0, 0, 0),
        },
        new go.Binding("location", "loc", go.Point.parse).makeTwoWay(
          go.Point.stringify
        ),
        {
          selectable: true,
          selectionAdornmentTemplate: nodeSelectionAdornmentTemplate,
        },
        $(go.Shape, "Circle", {
          fill: "#caffbf",
          portId: "",
          fromLinkable: true,
          cursor: "pointer",

          stroke: "#74c69d",

          strokeWidth: 4,
        }),
        $(
          go.TextBlock,
          "Data",
          textStyle(),
          {
            stroke: "#2d6a4f",
            minSize: new go.Size(40, NaN),
          },
          new go.Binding("text", "text").makeTwoWay()
        )
      )
    );

    myDiagram.nodeTemplateMap.add(
      "End",
      $(
        go.Node,
        "Auto",
        {
          locationSpot: go.Spot.Center,
        },
        new go.Binding("location", "loc", go.Point.parse).makeTwoWay(
          go.Point.stringify
        ),
        {
          selectable: true,
          selectionAdornmentTemplate: nodeSelectionAdornmentTemplate,
        },
        $(go.Shape, "Circle", {
          fill: "#ffadad",
          portId: "",
          toLinkable: true,
          cursor: "pointer",
          fromEndSegmentLength: 40,
          stroke: "#df7373",
          strokeWidth: 4,
        }),
        $(
          go.TextBlock,
          "End",
          textStyle(),
          {
            stroke: "#ad2e24",
            minSize: new go.Size(40, NaN),
          },
          new go.Binding("text", "text").makeTwoWay()
        )
      )
    );

    myDiagram.nodeTemplateMap.add(
      "ReLU",
      $(
        go.Node,
        "Auto",
        {
          locationSpot: go.Spot.Center,
        },
        new go.Binding("location", "loc", go.Point.parse).makeTwoWay(
          go.Point.stringify
        ),
        {
          selectable: true,
          selectionAdornmentTemplate: nodeSelectionAdornmentTemplate,
        },
        $(go.Shape, "Ellipse", {
          fill: "#fdffb6",
          portId: "",
          fromLinkable: true,
          toLinkable: true,
          cursor: "pointer",
          fromEndSegmentLength: 40,
          stroke: "#ffd100",
          strokeWidth: 4,
        }),
        $(
          go.TextBlock,
          "ReLU",
          textStyle(),
          {
            stroke: "#e2711d",

            minSize: new go.Size(60, NaN),
          },
          new go.Binding("text", "text").makeTwoWay()
        )
      )
    );

    var reasonTemplate = $(
      go.Panel,
      $(
        go.Panel,
        "Table",
        {
          maxSize: new go.Size(200, 999),
          margin: new go.Margin(0, 3, 10, 3),
          defaultAlignment: go.Spot.Center,
        },
        $(go.RowColumnDefinition, {
          column: 2,
          width: 2,
        }),
        $(
          go.TextBlock,
          "input = ",
          {
            margin: new go.Margin(4, 0, 0, 0),
            maxSize: new go.Size(200, NaN),
            wrap: go.TextBlock.WrapFit,

            editable: true,
            font: smallfont,
            row: 2,
            column: 0,
            stroke: "#3e5c76",
          },
          new go.Binding("text", "text0").makeTwoWay()
        ),

        $(
          go.TextBlock,
          "value",
          {
            margin: new go.Margin(4, 0, 0, 0),
            maxSize: new go.Size(200, NaN),
            wrap: go.TextBlock.WrapFit,

            editable: true,
            stroke: "#3e5c76",
            font: smallfont,
            row: 2,
            column: 1,
          },
          new go.Binding("text", "text1").makeTwoWay()
        ),

        $(
          go.TextBlock,
          "output = ",
          {
            margin: new go.Margin(4, 0, 0, 0),
            maxSize: new go.Size(200, NaN),
            wrap: go.TextBlock.WrapFit,

            editable: true,
            font: smallfont,
            stroke: "#3e5c76",
            row: 3,
            column: 0,
          },
          new go.Binding("text", "text2").makeTwoWay()
        ),

        $(
          go.TextBlock,
          "value",
          {
            margin: new go.Margin(4, 0, 0, 9),
            maxSize: new go.Size(200, NaN),
            wrap: go.TextBlock.WrapFit,

            editable: true,
            font: smallfont,
            stroke: "#3e5c76",
            row: 3,
            column: 1,
          },
          new go.Binding("text", "text3").makeTwoWay()
        )
      )
    );

    myDiagram.nodeTemplateMap.add(
      "FC",
      $(
        go.Node,
        "Auto",
        {
          locationSpot: go.Spot.Center,
        },
        new go.Binding("location", "loc", go.Point.parse).makeTwoWay(
          go.Point.stringify
        ),
        {
          selectable: true,
          selectionAdornmentTemplate: nodeSelectionAdornmentTemplate,
        },
        $(go.Shape, "RoundedRectangle", {
          fill: "#bde0fe",
          stroke: "#4ea8de",
          strokeWidth: 4,
          portId: "",
          fromLinkable: true,
          toLinkable: true,
          cursor: "pointer",
          toEndSegmentLength: 50,
          fromEndSegmentLength: 40,
        }),
        $(
          go.Panel,
          "Vertical",
          {
            defaultAlignment: go.Spot.Center,
          },

          $(
            go.TextBlock,
            "FC",
            textStyle(),
            {
              stroke: "#3e5c76",
              margin: new go.Margin(8, 0, 0, 0),
              minSize: new go.Size(100, NaN),
            },
            new go.Binding("text", "text").makeTwoWay()
          ),

          $(
            go.Panel,
            "Vertical",
            {
              defaultAlignment: go.Spot.TopLeft,
              itemTemplate: reasonTemplate,
            },
            new go.Binding("itemArray", "reasonsList").makeTwoWay()
          )
        )
      )
    );

    myDiagram.nodeTemplateMap.add(
      "RNN",
      $(
        go.Node,
        "Auto",
        {
          locationSpot: go.Spot.Center,
        },
        new go.Binding("location", "loc", go.Point.parse).makeTwoWay(
          go.Point.stringify
        ),
        {
          selectable: true,
          selectionAdornmentTemplate: nodeSelectionAdornmentTemplate,
        },
        $(go.Shape, "RoundedRectangle", {
          fill: "#E7C5FC",
          stroke: "#CF8BF9",
          strokeWidth: 4,
        }),
        $(
          go.TextBlock,
          "RNN\n(unavailable)",
          textStyle(),
          {
            margin: 9,
            maxSize: new go.Size(200, NaN),
            wrap: go.TextBlock.WrapFit,
            editable: true,
            stroke: "#560788",
            font: smallfont,
          },
          new go.Binding("text", "text").makeTwoWay()
        )
      )
    );

    myDiagram.nodeTemplateMap.add(
      "CNN",
      $(
        go.Node,
        "Auto",
        {
          locationSpot: go.Spot.Center,
        },
        new go.Binding("location", "loc", go.Point.parse).makeTwoWay(
          go.Point.stringify
        ),
        {
          selectable: true,
          selectionAdornmentTemplate: nodeSelectionAdornmentTemplate,
        },
        $(go.Shape, "RoundedRectangle", {
          fill: "#E7C5FC",
          stroke: "#CF8BF9",
          strokeWidth: 4,
        }),
        $(
          go.TextBlock,
          "CNN\n(unavailable)",
          textStyle(),
          {
            margin: 9,
            maxSize: new go.Size(200, NaN),
            wrap: go.TextBlock.WrapFit,
            editable: true,
            stroke: "#560788",
            font: smallfont,
          },
          new go.Binding("text", "text").makeTwoWay()
        )
      )
    );

    myDiagram.nodeTemplateMap.add(
      "LSTM",
      $(
        go.Node,
        "Auto",
        {
          locationSpot: go.Spot.Center,
        },
        new go.Binding("location", "loc", go.Point.parse).makeTwoWay(
          go.Point.stringify
        ),
        {
          selectable: true,
          selectionAdornmentTemplate: nodeSelectionAdornmentTemplate,
        },
        $(go.Shape, "RoundedRectangle", {
          fill: "#E7C5FC",
          stroke: "#CF8BF9",
          strokeWidth: 4,
        }),
        $(
          go.TextBlock,
          "LSTM\n(unavailable)",
          textStyle(),
          {
            margin: 9,
            maxSize: new go.Size(200, NaN),
            wrap: go.TextBlock.WrapFit,
            editable: true,
            stroke: "#560788",
            font: smallfont,
          },
          new go.Binding("text", "text").makeTwoWay()
        )
      )
    );

    myDiagram.nodeTemplateMap.add(
      "Softmax",
      $(
        go.Node,
        "Auto",
        {
          locationSpot: go.Spot.Center,
        },
        new go.Binding("location", "loc", go.Point.parse).makeTwoWay(
          go.Point.stringify
        ),
        {
          selectable: true,
          selectionAdornmentTemplate: nodeSelectionAdornmentTemplate,
        },
        $(go.Shape, "RoundedRectangle", {
          fill: "#E7C5FC",
          stroke: "#CF8BF9",
          strokeWidth: 4,
        }),
        $(
          go.TextBlock,
          "Softmax\n(unavailable)",
          textStyle(),
          {
            margin: 9,
            maxSize: new go.Size(200, NaN),
            wrap: go.TextBlock.WrapFit,
            editable: true,
            stroke: "#560788",
            font: smallfont,
          },
          new go.Binding("text", "text").makeTwoWay()
        )
      )
    );

    myDiagram.nodeTemplateMap.add(
      "Maximum Polling",
      $(
        go.Node,
        "Auto",
        {
          locationSpot: go.Spot.Center,
        },
        new go.Binding("location", "loc", go.Point.parse).makeTwoWay(
          go.Point.stringify
        ),
        {
          selectable: true,
          selectionAdornmentTemplate: nodeSelectionAdornmentTemplate,
        },
        $(go.Shape, "RoundedRectangle", {
          fill: "#E7C5FC",
          stroke: "#CF8BF9",
          strokeWidth: 4,
        }),
        $(
          go.TextBlock,
          "Maximum\nPolling\n(unavailable)",
          textStyle(),
          {
            margin: 9,
            maxSize: new go.Size(200, NaN),
            wrap: go.TextBlock.WrapFit,
            editable: true,
            stroke: "#560788",
            font: smallfont,
          },
          new go.Binding("text", "text").makeTwoWay()
        )
      )
    );

    var linkSelectionAdornmentTemplate = $(
      go.Adornment,
      "Link",
      $(
        go.Shape,

        {
          isPanelMain: true,
          fill: null,
          stroke: "deepskyblue",
          strokeWidth: 2.5,
        }
      )
    );

    myDiagram.linkTemplate = $(
      go.Link,
      {
        selectable: true,
        selectionAdornmentTemplate: linkSelectionAdornmentTemplate,
      },
      new go.Binding("points").makeTwoWay(),
      {
        toShortLength: 15,
      },

      $(go.Shape, {
        stroke: "#979dac",
        strokeWidth: 2.5,
      }),
      $(go.Shape, {
        toArrow: "kite",
        fill: "#979dac",
        stroke: null,
        scale: 2,
      })
    );

    var palette = $(go.Palette, "myPaletteDiv", {
      nodeTemplateMap: myDiagram.nodeTemplateMap,
      autoScale: go.Diagram.Uniform,
    });

    palette.model.nodeDataArray = [
      {
        category: "Data",
        reasonsList: [{}],
      },
      {
        category: "ReLU",
        reasonsList: [{}],
      },
      {
        category: "FC",
        reasonsList: [{}],
      },
      {
        category: "End",
        reasonsList: [{}],
      },
      {
        category: "CNN",
        reasonsList: [{}],
      },
      {
        category: "RNN",
        reasonsList: [{}],
      },
      {
        category: "LSTM",
        reasonsList: [{}],
      },
      {
        category: "Softmax",
        reasonsList: [{}],
      },
      {
        category: "Maximum Polling",
        reasonsList: [{}],
      },
    ];

    window.myDiagram = myDiagram;

    this.getData();
  },
};
</script>


<style scoped>
.body {
  padding: 0;
  margin: 0;
  height: 100%;
  width: 100%;
  overflow: visible;
}
</style>
<style scoped src="../../new_pages/vendor/fontawesome-free/css/all.min.css"></style>
<style scoped src="../../new_pages/css/sb-admin-2.min.css"></style>

<style>
/* required class */
.my-editor {
  /* we dont use `language-` classes anymore so thats why we need to add background and text color manually */
  background: #2d2d2d;
  color: #ccc;

  /* you must provide font-family font-size line-height. Example: */
  font-family: Fira code, Fira Mono, Consolas, Menlo, Courier, monospace;
  font-size: 14px;
  line-height: 1.5;
  padding: 5px;
}

/* optional class for removing the outline */
.prism-editor__textarea:focus {
  outline: none;
}
</style>

<style scpoed>
#myPaletteDiv {
  border-radius: 7px;
}

#myDiagramDiv_1 {
  border-radius: 7px;
}

#myDiagramDiv_2 {
  border-radius: 7px;
}

#myDiagramDiv_1 {
  resize: horizontal;
  overflow: auto;
}

div::-webkit-resizer {
  /* background: #82929B; */
  /* background-color: #82929B; */
  /* background: url("img/arrow.png"); */
  background-image: url("../../new_pages/img/1.jpg");
  border-radius: 0.1rem;
  /* border: 8px solid black;
            background: blue; */
  /* outline: 2px dashed green; */
}
</style>