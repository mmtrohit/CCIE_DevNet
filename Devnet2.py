import requests

# Cisco DNA Center API details
BASE_URL = "https://sandboxdnac.cisco.com"
USERNAME = "devnetuser"
PASSWORD = "Cisco123!"

# Disable SSL warnings (only for sandbox/demo purposes)
requests.packages.urllib3.disable_warnings()


def get_auth_token():
    """Step-by-step: Obtain authentication token from Cisco DNA Center API."""

    print("🔐 Step 1: Preparing to contact the Cisco DNA Center authentication API...")
    auth_url = f"{BASE_URL}/dna/system/api/v1/auth/token"
    print(f"➡️  Auth URL: {auth_url}")

    print("\n🧾 Step 2: Sending POST request with basic authentication...")
    print(f"➡️  Username: {USERNAME}")
    print("➡️  Password: [hidden for security]")

    try:
        response = requests.post(auth_url, auth=(USERNAME, PASSWORD), verify=False)

        print("\n📬 Step 3: Waiting for response from the server...")
        print(f"➡️  Status Code: {response.status_code}")

        if response.status_code == 200:
            print("✅ Step 4: Authentication successful!")
            token = response.json()["Token"]
            print(f"🔑 Authentication Token:\n{token}")
            return token
        else:
            print("❌ Step 4: Authentication failed!")
            print(f"➡️  Status Code: {response.status_code}")
            print(f"➡️  Response Body: {response.text}")
            return None

    except requests.exceptions.RequestException as e:
        print("🚨 An error occurred while communicating with the API:")
        print(str(e))
        return None


# Execute the function to get the token
if __name__ == "__main__":
    get_auth_token()