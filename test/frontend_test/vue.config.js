module.exports = {
    devServer: {
      proxy: {
    '/comment': {
        target: 'http://61.100.207.22',
        changeOrigin: true,
      }
    }
  }
}