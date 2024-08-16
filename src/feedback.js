document.getElementById('feedbackForm').addEventListener('submit', (event) => {
    event.preventDefault();
    const feedback = document.getElementById('feedbackText').value;
    fetch('http://localhost:8000/feedback', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ feedback })
    })
    .then(response => response.json())
    .then(data => alert('Feedback submitted successfully'))
    .catch(error => console.error('Error:', error));
  });
  