const https = require('https');
const qs = require('querystring');
const fs = require('fs');


function similarImage(access_token) {
    return new Promise((resolve, reject) => {
        let imageData = fs.readFileSync('../python/test2.png');
        const img = (Buffer.from(imageData)).toString('base64');
        const post_req = https.request(
            {
                hostname: 'aip.baidubce.com',
                path: '/rest/2.0/image-classify/v1/realtime_search/similar/search' + "?access_token=" + access_token,
                method: 'POST',
                headers: {
                    'content-type': 'application/x-www-form-urlencoded'
                },
                agent: false,
            },
            function (res) {
                res.on('data', (d) => {
                    resolve(JSON.parse('' + d));
                });
            }
        ).on('error', (e) => {
            reject({})
        });
        post_req.write(qs.stringify({"image": img, "pn": 0, "rn": 5}));
        post_req.end();
    })
}

module.exports = similarImage;
