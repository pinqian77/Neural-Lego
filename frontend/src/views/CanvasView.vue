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

        <li class="nav-item">
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
                    flex-grow: 4;
                    margin-right: 10px;
                    height: 600px;
                    border: solid 4px #82929b;
                  "
                ></div>
                <div
                  id="myDiagramDiv"
                  style="flex-grow: 2; height: 600px; border: solid 4px #82929b"
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

              <button class="btn btn-primary" type="submit" @click="layout()">
                Layout
              </button>

              <button class="btn btn-primary" type="submit" @click="download()">
                Download
              </button>

              <form style="display: inline-block" method="POST">
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
              </form>

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
            <a class="btn btn-primary" href="/login">Logout</a>
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
          nodeDataArray: [
            {
              category: "Data",
              key: -1,
              loc: "42.22500681322674 47.35735117835321",
            },
            {
              category: "End",
              key: -4,
              loc: "567.1497069414404 47.35735117835318",
            },
            {
              category: "ReLU",
              key: -2,
              loc: "403.0334278716728 47.357351178353184",
            },
            {
              category: "FC",
              reasonsList: [{ text1: "512", text3: "128" }],
              key: -3,
              loc: "216.57893005138874 47.357351178353184",
            },
          ],
          linkDataArray: [
            {
              from: -3,
              to: -2,
              points: [
                278.70784647632394, 47.35735117835319, 318.70784647632394,
                47.35735117835319, 338.707846476324, 47.3573511783532,
                348.707846476324, 47.3573511783532,
              ],
            },
            {
              from: -2,
              to: -4,
              points: [
                457.3590092670217, 47.3573511783532, 497.3590092670217,
                47.3573511783532, 517.3590092670217, 47.35735117835319,
                527.3590092670217, 47.35735117835319,
              ],
            },
            {
              from: -1,
              to: -3,
              points: [
                84.4500136264535, 47.3573511783532, 94.4500136264535,
                47.3573511783532, 104.45001362645351, 47.35735117835319,
                154.4500136264535, 47.35735117835319,
              ],
            },
          ],
        },
        code: `import torch import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torchvision import datasets, transforms
import argparse
import time
import os

#setup training parameters
parser = argparse.ArgumentParser(description='PyTorch MNIST Training')
parser.add_argument('--batch-size', type=int, default=128, metavar='N',
                    help='input batch size for training (default: 128)')
parser.add_argument('--test-batch-size', type=int, default=128, metavar='N',
                    help='input batch size for testing (default: 128)')
parser.add_argument('--epochs', type=int, default=5, metavar='N',
                    help='number of epochs to train')
parser.add_argument('--lr', type=float, default=0.01, metavar='LR',
                    help='learning rate')
parser.add_argument('--no-cuda', action='store_true', default=False,
                    help='disables CUDA training')
parser.add_argument('--seed', type=int, default=1, metavar='S',
                    help='random seed (default: 1)')
parser.add_argument('--model-dir', default='./model-mnist-cnn',
                    help='directory of model for saving checkpoint')
parser.add_argument('--load-model', action='store_true', default=False,
                    help='load model or not')
    
args = parser.parse_args(args=[]) 
    
if not os.path.exists(args.model_dir):
    os.makedirs(args.model_dir)
            
# Judge cuda is available or not
use_cuda = not args.no_cuda and torch.cuda.is_available()
#device = torch.device("cuda" if use_cuda else "cpu")
device = torch.device("cpu")
    
torch.manual_seed(args.seed)
kwargs = {'num_workers': 1, 'pin_memory': True} if use_cuda else {}
    
# Setup data loader
transform=transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize((0.1307,), (0.3081,))
        ])
trainset = datasets.MNIST('data', train=True, download=True,
                    transform=transform)
testset = datasets.MNIST('data', train=False,
                    transform=transform)
train_loader = torch.utils.data.DataLoader(trainset,batch_size=args.batch_size, shuffle=True,**kwargs)
test_loader = torch.utils.data.DataLoader(testset,batch_size=args.test_batch_size, shuffle=False, **kwargs)
    
    
# Define CNN
class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        # in_channels:1  out_channels:32  kernel_size:3  stride:1
        self.conv1 = nn.Conv2d(1, 32, 3, 1)
        # in_channels:32  out_channels:64  kernel_size:3  stride:1
        self.conv2 = nn.Conv2d(32, 64, 3, 1)
        self.fc1 = nn.Linear(9216, 128)
        self.fc2 = nn.Linear(128, 10)
    
    def forward(self, x):
        x = self.conv1(x)
        x = F.relu(x)
        x = self.conv2(x)
        x = F.relu(x)
        x = F.max_pool2d(x, 2)
        x = torch.flatten(x, 1)
        x = self.fc1(x)
        x = F.relu(x)
        x = self.fc2(x)
        output = F.log_softmax(x, dim=1)
        return output
    
    
    
# Train function
def train(args, model, device, train_loader, optimizer, epoch):
    model.train()
    for batch_idx, (data, target) in enumerate(train_loader):
        data, target = data.to(device), target.to(device)
            
        #clear gradients
        optimizer.zero_grad()
            
        #compute loss
        loss = F.cross_entropy(model(data), target)
            
        #get gradients and update
        loss.backward()
        optimizer.step()
    
# Predict function
def eval_test(model, device, test_loader):
    model.eval()
    test_loss = 0
    correct = 0
    with torch.no_grad():
        for data, target in test_loader:
            data, target = data.to(device), target.to(device)
            output = model(data)
            test_loss += F.cross_entropy(output, target, size_average=False).item()
            pred = output.max(1, keepdim=True)[1]
            correct += pred.eq(target.view_as(pred)).sum().item()
    test_loss /= len(test_loader.dataset)
    test_accuracy = correct / len(test_loader.dataset)
    return test_loss, test_accuracy
    
# Main function, train the initial model or load the model
def main():
    model = Net().to(device)
    optimizer = optim.SGD(model.parameters(), lr=args.lr)
        
    if args.load_model:
        # Load model
        model.load_state_dict(torch.load(os.path.join(args.model_dir, 'final_model.pt')))
        trnloss, trnacc = eval_test(model, device, train_loader)
        tstloss, tstacc = eval_test(model, device, test_loader)
        print('trn_loss: {:.4f}, trn_acc: {:.2f}%'.format(trnloss, 100. * trnacc), end=', ')
        print('test_loss: {:.4f}, test_acc: {:.2f}%'.format(tstloss, 100. * tstacc))
            
    else:
        # Train initial model
        for epoch in range(1, args.epochs + 1):
            start_time = time.time()
    
            #training
            train(args, model, device, train_loader, optimizer, epoch)
    
            #get trnloss and testloss
            trnloss, trnacc = eval_test(model, device, train_loader)
            tstloss, tstacc = eval_test(model, device, test_loader)
    
            #print trnloss and testloss
            print('Epoch '+str(epoch)+': '+str(int(time.time()-start_time))+'s', end=', ')
            print('trn_loss: {:.4f}, trn_acc: {:.2f}%'.format(trnloss, 100. * trnacc), end=', ')
            print('test_loss: {:.4f}, test_acc: {:.2f}%'.format(tstloss, 100. * tstacc))
            
        #save model
        torch.save(model.state_dict(), os.path.join(args.model_dir, 'final_model.pt'))
    
if __name__ == '__main__':
    main()
   		 `,
      },
    };
  },

  methods: {
    highlighter(code) {
      return highlight(code, languages.js); // languages.<insert language> to return html with markup
    },

    // Every time request /canvas/, use this method
    // getData() {
    //   axios({
    //     method: "get",
    //     url: "/canvas/" + localStorage.uid + "/" + localStorage.pid + "/",
    //   }).then((res) => {
    //     console.log(res.data);
    //     if (res.data.status == 200) {
    //       // render canvas and code
    //       this.renderJson();
    //       this.renderCode();
    //     } else {
    //       alert("canvas loading error!");
    //     }
    //   });
    // },

    getJson() {
      axios({
        method: "get",
        url:
          "/canvas/getJson/" + localStorage.uid + "/" + localStorage.pid + "/",
        responseType: "stream",
      }).then((res) => {
        console.log(res.data);
        if (res.data.status == 200) {
          this.canvas_data.file = res.data;
          this.renderJson();
        } else if (res.data.status == 204) {
          this.compile();
        } else {
          alert("can not get user's json!");
        }
      });
    },

    getPython() {
      axios({
        method: "get",
        url:
          "/canvas/getPython/" +
          localStorage.uid +
          "/" +
          localStorage.pid +
          "/",
        responseType: "stream",
      }).then((res) => {
        console.log(res.data);
        if (res.data.status == 200) {
          this.canvas_data.code = res.code;
        } else {
          alert("can not get user's python!");
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

    // Update json first, then send to backend and get python code
    compile() {
      // Update json
      this.updateJson();

      // send json to backend
      this.canvasData.file = myDiagram.model.toJson();

      let formData = new FormData();
      formData.append("file", this.canvasData.file);
      axios({
        method: "post",
        url:
          "/canvas/compile/" + localStorage.uid + "/" + localStorage.pid + "/",
        data: formData,
      }).then((res) => {
        console.log(res.data);
        // If compile successful 200, backend update database, frontend get data and reload
        if (res.data.status == "200") {
          console.log("compile ok!");
        }
        // If complie fails 500, frontend alert error
        else if (res.data.status == "500") {
          alert("The network model is not valid!");
        }
        location.replace("/canvas/");
      });
    },

    // Update Json accroding to user's operation
    updateJson() {
      document.getElementById("mySavedModel").value = myDiagram.model.toJson();
      myDiagram.isModified = false;
    },

    // Render Json on the canvas area
    renderJson() {
      myDiagram.model = go.Model.fromJson(
        document.getElementById("mySavedModel").value
      );
    },

    // Render .py on the code area
    renderCode() {},

    // To make canvas tidy 200
    layout() {
      this.updateJson();
      myDiagram.layoutDiagram(true);
    },

    // Go to train page 200
    enterTrain() {
      location.replace("/train/");
    },
  },

  mounted() {
    this.getJson();
    this.getJson();
    this.canvasData.file = JSON.stringify(this.canvasData.file);
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