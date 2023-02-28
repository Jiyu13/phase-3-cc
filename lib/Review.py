class Review:
    
    def __init__(self, viewer, movie, rating):
        self.viewer = viewer
        self.movie = movie
        self.rating = rating

        self.add_viewer_to_movie()
        self.add_movie_to_viewer()
        self.add_review_to_movie()
        self.add_review_to_viewer

    # rating property goes here!
    @property
    def rating(self):
        return self._rating
    
    @rating.setter
    def rating(self, ratingScore):
        if type(ratingScore) == int and 1 <= ratingScore <= 5:
            self._rating = ratingScore
        else:
            raise Exception("incorrect value")


    # viewer property goes here!
    @property
    def viewer(self):
            return self._viewer
    

    @viewer.setter
    def viewer(self, viewer):
        from Viewer import Viewer
        if isinstance(viewer, Viewer):
            self._viewer = viewer
        else:
            raise Exception("Must be instance of Viewer")

    
    # movie property goes here!
    @property
    def movie(self):
        return self._movie

    @movie.setter
    def movie(self, movie):
        from Movie import Movie
        if isinstance(movie, Movie):
            self._movie = movie
        else:
            raise Exception("Must be instance of Movie")


    def add_viewer_to_movie(self):
        if self._viewer not in self._movie.viewers:
            self._movie.viewers.append(self._viewer)
    

    def add_review_to_movie(self):
        self._movie.reviews.append(self)
    

    def add_movie_to_viewer(self):
        if self._movie not in self._viewer.movies:
            self._viewer.movies.append(self._movie)

    def add_review_to_viewer(self):
        self._viewer.reviews.append(self)


# from Review import Review
# from Movie import Movie
# from Viewer import Viewer
# movie = Movie("123")
# viewer = Viewer("12345678")
# r.viewer = "1"