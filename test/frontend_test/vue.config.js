module.exports = {
    devServer: {
      proxy: {
    '^/': {
        target: 'http://211.109.53.216',
        changeOrigin: true,
        ws = true
      }
    }
  }
}