document.addEventListener("DOMContentLoaded", function() {
    fetchRules();
});

// Function to fetch available rules from the server
function fetchRules() {
    fetch('/get_rules/')
    .then(response => response.json())
    .then(data => {
        const ruleList = document.getElementById('rule-list');
        ruleList.innerHTML = '';  // Clear any previous rules
        data.rules.forEach(rule => {
            const listItem = document.createElement('li');
            listItem.textContent = rule;
            ruleList.appendChild(listItem);
        });
    });
}

// Function to create a new rule
function createRule() {
    const ruleInput = document.getElementById('rule-input').value;
    if (ruleInput.trim() === "") {
        alert("Please enter a valid rule.");
        return;
    }

    fetch('/create_rule/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken')  // For CSRF protection in Django
        },
        body: JSON.stringify({ rule: ruleInput })
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            fetchRules();  // Refresh rule list after adding a new rule
        } else {
            alert("Error creating rule");
        }
    });

    // Clear the input field
    document.getElementById('rule-input').value = "";
}

// Helper function to get CSRF token
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
