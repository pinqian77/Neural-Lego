const { defineConfig } = require("@vue/cli-service");
const path = require("path");
module.exports = defineConfig({
  outputDir: "dist",
  assetsDir: "static",
  indexPath: "templates/index.html",
  filenameHashing: false,
  runtimeCompiler: true,
  // devServer: {
  //   writeToDisk: true, // Write files to disk in dev mode, so Django can serve the assets
  // },
});
