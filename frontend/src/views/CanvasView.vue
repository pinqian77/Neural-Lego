<template>
  <!-- <div>
    <div id="allSampleContent" class="p-4 w-full">
      <div id="sample">
        <div
          style="
            width: 100%;
            margin-bottom: 10px;
            display: flex;
            justify-content: space-between;
          "
        >
          <div
            id="myPaletteDiv"
            style="
              width: 150px;
              margin-right: 10px;
              background-color: whitesmoke;
              border: solid 4px #82929b;
            "
          ></div>
          <div
            id="myDiagramDiv"
            style="
              flex-grow: 3;
              margin-right: 10px;
              height: 600px;
              background-color: whitesmoke;
              border: solid 4px #82929b;
            "
          ></div>
          <div
            id="myDiagramDiv"
            style="
              flex-grow: 2;
              height: 600px;
              background-color: whitesmoke;
              border: solid 4px #82929b;
            "
          ></div>
        </div>

        <button type="submit" @click="save()">Save</button>
        <button type="submit" @click="load()">Load</button>
        <button type="submit" @click="layout()">Layout</button>

        <form method="POST">
          <input
            v-model="canvasData.file"
            type="hidden"
            class="form-control"
            id="file"
            name="file"
          />
          <button type="submit" @click="compile($event)">Compile</button>
        </form>

        <br />
        <textarea
          id="mySavedModel"
          style="width: 100%; height: 300px"
        ></textarea>
      </div>
    </div>
  </div> -->

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
          <a class="nav-link" href="template.html">
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
          <a class="nav-link" href="/register">
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
              <div
                style="
                  width: 100%;
                  margin-bottom: 10px;
                  display: flex;
                  justify-content: space-between;
                "
              >
                <!-- End of Sidebar -->
                <div
                  id="myPaletteDiv"
                  style="
                    width: 150px;
                    margin-right: 10px;
                    border: solid 4px #82929b;
                  "
                ></div>
                <div
                  id="myDiagramDiv"
                  style="
                    flex-grow: 3;
                    margin-right: 10px;
                    height: 600px;
                    border: solid 4px #82929b;
                  "
                ></div>
                <div
                  id="myDiagramDiv"
                  style="flex-grow: 2; height: 600px; border: solid 4px #82929b"
                ></div>
              </div>

              <button class="btn btn-primary" type="submit" @click="save()">
                Save
              </button>
              <button class="btn btn-primary" type="submit" @click="load()">
                Load
              </button>
              <button class="btn btn-primary" type="submit" @click="layout()">
                Layout
              </button>
              
              <form style="display:inline-block" method="POST">
                <input
                  v-model="canvasData.file"
                  type="hidden"
                  class="form-control"
                  id="file"
                  name="file"
                />
                <button type="submit" class="btn btn-primary" @click="compile($event)">Compile</button>
              </form>

              <a href="#"><button class="btn btn-primary">Train</button></a>
              <br />
              <textarea id="mySavedModel" style="width: 100%; height: 300px">
{ "class": "GraphLinksModel", 
"nodeDataArray": [ {"category":"Data", "key":-1, "loc":"-70.5 -90.19999980926514"} ], 
"linkDataArray": []}
  </textarea
              >
            </div>
          </div>
        </div>
      </div>
      <!-- End of Content Wrapper -->
    </div>
    <!-- End of Page Wrapper -->

    <!-- Scroll to Top Button
        <a class="scroll-to-top rounded" href="#page-top">
            <i class="fas fa-angle-up"></i>
        </a> -->

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
            <a class="btn btn-primary" href="/login">Logout</a>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>



<script>
import axios from "axios";
import * as go from "/public/go.js";

export default {
  name: "CanvasView",
  data() {
    return {
      canvasData: {
        file: {},
      },
    };
  },
  mounted() {
    const $ = go.GraphObject.make; // for conciseness in defining templates

    var yellowgrad = $(go.Brush, "Linear", {
      0: "#bde0fe",
      1: "#bde0fe",
    });
    var greengrad = $(go.Brush, "Linear", {
      0: "#fdffb6",
      1: "#fdffb6",
    });
    var bluegrad = $(go.Brush, "Linear", {
      0: "#caffbf",
      1: "#caffbf",
    });
    var redgrad = $(go.Brush, "Linear", {
      0: "#ffadad",
      1: "#ffadad",
    });
    var whitegrad = $(go.Brush, "Linear", {
      0: "#E7C5FC",
      1: "#E7C5FC",
    });
    var bigfont = "bold 15pt Helvetica, Arial, sans-serif";
    var smallfont = "bold 13pt Helvetica, Arial, sans-serif";

    // Common text styling
    function textStyle() {
      return {
        margin: 6,
        wrap: go.TextBlock.WrapFit,
        textAlign: "center",
        editable: true,
        font: bigfont,
      };
    }

    const myDiagram = $(go.Diagram, "myDiagramDiv", {
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

    // define the Node template
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
      // define the node's outer shape, which will surround the TextBlock
      $(go.Shape, "Rectangle", {
        fill: yellowgrad,
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
        "ReLU",
        {
          margin: 6,
          font: bigfont,
          editable: true,
          minSize: new go.Size(40, NaN),
        },
        new go.Binding("text", "text").makeTwoWay()
      )
    );
    // Data
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
          fill: bluegrad,
          portId: "",
          fromLinkable: true,
          cursor: "pointer",
          //fromEndSegmentLength: 40,
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
          fill: redgrad,
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
          fill: greengrad,
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
            // locationSpot: go.Spot.Center,
            //margin: new go.Margin(10, 0, 0, 0),
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
            //stroke: "whitesmoke",
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
            //stroke: "whitesmoke",
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
            //stroke: "whitesmoke",
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
            //stroke: "whitesmoke",
            editable: true,
            font: smallfont,
            stroke: "#3e5c76",
            row: 3,
            column: 1,
          },
          new go.Binding("text", "text3").makeTwoWay()
        )
      ) // end Table Panel
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
          fill: yellowgrad,
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
              //maxSize: new go.Size(200, NaN)
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

    var linkSelectionAdornmentTemplate = $(
      go.Adornment,
      "Link",
      $(
        go.Shape,
        // isPanelMain declares that this Shape shares the Link.geometry
        {
          isPanelMain: true,
          fill: null,
          stroke: "deepskyblue",
          strokeWidth: 2.5,
        }
      ) // use selection object's strokeWidth
    );
    // replace the default Link template in the linkTemplateMap
    myDiagram.linkTemplate = $(
      go.Link, // the whole link panel
      {
        selectable: true,
        selectionAdornmentTemplate: linkSelectionAdornmentTemplate,
      },
      new go.Binding("points").makeTwoWay(),
      {
        //curve: go.Link.Bezier,
        toShortLength: 15,
      },
      //new go.Binding("curviness", "curviness"),
      $(
        go.Shape, // the link shape
        {
          stroke: "#979dac",
          strokeWidth: 2.5,
        }
      ),
      $(
        go.Shape, // the arrowhead
        {
          toArrow: "kite",
          fill: "#979dac",
          stroke: null,
          scale: 2,
        }
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
          fill: whitegrad,
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
        // no ports, because no links are allowed to connect with a comment
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
          fill: whitegrad,
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
        // no ports, because no links are allowed to connect with a comment
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
          fill: whitegrad,
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
        // no ports, because no links are allowed to connect with a comment
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
          fill: whitegrad,
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
        // no ports, because no links are allowed to connect with a comment
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
          fill: whitegrad,
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
        // no ports, because no links are allowed to connect with a comment
      )
    );

    var palette = $(
      go.Palette,
      "myPaletteDiv", // create a new Palette in the HTML DIV element
      {
        // share the template map with the Palette
        nodeTemplateMap: myDiagram.nodeTemplateMap,
        autoScale: go.Diagram.Uniform, // everything always fits in viewport
      }
    );

    palette.model.nodeDataArray = [
      {
        category: "Data",
      },
      {
        category: "ReLU",
      },
      {
        category: "FC",
        reasonsList: [{}],
      },
      {
        category: "End",
      },
      {
        category: "CNN",
      },
      {
        category: "RNN",
      },
      {
        category: "LSTM",
      },
      {
        category: "Softmax",
      },
      {
        category: "Maximum Polling",
      },
    ];

    window.myDiagram = myDiagram;
  },

  methods: {
    layout() {
      myDiagram.layoutDiagram(true);
    },
    save() {
      document.getElementById("mySavedModel").value = myDiagram.model.toJson();
      myDiagram.isModified = false;
    },
    load() {
      myDiagram.model = go.Model.fromJson(
        document.getElementById("mySavedModel").value
      );
    },
    compile(event) {
      event.preventDefault();
      this.canvasData.file = myDiagram.model.toJson();
      console.log(myDiagram.model.toJson());
      console.log(this.canvasData.file);

      axios({
        method: "post",
        url: "/canvas/",
        data: {
          file: this.canvasData.file,
        },
      });

      // axios.post({
      //   url: "/canvas/",
      //   data: {
      //     file: this.canvasData.file,
      //   },
      //   headers: {
      //     "Content-Type": "application/json",
      //   },
      // });

      // let data = JSON.stringify({
      //   file: this.canvasData.file,
      // });
      // axios.post("/canvas/", data, {
      //   headers: {
      //     "Content-Type": "application/json",
      //   },
      // });
    },
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