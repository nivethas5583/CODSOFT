print("===================================")
print("     NivFlix - Tamil Movies")
print("      Movie Recommendation")
print("===================================")

movies = {
    "action": [
        "Leo", "Vikram", "Kaithi", "Master", "Thuppakki",
        "Mersal", "Beast", "The GOAT", "Jailer", "Petta",
        "Captain Miller", "Maaveeran", "Valimai", "Veeram",
        "Vedalam", "Sarkar", "Kaththi", "Theri", "Bigil", "Darbar"
    ],

    "love": [
        "96", "Love Today", "Oh My Kadavule", "OK Kanmani",
        "Remo", "Vinnaithaandi Varuvaayaa", "Sita Ramam",
        "Thiruchitrambalam", "Raja Rani", "Madrasapattinam",
        "Minnale", "Alaipayuthey", "Paiyaa", "Sachin",
        "Kushi", "Roja", "Poove Unakkaga", "Jeans", "Autograph", "Kadhal"
    ],

    "comedy": [
        "Doctor", "Don", "A1", "DD Returns", "Prince",
        "Boss Engira Bhaskaran", "Varuthapadatha Valibar Sangam",
        "Kalakalappu", "Winner", "Vasool Raja MBBS",
        "Sundara Travels", "Thillu Mullu", "Panchathanthiram",
        "Kanchana", "Gulu Gulu", "Junga", "Maragatha Naanayam",
        "Tamizh Padam", "Tamizh Padam 2", "SMS"
    ],

    "thriller": [
        "Ratsasan", "Por Thozhil", "Demonte Colony",
        "Maanagaram", "Thegidi", "Imaikkaa Nodigal",
        "Thadam", "Garudan", "Kuttram 23", "Pizza",
        "Maya", "Diary", "Yutham Sei",
        "8 Thottakkal", "Vettaiyaadu Vilaiyaadu",
        "Psycho", "Naan", "Vikram Vedha", "Irumbu Thirai"
    ],

    "family": [
        "Good Night", "Lubber Pandhu", "Nanban",
        "Velaiilla Pattadhari", "VIP 2", "Abhiyum Naanum",
        "Pasanga", "Pasanga 2", "Mozhi", "Kadaikutty Singam",
        "Aanandham", "Samuthiram", "Ethir Neechal",
        "Uthamaputhiran", "Un Samayal Arayil"
    ]
}

genre = input("\nEnter Genre (action/love/comedy/thriller/family): ").lower()

if genre in movies:
    print("\nNivFlix Recommendations:\n")
    for movie in movies[genre]:
        print("-", movie)
else:
    print("\nSorry! Genre not available.")