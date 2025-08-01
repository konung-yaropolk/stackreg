from mesmerize_core.motion_correction import get_shifts
import pandas as pd
from mesmerize_core import load_movie

movie_df = load_movie('path/to/your_movie.tif')


shifts_df = get_shifts(movie_df)
