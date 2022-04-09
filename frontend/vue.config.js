const { defineConfig } = require("@vue/cli-service");
const path = require("path");
module.exports = defineConfig({
  outputDir: "dist",
  assetsDir: "static",
  indexPath: "templates/index.html",
  filenameHashing: false,
  runtimeCompiler: true,
  devServer: {
    proxy: {
      "/api": {
        target: "http://127.0.0.1:8000/", // backend api address
        changeOrigin: true, // allow cross domain
        pathRewrite: { "^/api": "" }, // rewrite request api format
      },
    },
  },
});
