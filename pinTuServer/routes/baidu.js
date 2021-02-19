const router = require('koa-router')()
const baidu = require('../server/baidu/baidu')
router.prefix('/baidu')

router.get('/', async function (ctx, next) {
    const value = await baidu();
    ctx.body = {value}
})

module.exports = router
