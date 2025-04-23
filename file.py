def holder():
    try:
        response = requests.get(
            f"{BASE_URL}/api/Admin/holder",
            headers={
                "accept": "text/plain",
                "Authorization": f"Bearer {os.environ["API_ACCESS_TOKEN"]}",
            }
        )
        if not response.ok:
            response.raise_for_status()
        if not response.json():
            raise ValueError("Error getting all user from holder endpoint")
        return response.json()
    
    except requests.exceptions.HTTPError as http_err:
        print("HTTP error occurred during getting holder:", http_err)
        if http_err.response is not None and http_err.response.status_code == 404:
            print("holder endpoint not found. Please check the API URL and path")
        raise
    except Exception as err:
        print("An error occurred during getting holder:", err)
        raise