import { LOAD_WEATHER } from "../actionTypes/weatherActionTypes";
import { Weather } from "../types/weatherTypes";

export const loadWeather = (weathers: Weather[]) => ({
    type: LOAD_WEATHER,
    weathers,
  });
