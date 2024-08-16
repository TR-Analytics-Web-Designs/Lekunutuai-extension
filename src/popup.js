document.getElementById('checkLink').addEventListener('click', () => {
    const url = window.location.href;
    const features = extractFeaturesFromURL(url);
    chrome.runtime.sendMessage({ action: "predictLink", features }, response => {
      document.getElementById('result').innerText = response.prediction === 1 ? 'Malicious Link Detected' : 'Link is Safe';
    });
  });
  
  document.getElementById('checkTransaction').addEventListener('click', () => {
    const formData = new FormData(document.querySelector('form'));
    const features = extractFeaturesFromFormData(formData);
    chrome.runtime.sendMessage({ action: "predictTransaction", features }, response => {
      document.getElementById('result').innerText = response.prediction === 1 ? 'Fraudulent Transaction Detected' : 'Transaction is Safe';
    });
  });
  
  function extractFeaturesFromURL(url) {
    // Placeholder: Extract features from the URL
    return [/* feature values */];
  }
  
  function extractFeaturesFromFormData(formData) {
    // Placeholder: Extract features from form data
    return [/* feature values */];
  }
  
  document.addEventListener('DOMContentLoaded', () => {
    console.log('Popup script loaded');
});
