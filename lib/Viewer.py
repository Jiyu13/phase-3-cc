from Movie import Movie

class Viewer:
    all = []
    
    def __init__(self, username):
        self.username = username
        self.movies = []
        self.reviews = []

        Viewer.all.append(self)

    # username property goes here!
    @property
    def username(self):
        return self._username
    
    @username.setter
    def username(self, userName):
        # check if userName exists of not?  
        for viewer in Viewer.all:
            if viewer.username == userName:
                raise Exception("Username exists already.")


        if type(userName) == str and 6 <= len(userName) <= 16:
            self._username = userName
        else:
            raise Exception("Usernames must be _unique_ strings between 6 and 16 characters, inclusive")


    def reviewed_movie(self, movie):
        return  movie in self.movies

    def rate_movie(self, movie, rating):
        if movie not in self.movies:
            Review(self, movie, rating)
        else:
            for review in self.reviews:
                if review.movie == movie:
                    review.rating = rating
                    break
            
                    