const https = require('https');
const qs = require('querystring');

const param = qs.stringify({
    'grant_type': 'client_credentials',
    'client_id': 'BhgoOojWQj14BCuEfGiDkt0g',
    'client_secret': 'Rb8TZMSW23DvH2sU0tmBUPjE5ToKHYvx'
});

function getAccessToken() {
    return new Promise((resolve, reject) => {
        https.get(
            {
                hostname: 'aip.baidubce.com',
                path: '/oauth/2.0/token?' + param,
                agent: false
            },
            function (res) {
                res.on('data', (d) => {
                    resolve(JSON.parse('' + d));
                });
            }
        ).on('error', (e) => {
            reject({})
        });
    })
}

module.exports = getAccessToken;
