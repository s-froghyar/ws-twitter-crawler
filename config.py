


from nltk.corpus import stopwords
import nltk
nltk.download('stopwords')
en_stops = set(stopwords.words('english'))


# data
epl_clubs = [   "Arsenal",
                "Aston", "Villa",
                "Brighton", "Hove", "Albion",
                "Burnley",
                "Chelsea",
                "Crystal", "Palace",
                "Everton",
                "Fulham",
                "Leeds", "United",
                "Leicester", "City",
                "Liverpool",
                "Manchester", "City",
                "Manchester", "United",
                "Newcastle", "United",
                "Sheffield", "United",
                "Southampton",
                "Tottenham", "Hotspur",
                "West", "Bromwich", "Albion",
                "West", "Ham", "United",
                "Wolverhampton", "Wanderers"
            ]
championship_clubs = [
    "Barnsley",
    "Birmingham", "City",
    "Blackburn", "Rovers",
    "Brentford",
    "Bristol", "City",
    "AFC Bournemouth",
    "Charlton", "Athletic",
    "Cardiff", "City",
    "Derby", "County",
    "Huddersfield", "Town",
    "Hull", "City",
    "Luton", "town",
    "Middlesbrough",
    "Millwall",
    "Norwich", "City",
    "Nottingham", "Forest",
    "Preston", "North", "End",
    "Queens", "Park", "Rangers",
    "Reading",
    "Sheffield", "Wednesday",
    "Stoke", "City",
    "Swansea", "City",
    "Watford",
    "Wigan", "Athletic",
]
english_clubs = list(set(epl_clubs + championship_clubs))
