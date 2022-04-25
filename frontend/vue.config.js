const { defineConfig } = require("@vue/cli-service");
const path = require("path");
module.exports = defineConfig({
  outputDir: "dist",
//  assetsDir: "static",
//  indexPath: "templates/index.html",
  filenameHashing: false,
  runtimeCompiler: true,
  devServer: {
    host: '0.0.0.0',
    port: '8080',
    https: false,
    proxy: {
      "/api": {
        target: "http://124.220.206.81:8000/", // backend api address
        changeOrigin: true, // allow cross domain
        pathRewrite: { "^/api": "" }, // rewrite request api format
      },
    },
  },
});
