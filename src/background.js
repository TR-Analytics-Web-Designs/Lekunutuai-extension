chrome.runtime.onInstalled.addListener(() => {
  console.log('LekunutuAI Extension Installed');
});

chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
  if (request.action === "predictLink") {
      fetch('http://localhost:8000/predict', {
          method: 'POST',
          headers: {
              'Content-Type': 'application/json'
          },
          body: JSON.stringify({ url_features: request.features, transaction_features: {} }) // Empty transaction_features for link prediction
      })
      .then(response => response.json())
      .then(data => sendResponse({ prediction: data.url_prediction })) // Correct field name
      .catch(error => console.error('Error:', error));
      return true;
  }
  if (request.action === "predictTransaction") {
      fetch('http://localhost:8000/predict', {
          method: 'POST',
          headers: {
              'Content-Type': 'application/json'
          },
          body: JSON.stringify({ url_features: {}, transaction_features: request.features }) // Empty url_features for transaction prediction
      })
      .then(response => response.json())
      .then(data => sendResponse({ prediction: data.transaction_prediction })) // Correct field name
      .catch(error => console.error('Error:', error));
      return true;
  }
});
