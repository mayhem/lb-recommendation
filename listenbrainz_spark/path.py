import os

from listenbrainz_spark import config

# Note: When accessing HDFS files/folders using spark context always use config.HDFS_CLUTER_URI.
# When accessing HDFS files/folders using HDFS client specify the path as such.

# Parent directory containing listens and data driven from ListenBrainz.
LISTENBRAINZ_DATA_DIRECTORY = os.path.join('/', 'data', 'listenbrainz')
# Directory containing similar artist relation.
# (This is a temporary path till incremental dumps for similar artists are prepared)
SIMILAR_ARTIST_DIR = os.path.join(LISTENBRAINZ_DATA_DIRECTORY, 'similar_artists')


# Parent directory containing data used in and generated by recommendation engine.
RECOMMENDATION_PARENT_DIR = os.path.join('/', 'recommendation')
# Directory containing dataframes to be used in generating recommendations (not necessarily).
DATAFRAME_DIR = os.path.join(RECOMMENDATION_PARENT_DIR, 'dataframe')
# Directory containing model metadata and the real models to be used for generating recommendations.
MODEL_DIR = os.path.join(RECOMMENDATION_PARENT_DIR, 'model')
# Directory containing candidate sets to be used for generating recommendations.
CANDIDATE_SET_DIR = os.path.join(RECOMMENDATION_PARENT_DIR, 'candidate_set')
# Directory containing RDD checkpoints to break lineage while using iterative algorithms.
CHECKPOINT_DIR = os.path.join('/', 'checkpoint')
# Directory to save best models
DATA_DIR = os.path.join(MODEL_DIR, 'data')

# Absolute path to dataframes used in processing raw data/listens.
USERS_DATAFRAME_PATH = config.HDFS_CLUSTER_URI + DATAFRAME_DIR + '/' + 'users_df.parquet'
RECORDINGS_DATAFRAME_PATH = config.HDFS_CLUSTER_URI + DATAFRAME_DIR + '/' + 'recordings_df.parquet'
# Absolute path to processed data/listens ready to be trained.
PLAYCOUNTS_DATAFRAME_PATH = config.HDFS_CLUSTER_URI + DATAFRAME_DIR + '/' + 'playcounts_df.parquet'
# Absolute path to similar artist relation.
SIMILAR_ARTIST_DATAFRAME_PATH = config.HDFS_CLUSTER_URI + SIMILAR_ARTIST_DIR + '/' + 'artist_artist_relations.parquet'
# Absolute path to candidate sets.
TOP_ARTIST_CANDIDATE_SET = config.HDFS_CLUSTER_URI + CANDIDATE_SET_DIR + '/' + 'top_artist.parquet'
SIMILAR_ARTIST_CANDIDATE_SET = config.HDFS_CLUSTER_URI + CANDIDATE_SET_DIR + '/' + 'similar_artist.parquet'
# Absolute path to model metadata.
MODEL_METADATA = config.HDFS_CLUSTER_URI + MODEL_DIR + '/' + 'model_metadata.parquet'
# Absolute path to save model index
INDEX = config.HDFS_CLUSTER_URI + MODEL_DIR + '/' + 'index.parquet'
# Absolute path to save dataframe metadata
DATAFRAME_METADATA = config.HDFS_CLUSTER_URI + DATAFRAME_DIR + '/' + 'dataframe_metadata.parquet'
# Absolute path to save model ids of deleted models.
DELETED_MODELS = config.HDFS_CLUSTER_URI + MODEL_DIR + '/' + 'deleted.parquet'


