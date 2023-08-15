const axios = require('axios'); // Import the axios library

const data = { text: "where is Manjula Mam's cabin could You help me find it? Please" };

axios.post('http://localhost:5000/process_text', data, {
  headers: {
    'Content-Type': 'application/json'
  }
})
.then(response => {
  console.log('Processed Text:', response.data.processed_text);
})
.catch(error => {
  console.error('Error:', error);
});
