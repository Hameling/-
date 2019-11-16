module.exports = {
    devServer: {
      proxy: {
    '/member': {
        target: 'http://110.11.72.247',
        changeOrigin: true,
        ws = trueßß
      }
    }
  }
}