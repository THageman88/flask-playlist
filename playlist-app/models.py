"""Models for Playlist app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Playlist(db.Model):
    """Playlist."""
    __tablename__ = "playlists"
    
    id = db.Column(db.Integer, primary_key= True)
    name = db.Column(db.Text)
    description = db.Column(db.Text)
    
class Song(db.Model):
    """Song."""

    __tablename__= "song"
    
    id = db.Column(db.Integer , primary_key = True)
    title = db.Column (db.text)
    artist = db.Column(db.text)


class PlaylistSong(db.Model):
    """Mapping of a playlist to a song."""

    __tablename__= "playlist_songs"
    
    id = db.Column(db.Integer , primary_key = True)
    playlist_id = db.Column(db.Integer, db.foreign_key('playlists.id', ondelete='cascade'))
    song_id = db.Column(db.Integer, db.foreign_key('song_id',ondelete='cascade'))



# DO NOT MODIFY THIS FUNCTION
def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)
