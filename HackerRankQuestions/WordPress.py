import requests

def get_wordpress_global_data():
    url = "https://api.wordpress.org/stats/plugin/1.0/"
    
    try:
        # Send a GET request to the WordPress API endpoint
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for any HTTP errors
        
        # Parse the JSON response
        data = response.json()
        
        # Extract relevant global data
        global_data = {
            "Active Installs": data["active_installs"],
            "Total Downloads": data["total_downloads"],
            "Active Versions": len(data["versions"])
        }
        
        return global_data
        
    except requests.RequestException as e:
        print("Error fetching data:", e)
        return None

# Example usage:
wordpress_global_data = get_wordpress_global_data()
if wordpress_global_data:
    print("WordPress Global Data:")
    for key, value in wordpress_global_data.items():
        print(f"{key}: {value}")
else:
    print("Failed to fetch WordPress global data.")
