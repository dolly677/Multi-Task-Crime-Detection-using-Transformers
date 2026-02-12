import tweepy
import csv
import os
import random
from dotenv import load_dotenv

load_dotenv()

client = tweepy.Client(
    consumer_key=os.getenv("API_KEY"),
    consumer_secret=os.getenv("API_SECRET"),
    bearer_token=os.getenv("BEARER_TOKEN"),
    access_token=os.getenv("ACCESS_TOKEN"),
    access_token_secret=os.getenv("ACCESS_TOKEN_SECRET")
)

def fetch_top10_tweets():
    try:
        # Random topics
        random_topics = [
            "weather", "music", "food", "travel", "sports",
            "movies", "technology", "science", "gaming", "news"
        ]

        selected_topic = random.choice(random_topics)
        print(f"\n🔎 Searching tweets about: {selected_topic}")

        # Fetch more tweets → then retrieve top 10
        tweets = client.search_recent_tweets(
            query=f"{selected_topic} lang:en -is:retweet",
            max_results=50,   # fetch more for ranking
            tweet_fields=["created_at", "public_metrics", "author_id"],
            user_fields=["username", "name", "location"],
            expansions=["author_id"]
        )

        tweet_data = []

        if tweets.data:

            for tweet in tweets.data:

                # Get user info
                username = ""
                name = ""
                location = ""

                if "users" in tweets.includes:
                    for user in tweets.includes["users"]:
                        if user.id == tweet.author_id:
                            username = user.username
                            name = user.name
                            location = user.location
                            break

                # Engagement score
                metrics = tweet.public_metrics
                engagement = (
                    metrics["like_count"] +
                    metrics["retweet_count"] +
                    metrics["reply_count"]
                )

                tweet_data.append({
                    "date": tweet.created_at,
                    "username": username,
                    "name": name,
                    "location": location,
                    "text": tweet.text,
                    "likes": metrics["like_count"],
                    "retweets": metrics["retweet_count"],
                    "replies": metrics["reply_count"],
                    "engagement": engagement
                })

            # 🔥 TOP-10 RETRIEVAL (by engagement)
            top10 = sorted(
                tweet_data,
                key=lambda x: x["engagement"],
                reverse=True
            )[:10]

            # Save CSV
            csv_file = f"top10_{selected_topic}_tweets.csv"

            with open(csv_file, "w", newline="", encoding="utf-8") as f:
                fieldnames = list(top10[0].keys())
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(top10)

            print(f"\n✅ Top-10 tweets saved to {csv_file}")

            # Display Top-10
            print("\n🏆 Top-10 Retrieved Tweets:\n")

            for i, t in enumerate(top10, 1):
                print(f"{i}. {t['name']} (@{t['username']})")
                print(f"   Engagement: {t['engagement']}")
                print(f"   {t['text'][:80]}...\n")

        else:
            print("No tweets found.")

    except tweepy.TweepyException as e:
        print("Error:", e)


if __name__ == "__main__":
    fetch_top10_tweets()
