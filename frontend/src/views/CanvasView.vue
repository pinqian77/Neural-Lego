<template>
  <div>
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
#myPaletteDiv:hover {
  /* box-shadow: 1px 1px #82929B, 2px 2px #82929B, 3px 3px #82929B;
            -webkit-transform: translateX(-3px);
            transform: translateX(-3px);
            transition: .5s ease; */
  /* -webkit-transform: scale(1.2); */
  /* -ms-transform: scale(1.2); */
  transform: scale(1.015);
  transition: 1s ease;
}

#myDiagramDiv:hover {
  /* box-shadow: 1px 1px #82929B, 2px 2px #82929B, 3px 3px #82929B;
            -webkit-transform: translateX(-3px);
            transform: translateX(-3px);
            transition: .5s ease; */
  /* -webkit-transform: scale(1.2); */
  /* -ms-transform: scale(1.2); */
  transform: scale(1.01);
  transition: 1s ease;
}

#myPaletteDiv {
  border-radius: 7px;
}

#myDiagramDiv {
  border-radius: 7px;
}

.button,
button {
  --tw-bg-opacity: 1;
  background-color: rgba(31, 73, 99, var(--tw-bg-opacity));
  border-radius: 0.25rem;
  display: inline-block;
  margin: 0.25rem;
  font-size: 12pt;
  font-family: Helvetica, Arial;
  padding-top: 0.25rem;
  padding-bottom: 0.25rem;
  padding-left: 0.5rem;
  padding-right: 0.5rem;
  --tw-shadow: 0 1px 2px 0 rgba(0, 0, 0, 0.05);
  box-shadow: var(--tw-ring-offset-shadow, 0 0 #0000),
    var(--tw-ring-shadow, 0 0 #0000), var(--tw-shadow);
  --tw-text-opacity: 1;
  color: rgba(255, 255, 255, var(--tw-text-opacity));
}

.button:hover,
button:hover {
  --tw-bg-opacity: 1;
  background-color: rgba(98, 127, 145, var(--tw-bg-opacity));
  --tw-shadow: 0 1px 2px 0 rgba(0, 0, 0, 0.05);
  box-shadow: var(--tw-ring-offset-shadow, 0 0 #0000),
    var(--tw-ring-shadow, 0 0 #0000), var(--tw-shadow);
  --tw-text-opacity: 1;
  color: rgba(255, 255, 255, var(--tw-text-opacity));
  transition-property: background-color, border-color, color, fill, stroke;
  transition-timing-function: cubic-bezier(0.4, 0, 0.2, 1);
  transition-duration: 150ms;
  transition-duration: 0.2s;
}
</style>