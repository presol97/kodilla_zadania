import random
from faker import Faker
from datetime import date

fake = Faker("pl_PL")


class Movie:
    def __init__(self, title, year):
        self.title = title
        self.year = year
        
    def genres(self, kind):
        self.kind = kind
   

    def __str__(self):
         return f"{self.title.title()} | Genre: {self.kind} | Year: {self.year} | Audience: {self.views}"
    
    def play(self, current_played_numbers):
        current_played_numbers += 1
        self.current_played_numbers = current_played_numbers
    
    def get_title(self):
        return self.title
    
   

class Series(Movie):
    def __init__(self, season, episode, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.season = season
        self.episode = episode
    

    @property
    def ep_all(self):
        allep = random.randrange(8, 14, 2)
        self.allep = allep
        return self.allep * self.season
    
    def __str__(self):
        return f"{self.title.title()} | Genre: {self.kind} | Episode: S{self.season:02}E{self.episode:02} | Audience: {self.views}"


vid_lib = [] 

def how_many(func):
    def multiple():
        for i in range(10):
            func()
    return multiple()


for x in vid_lib:
    views = 0
    x.play(views)
    genre = ["Comedy", "Thriller", "Drama", "Action", "Biographic", "Horror"]
    x.kind(random.choice(genre))

@how_many
def generate_views():
    random.shuffle(vid_lib)
    vid_lib[0].views += random.randrange(1, 100)

def get_series():
    series = []
    for i in vid_lib:
        if i.__class__.__name__ == "Serials":
            series.append(i)
    return sorted(series, key=lambda serials: serials.title)

def get_movies():
    movies = []
    for i in vid_lib:
        if i.__class__.__name__ == "Movie":
            movies.append(i) 
    return sorted(movies, key=lambda movie: movie.title)

def search(x):
    for i in range(len(vid_lib)):
        if vid_lib[i] == x:
            print(f"\nSearch result: '{x.title.title()}'", x, sep = '\n')

def top_titles(num):
    vid_lib[:] = sorted(vid_lib, key = lambda video: video.views, reverse=True)
    print(f"\nMost popular {date.today():%d.%m.%Y}:\n")
    print(*vid_lib[:num], sep = '\n')

serials = get_series()
movies = get_movies()
   


print("\n Movie library\n")
generate_views(10)
print("Movies\n")
for i in movies:
    print(i)
print("\nSeries\n")
for i in serials:
    print(i)
top_titles(3)
search(x)
