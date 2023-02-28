class Movie:
    
    all = []

    def __init__(self, title):
        self.title = title

        self.viewers = []
        self.reviews = []
        Movie.all.append(self)


    # title property goes here!
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, movieTitle):
        if type(movieTitle) == str and len(movieTitle) > 0:
            self._title = movieTitle
        else:
            raise Exception("Titles must be strings greater than 0 characters")


    def average_rating(self):
        total_ratings = sum([review.rating for review in self.reviews])
        average = total_ratings / len(self.reviews)
        return average

    @classmethod
    def highest_rated(cls):
        if len(cls.all) == 0:
            return None
            
        top_movie = cls.all[0]
        top_rating = 0
        for movie in cls.all:
            if movie.average_rating() > top_rating:
                top_movie = movie
                top_rating = movie.average_rating()
        return top_movie

