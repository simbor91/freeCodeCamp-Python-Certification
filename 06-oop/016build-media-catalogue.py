# 06 Objects-Oriented Programming (OOP)
    # Inheritance and Polymorphism
# Workshop: Build a Media Catalogue

class MediaError(Exception):
    """Custom exception for media-related errors."""
    def __init__(self, message, obj):
        super().__init__(message)
        self.obj = obj

class Movie:
    """Parent class representing a movie."""
    # docstring is a string placed as the first statement in a class or function, and it's used to provide documentation for that class or function
    def __init__(self, title, year, director, duration):    
        if not title or title != title.strip():
            raise ValueError('Title cannot be empty')
        if year < 1895:
            raise ValueError('Year must be 1895 or later')
        if not director or director != director.strip():
            raise ValueError('Director cannot be empty')
        if duration <= 0:
            raise ValueError('Duration must be positive')
        self.title = title
        self.year = year
        self.director = director
        self.duration = duration
    
    # readable display for debugging and printing
    def __str__(self):
        return f"{self.title} ({self.year}) - {self.duration} min, {self.director}"

# inheritance: what if you want to represent a different type of media item, let's say a tv series?
class TVSeries(Movie):
    """Child class representing an entire TV series."""
    def __init__(self, title, year, director, duration, seasons, total_episodes):
        
        # avoid the override of __init__ method inherited from Movie, so avoid that TVSeries object will have only a seasons attribute and a total_episodes
        super().__init__(title, year, director, duration)
        
        if seasons < 1:
            raise ValueError('Seasons must be 1 or greater')
        if total_episodes < 1:
            raise ValueError('Total episodes must be 1 or greater')
        self.seasons = seasons
        self.total_episodes = total_episodes

    def __str__(self):
        return f"{self.title} ({self.year}) - {self.seasons} seasons, {self.total_episodes} episodes, {self.duration} min avg, {self.director}"
        
class MediaCatalogue:
    """A catalogue that can store different types of media items."""
    def __init__(self):
        self.items = []

    def add(self, media_item):
        # isinstance(obj, ClassName) returns True if obj is an instance of ClassName or any of its subclasses, because it considers the full inheritance chain
        if not isinstance(media_item, Movie): 
            # raise TypeError('Only Movie or TVSeries instances can be added') --> questo prima che creassi la classe MediaError
            raise MediaError('Only Movie or TVSeries instances can be added', media_item)
        self.items.append(media_item)

    def get_movies(self):
        return [item for item in self.items if type(item) is Movie] # list comprehension
    
    def get_tv_series(self):
        return [item for item in self.items if type(item) is TVSeries]

    def __str__(self):
        if not self.items:
            return 'Media Catalogue (empty)'
        
        movies = self.get_movies()
        series = self.get_tv_series()
        
        result = f'Media Catalogue ({len(self.items)} items):\n\n'

        if movies:
            result += '=== MOVIES ===\n'
            for index, item in enumerate(movies, 1):
                result += f'{index}. {item}\n'
        if series:
            result += '=== TV SERIES ===\n'
            for index, item in enumerate(series, 1):
                result += f'{index}. {item}\n'

        return result

catalogue = MediaCatalogue()
try:
    movie1 = Movie('The Matrix', 1999, 'The Wachowskis', 136)
    catalogue.add(movie1)
    movie2 = Movie('Inception', 2010, 'Christopher Nolan', 148)
    catalogue.add(movie2)

    series1 = TVSeries('Scrubs', 2001, 'Bill Lawrence', 24, 9, 182)
    catalogue.add(series1)
    series2 = TVSeries('Breaking Bad', 2008, 'Vince Gilligan', 47, 5, 62)
    catalogue.add(series2)

    print(catalogue)
except ValueError as e:
    print(f'Validation Error: {e}')
except MediaError as e:
    print(f'Media Error: {e}')
    print(f'Unable to add {e.obj}: {type(e.obj)}')


# docstrings can be accessed through the __doc__ attribute, which is set to None by default
# print(movie1.__doc__)
# print(series1.__doc__)
# print(catalogue.__doc__)