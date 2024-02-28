import { ThunkAction } from 'redux-thunk';
import { loadWeather } from '../actions/weatherActions';
import { RootState } from '../store/rootReducer';

export const loadWeatherThunk = (): ThunkAction<void, RootState, unknown, any> => async (dispatch) => {
    try {
      const response = await fetch('/api/weathers/');

      if (response.ok) {
        const data = await response.json();
        dispatch(loadWeather(data));
      } else {
        console.error('Failed to fetch weather data');
      }
    } catch (error) {
      console.error('An error occurred while fetching weather data:', error);
    }
  };
