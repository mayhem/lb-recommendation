from listenbrainz_spark.stats import run_query

def get_top_artists_recordings(user_id, top_artist_candidate_view):
    """ Prepare dataframe of recordings which belong to top artists listened to
        by the user.

        Args:
            user_id (int): User id of the user.

        Returns:
            top_artists_recordings_df (dataframe): Columns can be depicted as:
                [
                    'user_id', 'recording_id'
                ]
    """
    top_artists_recordings_df = run_query("""
        SELECT user_id
             , recording_id
          FROM {}
         WHERE user_id = {}
    """.format(top_artist_candidate_view, user_id))
    return top_artists_recordings_df

def get_similar_artists_recordings(user_id, similar_artist_candidate_view):
    """ Prepare dataframe of recordings which belong to artists similar to top artists
        listened to by the user.

        Args:
            user_id (int): User id of the user.

        Returns:
            similar_artists_recordings_df (dataframe): Columns can be depicted as:
                [
                    'user_id', 'recording_id'
                ]
    """
    similar_artists_recordings_df = run_query("""
        SELECT user_id
             , recording_id
          FROM {}
         WHERE user_id = {}
    """.format(similar_artist_candidate_view, user_id))
    return similar_artists_recordings_df

def get_recordings(recording_ids, recording_view):
    """ Prepare dataframe of recommended recordings.

        Args:
            recording_ids (tuple): A tuple of recording ids of recommended recordings.

        Returns:
            df (dataframe): Columns can be depicted as:
                [
                    'track_name', 'recording_msid', 'artist_name', 'artist_msid',
                    'release_name', 'release_msid'
                ]
    """
    df = run_query("""
        SELECT track_name
             , recording_msid
             , artist_name
             , artist_msid
             , release_name
             , release_msid
          FROM {}
         WHERE recording_id IN {}
    """.format(recording_view, recording_ids,))
    return df
