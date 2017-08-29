import media
import fresh_tomatoes

toy_story = media.Movie("toy_story","A story of a boy and his toys that can act like human","https://lumiere-a.akamaihd.net/v1/images/open-uri20150422-20810-m8zzyx_5670999f.jpeg?region=0,0,300,450","https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar","A marine on an elien planet","https://i2.kknews.cc/large/e520002b73c4f055c6e","https://www.youtube.com/watch?v=xCjPMKU1pI8")

collateral_beauty = media.Movie("Collateral Beauty","Retrating from life after a tragedy,a man questions the universe by writing to Love,Time and Death","http://static.tumblr.com/7fbaf089a33c330d9d808654573c7520/rvnxpnd/CnConglun/tumblr_static_855pfsalkeosssg8k0gw80w0k.jpg","https://www.youtube.com/watch?v=isQ5Ycie73U")

before_sunrise = media.Movie("Before Sunrise","A young man and woman meet on a train in Europe, and wind up spending one evening together in Vienna.","https://images-na.ssl-images-amazon.com/images/M/MV5BZDdiZTAwYzAtMDI3Ni00OTRjLTkzN2UtMGE3MDMyZmU4NTU4XkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_UX182_CR0,0,182,268_AL_.jpg","https://www.youtube.com/watch?v=9v6X-Dytlko")

dangal = media.Movie("Dangal","Dangal is an extraordinary true story based on the life of Mahavir Singh and his two daughters, Geeta and Babita Phogat.","https://static.juksy.com/files/articles/63168/58b6730aab4b9.jpg?m=widen&i=600&q=75","https://www.youtube.com/watch?v=x_7YlGv9u1g")

soul_mate = media.Movie("Soul mate","Soulmate portrays the decades-spanning friendship between Qiyue and Ansen, two disparate women who both struggle to find positions for their real selves within the modern world.","http://screenanarchy.com/assets/2016/10/EdkoFilm_SoulMate-161010.jpg","https://www.youtube.com/watch?v=teVSYRTbgS0")

moster_inc = media.Movie("Monster Inc."," In order to power the city, monsters have to scare children so that they scream.","https://lumiere-a.akamaihd.net/v1/images/image_3c4add40.jpeg","https://www.youtube.com/watch?v=Ue_SfrHHBAc")


movies = [moster_inc,avatar,collateral_beauty,before_sunrise,dangal,soul_mate]
fresh_tomatoes.open_movies_page(movies)



