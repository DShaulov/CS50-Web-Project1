import requests

def capitalizeAll(x):
    x = x.capitalize()
    for i in range(len(x)):
        if x[i] == " ":
            y = x[i+1 :len(x)].capitalize()
            x = x[0: i]
            x = x + " " + y
            break

    return x


def grRequest(isbn):
    res = requests.get("https://www.goodreads.com/book/review_counts.json",
                         params={"key": "3N1dZFOFzAAu9E7xnFCzPQ", "isbns": isbn})
    reviewDetails = []
    reviewDetails.append(res.json()['books'][0]['ratings_count'])
    reviewDetails.append(res.json()['books'][0]['average_rating'])

    return reviewDetails

