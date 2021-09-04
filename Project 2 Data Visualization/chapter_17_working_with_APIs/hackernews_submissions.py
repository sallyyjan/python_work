from operator import itemgetter

import requests

from requests.models import Response

from plotly import offline

# Make API call and store response.
url = "https://hacker-news.firebaseio.com/v0/topstories.json"
r = requests.get(url)
print(f"Status code: {r.status_code}")

# Process information about each submission.
submission_ids = r.json()
submission_dicts = []
for submission_id in submission_ids[:30]:
    # Make separate API call for each submission.
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    print(f"submission: {submission_id}\t status: {r.status_code}")
    response_dict = r.json()

    # Build a dictionary for each article.
    # Ignore submssions that have no descendant key
    try:
        comments = response_dict['descendants']
    except KeyError:
        print(f"submission: {submission_id} missing 'descendants' key")
        print(f"submission: {submission_id} will be ignored")
    else:
        submission_dict = {
        'title': response_dict['title'],
        'hn_link': f"http://news.ycombinator.com/item?id={submission_id}",
        'comments': comments,
        'id': submission_id,
        }

        submission_dicts.append(submission_dict)

# Sort based on 'comments' value
submission_dicts = sorted(submission_dicts, key=itemgetter('comments'), 
                            reverse=True) 

# Print results
for submission_dict in submission_dicts:
    print(f"\nTitle: {submission_dict['title']}")
    print(f"Discussion link: {submission_dict['hn_link']}")
    print(f"Comments: {submission_dict['comments']}")

# Extract information to visualize
ids, links, comments = [], [], []
for submission_dict in submission_dicts:
    ids.append(str(submission_dict['id']))

    link = f"<a href='{submission_dict['hn_link']}'>{submission_dict['title']}</a>"
    links.append(link)

    comments.append(submission_dict['comments'])


# Create visualization
# TODO: change hovertext format to make links more visible
data = [{
    'type': 'bar',
    'x': ids,
    'y': comments,
    'hovertext': links,
    'marker': {
        'color': 'rgb(60, 100, 150)',
        'line': {'width': 1.5, 'color': 'rgb(25,25,25)'}
    },
    'opacity': 0.6,
}]
my_layout = {
    'title': 'Top Most-Commented Submissions on Hacker News',
    'titlefont': {'size': 28},
    'xaxis': {
        'title': 'Submission ID',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    },
    'yaxis': {
        'title': 'Comments',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    },
}

fig = {'data':data, 'layout':my_layout}
offline.plot(fig, filename='hackernews_submissions.html')
