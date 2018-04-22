import json
import requests
import webbrowser


class Media:

	def __init__(self, title="No Title", author="No Author", release_year= "No Release Year", json = None):
		if json is not None:
			try:
				self.title = json["trackName"]
			except:
				self.title = json["collectionName"]
			self.author = json['artistName']
			self.release_year = json['releaseDate'][:4]
		else:
			self.title = title
			self.author = author
			self.release_year = str(release_year)


	def __str__(self):
		return "{} by {} ({})".format(self.title, self.author, self.release_year)

	def __len__(self):
		return 0

class Song(Media):

	def __init__(self, title = "No Title", author = "No Author", release_year = "No Release Year", album = "No Album", genre= "No Genre", track_length= "No Track Length",json = None):
		super().__init__(title, author, release_year, json)
		if json is not None:
			self.album = json["collectionName"]
			self.track_length = str(json["trackTimeMillis"])
			self.genre = json["primaryGenreName"]
		else:
			self.album = album
			self.genre = genre
			self.track_length = track_length

	def __str__(self):
		return super().__str__() + "[{}]".format(self.genre)

	def __len__(self):
		return (int(self.track_length) / 1000) #IN SECONDS starts in milliseconds (1000 milliseconds per second)

class Movie(Media):

	def __init__(self, title = "No Title", author = "No Author", release_year = "No Release Year", rating = "No Rating", movie_length = "No Movie Length", json = None):
		super().__init__(title, author, release_year, json)
		if json is not None:
			self.rating = json["contentAdvisoryRating"]
			self.movie_length = str(json["trackTimeMillis"])
		else:
			self.rating = rating
			self.movie_length = movie_length



	def __str__(self):
		return super().__str__() + "[{}]".format(self.rating)


	def __len__(self):
		return int((int(self.movie_length)/60000))
		#return movie length rounded to nearest minute then work on tests

def get_itunes_data(artist, limit):
	search = requests.get('https://itunes.apple.com/search', params = {
		'term': artist,
		'limit': limit
})
	artist_media = json.loads(search.text)
	return artist_media

#print(get_itunes_data('Scooby Doo', 3))

def get_results(more):
	media_num = 0
	num_results = input("How many results would you like to preview? ")
	results = get_itunes_data(more, num_results)
	print("SONGS")
	song_num = 0
	for result in results['results']:
		if 'song' in result['kind']:
			media_num += 1
			song_num += 1
			print(str(media_num) + ' ' + Song(json=result).__str__())
			media_list.append(result)
	if song_num < 1 :
		print ('There are no songs that match your search.')

	print("MOVIES")
	movie_num = 0
	for result in results['results']:
		if 'movie' in result['kind']:
			media_num += 1
			movie_num += 1
			print(str(media_num) + ' ' + Movie(json=result).__str__())
			media_list.append(result)
	if movie_num < 1:
		print('There are no movies that match your search.')

	print("OTHER MEDIA")
	other_media_num = 0
	for result in results['results']:
		if 'song' not in result['kind']:
			if 'movie' not in result['kind']:
				media_num += 1
				other_media_num += 1
				print(str(media_num) + ' ' + Media(json=result).__str__())
				media_list.append(result)
	if other_media_num < 1:
		print('There is no other media that matches your search.')

	if media_num == 0:
		print("\n" + "There are no results for your search.")


if __name__ == "__main__":
	media_list = []
	more = ''

	while True:
		if len(media_list) == 0:

			query = input("Enter a search query or enter 'exit' to quit: ")
			if query == 'exit':
				break
			#results = get_itunes_data(query, num_results)
			get_results(query)
		else:
			more = input('Enter a number for more info, or another search term, or exit: ')
			if more == 'exit':
				print('Bye!')
				break
			try:
				num = int(more)
				print("Launching")
				print(media_list[num-1]['trackViewUrl'])
				print("in web browser")
				webbrowser.open(media_list[num-1]['trackViewUrl'])
			except:
				media_list = []
				get_results(more)
