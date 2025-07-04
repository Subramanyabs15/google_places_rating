import requests

API_KEY = 'YOUR_API_KEY'  # Replace with your real API key if testing
PLACE_ID = 'ChIJN1t_tDeuEmsRUsoyG83frY4'  # Example: Google Sydney

url = f'https://maps.googleapis.com/maps/api/place/details/json?place_id={PLACE_ID}&key={API_KEY}'

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    result = data.get('result', {})
    name = result.get('name', '')
    rating = result.get('rating', 'N/A')
    user_ratings = result.get('user_ratings_total', 'N/A')
    print(f"Place: {name}\nRating: {rating}\nUser Ratings: {user_ratings}")
else:
    print('API request failed.')
    print(f'Status Code: {response.status_code}')
    print(f'Response: {response.text}')