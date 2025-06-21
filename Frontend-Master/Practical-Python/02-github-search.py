# to send requests on web
import requests

# Github open access search api
GITHUB_API_URL = "https://api.github.com/search/repositories"

def create_query(languages, min_stars=60000):
    query = f"star:>{min_stars}"

    for language in languages:
        query += f"language:{language}"

    return query

def repos_with_most_stars(languages, sort="stars", order="desc"):
    query = create_query(languages)
    params = {"q": query, "sort": sort, "order": order}

    response = requests.get(GITHUB_API_URL, params=params)
    status_code = response.status_code

    if status_code != 200:
        raise RuntimeError(f"An error occurred, HTTP Code: {status_code}.")
    else:
        response_json = response.json()
        return response_json["items"]


# How python will know that the main method is being run.
# If you start python from command line, this is going to be the point of entry.
if __name__ == "__main__":
    languages = ["python", "javascript", "ruby"]
    results = repos_with_most_stars(languages)

    for result in results:
        language = result["language"]
        stars = result["stargazers_count"]
        name = result["name"]

        print(f"-> {name} is a {language} repo with {stars} stars.")
