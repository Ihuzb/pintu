const getAccessToken = require('./accessToken');
const similarImage = require('./similarImage');

async function baidu() {
    const {access_token} = await getAccessToken();
    const info = await similarImage(access_token);
    return info
}

module.exports = baidu;
