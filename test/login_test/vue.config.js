module.exports = {
    devServer: {
      proxy: {
    '/member': {
        target: 'http://211.109.53.216',
        changeOrigin: true,
        ws = trueßß
      }
    }
  }
}