import unittest
import proj1_w18 as proj1
import json

class TestMedia(unittest.TestCase):

    def testConstructorMedia(self):
        m1 = proj1.Media()
        m2 = proj1.Media("Bridget Jones's Diary (Unabridged)", "Helen Fielding", "2012")

        self.assertEqual(m1.title, "No Title")
        self.assertEqual(m1.author, "No Author")
        self.assertEqual(m1.release_year, "No Release Year")
        self.assertEqual(m2.title, "Bridget Jones's Diary (Unabridged)")
        self.assertEqual(m2.author, "Helen Fielding")
        self.assertEqual(m2.release_year, "2012")

    def test_appropriate_instance_variables_Media(self):
        m1 = proj1.Media()

        self.assertFalse(hasattr(m1, "album"))
        self.assertFalse(hasattr(m1, "genre"))
        self.assertFalse(hasattr(m1, "track_length"))
        self.assertFalse(hasattr(m1, "rating"))
        self.assertFalse(hasattr(m1, "movie_length"))

    def test_str_and_len_Media(self):
        m1 = proj1.Media()
        m2 = proj1.Media("Bridget Jones's Diary (Unabridged)", "Helen Fielding", "2012")

        self.assertEqual(m2.__str__(), "Bridget Jones's Diary (Unabridged) by Helen Fielding (2012)")
        self.assertEqual(m2.__len__(), 0)

    def test_Media_json(self):
        f = open('sample_json.json', 'r')
        sample = json.loads(f.read())
        m1 = proj1.Media(json=sample[2])
        f.close()
        self.assertEqual(m1.author, "Helen Fielding")
        self.assertEqual(m1.title, "Bridget Jones's Diary (Unabridged)")
        self.assertEqual(m1.release_year, "2012")
        self.assertEqual(m1.__str__(), "Bridget Jones's Diary (Unabridged) by Helen Fielding (2012)")
        self.assertEqual(m1.__len__(), 0)

class TestSong(unittest.TestCase):

    def testConstructorSong(self):
        s1 = proj1.Song("Hey Jude", "The Beatles", "1968", "TheBeatles 1967-1970 (The Blue Album)", "Rock", '431333')
        self.assertEqual(s1.title, "Hey Jude")
        self.assertEqual(s1.author, "The Beatles")
        self.assertEqual(s1.release_year, "1968")
        self.assertEqual(s1.album, "TheBeatles 1967-1970 (The Blue Album)")
        self.assertEqual(s1.genre, "Rock")
        self.assertEqual(s1.track_length, '431333')

    def test_appropriate_instance_variables_Song(self):
        s1 = proj1.Song("Hey Jude", "The Beatles", "1968")

        self.assertFalse(hasattr(s1, "raitng"))
        self.assertFalse(hasattr(s1, "movie_length"))

    def test_str_and_len_Song(self):
        s1 = proj1.Song("Hey Jude", "The Beatles", "1968", "Hey Jude", "Rock", '431333')

        self.assertEqual(s1.__str__(), "Hey Jude by The Beatles (1968)[Rock]")
        self.assertEqual(s1.__len__(), 431.333)

    def test_Song_json(self):
        f = open('sample_json.json', 'r')
        sample = json.loads(f.read())
        s1 = proj1.Song(json=sample[1])
        f.close()
        self.assertEqual(s1.album, "TheBeatles 1967-1970 (The Blue Album)")
        self.assertEqual(s1.genre, "Rock")
        self.assertEqual(s1.track_length, "431333")
        self.assertEqual(s1.__str__(), "Hey Jude by The Beatles (1968)[Rock]")
        self.assertEqual(s1.__len__(), 431.333)



class TestMovie(unittest.TestCase):

    def testConstructorMovie(self):
        m1 = proj1.Movie("Jaws", "Steven Spielberg", "1975", "PG", "7451455")

        self.assertEqual(m1.title, "Jaws")
        self.assertEqual(m1.author, "Steven Spielberg")
        self.assertEqual(m1.release_year, "1975")
        self.assertEqual(m1.rating, "PG")
        self.assertEqual(m1.movie_length, "7451455")

    def test_appropriate_instance_variables_Song(self):
        m1 = proj1.Media()

        self.assertFalse(hasattr(m1, "album"))
        self.assertFalse(hasattr(m1, "genre"))
        self.assertFalse(hasattr(m1, "track_length"))

    def test_str_and_len_Movie(self):
        m1 = proj1.Movie("Jaws", "Steven Spielberg", "1975", "PG", "7451455")

        self.assertEqual(m1.__str__(), "Jaws by Steven Spielberg (1975)[PG]")
        self.assertEqual(m1.__len__(), 124)

    def test_Movie_json(self):
        f = open('sample_json.json', 'r')
        sample = json.loads(f.read())
        m1 = proj1.Movie(json=sample[0])
        f.close()
        self.assertEqual(m1.title, "Jaws")
        self.assertEqual(m1.rating, "PG")
        self.assertEqual(m1.movie_length, "7451455")
        self.assertEqual(m1.__str__(), "Jaws by Steven Spielberg (1975)[PG]")
        self.assertEqual(m1.__len__(), 124)


class part3(unittest.TestCase):
    def test_common_words(self):
        search1 = proj1.get_itunes_data("baby", 50)
        search2 = proj1.get_itunes_data("love", 50)
        self.assertEqual(search1['resultCount'], 50)
        self.assertEqual(search2['resultCount'], 50)
    def test_less_common_words(self):
        search1 = proj1.get_itunes_data("moana", 12)
        search2 = proj1.get_itunes_data("helter skelter", 5)
        self.assertEqual(search1['resultCount'], 12)
        self.assertEqual(search2['resultCount'], 5)
    def test_nonsense_words(self):
        search1 = proj1.get_itunes_data('sadfasdgas', 4)
        search2 = proj1.get_itunes_data('&DGSF*#', 23)
        self.assertEqual(search1['resultCount'], 0)
        self.assertEqual(search2['resultCount'], 0)
    def test_blank(self):
        search1 = proj1.get_itunes_data('', 19)
        self.assertEqual(search1['resultCount'], 0)




unittest.main()
