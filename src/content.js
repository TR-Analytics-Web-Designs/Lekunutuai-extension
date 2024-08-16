// Inject the widget into the webpage
const widget = document.createElement('div');
widget.id = 'lekunutuai-widget';
widget.innerHTML = `<iframe src="${chrome.runtime.getURL('widget.html')}" frameBorder="0"></iframe>`;
document.body.appendChild(widget);

// Add event listeners for form submissions or other user actions to collect data
document.addEventListener('submit', function(event) {
  event.preventDefault();
  const formData = new FormData(event.target);
  const features = extractFeaturesFromFormData(formData);
  chrome.runtime.sendMessage({ action: "predictTransaction", features }, response => {
    if (response.prediction === 1) {
      showAlert('Transaction detected as fraudulent');
    }
  });
});

function extractFeaturesFromFormData(formData) {
  // Placeholder: Extract features from form data
  return [/* feature values */];
}

function showAlert(message) {
  const alertBox = document.createElement('div');
  alertBox.className = 'lekunutuai-alert';
  alertBox.innerText = message;
  document.body.appendChild(alertBox);
  setTimeout(() => alertBox.remove(), 5000);
}
