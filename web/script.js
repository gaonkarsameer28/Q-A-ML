function callAPI(url, method = 'GET', data = {}) {
  debugger;
  return fetch(url, {
    method,
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(data)
  })
  .then(response => {
    console.log('Response status:', response.status); // Log status code
    if (!response.ok) {
      throw new Error(`HTTP error! Status: ${response.status}`);
    }
    return response.json();
  })
  .catch(error => {
    console.error('Error:', error);
    throw error; // Re-throw for further handling
  });
}

// Example usage:
const askButton = document.getElementById('askbutton');
const userInputField = document.getElementById('userquestion');
const answerDisplay = document.getElementById('answer');
const askButton2 = document.getElementById('askbutton2');


askButton.addEventListener('click', async () => {
  try {
    debugger;
    const userQuestion = userInputField.value;
    const API_URL = 'http://localhost:50000/answer'; // Replace with your API endpoint

    const response = await callAPI(API_URL, 'POST', { question: userQuestion });
    const answer = response.answer;

    answerDisplay.textContent = answer;
  } catch (error) {
    console.error('API call failed:', error);
    // Handle error gracefully, e.g., display an error message to the user
  }
});

askButton2.addEventListener('click', async () => {
  try {
    debugger;
    const userQuestion = userInputField.value;
    const API_URL = 'http://localhost:50000/answer2'; // Replace with your API endpoint

    const response = await callAPI(API_URL, 'POST', { question: userQuestion });
    const answer = response.answer;

    answerDisplay.textContent = answer;
  } catch (error) {
    console.error('API call failed:', error);
    // Handle error gracefully, e.g., display an error message to the user
  }
});