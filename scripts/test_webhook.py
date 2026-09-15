import requests

url = "https://nibhi-automation.app.n8n.cloud/webhook-test/support-ticket"

data = {
    "customer_name": "Nidhi",
    "email": "nidhi@example.com",
    "message": "I was charged twice for my subscription and need a refund."
}

response = requests.post(url, json=data)

print("Status:", response.status_code)
print("Response:", response.text)