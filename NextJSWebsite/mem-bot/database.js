import mysql from 'mysql2'


const connection = mysql.createConnection({
    // host : 'mysql.agh.edu.pl',
    // database : 'dominik3',
    // user : 'dominik3',
    // password : '5V3GWg3vAVRhPs5T'
    host : process.env.DB_HOST,
    database : process.env.DB_DATABASE,
    user : process.env.DB_USER,
    password : process.env.DB_PASSWORD,
});

connection.connect(function(err){
    if(err){
        throw err;
    }   
    else{
        console.log('MySQL Database is connected succesfully');
    }
})

const conPromise = (...args) => {
    return new Promise((resolve, reject) => {
        args.push((err, res) => {
            if (err) return reject(err)
            return resolve(res)
        })
        return connection.query(...args)
    })
}

export default conPromise