
import urllib.request
import urllib.error

# Banking microservices running on Azure Container Apps
services = {
    "Customer Service": "https://lbg-customer-app.blackdesert-8ef44e4b.centralindia.azurecontainerapps.io/",
    "Account Service": "https://lbg-account-app.blackdesert-8ef44e4b.centralindia.azurecontainerapps.io/",
    "Payment Service": "https://lbg-payment-app.blackdesert-8ef44e4b.centralindia.azurecontainerapps.io/",
    "Notification Service": "https://lbg-notification-app.blackdesert-8ef44e4b.centralindia.azurecontainerapps.io/"
}

def check_health(name, url):
    try:
        request = urllib.request.Request(
            url,
            headers={"User-Agent": "Banking-Health-Check"}
        )

        with urllib.request.urlopen(request, timeout=60) as response:
            if response.status == 200:
                print(f"[HEALTHY] {name} - HTTP {response.status}")
            else:
                print(f"[UNHEALTHY] {name} - HTTP {response.status}")

    except urllib.error.HTTPError as error:
        print(f"[UNHEALTHY] {name} - HTTP {error.code}")

    except urllib.error.URLError as error:
        print(f"[ERROR] {name} - {error.reason}")

    except TimeoutError:
        print(f"[ERROR] {name} - Request timed out")


if __name__ == "__main__":
    print("\nBanking Microservices Health Check")
    print("----------------------------------")

    for service_name, service_url in services.items():
        check_health(service_name, service_url)
