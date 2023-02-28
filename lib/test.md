from Review import Review
from Movie import Movie
from Viewer import Viewer
movie1 = Movie("mov1")
movie2 = Movie("mov2")
viewer1 = Viewer("12345678")
r1 = Review(viewer1, movie1,  5)
viewer2 = Viewer("asdffghf")
r2 = Review(viewer2, movie1,  5)
r2 = Review(viewer2, movie2,  4)
r2 = Review(viewer2, movie2,  5)

viewer.reviewed_movie(movie)
r.viewer.movies



viewer2 = Viewer("asdffghf")
r2 = Review(viewer2, movie1,  4)