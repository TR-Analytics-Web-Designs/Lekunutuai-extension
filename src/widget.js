document.getElementById('widget-action').addEventListener('click', function() {
  fetch('http://localhost:8000/api/behavior', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ action: 'widget-interaction' })
  })
  .then(response => response.json())
  .then(data => {
      document.getElementById('widget-status-text').textContent = 'Action Taken';
  });
});

window.onload = () => {
  const url = window.location.href;
  const features = extractFeaturesFromURL(url);

  chrome.runtime.sendMessage({ action: "predictLink", features }, response => {
      const message = response.prediction === 1 ? 'Malicious Link Detected' : 'Link is Safe';
      document.getElementById('widget-message').innerText = message;
  });
};

function extractFeaturesFromURL(url) {
  // Extract features from the URL (implement feature extraction logic)
  return {
      // Dummy data: Replace with actual feature extraction
      'feature1': 0.5,
      'feature2': 1.2,
      // Include all features expected by the backend
  };
}
