const http = require('https');

const options = {
	method: 'GET',
	hostname: 'daily-missal.p.rapidapi.com',
	port: null,
	path: '/readings',
	headers: {
		'X-RapidAPI-Key': '56c472c794msh0b140396436e607p13e6dfjsn11332428c919',
		'X-RapidAPI-Host': 'daily-missal.p.rapidapi.com'
	}
};

const req = http.request(options, function (res) {
	const chunks = [];

	res.on('data', function (chunk) {
		chunks.push(chunk);
	});

	res.on('end', function () {
		const body = Buffer.concat(chunks);
		console.log(body.toString());
	});
});

req.end();