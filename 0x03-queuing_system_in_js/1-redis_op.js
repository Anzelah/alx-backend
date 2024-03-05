import redis from 'redis';


const REDIS_PORT = process.env.REDIS_PORT || 6379;
const client = redis.createClient(REDIS_PORT);


client.on('connect', () => {
  console.log('Redis client connected to the server');
});
client.on('error', (err) => {
  console.log('Redis client not connected to the server: ', err.message);
});


function setNewSchool(schoolName, value) {
 client.SET(schoolName, value, redis.print);
}

function displaySchoolValue(schoolName) {
  client.GET(schoolName, (err, reply) => {
    if (err) {
     console.error(err);
     return;
    }
    console.log(reply);
  });
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
