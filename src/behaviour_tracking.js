setInterval(() => {
    let userBehaviorData = collectBehaviorData();
    fetch('http://localhost:8000/behavior', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(userBehaviorData)
    });
}, 60000); // Send every minute

function collectBehaviorData() {
    // Collect user behavior data
    return {};
}

